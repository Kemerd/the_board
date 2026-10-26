---
description: Convene The Board — spawn 5 persona-driven Red Teams or Blue Teams, a Board of Directors, and an Executive Lead to iteratively attack, synthesize, and harden code, plans, legal docs, or strategy across N waves until White-Flag convergence.
argument-hint: "[mode: red|blue|purple] [effort: 1-20|white-flag] <target or task description>"
---

Activate the `the-board` skill (`skills/the-board/SKILL.md`) to execute a full multi-agent **Lead + 5 Firms (Red Team / Blue Team) + The Board** iterative convergence workflow on the following request:

$ARGUMENTS

Follow all instructions in `skills/the-board/SKILL.md`, including:
1. Partitioning the problem into **5 orthogonal pillars** (`Firms 1–5`).
2. Requiring **immersive, high-stakes persona masks and verbatim war-room transcripts** (`400–800+` lines per firm/board) to force deep latent-space reasoning rather polite generic summaries.
3. Convening **The Board** to grade all 5 firms, select the Top 3 (or synthesize all 5), enforce the **Non-Regression Ratchet**, and emit a concrete **Patch Spec**.
4. Having **The Lead** (you, the main orchestrator) apply the Patch Spec directly to the target files, run deterministic verification (`tests`, `compilers`, `linters`, `auditors`), and loop `v1 -> v2 -> ... -> vN` until either **Unconditional White-Flag Convergence (`5/5` firms surrender)** or the requested effort budget (`1..20` passes) is reached.
