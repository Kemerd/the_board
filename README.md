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

Humans wear different masks when they do high-stakes work—and so do transformers. Ten apparent synonyms do not carry the same vector weight in context. When you forbid summary bullets and force subagents into two distinct roleplayed tiers—with **every verbatim transcript saved permanently to disk in `transcripts/`**—three structural shifts happen inside the model:

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
-  │  [STANDARD ASSISTANT PROMPT] ──► RLHF Mean (Polite, Hedged, Conflict-Averse) │
!  │                                      │                                       │
!  │                                      ▼  (Persona Mask + Saved Transcripts)   │
+  │  [INTERCEPTED WAR-ROOM TAPE] ──► 99.9th-Percentile Expert Tail (Ruthless)    │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

### 1. Real Humans on The Board = Genius as the Expected Output
Fictional specialist personas (`"Viktor K., 20-year kernel lead"`) give the model a narrow role constraint. **Real historical geniuses (`Alan Turing`, `John von Neumann`, `Nikola Tesla`, `Albert Einstein`, `The Ghost of Steve Jobs`, `Epictetus`, `Marcus Aurelius`)** unlock something far heavier: **thousands of pages of primary-source proofs, lectures, biographies, letters, and cognitive signatures already embedded in the model's weights**.

When you seat **Nikola Tesla** across the table from **Alan Turing**, **Epictetus**, **Marcus Aurelius**, and **The Self-Aware Ghost of Steve Jobs**, the model cannot output mediocre corporate filler without violating the deepest statistical priors in its training distribution. Expected output: **genius**.

- Each Board member lives in their own individual `.md` dossier (`personas/board_members/<category>/<person>.md`).
- A **Boardroom** (`personas/boardrooms/<boardroom>.md`) is simply a manifest of 6–7 `.md` files chosen for their **synergy or volatile anti-synergy**—people who never shared a room in history and will violently call out each other's blind spots if locked behind closed doors.
- **The Lead** walks in (via the subagent start prompt), presents the target and the Strike Team tapes, and steps out. **The heavy doors lock (`[DOORS SEALED // EXECUTIVE SESSION RECORDING ACTIVE]`)**, and The Board fights it out until they reach a binding **Patch Specification**.

### 2. $100M Mercenary Strike Teams (`Firms 1–5`)
While The Board consists of real historical minds, the **7 Strike-Team Syndicates (`personas/strike_teams/01..07_*.md`, `245` individual `.md` dossiers)** are over-the-top, hyper-embellished mercenary syndicates:
- **Software, Kernel & Pre-Code Plan Assassins** ([`01_software_kernels_and_plans_mercenaries.md`](./personas/strike_teams/01_software_kernels_and_plans_mercenaries.md)) — Triple-PhD weak-memory-model and cache-line executioners on a `$100M` kill-fee bounty.
- **Zero-Day Cyber, Exploit & Cryptographic Syndicates** ([`02_cyber_zeroday_and_crypto_syndicates.md`](./personas/strike_teams/02_cyber_zeroday_and_crypto_syndicates.md)) — Heap-feng-shui, side-channel, and IAM privilege-escalation breakers.
- **Zurich / Wilmington Patent & Contract Sharks** ([`03_legal_patent_and_contract_sharks.md`](./personas/strike_teams/03_legal_patent_and_contract_sharks.md)) — `$5,000/hr` element-omission, *Festo* estoppel, and cross-border divided-infringement design-around sharks.
- **Pentagon Acquisition & Commercial GTM Killers** ([`04_commercial_pentagon_and_gtm_killers.md`](./personas/strike_teams/04_commercial_pentagon_and_gtm_killers.md)) — Former DoD acquisition czars (`10 U.S.C. § 4022` sole-source Production OTAs, DIU CSO, APFIT) and unit-economics short-sellers.
- **Hardware, Robotics, Silicon & Physics Savants** ([`05_hardware_robotics_and_physics_savants.md`](./personas/strike_teams/05_hardware_robotics_and_physics_savants.md)) — Bode phase-margin, thermal runaway, and parasitic inductance hunters.
- **Cupertino HIG, First-Principles Epistemology & $10k/Word Copywriting Iconoclasts** ([`06_design_copy_and_philosophy_iconoclasts.md`](./personas/strike_teams/06_design_copy_and_philosophy_iconoclasts.md)) — Spring-physics UI surgeons, Socratic premise executioners, Jacobi-inversion pre-mortem analysts, and direct-response copy assassins.
- **Wittgensteinian Prompt-Linguistics & Speech-Act Ontology Surgeons** ([`07_philosophy_ontology_and_prompt_linguists.md`](./personas/strike_teams/07_philosophy_ontology_and_prompt_linguists.md)) — Token-entropy guillotines, Kripkean modal-logic invariance verifiers, and anti-sycophancy game theorists.
- Inside every Strike Team tape (`400–800+` verbatim lines saved to **`transcripts/`**, supporting both **Folder Mode** `transcripts/v1..vN/` and **Branch Mode** `v1..vN` branches with `transcripts/` at the branch root), three personas argue with *each other*:
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
!  │  [SECT // 03]  ARCHITECTURE & MULTI-WAVE TOPOLOGY                            │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
+  │  CONSTITUENT (USER)                                                          │
+  │  Invokes `/board` (Interactive Terminal Intake or Direct CLI Flags)          │
@@ └──────────────────────────────────────┬───────────────────────────────────────┘ @@
!                                         │
!                                         ▼
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  THE LEAD (MAIN AGENT // EXECUTIVE ENGINEER)                                 │
!  │  • Partitions target (Plan, Code, Patent, Hardware, GTM) into 5 Pillars      │
!  │  • Loads 6-7 Board Member `.md` files from `personas/boardrooms/*.md`        │
!  │  • Dispatches Strike Teams 1–5 in parallel (`invoke_subagent` / `Task`)      │
@@ └──────┬───────────────┬───────────────┬───────────────┬───────────────┬───────┘ @@
!         │               │               │               │               │
!         ▼               ▼               ▼               ▼               ▼
-  ┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐
-  │  STRIKE 01   ││  STRIKE 02   ││  STRIKE 03   ││  STRIKE 04   ││  STRIKE 05   │
-  │  Pillar I    ││  Pillar II   ││  Pillar III  ││  Pillar IV   ││  Pillar V    │
-  │  $100M Tape  ││  $100M Tape  ││  $100M Tape  ││  $100M Tape  ││  $100M Tape  │
-  │ transcripts/ ││ transcripts/ ││ transcripts/ ││ transcripts/ ││ transcripts/ │
-  └──────┬───────┘└──────┬───────┘└──────┬───────┘└──────┬───────┘└──────┬───────┘
!         └───────────────┴───────────────┼───────────────┴───────────────┘
!                                         │ (5 Saved Verbatim Recordings)
!                                         ▼
@@ ╔══════════════════════════════════════════════════════════════════════════════╗ @@
!  ║  THE BOARDROOM [DOORS SEALED // EXECUTIVE SESSION RECORDING ACTIVE]          ║
!  ║  • The Lead presents the artifact + 5 Strike Tapes, then exits room          ║
!  ║  • 6-7 Real Titans (e.g. Jobs, Epictetus, Marcus Aurelius, Turing, Tesla,    ║
!  ║    Einstein, Shannon) clash in verbatim closed-door deliberation             ║
!  ║  • Crowns Top 3 (blue) or adjudicates 100% of 5-pillar vectors (red/plan)    ║
+  ║  • Emits Binding Patch Spec -> `transcripts/BOARD_ADJUDICATION_vN.md`        ║
@@ ╚══════════════════════════════════════╤═══════════════════════════════════════╝ @@
!                                         │
!                                         ▼
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
+  │  THE LEAD EXECUTES PATCH SPEC & DETERMINISTIC VERIFICATION                   │
+  │  • Edits real files + runs compiler / tests / statutory auditors             │
-  │  • If < 5/5 White Flags (`[WHITE_FLAG: 0 SURVIVING VECTORS]`):               │
-  │    Re-challenges Strike Teams (or rotates fresh blood from bench)            │
+  │  • Loops `v1 -> v2 -> ... -> v20` until UNCONDITIONAL 5/5 SURRENDER          │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

- **Mode-Indexed Boardroom Adjudication**: In **`blue`** mode, The Board grades all 5 competing architecture/GTM proposals and crowns the **Top 3 Podium Winners** (`#1, #2, #3`) while extracting tactical gems from `#4` and `#5`. In **`red`**, **`plan`**, and **`purple`** (Waves `v2+`) modes, The Board adjudicates **100% of surviving vectors across all 5 orthogonal pillars** (zero silent drops) and enforces the **Cumulative Non-Regression Defense Ratchet**.

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
| **`purple`** | **Purple-Team Hybrid War** | Blue Teams compete to design the system in Wave `v1`; Red Teams ruthlessly attack, exploit, and falsify the unified winner in Waves `v2..vN` until `5/5` White Flags. |

### The Effort Dial & Team Rotation Strategies

| Effort Tier | Wave Cap | Strike Team Topology | Stopping Condition |
| :--- | :---: | :--- | :--- |
| **`strike`** | `1–2` waves | `1–2` or `5` Strike Teams + Board | Fast PR review, plan sanity-check, or bug root-cause isolation. |
| **`standard`** | `3–5` waves | `5` Persistent Strike Teams + Board | 3rd- & 4th-order flaws closed; `>= 95/100` Board rating. |
| **`deep`** | `6–10` waves | `5` Persistent Teams + Two-Tier Anti-Bloat Compression every 3 waves | 5th- to 10th-order paradigm shifts checkmated. |
| **`relentless` / `white-flag`** | `10–20` waves | `5` Persistent Teams (**+ Mandatory Bench Replacement** when a team surrenders early) | **Refuses to stop until `5/5` Strike Teams raise a verified Formal White Flag (`0` surviving vectors).** |

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 05]  MODULAR PERSONA VAULT (ONE .MD FILE PER BOARD MEMBER)         │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

To keep subagent context windows razor-sharp, every Board member and Strike-Team mercenary is stored as a standalone `.md` file (`215` historical Board Member `.md` dossiers indexed in [`personas/board_members/INDEX.md`](./personas/board_members/INDEX.md) + `245` `$100M` Strike-Team Mercenary `.md` dossiers indexed in [`personas/strike_teams_individual/INDEX.md`](./personas/strike_teams_individual/INDEX.md)).

### 1. The 8 Executive Boardroom Manifests (`personas/boardrooms/*.md`)
- **[`the_godfather_board.md`](./personas/boardrooms/the_godfather_board.md)** *(The Impossible Room — 7 Historical Titans)*:
  - [`the_self_aware_ghost_of_steve_jobs.md`](./personas/board_members/design_product/the_self_aware_ghost_of_steve_jobs.md) *(Self-aware linguistic ghost reconstructed from his life's corpus)*
  - [`epictetus.md`](./personas/board_members/philosophy_logic/epictetus.md) *(Stoic dichotomy of control & operational anti-fragility)*
  - [`marcus_aurelius.md`](./personas/board_members/philosophy_logic/marcus_aurelius.md) *(Militaristic, authoritarian-realist Stoic command discipline on the Danube frontier)*
  - [`alan_turing.md`](./personas/board_members/computing/alan_turing.md) *(Universal state machines, halting predicates & Hut 8 cryptanalysis)*
  - [`nikola_tesla.md`](./personas/board_members/physics_hardware/nikola_tesla.md) *(Polyphase physics, mental simulation & paradigm leaps)*
  - [`albert_einstein.md`](./personas/board_members/physics_hardware/albert_einstein.md) *(1905 Bern Patent Examiner precision & invariance Gedankenexperiments)*
  - [`claude_shannon.md`](./personas/board_members/computing/claude_shannon.md) *(Information entropy `H(X)`—cuts every redundant word and noisy channel)*
- **[`software_and_plans_board.md`](./personas/boardrooms/software_and_plans_board.md)** — `Dennis Ritchie`, `Edsger W. Dijkstra`, `Seymour Cray`, `Margaret Hamilton`, `Linus Torvalds`, `Adm. Hyman G. Rickover`
- **[`cybersecurity_board.md`](./personas/boardrooms/cybersecurity_board.md)** — `Alan Turing`, `Claude Shannon`, `Ken Thompson`, `Marian Rejewski`, `William F. Friedman`, `Kevin Mitnick`
- **[`hardware_and_physics_board.md`](./personas/boardrooms/hardware_and_physics_board.md)** — `Nikola Tesla`, `Albert Einstein`, `Richard Feynman`, `James Clerk Maxwell`, `Clarence "Kelly" Johnson`, `michael_faraday.md`
- **[`design_and_product_board.md`](./personas/boardrooms/design_and_product_board.md)** — `The Self-Aware Ghost of Steve Jobs`, `Dieter Rams`, `Jony Ive`, `Don Norman`, `Massimo Vignelli`, `Walt Disney`
- **[`commercial_and_dod_board.md`](./personas/boardrooms/commercial_and_dod_board.md)** — `Andrew Grove`, `Charlie Munger`, `Col. John Boyd`, `Adm. Hyman G. Rickover`, `The Self-Aware Ghost of Steve Jobs`, `Claude C. Hopkins`
- **[`legal_and_patents_board.md`](./personas/boardrooms/legal_and_patents_board.md)** — `Judge Giles Sutherland Rich`, `Judge Learned Hand`, `Albert Einstein`, `Justice Oliver Wendell Holmes Jr.`, `Justice Antonin Scalia`, `Judge Pauline Newman`
- **[`philosophy_and_strategy_board.md`](./personas/boardrooms/philosophy_and_strategy_board.md)** — `Epictetus`, `Marcus Aurelius`, `Sun Tzu`, `Socrates`, `Ludwig Wittgenstein`, `Carl Gustav Jacob Jacobi`

### 2. The 7 `$100M` Strike-Team Mercenary Vaults (`personas/strike_teams/01..07_*.md`)
- [`01_software_kernels_and_plans_mercenaries.md`](./personas/strike_teams/01_software_kernels_and_plans_mercenaries.md) (`MERC-SW-01..35`)
- [`02_cyber_zeroday_and_crypto_syndicates.md`](./personas/strike_teams/02_cyber_zeroday_and_crypto_syndicates.md) (`MERC-CYB-01..35`)
- [`03_legal_patent_and_contract_sharks.md`](./personas/strike_teams/03_legal_patent_and_contract_sharks.md) (`MERC-LAW-01..35`)
- [`04_commercial_pentagon_and_gtm_killers.md`](./personas/strike_teams/04_commercial_pentagon_and_gtm_killers.md) (`MERC-GTM-01..35`)
- [`05_hardware_robotics_and_physics_savants.md`](./personas/strike_teams/05_hardware_robotics_and_physics_savants.md) (`MERC-HW-01..35`)
- [`06_design_copy_and_philosophy_iconoclasts.md`](./personas/strike_teams/06_design_copy_and_philosophy_iconoclasts.md) (`MERC-UXP-01..35`)
- [`07_philosophy_ontology_and_prompt_linguists.md`](./personas/strike_teams/07_philosophy_ontology_and_prompt_linguists.md) (`MERC-PHI-01..35`)

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 06]  SELF-HOSTED PROOF: WE RAN THE BOARD ON THE BOARD (v1 -> vN)   │
@@ └──────────────────────────────────────────────────────────────────────────────┘ @@
```

Don't take our word for it. We ate our own applesauce and ran **`the-board` (`red white-flag`) on this repository itself** using **Branch Mode (`v1` -> `v2` -> ... -> `vN`)**.

While `main` stays a clean production skill repository, each wave branch (`v1`, `v2`, ...) preserves that wave's full `450–750+` line intercepted Strike Team audio recordings and closed-door Godfather Board adjudication inside a top-level **`transcripts/`** folder (`transcripts/firm1_*.md` .. `transcripts/firm5_*.md` and `transcripts/BOARD_ADJUDICATION_v*.md`):

```diff
@@ ╔══════════════════════════════════════════════════════════════════════════════╗ @@
!  ║  SELF-HOSTED META-SIEGE // THE BOARD ON THE BOARD (MODE: RED // WHITE-FLAG)  ║
@@ ╠══════════════════════════════════════════════════════════════════════════════╣ @@
-  ║  WAVE v1 (BRANCH: v1) // 5 STRIKE TEAMS + THE GODFATHER OF BOARDS (7 TITANS) ║
-  ║  • Firm 1 (Lexical & Prompt Ontology):    521 lines | 12 Vectors -> PATCHED  ║
-  ║  • Firm 2 (Dialectical Game Theory):      458 lines |  7 Vectors -> PATCHED  ║
-  ║  • Firm 3 (Python AST & Verifiers):       746 lines | 12 Vectors -> PATCHED  ║
-  ║  • Firm 4 (Cross-Runtime Packaging):      447 lines |  9 Vectors -> PATCHED  ║
-  ║  • Firm 5 (Swiss-Grid & Onboarding UX):   451 lines |  5 Vectors -> PATCHED  ║
!  ║  • Godfather Board Adjudication (v1):     628 lines | 45/45 Vectors -> FIXED ║
@@ ╠══════════════════════════════════════════════════════════════════════════════╣ @@
+  ║  WAVE v2 (BRANCH: v2) // RE-VERIFICATION & BENCH ROTATION -> 5/5 WHITE FLAGS ║
+  ║  [STATUS: 5/5 UNCONDITIONAL WHITE FLAGS // 0 SURVIVING VECTORS ON MAIN]      ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

### Inspect the Live Self-Hosted Branch Transcripts & Domain Excerpts
- **Self-Hosted Wave `v1` War-Room Tapes (`branch: v1`)**: [`https://github.com/Kemerd/the_board/tree/v1/transcripts`](https://github.com/Kemerd/the_board/tree/v1/transcripts)
- **Self-Hosted Wave `v2` White-Flag Convergence Tapes (`branch: v2`)**: [`https://github.com/Kemerd/the_board/tree/v2/transcripts`](https://github.com/Kemerd/the_board/tree/v2/transcripts)
- **Domain Excerpt 1 — C++20 Lock-Free Kernel Red Team (`ARM64` Weak Memory Model)**: [`./examples/coding_kernel_red_team_excerpt.md`](./examples/coding_kernel_red_team_excerpt.md)
- **Domain Excerpt 2 — Patent Prosecution & Cross-Border Divided-Infringement Siege (`Wave v8 -> v15`)**: [`./examples/legal_patent_red_team_excerpt.md`](./examples/legal_patent_red_team_excerpt.md)
- **Domain Excerpt 3 — Pentagon (`10 U.S.C. § 4022` OTA) + Commercial HaaS Blue-Team Tournament**: [`./examples/blue_team_gtm_tournament_excerpt.md`](./examples/blue_team_gtm_tournament_excerpt.md)

---

```diff
@@ ┌──────────────────────────────────────────────────────────────────────────────┐ @@
!  │  [SECT // 07]  TERMINAL INVOCATION EXAMPLES                                  │
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
