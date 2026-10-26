---
description: Convene The Board — Multi-Agent Red-Team, Blue-Team, Pre-Code Plan & Executive Boardroom Convergence Engine (v1 to vN until White Flag)
argument-hint: "[optional: red|blue|purple|plan] [optional: strike|standard|deep|white-flag] [optional: target files or goal]"
---

# `/board` — TERMINAL UPLINK INITIALIZED

When `/board` is invoked, ALWAYS open your first response by displaying this exact terminal boot banner:

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
-  ║  "Perfection has a price. And that price is more tokens."                    ║
+  ║  >>> WELCOME TO THE BOARD, CONSTITUENT.                                      ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

---

## 🔀 Execution Routing (`Direct Command` vs. `Interactive Intake`)

Inspect the user's arguments: `$ARGUMENTS`

### Case 1: User Ran `/board` With No Arguments (or Partial/Ambiguous Arguments)
If `$ARGUMENTS` is empty or missing the target/mode, **do NOT guess**. Immediately greet the Constituent with the ASCII banner above and ask them to lock in their mission parameters (using your platform's interactive `ask_question` tool if available, or a sharp numbered terminal prompt):

1. **🎯 TARGET ARTIFACT OR OBJECTIVE**:
   - *What are we putting on the table?* (e.g., a pre-code Implementation Plan, source code files, system architecture, legal/patent claims, commercial/Pentagon GTM playbook, hardware spec, or UI/UX design)
2. **⚔️ PROTOCOL MODE**:
   - **`[1] PRE-CODE PLAN SIEGE (plan)`** — Torture-test the implementation/action plan *before* writing a single line of code or executing.
   - **`[2] RED-TEAM SIEGE (red)`** — 5 `$100M` mercenary Strike Teams ruthlessly break, exploit, or design around the target until `5/5` raise the White Flag.
   - **`[3] BLUE-TEAM TOURNAMENT (blue)`** — 5 specialist boutiques compete; The Board grades all 5, crowns the **Top 3**, and The Lead synthesizes the Master Playbook.
   - **`[4] PURPLE-TEAM HYBRID (purple)`** — Blue Teams build competing architectures in Wave `v1`; Red Teams try to destroy the winner in Waves `v2..vN`.
3. **🏛️ EXECUTIVE BOARDROOM ROSTER**:
   - **`[A] THE GODFATHER OF BOARDS`** (`ghost_of_steve_jobs.md`, `epictetus.md`, `alan_turing.md`, `nikola_tesla.md`, `albert_einstein.md`, `claude_shannon.md`)
   - **`[B] DOMAIN-MATCHED BOARDROOM`** (Auto-selected from `personas/boardrooms/*.md` for Software, Hardware, Design, Legal/Patents, Cyber, Philosophy, or Commercial/DoD)
   - **`[C] CUSTOM IMPOSSIBLE ROOM`** (Draft any 6 real historical minds from `personas/board_members/<category>/<person>.md` picked for explosive synergy/anti-synergy)
4. **🔥 EFFORT & TOKEN BURN**:
   - **`strike`** (`1–2` waves, 1–2 or 5 teams)
   - **`standard`** (`3–5` waves, 5 teams + Board)
   - **`deep`** (`6–10` waves + Two-Tier anti-bloat compression)
   - **`relentless / white-flag`** (`Up to 20 waves` — refuses to stop until `5/5` verified White Flags)

---

### Case 2: User Provided Direct Arguments (`/board red white-flag src/...`)
1. Display the `WELCOME TO THE BOARD, CONSTITUENT.` ASCII banner and echo the locked mission manifest (`TARGET`, `MODE`, `BOARDROOM`, `STRIKE TEAMS`, `MAX WAVES`).
2. Follow the exact protocol in [`SKILL.md`](../SKILL.md):
   - Select the 6 individual Board member `.md` files listed in the chosen `personas/boardrooms/<boardroom>.md` manifest (or assemble a custom list of 6 `.md` files from `personas/board_members/<category>/*.md`).
   - Dispatch the Strike Teams in parallel (`invoke_subagent` or `Task`/`Agent`) to record their verbatim intercepted war-room transcripts in `.board/vN/firm1..5_*.md`.
   - Walk into the Boardroom via the Board subagent prompt, present the target and the Strike Team recordings, **shut the doors (`[THE DOORS CLOSE — EXECUTIVE SESSION BEGINS]`)**, and let the 6 real historical executives deliberate and issue their binding **Patch Spec** (`vN/BOARD_ADJUDICATION_vN.md`).
   - Apply the patches, run deterministic verification, and iterate `v1 -> v2 -> ... -> vN` until **5/5 White Flags**!
