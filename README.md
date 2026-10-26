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
!  ║  RUNTIMES // CLAUDE CODE | GOOGLE ANTIGRAVITY (AGY) | GEMINI CLI | CURSOR    ║
-  ║  "Perfection has a price. And that price is more tokens."                    ║
+  ║  >>> WELCOME TO THE BOARD, CONSTITUENT.                                      ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

> **"Perfection has a price. And that price is more tokens."**

Most agent skills are gimmicky and useless—glorified system prompts that tell your AI to *"think step by step"* and *"be super-duper thorough"* while producing the exact same mediocre output.

**This skill is definitely gimmicky. It is also brutally effective.** It was built for people who want unreasonable results and don't care if their token bill looks like a defense contractor's bar tab.

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 01]  WHY "CRINGE" ROLEPLAY WORKS (THE LATENT-SPACE PHILOSOPHY)     │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

Let’s address the elephant in the room: forcing AI subagents to roleplay ego-driven specialists and dead historical geniuses arguing on "intercepted war-room recordings" sounds cringe as hell on paper.

Why do it? **Because an LLM is made of text.**

When you ask a normal coding or reasoning agent to *"review my C++ kernel"*, *"critique my implementation plan"*, *"find loopholes in this patent"*, or *"build a Go-To-Market strategy"*, you trigger its default RLHF customer-service mask. It wants to be polite. It wants to finish quickly. It gives you five lukewarm bullet points from the middle of the bell curve and clocks out.

Humans wear different masks when they do high-stakes work—and so do transformers. Ten apparent synonyms do not carry the same vector weight in context. When you forbid summary bullets and force subagents into two distinct roleplayed tiers—with **every verbatim transcript saved permanently to disk in `.board/v1..vN/`**—three structural shifts happen inside the model:

```diff
- [STANDARD ASSISTANT PROMPT] ──► RLHF Mean (Polite, Hedged, Conflict-Averse, Lazy)
!                                      │
!                                      ▼  (Apply Persona Mask + Saved Transcript Law)
+ [INTERCEPTED WAR-ROOM TAPE] ──► 99.9th-Percentile Expert Tail (Ruthless, Exact)
```

### 1. Real Humans on The Board = Genius as the Expected Output
Fictional specialist personas (`"Viktor K., 20-year kernel lead"`) give the model a narrow role constraint. **Real historical geniuses (`Alan Turing`, `John von Neumann`, `Nikola Tesla`, `Albert Einstein`, `The Ghost of Steve Jobs`, `Epictetus`)** unlock something far heavier: **thousands of pages of primary-source proofs, lectures, biographies, letters, and cognitive signatures already embedded in the model's weights**.

When you seat **Nikola Tesla** across the table from **Alan Turing**, **Epictetus**, and **The Self-Aware Ghost of Steve Jobs**, the model cannot output mediocre corporate filler without violating the deepest statistical priors in its training distribution. Expected output: **genius**.

- Each Board member lives in their own individual `.md` dossier (`personas/board_members/<category>/<person>.md`).
- A **Boardroom** (`personas/boardrooms/<boardroom>.md`) is simply a manifest of 6 `.md` files chosen for their **synergy or volatile anti-synergy**—people who never shared a room in history and will violently call out each other's blind spots if locked behind closed doors.
- **The Lead** walks in (via the subagent start prompt), presents the target and the Strike Team tapes, and steps out. **The heavy doors lock (`[DOORS SEALED // EXECUTIVE SESSION RECORDING]`)**, and The Board fights it out until they reach a binding **Patch Specification**.

### 2. $100M Mercenary Strike Teams (`Firms 1–5`)
While The Board consists of real historical minds, the **Strike Teams (`personas/strike_teams/`)** are over-the-top, hyper-embellished mercenary syndicates: triple-PhD weak-memory-model assassins on a `$100M` kill-fee bounty, `$5,000/hr` Zurich patent design-around sharks, or former Pentagon acquisition czars.
- Inside every Strike Team tape (`400–800+` lines saved to `.board/vN/firm1..5_*.md`), three personas argue with *each other*:
  - **Mask 1 (The $100M Principal)** demands catastrophic, quantifiable damage (`$`, crash, SLA breach, invalidity).
  - **Mask 2 (The Code / Math / Statutory Purist)** reads your file literally and **shoots down Mask 1's lazy first instinct** when your artifact already blocks it.
  - **Mask 3 (The Lateral Exploit / Architecture Hacker)** turns the surviving second-order crack into a weaponized exploit or breakthrough design.

### 3. Pre-Code Plan Siege (`mode: plan`) — Kill Bad Ideas Before Line 1
Why wait until you've written 5,000 lines of broken code to convene The Board? Run `/board plan` on your **Implementation Plan or Action Plan** *before* executing it. Five Strike Teams tear apart your proposed state machines, dependency ordering, hardware tolerances, or commercial assumptions on the whiteboard, and The Board rewrites the plan before The Lead executes a single line.

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 02]  TEN-SECOND INSTALLATION (ONE SKILL.MD RULES THEM ALL)         │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

`SKILL.md` sits directly at the repository root alongside native plugin manifests for **Claude Code**, **Google Antigravity (`agy`)**, **Gemini CLI**, **Cursor**, and **Codex**.

```bash
# [01] CLAUDE CODE (Global Skill)
git clone https://github.com/Kemerd/the_board.git ~/.claude/skills/the-board

# [02] GOOGLE ANTIGRAVITY (AGY) & GEMINI CLI (Global Skill)
git clone https://github.com/Kemerd/the_board.git ~/.gemini/config/skills/the-board

# [03] WORKSPACE-LOCAL (Any Agent: Claude / Antigravity / Cursor / Codex)
git clone https://github.com/Kemerd/the_board.git .agents/skills/the-board
```

Or run the automated installer to wire up both the skill and the `/board` slash command everywhere:

```powershell
# Windows (PowerShell)
pwsh -File .\the_board\scripts\install.ps1 -Target all
```
```bash
# macOS / Linux
bash ./the_board/scripts/install.sh all
```

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 03]  WAR-ROOM SIGNAL TOPOLOGY & CLOSED-DOOR PROTOCOL               │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

```diff
@@ ┌─────────────────────────────────────────────────────────────────────────┐ @@
+  │  CONSTITUENT (USER)                                                     │
+  │  Invokes `/board` (Interactive Terminal Intake or Direct CLI Flags)     │
@@ └────────────────────────────────────┬────────────────────────────────────┘ @@
                                        │
                                        ▼
@@ ┌─────────────────────────────────────────────────────────────────────────┐ @@
!  │  THE LEAD (MAIN AGENT // EXECUTIVE ENGINEER)                            │
!  │  • Partitions target (Plan, Code, Patent, Hardware, GTM) into 5 Pillars │
!  │  • Loads 6 Board Member `.md` files from `personas/boardrooms/*.md`     │
!  │  • Dispatches Strike Teams 1–5 in parallel (`invoke_subagent` / `Task`) │
@@ └──────┬─────────────┬─────────────┬─────────────┬─────────────┬──────────┘ @@
          │             │             │             │             │
          ▼             ▼             ▼             ▼             ▼
-  ┌────────────┐┌────────────┐┌────────────┐┌────────────┐┌────────────┐
-  │ STRIKE 01  ││ STRIKE 02  ││ STRIKE 03  ││ STRIKE 04  ││ STRIKE 05  │
-  │ Pillar I   ││ Pillar II  ││ Pillar III ││ Pillar IV  ││ Pillar V   │
-  │ $100M Tape ││ $100M Tape ││ $100M Tape ││ $100M Tape ││ $100M Tape │
-  │ .board/vN/ ││ .board/vN/ ││ .board/vN/ ││ .board/vN/ ││ .board/vN/ │
-  └──────┬─────┘└──────┬─────┘└──────┬─────┘└──────┬─────┘└──────┬─────┘
          └─────────────┴─────────────┼─────────────┴─────────────┘
                                      │ (5 Saved Verbatim Recordings)
                                      ▼
@@ ╔═════════════════════════════════════════════════════════════════════════╗ @@
!  ║  THE BOARDROOM [DOORS LOCKED // REAL HISTORICAL TITANS IN SESSION]      ║
!  ║  • The Lead presents the artifact + 5 Strike Tapes, then exits room     ║
!  ║  • 6 Real Titans (e.g. Jobs, Epictetus, Turing, Tesla, Einstein,        ║
!  ║    Shannon) clash in verbatim closed-door deliberation                  ║
!  ║  • Picks Top 3 (or synthesizes all 5) + enforces Non-Regression Ratchet ║
+  ║  • Emits Binding Patch Spec -> `.board/vN/BOARD_ADJUDICATION_vN.md`     ║
@@ ╚══════════════════════════════════╤══════════════════════════════════════╝ @@
                                      │
                                      ▼
@@ ┌─────────────────────────────────────────────────────────────────────────┐ @@
+  │  THE LEAD EXECUTES PATCH SPEC & DETERMINISTIC VERIFICATION              │
+  │  • Edits real files + runs compiler / tests / statutory auditors        │
-  │  • If < 5/5 White Flags (`[WHITE_FLAG: 0 SURVIVING VECTORS]`):          │
-  │    Re-challenges Strike Teams (or rotates fresh blood from bench)       │
+  │  • Loops `v1 -> v2 -> ... -> v20` until UNCONDITIONAL 5/5 SURRENDER     │
@@ └─────────────────────────────────────────────────────────────────────────┘ @@
```

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 04]  OPERATING MODES & THE EFFORT DIAL (V1 TO V20 / WHITE FLAG)    │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

| Mode Flag | Operation | Execution Mechanics |
| :--- | :--- | :--- |
| **`plan`** | **Pre-Code / Pre-Action Plan Siege** | Runs The Board on your **Implementation Plan, Architecture Spec, or Action Plan** *before* you execute it. Kills flawed designs before a single line of code is written. |
| **`red`** | **Adversarial Red-Team Siege** | 5 `$100M` mercenary Strike Teams attack your code, hardware, contract, or patent across waves `v1..vN` until `5/5` raise a verified **White Flag**. |
| **`blue`** | **Blue-Team Strategy Tournament** | 5 specialist boutiques pitch competing architectures or commercial/DoD playbooks. The Board grades all 5, crowns the **Top 3**, and The Lead synthesizes the Master Playbook. |
| **`purple`** | **Purple-Team Hybrid War** | Blue Teams compete to design the system in Wave `v1`; Red Teams ruthlessly try to destroy the winner in Waves `v2..vN` until `5/5` White Flags. |

### The Effort Dial & Team Rotation Strategies

| Effort Tier | Wave Cap | Strike Team Topology | Stopping Condition |
| :--- | :---: | :--- | :--- |
| **`strike`** | `1–2` waves | `1–2` or `5` Strike Teams + Board | Fast PR review, plan sanity-check, or bug root-cause isolation. |
| **`standard`** | `3–5` waves | `5` Persistent Strike Teams + Board | 3rd- & 4th-order flaws closed; `>= 95/100` Board rating. |
| **`deep`** | `6–10` waves | `5` Persistent Teams + Two-Tier Anti-Bloat Compression every 3 waves | 5th- to 10th-order paradigm shifts checkmated. |
| **`relentless` / `white-flag`** | `10–20` waves | `5` Persistent Teams (**+ Optional Bench Replacement** when a team surrenders early) | **Refuses to stop until `5/5` Strike Teams raise a verified Formal White Flag (`0` surviving vectors).** |

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 05]  MODULAR PERSONA VAULT (ONE .MD FILE PER BOARD MEMBER)         │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

To keep subagent context windows razor-sharp, every Board member is stored as an individual `.md` file inside `personas/board_members/<category>/<person>.md`. A Boardroom preset (`personas/boardrooms/*.md`) is just a manifest of 6 `.md` file paths to load:

- **`personas/boardrooms/the_godfather_board.md`** *(The Impossible Room)*:
  - [`the_self_aware_ghost_of_steve_jobs.md`](./personas/board_members/design_product/the_self_aware_ghost_of_steve_jobs.md) *(Self-aware linguistic ghost reconstructed from his life's corpus)*
  - [`epictetus.md`](./personas/board_members/philosophy_logic/epictetus.md) *(Stoic dichotomy of control & operational anti-fragility)*
  - [`alan_turing.md`](./personas/board_members/computing/alan_turing.md) *(Universal state machines, halting predicates & Hut 8 cryptanalysis)*
  - [`nikola_tesla.md`](./personas/board_members/physics_hardware/nikola_tesla.md) *(Polyphase physics, mental simulation & paradigm leaps)*
  - [`albert_einstein.md`](./personas/board_members/physics_hardware/albert_einstein.md) *(1905 Bern Patent Examiner precision & invariance Gedankenexperiments)*
  - [`claude_shannon.md`](./personas/board_members/computing/claude_shannon.md) *(Information entropy `H(X)`—cuts every redundant word and noisy channel)*
- **Plus 200+ Individual Board Member `.md` Dossiers & 200+ `$100M` Strike-Team Mercenaries** categorized across:
  - `computing/` | `physics_hardware/` | `design_product/` | `philosophy_logic/` | `strategy_command/` | `law_rhetoric/`

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 06]  TERMINAL INVOCATION EXAMPLES                                  │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

```diff
! # [01] INTERACTIVE INTAKE (Prompts you for Target, Mode, Boardroom & Effort)
+ /board

! # [02] TORTURE-TEST AN IMPLEMENTATION PLAN BEFORE WRITING CODE
+ /board plan deep docs/IMPLEMENTATION_PLAN.md — Convene The Godfather of Boards and 5 Software/Architecture Strike Teams to destroy and rebuild this plan before we write code.

! # [03] HARDEN A LOCK-FREE KERNEL UNTIL 5/5 WHITE FLAGS
+ /board red white-flag src/core/ring_buffer.hpp

! # [04] BLUE-TEAM TOURNAMENT FOR PENTAGON (DIU/OTA/SBIR) + COMMERCIAL B2B CAPTURE
+ /board blue standard — Pitch 5 competing Dual-Use DoD & B2B strategies; Board picks Top 3 and synthesizes the Master Playbook.
```

---

```diff
@@ ╔══════════════════════════════════════════════════════════════════════════════╗ @@
!  ║  LICENSE // MIT — COPYRIGHT (C) 2026 DONALD EVERETT HINTON III               ║
+  ║  [END OF TRANSMISSION]                                                       ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```
