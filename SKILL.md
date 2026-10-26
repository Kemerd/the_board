---
name: the-board
description: >-
  Multi-agent persona-conditioned Red-Team, Blue-Team, Pre-Code Plan, and
  Executive Boardroom iterative convergence engine (v1 to vN until White Flag).
  Works in Claude Code, Google Antigravity (agy), Gemini CLI, Cursor, and Codex.
  Activate whenever the user invokes `/board`, asks to convene "The Board", run
  a Red-Team or Blue-Team tournament, torture-test an implementation plan before
  coding, or iterate code, hardware, legal/patent, design, philosophy, or
  commercial strategies until adversaries raise the white flag.
---

```diff
@@ ╔══════════════════════════════════════════════════════════════════════════════╗ @@
+  ║  ████████╗██╗  ██╗███████╗    ██████╗  ██████╗  █████╗ ██████╗ ██████╗       ║
+  ║  ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗      ║
+  ║     ██║   ███████║█████╗      ██████╔╝██║   ██║███████║██████╔╝██║  ██║      ║
+  ║     ██║   ██╔══██║██╔══╝      ██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║      ║
+  ║     ██║   ██║  ██║███████╗    ██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝      ║
+  ║     ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝       ║
@@ ╠══════════════════════════════════════════════════════════════════════════════╣ @@
!  ║  [SYS.UPLINK: ONLINE] // MULTI-AGENT ADVERSARIAL CONVERGENCE ENGINE v2.0     ║
!  ║  RUNTIMES // CLAUDE CODE | ANTIGRAVITY (AGY) | GEMINI CLI | CURSOR | CODEX   ║
-  ║  "Perfection has a price. And that price is more tokens."                    ║
+  ║  >>> WELCOME TO THE BOARD, CONSTITUENT.                                      ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

## [00] TERMINAL BOOT & DETERMINISTIC INTAKE GATE

1. **Always display the ASCII banner above** when activating `the-board`.
2. **Deterministic Two-Branch Intake Gate (`Interactive Intake` vs. `Direct Execution`)**:
   - **Branch A — Interactive Intake (`HALT & ASK`)**: If `target` is omitted or `$ARGUMENTS` is empty/ambiguous, **do NOT guess**. Greet the Constituent with the ASCII banner and invoke `ask_question` (or the 4-point intake prompt in [`commands/board.md`](./commands/board.md)) to lock: (1) `target`, (2) `mode` (`plan` | `red` | `blue` | `purple`), (3) `boardroom`, and (4) `effort` (`strike` | `standard` | `deep` | `white-flag` [alias: `relentless`]).
   - **Branch B — Direct Execution (`BIND DEFAULTS & RUN`)**: If `target` is explicitly supplied, deterministically bind any omitted optional parameters (`mode`: `plan` for pre-code plans/specs or `red` for existing code/IP/contracts; `boardroom`: domain-matched manifest from [`personas/boardrooms/*.md`](./personas/boardrooms/), defaulting to [`the_godfather_board.md`](./personas/boardrooms/the_godfather_board.md); `effort`: `standard`; `storage`: `folders` [`transcripts/v1..vN/`] or `branches` [`v1..vN` git branches with visible `transcripts/` at root]), echo the locked 5-field manifest, and execute Phase 0 immediately.

---

## [01] CROSS-RUNTIME SUBAGENT MAPPING

| Action | Google Antigravity (`agy`) / Gemini CLI | Claude Code (`claude`) | Single-Thread Fallback |
| :--- | :--- | :--- | :--- |
| **Spawn Strike Teams (`Wave v1`)** | Call `invoke_subagent` (`TypeName: "self"`) `K` times (`K=5` default; `K=1..2` for `strike`) in one turn | Call `Task` / `Agent` `K` times in a single message | Generate `firm1..K_*.md` in `transcripts/v1/` (or `transcripts/` on branch `v1`) |
| **Re-Challenge (`Wave v2..vN`)** | Call `send_message` to the **existing `conversationId`s** (or spawn a bench replacement when a Firm raises an early White Flag in `deep` / `white-flag` tiers) | Resume existing agent IDs (`resume`) or pass `v(N-1)` `firmK_*.md` paths to parallel `Task` calls | Read `v(N-1)` tapes and write `vN` `firm1..K_*.md` |
| **Convene The Board** | Call `invoke_subagent` / `send_message`: **The Lead** presents via the prompt, then exits as the Boardroom doors lock | Call `Task` / `Agent` with the `6–7` Board member `.md` files, `CONVERGENCE_TRACKER.md`, target files, and the 5 Strike Team transcript paths | Write `BOARD_ADJUDICATION_vN.md` |
| **Patch & Verify** | Edit files (`edit_file`/`write_file`) + run deterministic checks (`run_command`) | Edit files (`Edit`/`Write`) + run deterministic checks (`Bash`) | Edit files and run verification commands |

---

## [02] TWO-TIER PERSONA ARCHITECTURE (WHY THIS WORKS)

Ten apparent synonyms do not carry identical weight in a transformer's latent space. Every word in a subagent dispatch prompt must be surgical. `the-board` separates **Strike Teams** from **The Board**:

1. **STRIKE TEAMS (`Firms 1–5` — Over-The-Top `$100M` Mercenaries)**:
   - Drawn from [`personas/strike_teams/`](./personas/strike_teams/) and [`personas/strike_teams_individual/`](./personas/strike_teams_individual/) (`245` standalone `.md` dossiers across 7 syndicates).
   - Staffed with hyper-embellished specialists (`$100M` kill-fee bounty, triple PhDs, obsessive domain scars).
   - Each Firm is a **3-Persona Triad** recorded on a **saved verbatim war-room tape (`firmK_<pillar>.md`, `400–800+` lines)**:
     - **Mask 1 (The $100M Principal)**: Demands catastrophic, quantifiable failure or 10x leverage.
     - **Mask 2 (The Literal Purist)**: Reads the target artifact line-by-line and **shoots down Mask 1's lazy first instinct** when the artifact already defends against it.
     - **Mask 3 (The Lateral Breaker / Builder)**: Synthesizes Nth-order exploits, design-arounds, or architectures.
2. **THE BOARD (`6–7 Real Historical Humans Locked Behind Closed Doors`)**:
   - Each Board member is an individual `.md` file in [`personas/board_members/<category>/<person>.md`](./personas/board_members/) (`215` standalone `.md` dossiers across 6 categories).
   - Fictional specialist personas (`"Viktor K., 20-year kernel lead"`) give the model a narrow role constraint. **Real historical geniuses (`Alan Turing`, `John von Neumann`, `Nikola Tesla`, `Albert Einstein`, `The Self-Aware Ghost of Steve Jobs`, `Epictetus`, `Emperor Marcus Aurelius`, `Claude Shannon`)** unlock something far heavier: **thousands of pages of primary-source proofs, lectures, biographies, letters, and cognitive signatures already embedded in the model's weights**. When you seat **Nikola Tesla** across the table from **Alan Turing**, **Epictetus**, **Emperor Marcus Aurelius**, and **The Self-Aware Ghost of Steve Jobs**, the model cannot output mediocre corporate filler without violating the deepest statistical priors in its training distribution. Expected output: **genius** (99.9th-percentile primary-source rigor, zero-hedging root-cause adjudication, and non-regressive structural synthesis).
   - A **Boardroom** ([`personas/boardrooms/*.md`](./personas/boardrooms/)) is a manifest of **`6–7` `.md` file paths** selected for **synergy and volatile anti-synergy** (people who would fiercely argue if locked in a room together).
   - **Closed-Door Choreography**: **The Lead** walks in via the subagent prompt, presents the artifact/plan, `CONVERGENCE_TRACKER.md`, and the 5 Strike Team tapes, and leaves. **The doors lock (`[DOORS SEALED // EXECUTIVE SESSION RECORDING ACTIVE]`)**. The `6–7` Board members deliberate verbatim, grade the Strike Teams, crown the **Top 3 Podium Winners** while salvaging tactical gems from Firms 4–5 (`blue` mode) or adjudicate **100% of surviving root-cause vectors across all 5 orthogonal pillars** (`red` / `plan` / `purple` modes), enforce the **Non-Regression Ratchet**, and issue a binding **Executive Patch Specification** (`BOARD_ADJUDICATION_vN.md`).

---

## [03] FOUR OPERATING MODES

- **`plan` (Pre-Code / Pre-Execution Plan Siege)**: Run **The Board** on an **Implementation Plan, Architecture Spec, or Action Plan** *before* executing or writing production code. Strike Teams and The Board audit the Plan `.md` **against the actual existing codebase/interfaces on disk** and require an executable **Deterministic Verification & Post-Condition Matrix** before transitioning to code.
- **`red` (Adversarial Red-Team Siege)**: 5 hostile Strike Teams attack code, hardware, contracts, or patent claims across waves `v1..vN` until `5/5` hoist a verified **White Flag (`0` surviving non-suicidal vectors)**.
- **`blue` (Blue-Team Tournament)**: 5 specialist boutiques compete to pitch the sharpest architecture, product design, or commercial/Pentagon (`DIU/OTA/SBIR`) strategy. The Board scores all 5 (`0–100`), crowns the **Top 3 Podium Winners**, and **The Lead** synthesizes the Master Playbook (iterating until `>= 95/100` Board ratification with `0` blocking objections if run multi-wave).
- **`purple` (Purple-Team Hybrid)**: Blue Teams compete to build the system in Wave `v1`; Red Teams ruthlessly attack, exploit, and falsify the unified winner in Waves `v2..vN` until `5/5` verified White Flags.

---

## [04] STEP-BY-STEP EXECUTION PROTOCOL FOR THE LEAD

### Phase 0: Scaffold Transcripts Workspace & Select `6–7` Board Member `.md` Files
1. Read target files (and the codebase files touched by the plan if in `plan` mode).
2. Run [`scripts/init_board_workspace.py`](./scripts/init_board_workspace.py) using either:
   - **Folder Mode (default, `--strategy folders`)**: Stores wave transcripts in visible `transcripts/v1/`, `transcripts/v2/`, ..., `transcripts/vN/` directories (never hidden dot-folders).
   - **Branch Mode (`--strategy branches`)**: Stores Wave `v1` transcripts in `transcripts/` on branch `v1`; applies Wave `v1` patches onto branch `v2` and saves Wave `v2` transcripts in `transcripts/` on branch `v2`; and repeats across branches `v1 -> v2 -> ... -> vN` (excluding `transcripts/` only when merging the final converged code into `main`).
3. Partition the target into **5 mutually exclusive, collectively exhaustive orthogonal pillars (`Pillars I–V`; zero jurisdictional overlap)** (or `1–2` pillars for quick `strike` runs).
4. Pick a Boardroom manifest from [`personas/boardrooms/`](./personas/boardrooms/) (e.g., [`the_godfather_board.md`](./personas/boardrooms/the_godfather_board.md))—or assemble a custom list of **`6–7` `.md` files** from [`personas/board_members/<category>/`](./personas/board_members/).

### Phase 1: Dispatch Strike Teams (`Wave vN`) — Saved Verbatim Recordings
1. Spawn Strike Teams `1..K` in parallel using [`references/prompt_templates.md`](./references/prompt_templates.md) and persona dossiers from [`personas/strike_teams/`](./personas/strike_teams/).
2. **Mandatory Recording Laws**:
   - **Save Every Transcript**: Each subagent MUST write its full `400–800+` line verbatim war-room recording to `firmK_<pillar>.md` inside the active wave's `transcripts/` directory.
   - **Exact Citations & Internal Pushback**: Characters must quote exact line numbers, equations, or clauses, and Mask 2 must reject at least two naive theories from Mask 1 that the target already handles.
   - **Wave `v2..vN` Escalation, Bench Rotation & Cross-Pillar Diff Re-Verification**: By default, message the **same subagent IDs** so they remember their Wave `v(N-1)` defeat and invent `Nth-order` attacks. In `deep` and `white-flag`/`relentless` tiers, **Bench Rotation is enabled by default** whenever a Firm raises an early White Flag while `< 5/5` Firms have converged (rotating in a fresh reserve Strike Team from [`personas/strike_teams/`](./personas/strike_teams/) to audit that pillar with fresh eyes), and any previously White-Flagged pillar must re-verify non-regression whenever shared target files are modified.
   - **Earned White Flag Only**: A Firm may output `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]` only after testing and falsifying at least **3 non-suicidal, steel-manned candidate Nth-order vectors** anchored to exact target lines and refuted line-by-line by Mask 2 (suicidal straw-men are strictly banned).

### Phase 2: Present to THE BOARD & Shut the Doors
1. Once `firm1..K_*.md` are saved on disk, launch **The Board** subagent (`BOARD_ADJUDICATION_vN.md`).
2. Instruct The Board subagent to read the **`6–7` selected Board member `.md` files** (`personas/board_members/...`), `CONVERGENCE_TRACKER.md`, the target artifact, and all Strike Team recordings.
3. Inside `BOARD_ADJUDICATION_vN.md`, The Board records:
   - **Part 1 (`[DOORS SEALED // EXECUTIVE SESSION RECORDING ACTIVE]`)**: Verbatim closed-door deliberation (`400–700+` lines) among the `6–7` historical executives—clashing in-character, auditing every Strike Team vector against the raw files, crowning the **Top 3 Podium Winners** (`blue` mode) or adjudicating **100% of surviving vectors across Pillars I–V** (`red`/`plan`/`purple` modes), enforcing the **Unanimous Falsification Veto** (no valid vector may be dismissed without a concrete line-level proof), exercising **White-Flag Revocation Authority (`[WHITE FLAG REVOKED BY BOARD]`)** against any premature surrender, enforcing the **Non-Regression Ratchet** (`DEF-v1..v(N-1)`), and enforcing **Two-Tier Anti-Bloat Compression**.
   - **Part 2 (`BINDING EXECUTIVE PATCH SPECIFICATION`)**: Exact file-by-file, line-by-line edits, new `DEF-vN-XX` ratchet rows, and the **Wave `vN` White-Flag Scorecard (`X / 5`)**.

### Phase 3: Apply Patch Spec & Run Deterministic Verification
1. **The Lead** applies the Board's Patch Spec directly to the target files (in Branch Mode, on branch `v(N+1)`), fixing root causes, never symptoms, and preserving 100% of working functionality, then appends the new `DEF-vN-XX` rows and White-Flag tally into `CONVERGENCE_TRACKER.md`.
2. Run deterministic checks immediately (`compiler`, `unit tests`, `linter`, `statutory/claim-numeral checks`, and [`scripts/verify_convergence.py`](./scripts/verify_convergence.py) with `--check-links`).

### Phase 4: Loop Until `5/5` White Flags + Final Sync (`v(N).5` & `v(N+1)`)
1. If `< 5/5` White Flags and `N < max_waves`, loop immediately to **Phase 1 (`Wave v(N+1)`)**.
2. Once `5/5` White Flags are verified (`verify_convergence.py` exit code `0`):
   - If running in **`plan` mode**: if the user's prompt authorized end-to-end implementation, transition immediately to executing the converged plan and verifying its Post-Condition Matrix; if the user requested plan verification only, present the converged `vN` plan and await confirmation.
   - Run **Stage `v(N).5` (Data / Benchmark / Diagram Sync)** and **Stage `v(N+1)` (Final Board Sign-Off)** so every metric, test, and document is 100% aligned.

---

## [05] MODULAR INDEX (LOAD ON DEMAND)

- **Individual Board Member Dossiers (`215` real historical figures, `1 .md per person`)**: [`personas/board_members/INDEX.md`](./personas/board_members/INDEX.md) (`computing/`, `physics_hardware/`, `design_product/`, `philosophy_logic/`, `strategy_command/`, `law_rhetoric/`)
- **Pre-Selected Boardroom Manifests (`8` Boardrooms)**: [`personas/boardrooms/`](./personas/boardrooms/) (including [`the_godfather_board.md`](./personas/boardrooms/the_godfather_board.md))
- **`$100M` Mercenary Strike-Team Vault (`245` mercenaries across `7` syndicates)**: [`personas/strike_teams/`](./personas/strike_teams/) & [`personas/strike_teams_individual/INDEX.md`](./personas/strike_teams_individual/INDEX.md)
- **Dispatch Prompt Templates**: [`references/prompt_templates.md`](./references/prompt_templates.md)
- **Effort Dial, Ratchet & White-Flag Protocol**: [`references/effort_and_white_flag.md`](./references/effort_and_white_flag.md)
- **Latent-Space Mask Theory**: [`references/persona_mask_theory.md`](./references/persona_mask_theory.md)
- **Domain Playbooks**: [`references/domain_playbooks.md`](./references/domain_playbooks.md)
- **Automation Scripts**: [`scripts/init_board_workspace.py`](./scripts/init_board_workspace.py), [`scripts/verify_convergence.py`](./scripts/verify_convergence.py), & [`scripts/split_personas_to_files.py`](./scripts/split_personas_to_files.py)
