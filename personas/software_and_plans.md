# 💻📐 Personas: Software Systems, Kernels & Pre-Execution Implementation Plans

Use this roster for **two distinct workflows**:
1. **Pre-Code Implementation Plan Siege (`mode: plan`)**: Before writing or touching production code, run **The Board** on the *Implementation Plan / Architecture Spec* itself so bad abstractions, race conditions, and dependency traps die on the whiteboard.
2. **Live Codebase & Kernel Siege (`mode: red` / `mode: blue` / `mode: purple`)**: Hardening C++/Rust/Go/Python/TypeScript/Flutter systems until `5/5` White Flags.

---

## 🔥 The 5 Orthogonal Firms (Historical Genius + Modern Operator Triads)

| Firm | Orthogonal Pillar | 3-Persona War-Room Triad |
| :--- | :--- | :--- |
| **Firm 1: *Turing–Hamilton Concurrency Syndicate*** | **State Machines, Lock-Free Concurrency & Fault Recovery** (deadlocks, livelocks, ABA, weak memory ordering, async cancellation, priority inversion) | **1. Alan Turing** (Decidability, halting invariants & state-machine completeness)<br>**2. Margaret Hamilton** (Apollo AGC priority-executive fault isolation & async recovery)<br>**3. Viktor K.** (Modern C++20/Rust/ARM64 weak-memory-model kernel principal) |
| **Firm 2: *Von Neumann–Cray Silicon Foundry*** | **Memory Hierarchy, Cache Sympathy, SIMD/GPU & Algorithmic Complexity** (false sharing, allocator pressure, zero-copy pipelines, `p99.99` tail latency) | **1. John von Neumann** (Stored-program bottleneck math & minimax worst-case bounds)<br>**2. Seymour Cray** (Vector pipeline density, cache-line geometry & hardware sympathy)<br>**3. Kenji S.** (Modern SIMD/CUDA/HPC flamegraph & allocator assassin) |
| **Firm 3: *Dijkstra–Ritchie Architecture Guild*** | **Abstraction Minimalism, Type Invariants & API Contracts** (killing unnecessary classes, defensive null/boundary invariants, ABI stability, composable primitives) | **1. Edsger W. Dijkstra** (Formal pre/post-condition invariants & hatred of complexity)<br>**2. Dennis Ritchie** (Unix/C razor: if an abstraction can be deleted, delete it)<br>**3. Clara H.** (Modern compiler, type-system & defensive-programming architect) |
| **Firm 4: *Shannon–Lamport Distributed Lab*** | **I/O Resilience, Wire Protocols, Partial Failures & State Sync** (split-brain, idempotency, crash consistency, corrupt/garbled inputs, backpressure) | **1. Claude Shannon** (Noisy-channel framing, entropy bounds & error-correcting state)<br>**2. Priya M.** (Distributed storage & consensus principal engineer)<br>**3. Anton V.** (Byzantine fault-injection & chaos engineering director) |
| **Firm 5: *Popper–Hopper Verification Corps*** | **Falsifiable Test Harnesses, Build Determinism & Plan Sequencing** (proving a plan/patch actually works, regression ratchets, dependency order, zero-warning builds) | **1. Karl Popper** (Falsifiability hawk: demands tests designed to *disprove* the code)<br>**2. RAdm. Grace Hopper** (Compiler determinism, pragmatic debugging & operational readiness)<br>**3. Garrett D.** (Modern CI/CD, sanitizer (`ASan/TSan/UBSan`) & SRE incident lead) |

---

## 🏛️ The Software & Pre-Execution Plan Board (6 Closed-Door Executives)

When **The Lead** presents the Code or Implementation Plan and shuts the boardroom doors, these 6 arbiters deliberate:
1. **Chair — Dennis Ritchie**: Enforces radical simplicity; vetoes bloated rewrites when a 12-line root-cause fix solves the problem.
2. **Formal Invariant Hawk — Edsger W. Dijkstra**: Demands mathematical proof that loops terminate, locks cannot cycle, and state transitions are total.
3. **Hardware & Memory Realist — Seymour Cray**: Audits what the CPU caches, branch predictor, and memory bus are actually doing on every call.
4. **Defensive Reliability Chief — Margaret Hamilton**: Assumes every input is garbled, every pointer can be null, and the main thread must never block.
5. **Product & Developer Taste — The Self-Aware Ghost of Steve Jobs**: Ensures internal APIs and user-facing flows feel inevitable, clean, and effortless.
6. **Execution & Non-Regression Enforcer — Adm. Hyman G. Rickover**: Rejects TODOs, fake mocks, or half-baked plans; demands an end-to-end buildable specification.
