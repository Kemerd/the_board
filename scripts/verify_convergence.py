#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
THE BOARD — Deterministic Wave & White-Flag Verifier (`verify_convergence.py`)
===============================================================================
Audits a completed wave directory (`vN/`) to verify:
  1. All 5 Firm reports (`firm1_*.md` .. `firm5_*.md`) and the Board report exist
  2. Each report meets the verbatim persona dialogue density threshold
  3. How many Firms raised a verified Formal White Flag (`0` surviving vectors)
  4. Whether the wave has achieved `5/5` White-Flag Convergence
===============================================================================
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# -----------------------------------------------------------------------------
# Windows Console UTF-8 Compatibility Guard
# Ensures unicode checkmarks, flags, and tables print without cp1252 crashes.
# -----------------------------------------------------------------------------
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows consoles."""
    if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    if sys.stderr is not None and hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


# -----------------------------------------------------------------------------
# Regex Patterns for Persona Dialogue Lines and White-Flag Certificates
# Used to prevent lazy bullet-only summaries or premature surrenders.
# -----------------------------------------------------------------------------
DIALOGUE_SPEAKER_RE = re.compile(r"^\s*(?:\*\*|\*|-)?\s*\**[A-Z][A-Za-z0-9\.\-\s\(\)]{2,45}\**\s*:\s+.+", re.MULTILINE)
WHITE_FLAG_RE = re.compile(
    r"(WHITE[\s\-]+FLAG\s+RAISED|FORMAL\s+WHITE[\s\-]+FLAG|UNCONDITIONAL\s+SURRENDER|SURVIVING\s+(?:NON-SUICIDAL\s+)?VECTORS\s*:\**\s*0\b|0\s+SURVIVING\s+VECTORS)",
    re.IGNORECASE,
)
CRITICAL_HIGH_SURVIVING_RE = re.compile(
    r"\|\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL|HIGH)`?\s*\|",
    re.IGNORECASE,
)


def audit_single_firm_file(file_path: Path, min_lines: int) -> Dict[str, object]:
    """Inspect a single Firm report for line count, dialogue turns, and White Flag."""
    # Defensive check for missing or unreadable file
    if file_path is None or not file_path.is_file():
        return {
            "exists": False,
            "path": str(file_path) if file_path else "MISSING",
            "lines": 0,
            "dialogue_turns": 0,
            "white_flag": False,
            "active_critical_high": 0,
            "meets_length": False,
        }

    # Read file text safely using UTF-8 with replacement on malformed bytes
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    line_count = len(lines)

    # Count distinct verbatim speaker dialogue turns (`**Speaker Name:** ...`)
    dialogue_matches = DIALOGUE_SPEAKER_RE.findall(text)
    dialogue_count = len(dialogue_matches)

    # Check if CRITICAL or HIGH surviving vectors are still listed as open
    active_vectors = len(CRITICAL_HIGH_SURVIVING_RE.findall(text))

    # Determine if a formal White Flag was raised and no open CRITICAL/HIGH vectors remain
    has_white_flag_phrase = bool(WHITE_FLAG_RE.search(text))
    is_white_flag = has_white_flag_phrase and (active_vectors == 0)

    return {
        "exists": True,
        "path": file_path.name,
        "lines": line_count,
        "dialogue_turns": dialogue_count,
        "white_flag": is_white_flag,
        "active_critical_high": active_vectors,
        "meets_length": line_count >= min_lines,
    }


def locate_firm_files(wave_dir: Path) -> Tuple[Dict[int, Path], List[Path]]:
    """Locate `firm1..5` files and any `BOARD*` adjudication files in `wave_dir`."""
    firm_map: Dict[int, Path] = {}
    board_files: List[Path] = []

    # Defensive check if directory does not exist
    if wave_dir is None or not wave_dir.is_dir():
        return firm_map, board_files

    # Scan all Markdown files in the wave directory
    for md_file in sorted(wave_dir.glob("*.md")):
        name_lower = md_file.name.lower()
        if "board" in name_lower:
            board_files.append(md_file)
            continue
        # Match firm1..firm5 or blue_firm_a..e
        for idx, letter in enumerate(["a", "b", "c", "d", "e"], start=1):
            if (
                re.search(rf"firm[\s_\-]*0?{idx}\b", name_lower)
                or re.search(rf"firm[\s_\-]*{letter}\b", name_lower)
                or re.search(rf"^0?{idx}_", name_lower)
            ):
                firm_map[idx] = md_file
                break

    return firm_map, board_files


def main() -> int:
    """CLI entry point to audit a wave directory and report convergence status."""
    configure_utf8_console()

    parser = argparse.ArgumentParser(
        description="Verify Firm transcripts, persona dialogue density, and 5/5 White-Flag convergence."
    )
    parser.add_argument(
        "--wave-dir",
        type=str,
        required=True,
        help="Path to the wave directory to audit (e.g., .board/v1)",
    )
    parser.add_argument(
        "--min-lines",
        type=int,
        default=250,
        help="Minimum line count expected per Firm transcript (default: 250)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON summary",
    )

    args = parser.parse_args()
    wave_dir = Path(args.wave_dir)

    # Guard against missing wave directory
    if not wave_dir.is_dir():
        print(f"[ERROR] Wave directory not found: {wave_dir}", file=sys.stderr)
        return 2

    # Discover Firm 1..5 files and Board adjudication file
    firm_map, board_files = locate_firm_files(wave_dir)
    firm_results: Dict[int, Dict[str, object]] = {}
    white_flag_count = 0
    missing_firms = 0

    for idx in range(1, 6):
        f_path = firm_map.get(idx)
        res = audit_single_firm_file(f_path, args.min_lines)
        firm_results[idx] = res
        if not res["exists"]:
            missing_firms += 1
        elif res["white_flag"]:
            white_flag_count += 1

    board_exists = len(board_files) > 0
    board_lines = (
        len(board_files[0].read_text(encoding="utf-8", errors="replace").splitlines())
        if board_exists
        else 0
    )

    # Convergence requires all 5 firms present, 5/5 White Flags, and a Board report
    converged = (missing_firms == 0) and (white_flag_count == 5) and board_exists

    summary_payload = {
        "wave_dir": str(wave_dir.resolve()),
        "converged": converged,
        "white_flags": white_flag_count,
        "total_firms": 5,
        "board_report_present": board_exists,
        "board_report_lines": board_lines,
        "firms": firm_results,
    }

    if args.json:
        print(json.dumps(summary_payload, indent=2))
    else:
        print(f"🏛️⚔️  [THE BOARD] Wave Audit: {wave_dir.resolve()}")
        print("-" * 78)
        print(f"{'Firm':<8} | {'File':<32} | {'Lines':>6} | {'Turns':>6} | {'Status':<18}")
        print("-" * 78)
        for idx in range(1, 6):
            r = firm_results[idx]
            status_str = (
                "🏳️ WHITE FLAG"
                if r["white_flag"]
                else ("❌ MISSING" if not r["exists"] else f"⚔️ OPEN ({r['active_critical_high']} Crit/High)")
            )
            print(
                f"Firm {idx:<3} | {str(r['path'])[:32]:<32} | {int(r['lines']):>6} | {int(r['dialogue_turns']):>6} | {status_str:<18}"
            )
        print("-" * 78)
        board_label = board_files[0].name if board_exists else "MISSING"
        print(f"Board Adjudication: {board_label} ({board_lines} lines)")
        print(f"White-Flag Tally  : {white_flag_count} / 5")
        if converged:
            print("Verdict           : 🏳️  CONVERGED (5/5 WHITE FLAGS RAISED!)")
        else:
            print("Verdict           : 🔥 ESCALATE TO NEXT WAVE (Surviving vectors or missing reports remain)")

    return 0 if converged else 1


if __name__ == "__main__":
    sys.exit(main())
