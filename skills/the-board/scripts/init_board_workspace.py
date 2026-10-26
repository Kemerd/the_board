#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
THE BOARD — Workspace Scaffolder (`init_board_workspace.py`)
===============================================================================
Initializes a `.board/` (or custom) multi-wave war-room directory with:
  1. Wave directories (`v1` .. `vN`)
  2. `board_config.json` (mode, domain, effort dial, max waves, target files)
  3. `CONVERGENCE_TRACKER.md` (live wave-by-wave White-Flag & Defense Ledger)
===============================================================================
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional


# -----------------------------------------------------------------------------
# Windows Console UTF-8 Compatibility Guard
# Ensures box-drawing characters and emojis render cleanly on Windows pwsh/cmd.
# -----------------------------------------------------------------------------
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows platforms."""
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
# Effort Level to Default Wave Budget Mapping
# Maps human-readable effort tiers to their standard wave ceiling.
# -----------------------------------------------------------------------------
EFFORT_DEFAULT_WAVES = {
    "strike": 2,
    "standard": 5,
    "deep": 10,
    "relentless": 16,
    "white-flag": 20,
}


def build_convergence_tracker_markdown(
    project_name: str,
    mode: str,
    domain: str,
    effort: str,
    max_waves: int,
    targets: List[str],
) -> str:
    """Generate the initial Markdown content for `CONVERGENCE_TRACKER.md`."""
    # Defensive fallback for empty project names or target lists
    safe_project = project_name.strip() if project_name and project_name.strip() else "Untitled Target"
    safe_targets = targets if targets else ["(Specify target files)"]
    target_bullets = "\n".join(f"- `{t}`" for t in safe_targets)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Generate wave rows up to max_waves so The Lead can update them after each wave
    wave_rows = []
    for w in range(1, max_waves + 1):
        wave_rows.append(
            f"| `v{w}` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `0 / 5` | `Awaiting Wave v{w}` |"
        )
    wave_table = "\n".join(wave_rows)

    # Return the complete tracker document
    return f"""# 🏛️⚔️ THE BOARD — Multi-Wave Convergence & Non-Regression Tracker

- **Project / Target**: **{safe_project}**
- **Operating Mode**: `{mode.upper()}`
- **Domain Playbook**: `{domain}`
- **Effort Level**: `{effort}` (Max Waves: `{max_waves}`)
- **Initialized**: `{timestamp}`

## 🎯 Target Artifacts Under Review
{target_bullets}

---

## 🏳️ Wave-by-Wave White-Flag Convergence Matrix

| Wave | Firm 1 | Firm 2 | Firm 3 | Firm 4 | Firm 5 | White Flags | Board Verdict & Patch Summary |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
{wave_table}

---

## 🛡️ Cumulative Non-Regression Defense Ratchet Ledger
> **Rule**: No patch in Wave `vN` may delete, weaken, or regress a defense logged in Waves `v1..v(N-1)`.

| Defense ID | Wave Added | Pillar / Firm | Vector Neutralized | Target File & Lines / Section | Verification Check |
| :--- | :---: | :--- | :--- | :--- | :--- |
| `DEF-v1-01` | `v1` | *Pending* | *Pending* | *Pending* | *Pending* |
"""


def init_workspace(
    board_dir: Path,
    project_name: str,
    mode: str,
    domain: str,
    effort: str,
    max_waves: Optional[int],
    targets: List[str],
) -> int:
    """Create the `.board` directory tree, configuration JSON, and tracker file."""
    # Defensive null check on board_dir
    if board_dir is None:
        print("[ERROR] board_dir cannot be None.", file=sys.stderr)
        return 1

    # Normalize effort string and resolve wave ceiling
    norm_effort = (effort or "standard").strip().lower()
    if norm_effort not in EFFORT_DEFAULT_WAVES:
        print(f"[WARN] Unknown effort '{norm_effort}', defaulting to 'standard'.")
        norm_effort = "standard"

    # Determine final max_waves count with bounds clamping (1..30)
    resolved_waves = max_waves if (max_waves is not None and max_waves > 0) else EFFORT_DEFAULT_WAVES[norm_effort]
    resolved_waves = max(1, min(resolved_waves, 30))

    # Create root board directory and initial `v1` wave directory
    try:
        board_dir.mkdir(parents=True, exist_ok=True)
        (board_dir / "v1").mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"[ERROR] Failed to create directory '{board_dir}': {exc}", file=sys.stderr)
        return 1

    # Write `board_config.json` with deterministic UTF-8 encoding
    config_payload = {
        "project_name": project_name or "Target Project",
        "mode": (mode or "red").lower(),
        "domain": (domain or "coding").lower(),
        "effort": norm_effort,
        "max_waves": resolved_waves,
        "current_wave": 1,
        "converged": False,
        "targets": targets or [],
        "subagent_ids": {
            "firm1": None,
            "firm2": None,
            "firm3": None,
            "firm4": None,
            "firm5": None,
            "board": None,
        },
    }
    config_path = board_dir / "board_config.json"
    config_path.write_text(json.dumps(config_payload, indent=2), encoding="utf-8")

    # Write `CONVERGENCE_TRACKER.md` if it does not already exist
    tracker_path = board_dir / "CONVERGENCE_TRACKER.md"
    if not tracker_path.exists():
        tracker_md = build_convergence_tracker_markdown(
            project_name=project_name,
            mode=mode,
            domain=domain,
            effort=norm_effort,
            max_waves=resolved_waves,
            targets=targets,
        )
        tracker_path.write_text(tracker_md, encoding="utf-8")

    # Print crisp confirmation summary for The Lead
    print(f"🏛️⚔️  [THE BOARD] Workspace initialized at: {board_dir.resolve()}")
    print(f"    • Mode      : {mode.upper()}")
    print(f"    • Domain    : {domain}")
    print(f"    • Effort    : {norm_effort} (Max Waves: {resolved_waves})")
    print(f"    • Wave 1 Dir: {(board_dir / 'v1').resolve()}")
    print(f"    • Tracker   : {tracker_path.resolve()}")
    return 0


def main() -> int:
    """CLI entry point for initializing a Board workspace."""
    configure_utf8_console()

    # Build argument parser with clear defaults
    parser = argparse.ArgumentParser(
        description="Initialize a multi-wave workspace for The Board skill."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=".board",
        help="Path to the board workspace directory (default: .board)",
    )
    parser.add_argument(
        "--project",
        type=str,
        default="Target Artifact",
        help="Human-readable project or target artifact name",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["red", "blue", "purple"],
        default="red",
        help="Operating mode: red (Red-Team), blue (Blue-Team Tournament), or purple (Hybrid)",
    )
    parser.add_argument(
        "--domain",
        type=str,
        default="coding",
        help="Domain playbook: coding, security, legal, patent, commercial, research",
    )
    parser.add_argument(
        "--effort",
        type=str,
        choices=["strike", "standard", "deep", "relentless", "white-flag"],
        default="standard",
        help="Effort tier controlling wave depth",
    )
    parser.add_argument(
        "--max-waves",
        type=int,
        default=None,
        help="Explicit maximum wave count override (1..30)",
    )
    parser.add_argument(
        "--targets",
        nargs="*",
        default=[],
        help="List of target file paths being audited or designed",
    )

    args = parser.parse_args()
    return init_workspace(
        board_dir=Path(args.dir),
        project_name=args.project,
        mode=args.mode,
        domain=args.domain,
        effort=args.effort,
        max_waves=args.max_waves,
        targets=args.targets,
    )


if __name__ == "__main__":
    sys.exit(main())
