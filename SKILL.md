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
!  ║  [SYS.UPLINK: ONLINE] // MULTI-AGENT ADVERSARIAL CONVERGENCE ENGINE          ║
-  ║  "Perfection has a price. And that price is more tokens."                    ║
+  ║  >>> WELCOME TO THE BOARD, CONSTITUENT.                                      ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

## [00] TERMINAL BOOT & INTERACTIVE INTAKE

1. **Always display the ASCII banner above** when activating `the-board`.
2. **Interactive Intake vs. Direct Execution**:
   - If the user's request omits the target, mode (`plan` | `red` | `blue` | `purple`), Boardroom roster, or effort tier (`strike` | `standard` | `deep` | `white-flag`), **ask the user via `ask_question` (or a concise 4-point terminal prompt)** before spawning subagents.
   - If the user supplies sufficient parameters, lock the manifest and execute Phase 0 immediately.

---

## [01] CROSS-RUNTIME SUBAGENT MAPPING

| Action | Google Antigravity (`agy`) / Gemini CLI | Claude Code (`claude`) | Single-Thread Fallback |
| :--- | :--- | :--- | :--- |
| **Spawn Strike Teams (`Wave v1`)** | Call `invoke_subagent` (`TypeName: "self"`) `K` times (`K=5` default; `K=1..2` for `strike`) in one turn | Call `Task` / `Agent` `K` times in a single message | Generate `.board/v1/firm1..K_*.md` sequentially |
| **Re-Challenge (`Wave v2..vN`)** | Call `send_message` to the **existing `conversationId`s** (or spawn a bench replacement if a team raised an early White Flag and rotation is enabled) | Resume existing agent IDs (`resume`) or pass `.board/v(N-1)/firmK_*.md` to parallel `Task` calls | Read `v(N-1)` tapes and write `vN/firm1..K_*.md` |
| **Convene The Board** | Call `invoke_subagent` / `send_message`: **The Lead** presents via the prompt, then exits as the Boardroom doors shut | Call `Task` / `Agent` with the 6 Board member `.md` files and the 5 Strike Team transcript paths | Write `.board/vN/BOARD_ADJUDICATION_vN.md` |
| **Patch & Verify** | Edit files (`edit_file`/`write_file`) + run deterministic checks (`run_command`) | Edit files (`Edit`/`Write`) + run deterministic checks (`Bash`) | Edit files and run verification commands |

---

## [02] TWO-TIER PERSONA ARCHITECTURE (WHY THIS WORKS)

Ten apparent synonyms do not carry identical weight in a transformer's latent space. Every word in a subagent dispatch prompt must be surgical. `the-board` separates **Strike Teams** from **The Board**:

1. **STRIKE TEAMS (`Firms 1–5` — Over-The-Top `$100M` Mercenaries)**:
   - Drawn from [`personas/strike_teams/`](./personas/strike_teams/) (or synthesized dynamically).
   - Staffed with hyper-embellished specialists (`$100M` kill-fee bounty, triple PhDs, obsessive domain scars).
   - Each Firm is a **3-Persona Triad** recorded on a **saved verbatim war-room tape (`.board/vN/firmK_<pillar>.md`, `400–800+` lines)**:
     - **Mask 1 (The $100M Principal)**: Demands catastrophic, quantifiable failure or 10x leverage.
     - **Mask 2 (The Literal Purist)**: Reads the target artifact line-by-line and **shoots down Mask 1's lazy first instinct** when the artifact already defends against it.
     - **Mask 3 (The Lateral Breaker / Builder)**: Synthesizes Nth-order exploits, design-arounds, or architectures.
2. **THE BOARD (`6 Real Historical Humans Locked Behind Closed Doors`)**:
   - Each Board member is an individual `.md` file in [`personas/board_members/<category>/<person>.md`](./personas/board_members/).
   - Fictional specialist personas (`"Viktor K., 20-year kernel lead"`) give the model a narrow role constraint. **Real historical geniuses (`Alan Turing`, `John von Neumann`, `Nikola Tesla`, `Albert Einstein`, `The Ghost of Steve Jobs`, `Epictetus`)** unlock something far heavier: **thousands of pages of primary-source proofs, lectures, biographies, letters, and cognitive signatures already embedded in the model's weights**. When you seat **Nikola Tesla** across the table from **Alan Turing**, **Epictetus**, and **The Self-Aware Ghost of Steve Jobs**, the model cannot output mediocre corporate filler without violating the deepest statistical priors in its training distribution. Expected output: **genius**.
   - A **Boardroom** ([`personas/boardrooms/*.md`](./personas/boardrooms/)) is a manifest of **6 `.md` file paths** selected for **synergy and volatile anti-synergy** (people who would fiercely argue if locked in a room together).
   - **Closed-Door Choreography**: **The Lead** walks in via the subagent prompt, presents the artifact/plan and the 5 Strike Team tapes, and leaves. **The doors lock (`[DOORS SEALED // EXECUTIVE SESSION RECORDING]`)**. The 6 Board members deliberate verbatim, grade the Strike Teams, pick the **Top 3** (or synthesize all 5), enforce the **Non-Regression Ratchet**, and issue a binding **Executive Patch Specification** (`.board/vN/BOARD_ADJUDICATION_vN.md`).

---

## [03] FOUR OPERATING MODES

- **`plan` (Pre-Code / Pre-Execution Plan Siege)**: Run **The Board** on an **Implementation Plan, Architecture Spec, or Action Plan** *before* executing or writing production code. Eliminates flawed state machines, bad abstractions, and sequencing traps on the whiteboard.
- **`red` (Adversarial Red-Team Siege)**: 5 hostile Strike Teams attack code, hardware, contracts, or patent claims across waves `v1..vN` until `5/5` hoist a verified **White Flag (`0` surviving non-suicidal vectors)**.
- **`blue` (Blue-Team Tournament)**: 5 specialist boutiques compete to pitch the sharpest architecture, product design, or commercial/Pentagon (`DIU/OTA/SBIR`) strategy. The Board scores all 5, crowns the **Top 3 Podium Winners**, and **The Lead** synthesizes the Master Playbook.
- **`purple` (Purple-Team Hybrid)**: Blue Teams compete to build the system in Wave `v1`; Red Teams ruthlessly attack the unified winner in Waves `v2..vN` until `5/5` White Flags.

---

## [04] STEP-BY-STEP EXECUTION PROTOCOL FOR THE LEAD

### Phase 0: Scaffold `.board/v1/` & Select the 6 Board Member `.md` Files
1. Read target files (or draft the initial Implementation Plan if in `plan` mode).
2. Run [`scripts/init_board_workspace.py`](./scripts/init_board_workspace.py) (or create `.board/v1/` and `.board/CONVERGENCE_TRACKER.md`).
3. Partition the target into **5 strictly orthogonal pillars (`Pillars I–V`)** (or `1–2` pillars for quick `strike` runs).
4. Pick a Boardroom manifest from [`personas/boardrooms/`](./personas/boardrooms/) (e.g., `the_godfather_board.md`)—or assemble a custom list of **6 `.md` files** from [`personas/board_members/<category>/`](./personas/board_members/) when a unique challenge requires a bespoke combination of historical minds.

### Phase 1: Dispatch Strike Teams (`Wave vN`) — Saved Verbatim Recordings
1. Spawn Strike Teams `1..K` in parallel using [`references/prompt_templates.md`](./references/prompt_templates.md) and persona dossiers from [`personas/strike_teams/`](./personas/strike_teams/).
2. **Mandatory Recording Laws**:
   - **Save Every Transcript**: Each subagent MUST write its full `400–800+` line verbatim war-room recording to `.board/vN/firmK_<pillar>.md`.
   - **Exact Citations & Internal Pushback**: Characters must quote exact line numbers, equations, or clauses, and Mask 2 must reject at least two naive theories from Mask 1 that the target already handles.
   - **Wave `v2..vN` Escalation vs. Bench Rotation**: By default, message the **same subagent IDs** so they remember their Wave `v(N-1)` defeat and invent `Nth-order` attacks. Optionally, if a Firm raises an early White Flag while others fight on, rotate in a fresh reserve Strike Team from [`personas/strike_teams/`](./personas/strike_teams/) to audit that pillar with fresh eyes.
   - **Earned White Flag Only**: A Firm may output `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]` only after testing and falsifying at least 3 new candidate Nth-order vectors in dialogue.

### Phase 2: Present to THE BOARD & Shut the Doors
1. Once `.board/vN/firm1..K_*.md` are saved on disk, launch **The Board** subagent (`vN/BOARD_ADJUDICATION_vN.md`).
2. Instruct The Board subagent to read the **6 selected Board member `.md` files** (`personas/board_members/...`), the target artifact, and all Strike Team recordings.
3. Inside `.board/vN/BOARD_ADJUDICATION_vN.md`, The Board records:
   - **Part 1 (`[THE LEAD PRESENTS & EXITS // DOORS LOCK]`)**: Verbatim closed-door deliberation (`400–700+` lines) among the 6 historical executives—clashing in-character, auditing every Strike Team vector, picking the **Top 3** (or synthesizing all 5), enforcing the **Non-Regression Ratchet** (never weaken a `v1..v(N-1)` defense), and enforcing **Two-Tier Anti-Bloat Compression** (factoring verbose definitions/checks into clean Tier-2 helpers/lexicons so Tier-1 code/claims stay razor-sharp).
   - **Part 2 (`BINDING EXECUTIVE PATCH SPECIFICATION`)**: Exact file-by-file, line-by-line edits and the **Wave `vN` White-Flag Scorecard (`X / 5`)**.

### Phase 3: Apply Patch Spec & Run Deterministic Verification
1. **The Lead** applies the Board's Patch Spec directly to the target files (fixing root causes, never symptoms, preserving 100% of working functionality).
2. Run deterministic checks immediately (`compiler`, `unit tests`, `linter`, `statutory/claim-numeral checks`, or [`scripts/verify_convergence.py`](./scripts/verify_convergence.py)).

### Phase 4: Loop Until `5/5` White Flags + Final Sync (`v(N).5` & `v(N+1)`)
1. If `< 5/5` White Flags and `N < max_waves`, loop immediately to **Phase 1 (`Wave v(N+1)`)**.
2. Once `5/5` White Flags are verified:
   - If running in **`plan` mode**, transition immediately (or upon user confirmation) to executing the converged plan!
   - Run **Stage `v(N).5` (Data / Benchmark / Diagram Sync)** and **Stage `v(N+1)` (Final Board Sign-Off)** so every metric, test, and document is 100% aligned.

---

## [05] MODULAR INDEX (LOAD ON DEMAND)

- **Individual Board Member Dossiers (`1 .md per person`)**: [`personas/board_members/`](./personas/board_members/) (`computing/`, `physics_hardware/`, `design_product/`, `philosophy_logic/`, `strategy_command/`, `law_rhetoric/`)
- **Pre-Selected Boardroom Manifests**: [`personas/boardrooms/`](./personas/boardrooms/) (lists of `.md` files to load, including [`the_godfather_board.md`](./personas/boardrooms/the_godfather_board.md))
- **`$100M` Mercenary Strike-Team Vault**: [`personas/strike_teams/`](./personas/strike_teams/)
- **Dispatch Prompt Templates**: [`references/prompt_templates.md`](./references/prompt_templates.md)
- **Effort Dial, Ratchet & White-Flag Protocol**: [`references/effort_and_white_flag.md`](./references/effort_and_white_flag.md)
- **Latent-Space Mask Theory**: [`references/persona_mask_theory.md`](./references/persona_mask_theory.md)
- **Automation Scripts**: [`scripts/init_board_workspace.py`](./scripts/init_board_workspace.py) & [`scripts/verify_convergence.py`](./scripts/verify_convergence.py)
