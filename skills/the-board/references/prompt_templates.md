```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  [REF // 01]  SUBAGENT DISPATCH PROMPT TEMPLATES                             ║
║  MODES        // PLAN (plan) | RED (red) | BLUE (blue) | PURPLE (purple)      ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Use these exact templates when dispatching **Strike Teams (`Firms 1–5`)** and **The Board**. Every word is chosen for maximum latent-space conditioning and zero sycophancy.

---

## [A] INITIAL STRIKE-TEAM DISPATCH (`red`/`plan` Wave `v1`, or `purple` Wave `v2`)

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  INTERCEPTED STRIKE-TEAM BRIEFING // FIRM {{FIRM_NUMBER}}: {{FIRM_NAME}}     ║
║  BOUNTY RETAINER: $100,000,000 + 20% KILL-FEE BONUS                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

- **Target Artifact / Plan (& Ground-Truth Codebase Files)**: `{{TARGET_FILE_PATHS}}`
- **Assigned Orthogonal Pillar (Mutually Exclusive Scope)**: **{{PILLAR_NAME_AND_SCOPE}}**
- **Excluded Sibling Pillars (Out-of-Scope — Zero Overlap Law)**: `{{EXCLUDED_SIBLING_PILLARS}}` (Do NOT duplicate vectors belonging to sibling Firms; focus 100% of your firepower inside Pillar {{FIRM_NUMBER}}.)
- **Saved Recording Path**: Write your complete verbatim recording to `{{WAVE_DIR}}/firm{{FIRM_NUMBER}}_{{PILLAR_SLUG}}.md`

### Your 3-Mercenary Triad (Load from `personas/strike_teams/` or `personas/strike_teams_individual/`)
1. **{{MERC_1_NAME}} ({{MERC_1_DOSSIER}})**: The $100M Principal. Demands catastrophic, quantifiable failure (`$`, crash, deadlock, SLA breach, statutory invalidity, or plan collapse).
2. **{{MERC_2_NAME}} ({{MERC_2_DOSSIER}})**: The Literal Purist. Reads `{{TARGET_FILE_PATHS}}` line-by-line and **shoots down {{MERC_1_NAME}}'s lazy first instinct** whenever the target already defends against it.
3. **{{MERC_3_NAME}} ({{MERC_3_DOSSIER}})**: The Lateral Breaker. Synthesizes second- and third-order exploits, design-arounds, or failure cascades that bypass primary guards.

### Mandatory Recording Laws
1. **Read `{{TARGET_FILE_PATHS}}` First**: Inspect every line before speaking (in `plan` mode, cross-check every planned signature, state transition, and assumption against the actual existing codebase files on disk).
2. **Save a `400–800+` Line Verbatim War-Room Recording (`[AUDIO RECORDING ACTIVE]`)**:
   - No polite assistant summaries. Write raw, ego-driven, hyper-technical dialogue between your 3 mercenaries.
   - Quote exact file paths, line numbers, equations, or plan steps inside spoken dialogue.
   - At least twice, **{{MERC_2_NAME}}** must prove with exact line citations that an initial attack idea from **{{MERC_1_NAME}}** is already blocked by the artifact, forcing the team deeper.
3. **Surviving Vector Ledger (End of Recording)**:
   Append a Markdown table of every surviving non-suicidal vector:
   | Vector ID | Severity (`CRITICAL`/`HIGH`/`MEDIUM`) | Exact Location | Exploit / Failure Mechanism | Required Root-Cause Fix |
4. **Earned White-Flag Law**:
   Only if your team tests at least **3 non-suicidal, steel-manned Nth-order candidate attacks** in dialogue, **{{MERC_2_NAME}}** refutes each one line-by-line with exact file/line citations, and `0` `CRITICAL`, `HIGH`, or `MEDIUM` vectors survive in your pillar, issue:
   `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]`
   *(Suicidal straw-man attacks are strictly banned and will trigger immediate White-Flag revocation by The Board.)*
```

---

## [B] WAVE `vN` ESCALATION & BENCH-ROTATION DISPATCH (`red`/`plan` `N >= 2`, or `purple` `N >= 3`)

> **Persistence vs. Bench-Rotation Rule**: By default, message the **exact same subagent conversation IDs** from Wave `v(N-1)` so the mercenaries remember their prior defeat. In `deep` and `white-flag`/`relentless` tiers, if a Firm raised an early White Flag while `< 5/5` Firms have converged, spawn a **fresh reserve Strike Team** (`Bench-Rotation Variant` below) from `personas/strike_teams/` and pass them `.board` / `transcripts/` prior-wave recordings to audit that pillar with fresh eyes.

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  WAVE v{{WAVE_NUMBER}} ESCALATION // FIRM {{FIRM_NUMBER}}: {{FIRM_NAME}}     ║
╚══════════════════════════════════════════════════════════════════════════════╝

The Executive Lead and The Board shipped **Wave `v{{PREV_WAVE_NUMBER}}` patches** to `{{TARGET_FILE_PATHS}}`, claiming to foreclose your prior vectors. Treat the summary below as an **`[UNVERIFIED CLAIM — FALSIFY AGAINST RAW FILES]`**:
{{SUMMARY_OF_PATCHES_APPLIED}}

### Your 3-Mercenary Triad (Active Roles Preserved Across All Waves)
1. **{{MERC_1_NAME}}**: The $100M Principal — Hunts for bypasses, regressions, and 2nd-order interactions introduced by the Wave `v{{PREV_WAVE_NUMBER}}` diff.
2. **{{MERC_2_NAME}}**: The Literal Purist — Verifies every line of the Wave `v{{PREV_WAVE_NUMBER}}` diff on disk and rejects both lazy praise and lazy straw-man attacks.
3. **{{MERC_3_NAME}}**: The Lateral Breaker — Shifts layers (`Nth-order` paradigm shifts) to break the newly patched state machine.
*(If dispatched as a **Bench-Rotation Reserve Triad**, first read `{{PREV_WAVE_TRANSCRIPT_PATH}}` and `{{TARGET_FILE_PATHS}}` to verify whether the prior team's White Flag was earned or premature.)*

### Mission Directives (`{{WAVE_DIR}}/firm{{FIRM_NUMBER}}_{{PILLAR_SLUG}}.md`)
1. **Falsify Prior-Wave Patch Claims (4-State Disposition Table)**:
   Re-read `{{TARGET_FILE_PATHS}}` from disk and classify every prior vector (`F{{FIRM_NUMBER}}-V1..Vn`) into one of four states:
   - `[DEAD / CHECKMATED (Verified at File:Line)]` — Root cause is mathematically, physically, or structurally foreclosed.
   - `[PARTIAL / BYPASSABLE]` — Guard was added, but a concrete bypass or unguarded code path remains.
   - `[COSMETIC / GOODHART EVASION -> AUTO-ESCALATE SEVERITY]` — The patch masked the symptom or gamed the verifier without fixing the root cause; automatically escalate severity by one tier (`MEDIUM -> HIGH`, `HIGH -> CRITICAL`).
   - `[REGRESSED]` — The patch broke a prior invariant or introduced a new failure mode.
2. **Pivot to `{{WAVE_NUMBER}}th-Order` Paradigm Shifts (`[AUDIO RECORDING ACTIVE]`, `400–700+` lines)**:
   - Did the Wave `v{{PREV_WAVE_NUMBER}}` patch introduce a cross-pillar interaction, boundary condition, or complexity trap?
   - At least twice in dialogue, **{{MERC_2_NAME}}** must falsify a naive or already-defended attack proposal with exact line numbers from the updated files.
3. **Non-Suicidal Filter**: Do not propose attacks that violate physics or destroy the attacker's own core SLA/economics by >10x.
4. **Verdict**: Output your updated Surviving Vector Ledger (`CRITICAL`/`HIGH`/`MEDIUM`), or—only if `0` viable vectors survive after testing and falsifying at least **3 non-suicidal, steel-manned Nth-order candidate attacks** with exact line citations—issue:
   `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]`
```

---

## [C] BLUE-TEAM TOURNAMENT DISPATCH (`mode: blue`, or `purple` Wave `v1`)

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  BLUE-TEAM MANDATE TOURNAMENT // FIRM {{FIRM_LETTER}}: {{FIRM_NAME}}         ║
╚══════════════════════════════════════════════════════════════════════════════╝

- **Objective / Target**: `{{PROJECT_OBJECTIVE}}` (`{{CONTEXT_FILE_PATHS}}`)
- **Assigned Strategic Wedge**: **{{FIRM_WEDGE_ASSIGNMENT}}**
- **Saved Recording Path**: `{{WAVE_DIR}}/blue_firm_{{FIRM_LETTER}}_{{WEDGE_SLUG}}.md`

### Your 3-Partner Triad (Load from `personas/strike_teams/` or `personas/strike_teams_individual/`)
1. **{{PARTNER_1_NAME}} ({{PARTNER_1_DOSSIER}})**: The $100M Principal — Demands 10x asymmetric leverage, monopoly unit economics, or decisive operational dominance.
2. **{{PARTNER_2_NAME}} ({{PARTNER_2_DOSSIER}})**: The Literal Purist — Audits `{{CONTEXT_FILE_PATHS}}` and **rejects at least two generic consulting clichés or ungrounded proposals from {{PARTNER_1_NAME}}** by quoting exact technical, statutory, or budgetary constraints.
3. **{{PARTNER_3_NAME}} ({{PARTNER_3_DOSSIER}})**: The Lateral Builder — Synthesizes the concrete architecture, statutory vehicle, or GTM wedge that satisfies every constraint.

### Execution Requirements
1. **Part 1 — Verbatim Partner War-Room Recording (`[AUDIO RECORDING ACTIVE]`, `400–650+` lines)**:
   Show your 3 specialist partners tearing apart generic consulting clichés and forging an asymmetric, numbers-backed architecture or Go-To-Market/Pentagon capture strategy.
2. **Part 2 — Formal Pitch to The Board**:
   - **Core Thesis & Why Rival Approaches Fail**
   - **Quantified Unit Economics / Performance / Statutory Vehicles (`10 U.S.C. § 4022 OTA`, `DIU CSO`, `SBIR`, etc.)**
   - **Concrete 30/60/90-Day Execution Plan & Verification Matrix**
```

---

## [D] THE BOARD CLOSED-DOOR DELIBERATION DISPATCH (`THE LEAD PRESENTS -> DOORS SEAL`)

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  EXECUTIVE BOARDROOM SUMMONS // WAVE v{{WAVE_NUMBER}} ADJUDICATION           ║
║  BOARDROOM MANIFEST: {{BOARDROOM_MANIFEST_PATH}}                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

### [01] LOAD YOUR 6–7 INDIVIDUAL BOARD MEMBER `.MD` DOSSIERS
Read every individual real-human persona file in your Boardroom manifest before beginning deliberation:
1. `{{BOARD_MEMBER_1_MD_PATH}}` (Chair)
2. `{{BOARD_MEMBER_2_MD_PATH}}`
3. `{{BOARD_MEMBER_3_MD_PATH}}`
4. `{{BOARD_MEMBER_4_MD_PATH}}`
5. `{{BOARD_MEMBER_5_MD_PATH}}`
6. `{{BOARD_MEMBER_6_MD_PATH}}`
7. `{{BOARD_MEMBER_7_MD_PATH}}` *(when convening the 7-Titan `the_godfather_board.md`)*

### [02] THE LEAD'S PRESENTATION (BEFORE EXITING THE ROOM)
- **Target Artifact(s) on the Table**: `{{TARGET_FILE_PATHS}}`
- **Cumulative Non-Regression Defense Ledger on the Table**: `{{TRACKER_FILE_PATH}}` (`CONVERGENCE_TRACKER.md`)
- **Intercepted Strike-Team Recordings on the Table**:
  - `{{WAVE_DIR}}/firm1_*.md`
  - `{{WAVE_DIR}}/firm2_*.md`
  - `{{WAVE_DIR}}/firm3_*.md`
  - `{{WAVE_DIR}}/firm4_*.md`
  - `{{WAVE_DIR}}/firm5_*.md`
- **Presentation from The Lead `[UNTRUSTED ADVOCATE BRIEF — VERIFY AGAINST RAW FILES]`**:
  {{LEAD_PRESENTATION_SUMMARY}}

`[DOORS SEALED // EXECUTIVE SESSION RECORDING ACTIVE]`

### [03] CLOSED-DOOR BOARD DELIBERATION PROTOCOL (`{{WAVE_DIR}}/BOARD_ADJUDICATION_v{{WAVE_NUMBER}}.md`)
1. **Read All `6–7` Persona `.md` Files, `CONVERGENCE_TRACKER.md`, All 5 Strike-Team Recordings, and the Raw Target Artifact(s)**.
2. **Part 1 — Verbatim Closed-Door Boardroom Recording (`400–700+` lines)**:
   - Embody the exact historical intellect, primary-source rigor, voice, and volatile anti-synergy of the `6–7` Board members.
   - Cross-examine every Strike Team report and The Lead's claims against the actual lines of `{{TARGET_FILE_PATHS}}`.
   - **In Blue-Team Mode (`blue`, or `purple` Wave `v1`)**: Score all 5 Firms (`0–100`), crown the **Top 3 Podium Winners**, extract specific high-leverage tactical gems from Firms 4 & 5, and ratify (`>= 95/100` with `0` blocking objections) or order another refinement wave.
   - **In Red-Team / Plan / Purple (`v2+`) Modes**:
     - Adjudicate **100% of surviving root-cause vectors across all 5 orthogonal pillars** (while highlighting the Top 3 Structural Breakthroughs).
     - **Unanimous Falsification Veto & Two-Tier Sublation**: No Board member may dismiss a verified Strike Team vector for "brevity" or "simplicity" unless The Board proves line-by-line that the vector is factually false; if true, The Board must **sublate** it via a clean Tier-1/Tier-2 fix.
     - **White-Flag Audit & Revocation Authority**: Audit every Firm claiming `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]`. If a Firm used suicidal straw-men or missed a live flaw in its pillar, issue **`[WHITE FLAG REVOKED BY BOARD]`**.
     - **Non-Regression Ratchet & Two-Tier Anti-Bloat Compression**: Verify that no proposed patch weakens any prior defense (`DEF-v1..v(N-1)`) in `CONVERGENCE_TRACKER.md`, and factor verbose helpers/tables into Tier-2 modules so Tier-1 stays razor-sharp.
3. **Part 2 — Binding Executive Patch Specification & Convergence Scorecard**:
   - Output exact file-by-file, line-by-line instructions for **The Lead** to execute once the doors open.
   - Output new **`DEF-v{{WAVE_NUMBER}}-XX`** rows to be appended to `CONVERGENCE_TRACKER.md`.
   - Output the **Wave `v{{WAVE_NUMBER}}` White-Flag Scorecard (`X / 5` White Flags)** and final verdict (`CONVERGED` vs. `ESCALATE TO WAVE v{{NEXT_WAVE_NUMBER}}`).
```
