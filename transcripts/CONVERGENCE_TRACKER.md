# THE BOARD — Multi-Wave Convergence & Non-Regression Tracker

- **Project / Target**: **The Board (`the-board` Skill Repository Self-Audit)**
- **Operating Mode**: `RED`
- **Domain Playbook**: `philosophy_and_coding`
- **Effort Level**: `white-flag` (Max Waves: `20`)
- **Storage Strategy**: `branches` (`v1`, `v2`, ..., `vN` with visible `transcripts/` at root)
- **Initialized**: `2026-10-26 06:51:47 UTC`

## [01] TARGET ARTIFACTS UNDER REVIEW
- `SKILL.md`
- `README.md`
- `commands/board.md`
- `references/prompt_templates.md`
- `references/persona_mask_theory.md`
- `references/effort_and_white_flag.md`
- `references/domain_playbooks.md`
- `personas/boardrooms/the_godfather_board.md`
- `scripts/init_board_workspace.py`
- `scripts/verify_convergence.py`
- `scripts/split_personas_to_files.py`
- `scripts/install.ps1`
- `scripts/install.sh`

---

## [02] WAVE-BY-WAVE WHITE-FLAG CONVERGENCE MATRIX

| Wave | Firm 1 | Firm 2 | Firm 3 | Firm 4 | Firm 5 | White Flags | Board Verdict & Patch Summary |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `v1` | `OPEN (12 Vec)` | `OPEN (7 Vec)` | `OPEN (12 Vec)` | `OPEN (9 Vec)` | `OPEN (5 Vec)` | `0 / 5` | `45 vectors adjudicated in BOARD_ADJUDICATION_v1.md; 100% patched on branch v2 (DEF-v1-01..12)` |
| `v2` | `IN PROGRESS` | `IN PROGRESS` | `IN PROGRESS` | `IN PROGRESS` | `IN PROGRESS` | `PENDING` | `Wave v2 audit of v1 patches on branch v2` |
| `v3` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `0 / 5` | `Awaiting Wave v3` |

---

## [03] CUMULATIVE NON-REGRESSION DEFENSE RATCHET LEDGER
> **Law**: No patch in Wave `vN` may delete, weaken, or regress a defense logged in Waves `v1..v(N-1)`. The Board audits this ledger on every wave.

| Defense ID | Wave Added | Pillar / Firm | Vector Neutralized | Target File & Lines / Section | Verification Check |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **`DEF-v1-01`** | `v1` | Pillar I (`Firm 1`) | `F1-V1`, `F1-V8`, `F1-V9` | `SKILL.md` `[00]`, `[04]`; `commands/board.md` `[01]` | Deterministic 2-branch Intake Gate (`HALT & ASK` if `target` missing vs `BIND DEFAULTS & RUN`), `white-flag`/`relentless` enum parity, and explicit `plan` post-convergence gate. |
| **`DEF-v1-02`** | `v1` | Pillars I & II (`Firms 1, 2`) | `F1-V2`, `F2-V4`, `F2-V7` | `SKILL.md` `[02]`, `[03]`, `[04]`; `the_godfather_board.md` `[03]`; `prompt_templates.md` `[D]` | Mode-indexed Board adjudication (`Top 3 Podium` in `blue` mode vs `100% of surviving vectors across all 5 orthogonal pillars` in `red`/`plan`/`purple` modes) + **Unanimous Falsification Veto & Two-Tier Sublation Rule**. |
| **`DEF-v1-03`** | `v1` | Pillars I & II (`Firms 1, 2`) | `F1-V3`, `F2-V1`, `F2-V2` | `SKILL.md` `[04]`; `effort_and_white_flag.md` `[03]`; `prompt_templates.md` `[A]`, `[B]`, `[D]` | `[UNVERIFIED CLAIM — FALSIFY AGAINST RAW FILES]` framing, 4-state vector disposition with Tit-for-Tat cosmetic severity escalation, ban on suicidal straw-man White Flags, preservation of `MERC_1..3` in Template `[B]`, and Board **White-Flag Revocation Authority**. |
| **`DEF-v1-04`** | `v1` | Pillar II (`Firm 2`) | `F2-V3`, `F2-V6` | `SKILL.md` `[03]`, `[04]`; `prompt_templates.md` `[A]`, `[D]` | Mandatory `CONVERGENCE_TRACKER.md` handoff to The Board in Template `[D]`, Phase 3 ratchet ledger updates, and `plan` mode grounding against existing codebase files + Post-Condition Matrix. |
| **`DEF-v1-05`** | `v1` | Pillars I & II (`Firms 1, 2`) | `F1-V4`, `F1-V5`, `F1-V10`, `F1-V12`, `F2-V5` | `SKILL.md` `[04]`; `effort_and_white_flag.md` `[01]`, `[02]`; `prompt_templates.md` `[A]`, `[B]`, `[C]` | Default Bench Rotation in `deep`/`white-flag` tiers + Cross-Pillar Diff Re-Verification, `purple` mode Wave `v1`/`v2`/`v3+` template routing, `Excluded Sibling Pillars` boundary, and 3-Partner Triad in Template `[C]`. |
| **`DEF-v1-06`** | `v1` | Pillars I & V (`Firms 1, 5`) | `F1-V6`, `F1-V7`, `F1-V11`, `F5-V3`, `F5-V4` | `README.md`; `SKILL.md`; `commands/board.md`; `persona_mask_theory.md` | Unified 5-runtime `v2.0` ASCII boot banner (`Col 83` exact), canonical `[DOORS SEALED // EXECUTIVE SESSION RECORDING ACTIVE]` delimiter, removal of `"try to destroy"`, and mechanistic binding of `"Expected output: genius"`. |
| **`DEF-v1-07`** | `v1` | Pillars III & IV (`Firms 3, 4`) | `F3-V1..V5`, `F4-V9` | `scripts/verify_convergence.py` | Fixed `firm1..5` regex (`(?:[\s_\-\.]\|$)` before `board_files`), enforced `meets_length`, `meets_turns`, and `board_lines`, negation-guarded White-Flag certificate check, cell-level `CRITICAL\|HIGH\|MEDIUM` open-vector scanner, Unicode/quoted speaker turn counter, and `--check-links` static link verifier. |
| **`DEF-v1-08`** | `v1` | Pillars III & IV (`Firms 3, 4`) | `F3-V6`, `F3-V7`, `F4-V9` | `scripts/init_board_workspace.py` | Added `"plan"` to `--mode` choices (`choices=["plan", "red", "blue", "purple"]`), visible `transcripts/` default with `--strategy folders\|branches`, normalized `norm_mode`/`norm_domain`, and protected `board_config.json` from accidental overwrite unless `--force` is passed. |
| **`DEF-v1-09`** | `v1` | Pillars III & IV (`Firms 3, 4`) | `F3-V8..V10`, `F4-V3..V5` | `scripts/split_personas_to_files.py`; `personas/board_members/`; `personas/strike_teams_individual/` | Excluded `Category`/`Division` & ID-range headers (`0` stub files), transliterated `ø/æ/ł/ß/đ` (`soren_kierkegaard.md`), preserved `(Lu)` (`dr_lu_strict_alias_jian_guo.md`), stripped ` — <Role>` suffixes, and purged all `190` orphan `.md` files (`215` Board members + `245` Strike-Team mercenaries exact). |
| **`DEF-v1-10`** | `v1` | Pillars III & IV (`Firms 3, 4`) | `F3-V11`, `F3-V12`, `F4-V1`, `F4-V2` | `scripts/install.ps1`; `scripts/install.sh`; `skills/the-board/` | Added `personas` and `commands` to `install.ps1` and `install.sh` with clean destination sync, added target validation to `install.sh`, and mirrored root 100% into `skills/the-board/`. |
| **`DEF-v1-11`** | `v1` | Pillar IV (`Firm 4`) | `F4-V6`, `F4-V7`, `F4-V8` | `commands/board.md`; `gemini-extension.json`; `plugin.json`; `.claude-plugin/plugin.json`; `personas/*.md`; `references/domain_playbooks.md` | Fixed `the_self_aware_ghost_of_steve_jobs.md` + `marcus_aurelius.md`, added `"contextFileName": "SKILL.md"` to `gemini-extension.json`, updated `plugin.json` manifests with `<160`-char description, and synchronized legacy `personas/*.md` & `domain_playbooks.md` with `personas/boardrooms/*.md`. |
| **`DEF-v1-12`** | `v1` | Pillar V (`Firm 5`) | `F5-V1`, `F5-V2`, `F5-V5` | `README.md`; `examples/*.md` | Locked `Col 4..83` (`5 × 16 = 80`, spine at `Col 43`) `diff` ASCII topology diagram, added `[SECT // 06] SELF-HOSTED PROOF: WE RAN THE BOARD ON THE BOARD` with clickable links to `v1..vN` `transcripts/` and `examples/*.md`, and upgraded all 3 `examples/*.md` files with `Col 4..83` `diff` headers and real historical Board members. |
