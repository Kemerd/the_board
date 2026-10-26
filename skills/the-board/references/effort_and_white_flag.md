# Effort Dial, Non-Regression Ratchet & The White-Flag Protocol

## 1. The Effort Dial (`1` to `20` Waves)

Not every task needs 16 waves of adversarial warfare, and not every critical system can afford to stop at Wave 1. `the-board` exposes a deterministic **Effort Dial** that the user can pass directly (e.g., `/board red deep` or `/board red white-flag max=16`):

| Effort Level | Wave Cap | Subagent Topology | Target Use Cases | Convergence Stopping Condition |
| :--- | :---: | :--- | :--- | :--- |
| **`strike`** (`1–2` waves) | `2` | 5 Firms + 1 Board (`v1`), optional `v2` verification | PR reviews, bug root-cause isolation, tactical memos, quick architecture sanity checks | Stops after Wave `v1` patch (or `v2` sign-off) |
| **`standard`** (`3–5` waves) | `5` | Persistent 5 Firms + Board across `v1..v5` | Feature architectures, production services, commercial B2B/DoD strategies, commercial contracts | Stops at `5/5` White Flags or Wave `v5` |
| **`deep`** (`6–10` waves) | `10` | Persistent 5 Firms + Board + Two-Tier Compression every 3 waves | Zero-day security audits, lock-free/SIMD kernels, core patent claim sets, M&A/licensing deals | Stops at `5/5` White Flags or Wave `v10` |
| **`relentless` / `white-flag`** (`10–20` waves) | `20` (or custom `N`) | Full `v1..vN` multi-wave siege + Stage `v(N).5` Empirical Sync + Stage `v(N+1)` Pre-Ship Audit | Flagship patent filings, safety-critical flight/medical/crypto systems, foundational protocols | **Refuses to stop** until `5/5` firms raise a verified **Formal White Flag** (`0` surviving vectors) or `max_waves` is reached |

---

## 2. How Multi-Wave Escalation Evolves (`v1` -> `v16+`)

Why did our flagship runs discover game-changing flaws in Waves `v7`, `v11`, and `v14` that were completely invisible in Wave `v1`? Because **each wave strips away a defensive layer**, forcing the 5 firms to invent higher-order attacks:

```
Wave v1–v2   : 1st-Order Defects       (Missing guards, obvious race conditions, literal claim omissions)
Wave v3–v5   : 2nd/3rd-Order Bypasses  (Cross-module interactions, proxy metrics, duty-cycle/timing evasion)
Wave v6–v9   : Paradigm-Shift Attacks  (Split-actor/cloud offloading, hardware/sensor aliasing, two-tier structural refactoring)
Wave v10–v14 : Asymptotic & Edge Sieges (Degraded-mode corner cases, Byzantine fault injection, lifecycle/aftermarket loopholes)
Wave v15–v16 : White-Flag Convergence  (Every remaining attack requires violating physics, math, or economic survival -> 5/5 White Flags)
```

---

## 3. The Three Engineering Safeguards Across Multi-Wave Runs

When running `deep` (`6–10` waves) or `relentless / white-flag` (`10–20` waves), naive iterative editing causes three failure modes: **Regression**, **Bloat**, and **Fake Surrender**. `the-board` prevents all three with mandatory structural invariants:

### Safeguard A: The Non-Regression Ratchet
Every patch applied by the Executive Lead in Wave `vN` is logged in `.board/CONVERGENCE_TRACKER.md` with a unique Defense ID (`DEF-v1-01`, `DEF-v2-04`, ...).
- **Rule**: No patch in Wave `vN` is allowed to delete, weaken, or contradict a defense established in Waves `v1..v(N-1)`.
- **Verification**: The Board's Arbiter #6 (*Cross-Pillar Integration Lead*) explicitly checks every new patch against the cumulative Defense Ledger before approving it.

### Safeguard B: Two-Tier Compression (The Anti-Bloat Pass)
If you add inline guards or clauses for 12 consecutive waves without refactoring, code turns into spaghetti and legal/patent claims turn into 600-word run-on paragraphs.
- **Rule**: Every 3 waves (and mandatorily before final sign-off), the Executive Lead executes a **Two-Tier Compression Pass**:
  - **In Codebases**: Factor verbose defensive checks, invariant validators, and protocol constants into clean, zero-overhead Tier-2 helper modules/types so the Tier-1 hot-path/API remains crystal clear.
  - **In Legal / Patent Docs**: Move sprawling technical definitions, alternative equivalence lists, and statutory fallback tables into a dedicated **Tier-2 Specification Lexicon / Definitions Section**, keeping **Tier-1 Independent Claims** short, structural, and devastatingly broad.

### Safeguard C: Strict White-Flag Validation (No Lazy Surrenders)
Subagents are forbidden from raising a White Flag just to finish early. A **Formal White-Flag Concession Certificate** is accepted by The Board **only** if the Firm's transcript demonstrates:
1. **Verification of Prior Fixes**: Exact line-by-line confirmation that every vector from Wave `v(N-1)` is closed in the current artifact.
2. **At Least 3 New Candidate Nth-Order Attacks Tested & Falsified**: In the transcript, the 3 personas must propose at least 3 new candidate attacks in their pillar and prove mathematically, physically, or statutorily why the current artifact already defeats them (or why executing the attack would be technically/economically suicidal).
3. **Zero Surviving Vectors**: The final ledger table explicitly records `0` `CRITICAL`, `0` `HIGH`, and `0` `MEDIUM` surviving vectors.

---

## 4. The Post-Convergence Finishing Sequence (`Stage v(N).5` + `Stage v(N+1)`)

Once all 5 Firms raise their White Flags in Wave `vN`, the Executive Lead executes two final polishing stages before declaring victory:

1. **Stage `v(N).5` — Empirical / Benchmark / Data Synchronization**:
   - Run the compiler, test suite, linter, simulation benchmarks, or document validator (`verify_convergence.py`) and synchronize every table, figure, metric, and cross-reference across the entire workspace.
2. **Stage `v(N+1)` — Final Pre-Ship Board Sign-Off**:
   - Convene The Board one final time to audit the synchronized deliverable for zero regressions, zero formatting/compiler warnings, and 100% alignment between all files.
