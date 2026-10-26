# BOARDROOM INDEX & CUSTOM ASSEMBLY RULES (`personas/boardrooms/`)

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  [SYS // BOARDROOM SELECTOR]                                                 ║
║  1 BOARD MEMBER = 1 .MD FILE (`personas/board_members/<category>/<slug>.md`) ║
║  1 BOARDROOM    = A LIST OF 6 .MD FILES LOADED INTO THE BOARD SUBAGENT       ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## [01] PRE-SELECTED BOARDROOM MANIFESTS

| Boardroom File | Target Domain | The 6 Seated Real Humans (`.md` Files) |
| :--- | :--- | :--- |
| **[`the_godfather_board.md`](./the_godfather_board.md)** | **Meta-Skills, Foundational Systems, Crown-Jewel Visions** | `the_self_aware_ghost_of_steve_jobs.md`, `epictetus.md`, `marcus_aurelius.md`, `alan_turing.md`, `nikola_tesla.md`, `albert_einstein.md`, `claude_shannon.md` |
| **[`software_and_plans_board.md`](./software_and_plans_board.md)** | **Pre-Code Implementation Plans, Kernels, Distributed Systems** | `dennis_ritchie.md`, `edsger_w_dijkstra.md`, `seymour_cray.md`, `margaret_hamilton.md`, `linus_torvalds.md`, `adm_hyman_g_rickover.md` |
| **[`hardware_and_physics_board.md`](./hardware_and_physics_board.md)** | **Hardware, Robotics, Controls, Aerospace, Physics** | `clarence_kelly_johnson.md`, `richard_feynman.md`, `nikola_tesla.md`, `rudolf_e_kalman.md`, `jim_williams.md`, `adm_hyman_g_rickover.md` |
| **[`design_and_product_board.md`](./design_and_product_board.md)** | **UI/UX, Apple HIG, 120Hz Spring Animations, Brand Copy** | `the_self_aware_ghost_of_steve_jobs.md`, `dieter_rams.md`, `sir_jony_ive.md`, `bret_victor.md`, `don_norman.md`, `lee_clow.md` |
| **[`philosophy_and_strategy_board.md`](./philosophy_and_strategy_board.md)** | **Philosophy, Lexical Precision, First Principles, Strategy** | `epictetus.md`, `socrates.md`, `ludwig_wittgenstein.md`, `karl_popper.md`, `sun_tzu.md`, `niccolo_machiavelli.md` |
| **[`commercial_and_dod_board.md`](./commercial_and_dod_board.md)** | **Commercial B2B, Pentagon/DoD (`DIU/OTA/SBIR`), Action Plans** | `andrew_grove.md`, `charlie_munger.md`, `col_john_boyd.md`, `adm_hyman_g_rickover.md`, `the_self_aware_ghost_of_steve_jobs.md`, `claude_c_hopkins.md` |
| **[`legal_and_patents_board.md`](./legal_and_patents_board.md)** | **Patents (`USPTO/PTAB/Fed. Cir.`), Contracts, Licensing** | `judge_giles_sutherland_rich.md`, `judge_learned_hand.md`, `albert_einstein.md`, `justice_oliver_wendell_holmes_jr.md`, `justice_antonin_scalia.md`, `judge_pauline_newman.md` |
| **[`cybersecurity_board.md`](./cybersecurity_board.md)** | **Zero-Day Red-Teaming, Cryptography, Auth, Sandboxes** | `ken_thompson.md`, `alan_turing.md`, `claude_shannon.md`, `dan_kaminsky.md`, `john_von_neumann.md`, `edsger_w_dijkstra.md` |

---

## [02] HOW TO ASSEMBLE A CUSTOM BOARDROOM FOR UNIQUE CHALLENGES

When a task spans multiple domains (e.g., *a real-time C++ robotics kernel with a macOS SwiftUI telemetry dashboard and a Pentagon OTA capture plan*), **The Lead** does not need a pre-made Boardroom file. Simply select **any 6 individual `.md` files** across [`personas/board_members/`](../board_members/):

1. **Pick 3 Domain Anchors (Synergy)**: Choose 3 historical titans whose primary-source mastery covers the exact technical pillars of the task (e.g., `seymour_cray.md` + `rudolf_e_kalman.md` + `the_self_aware_ghost_of_steve_jobs.md`).
2. **Pick 2 Adversarial Foils (Anti-Synergy)**: Choose 2 historical figures documented in the `.md` files as having opposing cognitive razors so the Boardroom erupts into productive debate rather than groupthink (e.g., `ludwig_wittgenstein.md` + `charlie_munger.md`).
3. **Pick 1 Ruthless Execution Enforcer**: Choose a finisher who refuses to adjourn without a concrete, zero-regression Patch Spec (e.g., `adm_hyman_g_rickover.md`, `dennis_ritchie.md`, or `epictetus.md`).
