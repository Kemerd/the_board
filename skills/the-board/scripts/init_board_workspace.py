#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
THE BOARD — Workspace Scaffolder (`init_board_workspace.py`)
===============================================================================
Initializes a visible `transcripts/` (or custom) multi-wave war-room directory
supporting both storage strategies:
  1. `folders` strategy (default): `transcripts/v1/`, `transcripts/v2/`, ...
  2. `branches` strategy: `transcripts/` directly at the root of each wave
     branch (`v1`, `v2`, ..., `vN`), keeping `main` clean on final merge.
Also writes `board_config.json` and `CONVERGENCE_TRACKER.md`.
===============================================================================
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional


# -----------------------------------------------------------------------------
# Windows Console UTF-8 Compatibility Guard
# Ensures box-drawing characters and tables render cleanly on Windows pwsh/cmd.
# -----------------------------------------------------------------------------
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows platforms."""
    # Reconfigure stdout stream if supported
    if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    # Reconfigure stderr stream if supported
    if sys.stderr is not None and hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


# -----------------------------------------------------------------------------
# Effort Level to Default Wave Budget Mapping
# Maps human-readable effort tiers to their standard wave ceiling.
# -----------------------------------------------------------------------------
EFFORT_DEFAULT_WAVES: Dict[str, int] = {
    "strike": 2,
    "standard": 5,
    "deep": 10,
    "relentless": 20,
    "white-flag": 20,
}


def build_convergence_tracker_markdown(
    project_name: str,
    mode: str,
    domain: str,
    effort: str,
    strategy: str,
    max_waves: int,
    targets: List[str],
) -> str:
    """Generate the initial Markdown content for `CONVERGENCE_TRACKER.md`."""
    # Defensive fallback for empty project names, modes, domains, or target lists
    safe_project = project_name.strip() if project_name and project_name.strip() else "Untitled Target"
    norm_mode = (mode or "red").strip().upper()
    norm_domain = (domain or "coding").strip().lower()
    norm_strategy = (strategy or "folders").strip().lower()
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
    return f"""# THE BOARD — Multi-Wave Convergence & Non-Regression Tracker

- **Project / Target**: **{safe_project}**
- **Operating Mode**: `{norm_mode}`
- **Domain Playbook**: `{norm_domain}`
- **Effort Level**: `{effort}` (Max Waves: `{max_waves}`)
- **Storage Strategy**: `{norm_strategy}`
- **Initialized**: `{timestamp}`

## [01] TARGET ARTIFACTS UNDER REVIEW
{target_bullets}

---

## [02] WAVE-BY-WAVE WHITE-FLAG CONVERGENCE MATRIX

| Wave | Firm 1 | Firm 2 | Firm 3 | Firm 4 | Firm 5 | White Flags | Board Verdict & Patch Summary |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
{wave_table}

---

## [03] CUMULATIVE NON-REGRESSION DEFENSE RATCHET LEDGER
> **Law**: No patch in Wave `vN` may delete, weaken, or regress a defense logged in Waves `v1..v(N-1)`. The Board audits this ledger on every wave.

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
    strategy: str,
    max_waves: Optional[int],
    targets: List[str],
    force: bool = False,
) -> int:
    """Create the `transcripts` directory tree, configuration JSON, and tracker file."""
    # Defensive null check on board_dir
    if board_dir is None:
        print("[ERROR] board_dir cannot be None.", file=sys.stderr)
        return 1

    # Normalize mode, domain, effort, and strategy strings defensively
    norm_mode = (mode or "red").strip().lower()
    norm_domain = (domain or "coding").strip().lower()
    norm_effort = (effort or "standard").strip().lower()
    norm_strategy = (strategy or "folders").strip().lower()
    if norm_effort not in EFFORT_DEFAULT_WAVES:
        print(f"[WARN] Unknown effort '{norm_effort}', defaulting to 'standard'.")
        norm_effort = "standard"
    if norm_strategy not in ("folders", "branches"):
        norm_strategy = "folders"

    # Determine final max_waves count with bounds clamping (1..30)
    resolved_waves = (
        max_waves
        if (max_waves is not None and max_waves > 0)
        else EFFORT_DEFAULT_WAVES[norm_effort]
    )
    resolved_waves = max(1, min(resolved_waves, 30))

    # Create root transcripts directory (and `v1/` subdirectory if using `folders` strategy)
    wave_1_dir = (board_dir / "v1") if norm_strategy == "folders" else board_dir
    try:
        board_dir.mkdir(parents=True, exist_ok=True)
        wave_1_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"[ERROR] Failed to create directory '{board_dir}': {exc}", file=sys.stderr)
        return 1

    # Preserve existing `current_wave`, `converged`, and `subagent_ids` if `board_config.json`
    # already exists and `--force` was not passed, preventing mid-run state wipes!
    config_path = board_dir / "board_config.json"
    existing_wave = 1
    existing_converged = False
    existing_subagents = {
        "firm1": None,
        "firm2": None,
        "firm3": None,
        "firm4": None,
        "firm5": None,
        "board": None,
    }
    if config_path.exists() and not force:
        try:
            old_cfg = json.loads(config_path.read_text(encoding="utf-8", errors="replace"))
            if isinstance(old_cfg, dict):
                existing_wave = int(old_cfg.get("current_wave", 1))
                existing_converged = bool(old_cfg.get("converged", False))
                if isinstance(old_cfg.get("subagent_ids"), dict):
                    existing_subagents.update(old_cfg["subagent_ids"])
        except Exception:
            pass

    # Write `board_config.json` with deterministic UTF-8 encoding
    config_payload = {
        "project_name": (project_name or "Target Project").strip(),
        "mode": norm_mode,
        "domain": norm_domain,
        "effort": norm_effort,
        "strategy": norm_strategy,
        "max_waves": resolved_waves,
        "current_wave": existing_wave,
        "converged": existing_converged,
        "targets": targets or [],
        "subagent_ids": existing_subagents,
    }
    config_path.write_text(json.dumps(config_payload, indent=2) + "\n", encoding="utf-8")

    # Write `CONVERGENCE_TRACKER.md` if it does not already exist (or if `--force` is set)
    tracker_path = board_dir / "CONVERGENCE_TRACKER.md"
    if not tracker_path.exists() or force:
        tracker_md = build_convergence_tracker_markdown(
            project_name=project_name,
            mode=norm_mode,
            domain=norm_domain,
            effort=norm_effort,
            strategy=norm_strategy,
            max_waves=resolved_waves,
            targets=targets,
        )
        tracker_path.write_text(tracker_md, encoding="utf-8")

    # Print crisp confirmation summary for The Lead
    print(f"[THE BOARD] Workspace initialized at: {board_dir.resolve()}")
    print(f"    * Mode      : {norm_mode.upper()}")
    print(f"    * Domain    : {norm_domain}")
    print(f"    * Effort    : {norm_effort} (Max Waves: {resolved_waves})")
    print(f"    * Strategy  : {norm_strategy}")
    print(f"    * Wave Dir  : {wave_1_dir.resolve()}")
    print(f"    * Tracker   : {tracker_path.resolve()}")
    return 0


def main() -> int:
    """CLI entry point for initializing a Board workspace."""
    configure_utf8_console()

    # Build argument parser with visible `transcripts` default and folder/branch strategies
    parser = argparse.ArgumentParser(
        description="Initialize a multi-wave workspace for The Board skill."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="transcripts",
        help="Path to the visible transcripts workspace directory (default: transcripts)",
    )
    parser.add_argument(
        "--strategy",
        type=str,
        choices=["folders", "branches"],
        default="folders",
        help="Storage strategy: folders (transcripts/v1..vN/) or branches (v1..vN git branches with transcripts/ at root)",
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
        choices=["plan", "red", "blue", "purple"],
        default="red",
        help="Operating mode: plan (Pre-Code Plan Verification), red (Red-Team), blue (Blue-Team Tournament), or purple (Hybrid)",
    )
    parser.add_argument(
        "--domain",
        type=str,
        default="coding",
        help="Domain playbook: coding, security, legal, patent, commercial, hardware, design, philosophy",
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
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing board_config.json state and CONVERGENCE_TRACKER.md",
    )

    args = parser.parse_args()
    return init_workspace(
        board_dir=Path(args.dir),
        project_name=args.project,
        mode=args.mode,
        domain=args.domain,
        effort=args.effort,
        strategy=args.strategy,
        max_waves=args.max_waves,
        targets=args.targets,
        force=args.force,
    )


if __name__ == "__main__":
    sys.exit(main())
