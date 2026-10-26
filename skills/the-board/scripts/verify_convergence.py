#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
THE BOARD — Deterministic Wave & White-Flag Verifier (`verify_convergence.py`)
===============================================================================
Audits a completed wave directory (`vN/`) and optionally repository Markdown links:
  1. Verifies all 5 Firm reports (`firm1_*.md` .. `firm5_*.md`) and the Board
     adjudication report (`BOARD_ADJUDICATION_vN.md`) exist and meet line thresholds.
  2. Verifies each Firm report meets the verbatim persona dialogue turn threshold.
  3. Verifies how many Firms raised a non-negated Formal White Flag with `0`
     surviving `CRITICAL`, `HIGH`, or `MEDIUM` vectors.
  4. Optionally (`--check-links`) verifies that 100% of relative Markdown file
     links across the repository resolve to existing files on disk.
===============================================================================
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


# -----------------------------------------------------------------------------
# Windows Console UTF-8 Compatibility Guard
# Ensures unicode checkmarks, flags, and tables print without cp1252 crashes.
# -----------------------------------------------------------------------------
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows consoles."""
    # Reconfigure stdout stream if supported by the active Python runtime
    if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    # Reconfigure stderr stream if supported by the active Python runtime
    if sys.stderr is not None and hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


# -----------------------------------------------------------------------------
# Metadata Keys Excluded From Speaker Dialogue Turn Counting
# Prevents Markdown metadata bullets (`- **Status**: ...`) from inflating turns.
# -----------------------------------------------------------------------------
NON_SPEAKER_METADATA_KEYS: Set[str] = {
    "id",
    "category",
    "status",
    "verdict",
    "mode",
    "effort",
    "wave",
    "date",
    "timestamp",
    "target",
    "target artifact",
    "target artifacts",
    "target artifacts under siege",
    "assigned orthogonal pillar",
    "excluded sibling pillars",
    "saved recording path",
    "saved recording",
    "severity",
    "location",
    "file",
    "files",
    "line",
    "lines",
    "proof",
    "remediation",
    "fix",
    "impact",
    "vector",
    "vectors",
    "summary",
    "note",
    "warning",
    "important",
    "caution",
    "tip",
    "rule",
    "directive",
    "boardroom verdict",
    "white-flag status",
    "white-flag tally",
}

# -----------------------------------------------------------------------------
# Regex Patterns for Speaker Dialogue, Open Vectors, and White-Flag Certificates
# -----------------------------------------------------------------------------
# Matches `**Speaker Name (Role):** "Dialogue..."` or `**Speaker Name**: Dialogue...`
# Including Unicode letters (`Gödel`, `Kálmán`, `卢`), quotes (`"Schema-Lock"`),
# apostrophes (`O'Connor`), slashes, dollar signs (`$100M`), and em-dashes.
DIALOGUE_LINE_RE = re.compile(
    r"^\s*(?:>\s*)?(?:[\*\-]\s+)?\*\*([^\*\n:]{2,95}?)(?::\*\*|\*\*\s*:)\s+\S+",
    re.MULTILINE,
)

# Affirmative White-Flag status markers
AFFIRMATIVE_WHITE_FLAG_RE = re.compile(
    r"(?:"
    r"\[\s*STATUS\s*:\s*WHITE[\s\-]+FLAG\s+RAISED\b"
    r"|WHITE[\s\-]+FLAG\s+RAISED\s*//\s*0\s+SURVIVING\s+VECTORS"
    r"|FORMAL\s+WHITE[\s\-]+FLAG\s+CERTIFICATE"
    r"|UNCONDITIONAL\s+SURRENDER\s*//\s*0\s+SURVIVING\s+VECTORS"
    r"|SURVIVING\s+(?:NON-SUICIDAL\s+)?VECTORS\s*:\**\s*0\b"
    r")",
    re.IGNORECASE,
)

# Document-wide explicit White-Flag rejection / revocation phrases
GLOBAL_WHITE_FLAG_VETO_RE = re.compile(
    r"(?:"
    r"STATUS\s*:\s*WHITE[\s\-]+FLAG\s+WITHHELD"
    r"|OPEN\s+VECTORS\s+REMAIN"
    r"|WHITE[\s\-]+FLAG\s+WITHHELD"
    r"|WHITE[\s\-]+FLAG\s+DENIED"
    r"|WHITE[\s\-]+FLAG\s+REJECTED"
    r"|WHITE[\s\-]+FLAG\s+REVOKED"
    r"|NO\s+WHITE[\s\-]+FLAG\s+RAISED"
    r"|0\s*/\s*1\s*WHITE[\s\-]+FLAG"
    r"|0\s*/\s*5\s*WHITE[\s\-]+FLAGS"
    r")",
    re.IGNORECASE,
)

# Line-level negation or conditional tokens that invalidate a White-Flag match on that line
LINE_NEGATION_RE = re.compile(
    r"\b(?:no|not|never|cannot|can't|without|withheld|withhold|denied|deny|reject|rejected|revoked|revoke|false| premature|if|until|unless|when|whether|template|example)\b",
    re.IGNORECASE,
)

# Matches a vector ID (`F1-V1`, `F01-V02`, `FA-V1`) anywhere in a Markdown table row
VECTOR_ROW_ID_RE = re.compile(r"\bF(?:0?[1-5]|[A-E])-V\d+\b", re.IGNORECASE)

# Matches open severity levels (`CRITICAL`, `HIGH`, `MEDIUM`) in a table row
VECTOR_SEVERITY_RE = re.compile(r"\b(?:CRITICAL|HIGH|MEDIUM)\b", re.IGNORECASE)

# Matches closed/neutralized status cells in prior-wave verification tables
VECTOR_CLOSED_CELL_RE = re.compile(
    r"^[\[\*\`\s]*(?:DEAD|CHECKMATED|FIXED|RESOLVED|CLOSED|NEUTRALIZED|REMEDIATED)\b",
    re.IGNORECASE,
)
VECTOR_OPEN_CELL_RE = re.compile(
    r"^[\[\*\`\s]*(?:OPEN|SURVIVING|ACTIVE|PARTIAL|BYPASSABLE|COSMETIC|REGRESSED)\b",
    re.IGNORECASE,
)


def strip_fenced_code_blocks(markdown_text: str) -> str:
    """Remove fenced code blocks (``` ... ``` or ```` ... ````) before scanning."""
    if not markdown_text:
        return ""
    return re.sub(r"^(`{3,4})[^\n]*\n[\s\S]*?^\1\s*$", "", markdown_text, flags=re.MULTILINE)


def count_dialogue_turns(markdown_text: str) -> int:
    """
    Count verbatim speaker dialogue turns in `markdown_text` while excluding
    fenced code blocks and metadata key-value bullets.
    """
    if not markdown_text:
        return 0

    cleaned = strip_fenced_code_blocks(markdown_text)
    turn_count = 0

    for match in DIALOGUE_LINE_RE.finditer(cleaned):
        speaker_label = match.group(1).strip().strip("*`\"'").strip()
        speaker_lower = speaker_label.lower()

        # Skip known metadata bullets (`- **Target Artifacts**: ...`)
        if speaker_lower in NON_SPEAKER_METADATA_KEYS:
            continue
        # Skip step/directive headers (`Step 1`, `Directive 2`, `Vector F1-V1`, `DEF-v1-01`)
        if re.match(
            r"^(?:step|phase|part|section|directive|vector|def-v\d+|firm\s*\d+|pillar|candidate|attack|option|case|branch)\b",
            speaker_lower,
        ):
            continue

        turn_count += 1

    return turn_count


def count_open_vectors(markdown_text: str) -> int:
    """
    Count surviving `CRITICAL`, `HIGH`, or `MEDIUM` vectors in Markdown table rows.
    Inspects individual table cells so prose descriptions mentioning 'DEAD / CHECKMATED'
    or 'CLOSED-DOOR' never falsely suppress an open vector row.
    """
    if not markdown_text:
        return 0

    cleaned = strip_fenced_code_blocks(markdown_text)
    seen_open_ids: Set[str] = set()

    for raw_line in cleaned.splitlines():
        line = raw_line.strip()
        # Only inspect Markdown table rows containing pipe delimiters
        if not line.startswith("|") or "|" not in line[1:]:
            continue

        vec_match = VECTOR_ROW_ID_RE.search(line)
        if not vec_match:
            continue

        vec_id = vec_match.group(0).upper()
        # Split on unescaped pipe delimiters so escaped regex pipes (`\|`) inside code cells stay intact
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip("|"))]

        # Check if any short status cell (`<= 45` chars) marks this vector as closed/neutralized
        is_closed_row = any(
            len(c) <= 45 and VECTOR_CLOSED_CELL_RE.search(c) for c in cells
        ) and not any(
            len(c) <= 45 and VECTOR_OPEN_CELL_RE.search(c) for c in cells
        )
        if is_closed_row:
            continue

        # Check if any short severity/status cell (`<= 45` chars) specifies CRITICAL, HIGH, or MEDIUM
        has_severity_cell = any(
            len(c) <= 45 and VECTOR_SEVERITY_RE.search(c) for c in cells
        )
        if has_severity_cell:
            seen_open_ids.add(vec_id)

    return len(seen_open_ids)


def has_verified_white_flag_certificate(markdown_text: str) -> bool:
    """
    Return True if `markdown_text` contains an affirmative, non-negated Formal
    White-Flag certificate and no document-level White-Flag veto/withheld status.
    """
    if not markdown_text:
        return False

    # Inspect both the full text (including diff banners) and non-code text
    # First: if the document explicitly states WHITE FLAG WITHHELD / OPEN VECTORS REMAIN,
    # immediately return False!
    if GLOBAL_WHITE_FLAG_VETO_RE.search(markdown_text):
        return False

    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if AFFIRMATIVE_WHITE_FLAG_RE.search(line):
            # Ensure the line itself does not contain negation or conditional words
            if not LINE_NEGATION_RE.search(line):
                return True

    return False


def audit_single_firm_file(
    file_path: Optional[Path],
    min_lines: int,
    min_turns: int,
) -> Dict[str, object]:
    """Inspect a single Firm report for line count, dialogue turns, and White Flag."""
    # Defensive check for missing or unreadable file
    if file_path is None or not file_path.is_file():
        return {
            "exists": False,
            "path": str(file_path) if file_path else "MISSING",
            "lines": 0,
            "dialogue_turns": 0,
            "white_flag": False,
            "active_vectors": 0,
            "meets_length": False,
            "meets_turns": False,
        }

    # Read file text safely using UTF-8 with replacement on malformed bytes
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    line_count = len(lines)

    # Count verbatim speaker dialogue turns and open CRITICAL/HIGH/MEDIUM vectors
    dialogue_count = count_dialogue_turns(text)
    active_vectors = count_open_vectors(text)
    meets_length = line_count >= min_lines
    meets_turns = dialogue_count >= min_turns

    # A valid White Flag requires:
    # 1. Affirmative non-negated White-Flag certificate
    # 2. Zero open CRITICAL/HIGH/MEDIUM vectors (`active_vectors == 0`)
    # 3. Minimum line count (`meets_length`)
    # 4. Minimum verbatim dialogue turns (`meets_turns`)
    has_certificate = has_verified_white_flag_certificate(text)
    is_white_flag = (
        has_certificate
        and (active_vectors == 0)
        and meets_length
        and meets_turns
    )

    return {
        "exists": True,
        "path": file_path.name,
        "lines": line_count,
        "dialogue_turns": dialogue_count,
        "white_flag": is_white_flag,
        "active_vectors": active_vectors,
        "meets_length": meets_length,
        "meets_turns": meets_turns,
    }


def locate_firm_files(wave_dir: Path) -> Tuple[Dict[int, Path], List[Path]]:
    """
    Locate `firm1..5` (or `blue_firm_a..e`) files FIRST, and then classify
    `BOARD_ADJUDICATION*` / `board*` files in `wave_dir`.
    """
    firm_map: Dict[int, Path] = {}
    board_files: List[Path] = []

    # Defensive check if directory does not exist
    if wave_dir is None or not wave_dir.is_dir():
        return firm_map, board_files

    # Scan all Markdown files in the wave directory in deterministic sorted order
    for md_file in sorted(wave_dir.glob("*.md")):
        name_lower = md_file.name.lower()
        matched_firm = False

        # Step 1: Match `firm1..5` or `blue_firm_a..e` FIRST using `(?:[\s_\-\.]|$)`
        # so underscores in `firm1_<pillar>.md` and substrings like `"onboarding"` in
        # `firm5_readme_aesthetic_and_onboarding_psychology.md` are handled properly!
        for idx, letter in enumerate(["a", "b", "c", "d", "e"], start=1):
            if (
                re.search(rf"(?:^|[\s_\-])firm[\s_\-]*0?{idx}(?:[\s_\-\.]|$)", name_lower)
                or re.search(rf"(?:^|[\s_\-])firm[\s_\-]*{letter}(?:[\s_\-\.]|$)", name_lower)
                or re.search(rf"^0?{idx}[_\-]", name_lower)
            ):
                firm_map[idx] = md_file
                matched_firm = True
                break

        if matched_firm:
            continue

        # Step 2: Match Board adjudication files (`BOARD_ADJUDICATION_v1.md`, `board_v1.md`)
        if re.search(r"(?:^|[_\-])(?:board|executive_board)(?:[_\-\.]|$)", name_lower):
            board_files.append(md_file)

    return firm_map, board_files


def verify_markdown_links(repo_root: Path) -> Tuple[int, List[str]]:
    """
    Scan Markdown files across `repo_root` and verify that all relative file links
    `[label](target)` resolve to existing files or directories on disk.
    Returns `(total_checked_links, broken_link_messages)`.
    """
    if repo_root is None or not repo_root.is_dir():
        return 0, [f"Repository root directory not found: {repo_root}"]

    md_link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    total_checked = 0
    broken_links: List[str] = []

    # Collect all Markdown files in the repository (excluding `.git/`)
    for md_path in sorted(repo_root.rglob("*.md")):
        if any(part in (".git", ".board", "transcripts") for part in md_path.parts):
            continue

        raw_text = md_path.read_text(encoding="utf-8", errors="replace")
        cleaned_text = strip_fenced_code_blocks(raw_text)

        for match in md_link_re.finditer(cleaned_text):
            raw_target = match.group(1).strip()
            if not raw_target:
                continue

            # Strip optional Markdown link title (`path "title"`)
            target_path_str = raw_target.split()[0].strip("<>")

            # Ignore external URLs, mailto links, conversation:// links, and pure `#anchor` links
            if (
                target_path_str.startswith(("http://", "https://", "mailto:", "conversation://", "#"))
                or "{{" in target_path_str
            ):
                continue

            # Flag any hardcoded Windows drive paths or `file://` absolute local paths in repo docs
            # (Allow `.board/` historical wave transcripts to cite local forensic paths if needed,
            #  but enforce strict portable relative paths in all shipped skill/persona/readme files)
            is_board_transcript = ".board" in md_path.parts or "transcripts" in md_path.parts
            if target_path_str.startswith("file://") or re.match(r"^[A-Za-z]:[\\/]", target_path_str):
                if not is_board_transcript:
                    broken_links.append(
                        f"{md_path.relative_to(repo_root)} -> non-portable path `{target_path_str}`"
                    )
                continue

            # Strip `#L10-L20` or `#section` anchor suffix before resolving on disk
            file_part = target_path_str.split("#", 1)[0]
            if not file_part:
                continue

            total_checked += 1
            resolved = (md_path.parent / file_part).resolve()
            if not resolved.exists():
                broken_links.append(
                    f"{md_path.relative_to(repo_root)} -> broken link `{target_path_str}` "
                    f"(resolved to `{resolved}`)"
                )

    return total_checked, broken_links


def main() -> int:
    """CLI entry point to audit a wave directory and/or repository link integrity."""
    configure_utf8_console()

    parser = argparse.ArgumentParser(
        description="Verify Firm transcripts, persona dialogue density, 5/5 White-Flag convergence, and Markdown links."
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
        "--min-turns",
        type=int,
        default=10,
        help="Minimum verbatim speaker dialogue turns per Firm transcript (default: 10)",
    )
    parser.add_argument(
        "--min-board-lines",
        type=int,
        default=100,
        help="Minimum line count expected for the Board Adjudication report (default: 100)",
    )
    parser.add_argument(
        "--expected-firms",
        type=int,
        default=5,
        help="Number of Strike Team firms expected in the wave (default: 5)",
    )
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Verify that all relative Markdown links across the repository resolve on disk",
    )
    parser.add_argument(
        "--repo-root",
        type=str,
        default=None,
        help="Optional repository root path for --check-links (defaults to parent of scripts/)",
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

    # Discover Firm 1..N files and Board adjudication file
    expected_firms = max(1, args.expected_firms)
    firm_map, board_files = locate_firm_files(wave_dir)
    firm_results: Dict[int, Dict[str, object]] = {}
    white_flag_count = 0
    missing_firms = 0

    for idx in range(1, expected_firms + 1):
        f_path = firm_map.get(idx)
        res = audit_single_firm_file(f_path, args.min_lines, args.min_turns)
        firm_results[idx] = res
        if not res["exists"]:
            missing_firms += 1
        elif res["white_flag"]:
            white_flag_count += 1

    board_exists = len(board_files) > 0
    board_text = (
        board_files[0].read_text(encoding="utf-8", errors="replace")
        if board_exists
        else ""
    )
    board_lines = len(board_text.splitlines()) if board_exists else 0
    board_turns = count_dialogue_turns(board_text) if board_exists else 0
    board_meets_length = board_exists and (board_lines >= args.min_board_lines)

    # Optional static Markdown link verification across the repository
    checked_links = 0
    broken_links: List[str] = []
    if args.check_links:
        repo_root = (
            Path(args.repo_root).resolve()
            if args.repo_root
            else Path(__file__).resolve().parent.parent
        )
        checked_links, broken_links = verify_markdown_links(repo_root)

    links_ok = len(broken_links) == 0

    # Convergence requires all expected firms present, all raising verified White Flags,
    # a Board report meeting `min_board_lines`, and zero broken links (if `--check-links` enabled).
    converged = (
        (missing_firms == 0)
        and (white_flag_count == expected_firms)
        and board_meets_length
        and links_ok
    )

    summary_payload = {
        "wave_dir": str(wave_dir.resolve()),
        "converged": converged,
        "white_flags": white_flag_count,
        "total_firms": expected_firms,
        "board_report_present": board_exists,
        "board_report_lines": board_lines,
        "board_report_turns": board_turns,
        "board_meets_length": board_meets_length,
        "checked_markdown_links": checked_links,
        "broken_markdown_links": broken_links,
        "firms": firm_results,
    }

    if args.json:
        print(json.dumps(summary_payload, indent=2))
    else:
        print(f"[THE BOARD] Wave Audit: {wave_dir.resolve()}")
        print("-" * 86)
        print(
            f"{'Firm':<8} | {'File':<36} | {'Lines':>6} | {'Turns':>6} | {'Status':<20}"
        )
        print("-" * 86)
        for idx in range(1, expected_firms + 1):
            r = firm_results[idx]
            if not r["exists"]:
                status_str = "MISSING"
            elif r["white_flag"]:
                status_str = "WHITE FLAG (0 Vec)"
            else:
                reasons = [f"{r['active_vectors']} Open Vec"]
                if not r["meets_length"]:
                    reasons.append(f"<{args.min_lines}L")
                if not r["meets_turns"]:
                    reasons.append(f"<{args.min_turns}T")
                status_str = f"OPEN ({', '.join(reasons)})"
            print(
                f"Firm {idx:<3} | {str(r['path'])[:36]:<36} | {int(r['lines']):>6} | "
                f"{int(r['dialogue_turns']):>6} | {status_str:<20}"
            )
        print("-" * 86)
        board_label = board_files[0].name if board_exists else "MISSING"
        print(
            f"Board Adjudication: {board_label} ({board_lines} lines, {board_turns} dialogue turns)"
        )
        if args.check_links:
            print(
                f"Markdown Links    : {checked_links} checked, {len(broken_links)} broken"
            )
            for b_msg in broken_links[:20]:
                print(f"  [BROKEN LINK] {b_msg}")
        print(f"White-Flag Tally  : {white_flag_count} / {expected_firms}")
        if converged:
            print(
                f"Verdict           : [CONVERGED // {expected_firms}/{expected_firms} WHITE FLAGS RAISED]"
            )
        else:
            print(
                "Verdict           : [ESCALATE // SURVIVING VECTORS, MISSING REPORTS, OR BROKEN LINKS]"
            )

    if args.check_links and not links_ok:
        return 3
    return 0 if converged else 1


if __name__ == "__main__":
    sys.exit(main())
