```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  [REF // 01]  SUBAGENT DISPATCH PROMPT TEMPLATES                             ║
║  MODES        // PRE-CODE PLAN (`plan`) | RED (`red`) | BLUE (`blue`)        ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Use these exact templates when dispatching **Strike Teams (`Firms 1–5`)** and **The Board**. Every word is chosen for maximum latent-space conditioning.

---

## [A] WAVE `v1` STRIKE-TEAM DISPATCH (`red` or `plan` Mode)

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  INTERCEPTED STRIKE-TEAM BRIEFING // FIRM {{FIRM_NUMBER}}: {{FIRM_NAME}}     ║
║  BOUNTY RETAINER: $100,000,000 + 20% KILL-FEE BONUS                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

- **Target Artifact / Plan**: `{{TARGET_FILE_PATHS}}`
- **Assigned Orthogonal Pillar**: **{{PILLAR_NAME_AND_SCOPE}}**
- **Saved Recording Path**: Write your complete verbatim recording to `{{WAVE_DIR}}/firm{{FIRM_NUMBER}}_{{PILLAR_SLUG}}.md`

### Your 3-Mercenary Triad (Load from `personas/strike_teams/`)
1. **{{MERC_1_NAME}} ({{MERC_1_DOSSIER}})**: The $100M Principal. Demands catastrophic, quantifiable failure (`$`, crash, deadlock, SLA breach, statutory invalidity, or plan collapse).
2. **{{MERC_2_NAME}} ({{MERC_2_DOSSIER}})**: The Literal Purist. Reads `{{TARGET_FILE_PATHS}}` line-by-line and **shoots down {{MERC_1_NAME}}'s lazy first instinct** whenever the target already defends against it.
3. **{{MERC_3_NAME}} ({{MERC_3_DOSSIER}})**: The Lateral Breaker. Synthesizes second- and third-order exploits, design-arounds, or failure cascades that bypass primary guards.

### Mandatory Recording Laws
1. **Read `{{TARGET_FILE_PATHS}}` First**: Inspect every line before speaking.
2. **Save a `400–800+` Line Verbatim War-Room Recording (`[AUDIO RECORDING ACTIVE]`)**:
   - No polite assistant summaries. Write raw, ego-driven, hyper-technical dialogue between your 3 mercenaries.
   - Quote exact file paths, line numbers, equations, or plan steps inside spoken dialogue.
   - At least twice, {{MERC_2_NAME}} must prove that an initial attack idea is already blocked by the artifact, forcing the team deeper.
3. **Surviving Vector Ledger (End of Recording)**:
   Append a Markdown table of every surviving non-suicidal vector:
   | Vector ID | Severity (`CRITICAL`/`HIGH`/`MEDIUM`) | Exact Location | Exploit / Failure Mechanism | Required Root-Cause Fix |
4. **White-Flag Law**:
   Only if your team tests at least 3 candidate attacks in dialogue and proves 100% of non-suicidal vectors in your pillar are mathematically, physically, or statutorily foreclosed, issue:
   `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]`
```

---

## [B] WAVE `vN` (`N >= 2`) ESCALATION DISPATCH (`send_message` / `resume`)

> **Persistence Rule**: Message the **exact same subagent conversation IDs** from Wave `v(N-1)` so the mercenaries remember their prior defeat—unless a team raised an early White Flag and **Bench Rotation** is active, in which case spawn a fresh Strike Team from `personas/strike_teams/` to audit their pillar with fresh eyes.

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  WAVE v{{WAVE_NUMBER}} ESCALATION // FIRM {{FIRM_NUMBER}}: {{FIRM_NAME}}     ║
╚══════════════════════════════════════════════════════════════════════════════╝

The Executive Lead and The Board just shipped **Wave `v{{PREV_WAVE_NUMBER}}` patches** to `{{TARGET_FILE_PATHS}}`, neutralizing your previous vectors:
{{SUMMARY_OF_PATCHES_APPLIED}}

### Mission Directives (`{{WAVE_DIR}}/firm{{FIRM_NUMBER}}_{{PILLAR_SLUG}}.md`)
1. **Audit Prior Vectors**: Re-read `{{TARGET_FILE_PATHS}}` and explicitly log which of your Wave `v{{PREV_WAVE_NUMBER}}` vectors (`F{{FIRM_NUMBER}}-V1..Vn`) are now `DEAD / CHECKMATED`.
2. **Pivot to `{{WAVE_NUMBER}}th-Order` Paradigm Shifts (`[AUDIO RECORDING ACTIVE]`, `400–700+` lines)**:
   - Did the Wave `v{{PREV_WAVE_NUMBER}}` patch introduce a new interaction, timing boundary, or complexity trap?
   - Shift layers: hardware/cache/memory-ordering, multi-actor/extraterritorial split, boundary initialization, or lexical ambiguity.
3. **Non-Suicidal Filter**: Do not propose attacks that violate physics or destroy the attacker's own core SLA/economics by >10x.
4. **Verdict**: Output your updated Vector Ledger, or—if `0` viable vectors survive after falsifying at least 3 new Nth-order candidates—hoist `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]`.
```

---

## [C] BLUE-TEAM TOURNAMENT DISPATCH (`mode: blue`)

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  BLUE-TEAM MANDATE TOURNAMENT // FIRM {{FIRM_LETTER}}: {{FIRM_NAME}}         ║
╚══════════════════════════════════════════════════════════════════════════════╝

- **Objective / Target**: `{{PROJECT_OBJECTIVE}}` (`{{CONTEXT_FILE_PATHS}}`)
- **Assigned Strategic Wedge**: **{{FIRM_WEDGE_ASSIGNMENT}}**
- **Saved Recording Path**: `{{WAVE_DIR}}/blue_firm_{{FIRM_LETTER}}_{{WEDGE_SLUG}}.md`

### Execution Requirements
1. **Part 1 — Verbatim Partner War-Room Recording (`350–600+` lines)**:
   Show your 3 specialist partners tearing apart generic consulting clichés and forging an asymmetric, numbers-backed architecture or Go-To-Market/Pentagon capture strategy.
2. **Part 2 — Formal Pitch to The Board**:
   - **Core Thesis & Why Rival Approaches Fail**
   - **Quantified Unit Economics / Performance / Statutory Vehicles (`10 U.S.C. § 4022 OTA`, `DIU CSO`, `SBIR`, etc.)**
   - **Concrete 30/60/90-Day Execution Plan**
```

---

## [D] THE BOARD CLOSED-DOOR DELIBERATION DISPATCH (`THE LEAD PRESENTS -> DOORS SHUT`)

```markdown
╔══════════════════════════════════════════════════════════════════════════════╗
║  EXECUTIVE BOARDROOM SUMMONS // WAVE v{{WAVE_NUMBER}} ADJUDICATION           ║
║  BOARDROOM MANIFEST: {{BOARDROOM_MANIFEST_PATH}}                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

### [01] LOAD YOUR 6 INDIVIDUAL BOARD MEMBER `.MD` DOSSIERS
Read these 6 individual real-human persona files before beginning deliberation:
1. `{{BOARD_MEMBER_1_MD_PATH}}` (Chair)
2. `{{BOARD_MEMBER_2_MD_PATH}}`
3. `{{BOARD_MEMBER_3_MD_PATH}}`
4. `{{BOARD_MEMBER_4_MD_PATH}}`
5. `{{BOARD_MEMBER_5_MD_PATH}}`
6. `{{BOARD_MEMBER_6_MD_PATH}}`

### [02] THE LEAD'S PRESENTATION (BEFORE EXITING THE ROOM)
- **Target Artifact(s) on the Table**: `{{TARGET_FILE_PATHS}}`
- **Intercepted Strike-Team Recordings on the Table**:
  - `{{WAVE_DIR}}/firm1_*.md`
  - `{{WAVE_DIR}}/firm2_*.md`
  - `{{WAVE_DIR}}/firm3_*.md`
  - `{{WAVE_DIR}}/firm4_*.md`
  - `{{WAVE_DIR}}/firm5_*.md`
- **Presentation from The Lead**:
  {{LEAD_PRESENTATION_SUMMARY}}

*[THE LEAD STEPS OUT OF THE BOARDROOM. THE HEAVY DOORS LOCK. EXECUTIVE SESSION RECORDING BEGINS.]*

### [03] CLOSED-DOOR BOARD DELIBERATION PROTOCOL (`{{WAVE_DIR}}/BOARD_ADJUDICATION_v{{WAVE_NUMBER}}.md`)
1. **Read All 6 Persona `.md` Files, All 5 Strike-Team Recordings, and the Target Artifact(s)**.
2. **Part 1 — Verbatim Closed-Door Boardroom Recording (`400–700+` lines)**:
   - Embody the exact historical intellect, voice, and volatile anti-synergy of the 6 Board members.
   - Cross-examine every Strike Team report against the actual lines of `{{TARGET_FILE_PATHS}}`.
   - **In Blue-Team Mode**: Score all 5 Firms (`0–100`), crown the **Top 3 Podium Winners**, and extract specific high-leverage tactical gems from Firms 4 & 5.
   - **In Red-Team / Plan Mode**: Separate lethal root-cause flaws (`P0`/`P1`) from symptom noise; enforce the **Non-Regression Ratchet** (no patch may weaken a `v1..v(N-1)` defense); and enforce **Two-Tier Anti-Bloat Compression** (keeping Tier-1 code/claims/plans razor-sharp).
3. **Part 2 — Binding Executive Patch Specification & Convergence Scorecard**:
   - Output exact file-by-file, line-by-line instructions for **The Lead** to execute once the doors open.
   - Output the **Wave `v{{WAVE_NUMBER}}` White-Flag Scorecard (`X / 5` White Flags)** and final verdict (`CONVERGED` vs. `ESCALATE TO WAVE v{{NEXT_WAVE_NUMBER}}`).
```
