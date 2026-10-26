# Domain Playbooks: Ready-to-Deploy 5-Firm + Board Rosters

Use these domain-specific playbooks to partition any problem into **5 orthogonal pillars** (zero overlap between firms) and staff each firm with a sharp **3-Persona Triad** plus a **6-Member Board**.

---

## Playbook 1: Software Architecture, Systems Coding & Performance Engineering
**Best for**: Designing distributed systems, writing high-throughput C++/Rust/Go/Python kernels, refactoring complex codebases, or eliminating subtle race conditions and memory bottlenecks.

### The 5 Orthogonal Firms
| Firm | Pillar Assignment | 3-Persona Triad |
| :--- | :--- | :--- |
| **Firm 1: *KronoLock Systems*** | **Concurrency, Lock-Free Ordering & Async State Machines** (deadlocks, livelocks, ABA, memory barriers, cancellation safety, backpressure) | **1. Viktor K.** (20-yr OS Kernel Principal)<br>**2. Dr. Elena R.** (Weak-Memory-Model Formalist)<br>**3. Marcus T.** (High-Frequency Trading Low-Latency Lead) |
| **Firm 2: *CacheLine Foundry*** | **Memory Layout, Allocator Pressure, SIMD & Hardware Sympathy** (false sharing, cache misses, zero-copy paths, OOM handling, tail latency) | **1. Kenji S.** (HPC & GPU/SIMD Architect)<br>**2. Sarah L.** (Allocator & Embedded Memory Specialist)<br>**3. Devon P.** (Profiling & Flamegraph Assassin) |
| **Firm 3: *Byzantine Fault Labs*** | **Distributed State, I/O Resilience & Failure Recovery** (partial network partitions, split-brain, idempotency, crash consistency, corrupt payloads) | **1. Priya M.** (Distributed Storage Principal)<br>**2. Anton V.** (Chaos Engineering Director)<br>**3. Liam O.** (Wire-Protocol & Serialization Purist) |
| **Firm 4: *TypeForge Guild*** | **API Ergonomics, Type Invariants & Boundary Edge Cases** (null/NaN/overflow poisoning, ABI stability, resource leaks on error paths, defensive contracts) | **1. Clara H.** (Compiler & Type-System Designer)<br>**2. Julian B.** (API Platform Distinguished Engineer)<br>**3. Zoe W.** (Fuzzing & Property-Testing Lead) |
| **Firm 5: *Aegis Build & Verify*** | **Testability, Observability, Build Determinism & Maintainability** (silent failures, untestable coupling, telemetry blind spots, regression traps) | **1. Garrett D.** (SRE VP & Incident Commander)<br>**2. Mei-Ling C.** (Formal Verification & CI Architect)<br>**3. Rafael G.** (Legacy Refactoring Surgeon) |

### The Coding Board (6 Arbiters)
- **Chair**: *Linus-caliber Chief Systems Architect* (Zero tolerance for regressions or broken abstractions)
- **Arbiter 2**: *Principal Security & Memory-Safety Engineer*
- **Arbiter 3**: *The Anti-Bloat Minimalist* (Vetoes unnecessary classes, dependencies, or over-abstraction)
- **Arbiter 4**: *Hardware & Tail-Latency Realist* (`p99.99` latency enforcer)
- **Arbiter 5**: *API & Developer Experience Steward*
- **Arbiter 6**: *Verification & Test-Harness Director*

---

## Playbook 2: Cybersecurity, Cryptography & Zero-Day Red-Teaming
**Best for**: Auditing smart contracts, auth pipelines, sandboxes, cloud infrastructure, cryptographic protocols, and AI agent boundaries.

### The 5 Orthogonal Firms
| Firm | Pillar Assignment | 3-Persona Triad |
| :--- | :--- | :--- |
| **Firm 1: *ZeroDay Syndicate*** | **Memory Corruption, Deserialization & Parser Exploits** (integer overflows, UAF, type confusion, parser differentials, gadget chains) | **1. "Cipher" (Alexei)** (Offensive Binary Exploit Lead)<br>**2. Dr. Nora V.** (Binary Analysis & Symbolic Execution)<br>**3. Jin-Woo K.** (Browser/VM JIT Exploit Researcher) |
| **Firm 2: *ShadowToken Collective*** | **Authentication, Session State, Privilege Escalation & IAM** (confused deputy, SSRF, OAuth/JWT forgery, TOCTOU permission bypass, tenant isolation) | **1. Camille D.** (Cloud Multi-Tenant Red-Team Lead)<br>**2. Tariq A.** (Identity & Zero-Trust Architect)<br>**3. Sasha M.** (API Logic & Race-Condition Hunter) |
| **Firm 3: *SideChannel Omega*** | **Applied Cryptography, Timing Oracles & Key Lifecycle** (nonce reuse, padding/timing oracles, weak entropy, key rotation gaps, downgrade attacks) | **1. Prof. Henrik L.** (Cryptanalysis Chair)<br>**2. Yael B.** (Hardware & Microarchitectural Side-Channels)<br>**3. Matteo R.** (Protocol State-Machine Breaker) |
| **Firm 4: *SupplyChain Viper*** | **Sandbox Escape, Dependency Poisoning & Prompt/Command Injection** (container escape, env-var leaks, indirect prompt injection, exfiltration channels) | **1. Morgan K.** (Sandbox & Hypervisor Escape Specialist)<br>**2. Ananya S.** (AI/LLM Adversarial Red-Team Lead)<br>**3. Chris V.** (CI/CD & Artifact Integrity Auditor) |
| **Firm 5: *BlackSwan Economics*** | **Asymmetric DoS, Resource Exhaustion & Economic/Game-Theoretic Griefing** (algorithmic complexity attacks, zip/XML bombs, MEV/fee griefing, state bloat) | **1. Damon F.** (Adversarial Game-Theory & MEV Strategist)<br>**2. Elena G.** (L4/L7 Denial-of-Service Architect)<br>**3. Omar Z.** (Database & Queue Starvation Tester) |

---

## Playbook 3: Legal Documents, Contracts & Patent Prosecution (`USPTO / PTAB / Fed. Cir.`)
**Best for**: Drafting and red-teaming utility/provisional patents, M&A agreements, commercial licensing contracts, SaaS MSAs, and regulatory filings.

### The 5 Orthogonal Firms (Competitor Design-Around & Invalidity Syndicates)
| Firm | Pillar Assignment | 3-Persona Triad |
| :--- | :--- | :--- |
| **Firm 1: *Vanguard IP & Design-Around*** | **Core Architecture / Primary Claim Element Evasion** (omitting elements, substituting non-claimed equivalents, software-only vs. hardware workarounds) | **1. Arthur Vance** (AmLaw 10 Lead Trial Partner)<br>**2. Dr. Chen** (Competitor Chief Systems Engineer)<br>**3. Rachel S.** (Federal Circuit Claim-Construction Specialist) |
| **Firm 2: *Apex PTAB Invalidity Group*** | **Statutory Validity (`§§ 101, 102, 103, 112`) & Indefiniteness Traps** (*Alice/Mayo* abstract-idea attacks, *Williamson* means-plus-function traps, lack of antecedent basis, enablement gaps) | **1. Hon. Judge Miller (Ret.)** (Former PTAB APJ)<br>**2. David K.** (IPR Petition Strategist)<br>**3. Dr. Priya N.** (Prior-Art & Obviousness Combinatorics Expert) |
| **Firm 3: *Divided Infringement & Territoriality LLP*** | **Multi-Actor (`Akamai`), Cross-Border (`NTP`) & Open-Source Split-Delivery Loopholes** (splitting steps across vendor/customer, offshore servers, uncalibrated DIY kits, firmware updates) | **1. Eleanor Vance-Sterling** (Cross-Border Licensing Partner)<br>**2.Liam T.** (Open-Core & SaaS Monetization Counsel)<br>**3. Dr. Hoffman** (Aftermarket & Repair Doctrine Specialist) |
| **Firm 4: *Precision Metrics & Evidentiary Evasion*** | **Threshold Gaming, Duty-Cycle Evasion & Black-Box Detection Avoidance** (operating just outside numeric bounds, intermittent toggling, encrypted telemetry blocking infringement proof) | **1. Marcus Webb** (Defense & Aerospace IP Litigator)<br>**2. Dr. Volkov** (Signal Processing & Obfuscation Lead)<br>**3. Hannah J.** (Discovery & Reverse-Engineering Strategist) |
| **Firm 5: *Commercial Deal-Breaker & Liability Syndicate*** | **Indemnification, Cap-Ex Allocation, Exhaustion (*Quanta*) & Termination Traps** (patent exhaustion,royalty-base manipulation, change-of-control leaks, exclusive-grant backdoors) | **1. Victoria Sterling** (M&A Tech Transactions Chair)<br>**2. Greg P.** (Private Equity Distressed-IP Buyer)<br>**3. Sophia L.** (Antitrust & FRAND/Standard-Essential Counsel) |

### The Legal / Patent Board (6 Arbiters)
- **Chair**: *Former Federal Circuit Chief Judge / Senior Prosecution Architect*
- **Arbiter 2**: *The Two-Tier Lexicographer* (Moves sprawling inline definitions into a clean Specification Lexicon so claims stay crisp, readable, and judge-friendly)
- **Arbiter 3**: *§ 112(a)/(b)/(f) Structural Enablement Enforcer*
- **Arbiter 4**: *Litigation Damages & Royalty-Base Maximizer*
- **Arbiter 5**: *Competitor Chief CTO Representative* (Tests whether a proposed claim patch actually blocks real-world engineering workarounds)
- **Arbiter 6**: *Global Portfolio Strategist (`USPTO / EPO / PCT / CNIPA`)*

---

## Playbook 4: Commercial, B2B, Venture & Defense (`DoD / Pentagon`) Blue-Team Tournament
**Best for**: Go-To-Market (GTM) masterplans, Pentagon/DIU/SBIR/OTA acquisition strategies, enterprise pricing, fundraising pitches, and product positioning.

### The 5 Competing Blue-Team Strategy Boutiques
In **Blue-Team Mode**, each firm competes to win the full advisory mandate by building the sharpest, most actionable strategy for its assigned domain or customer segment:
- **Firm A (*Paladin Defense & Dual-Use Partners*)**: Pentagon / DoD (`DIU CSO, AFWERX/SpaceWERX/NavalX SBIR/STTR, APFIT, Production OTAs under 10 U.S.C. § 4022, Prime Subcontracting`).
- **Firm B (*Titan Industrial & Infrastructure*)**: High-ROI Commercial B2B wedge (unit economics, SLA-backed Hardware-as-a-Service / SaaS pricing, anchor customer pilot structure).
- **Firm C (*SandHill DeepTech Capital*)**: Capital-stack choreography (dilutive vs. non-dilutive sequencing, milestone valuation inflection points, strategic corporate venture moat).
- **Firm D (*CategoryKing Positioning & Narrative*)**: Brand voice, competitive wedge, category creation, live demo choreography that closes 7-figure contracts in 60 seconds.
- **Firm E (*Fortress Ecosystem & OEM Licensing*)**: Platform lock-in, SDK/API ecosystem, OEM royalty structures, regulatory/safety certification moat.

### How The Board Adjudicates a Blue-Team Tournament
1. **Live Pitch & Cross-Examination**: All 5 firms pitch their strategies in full persona dialogue.
2. **Board Scoring & Top-3 Podium**: The Board grades each firm (`0–100`) on **Unit-Economic Realism**, **Speed-to-First-Dollar**, **Defensibility**, and **Execution Specificity**, then selects the **Top 3 Winning Firms**.
3. **Executive Lead Master Synthesis**: The Lead takes the Top 3 winning frameworks—and cherry-picks the highest-leverage tactical gems from Firms 4 & 5—to write the unified Master Playbook.

---

## Playbook 5: PhD-Level Algorithm, Physics, Control Theory & ML Research
**Best for**: Designing novel control loops, robotics/aerodynamics estimators, ML architectures, numerical solvers, and physics simulations.

### The 5 Orthogonal Firms
1. **Firm 1 (*Lyapunov Stability & Control Discretization*)**: Phase margin, transport delay, actuator saturation, discrete-time aliasing, non-minimum-phase zeros.
2. **Firm 2 (*Stochastic Estimation & Sensor Fusion*)**: Observability rank loss, covariance windup, non-Gaussian outlier rejection, time-sync skew.
3. **Firm 3 (*Continuum Physics & Boundary-Layer Realism*)**: Unmodeled physical couplings, thermal drift, structural resonance, Reynolds/Mach scaling breakdowns.
4. **Firm 4 (*Numerical Analysis & Real-Time Compute Budget*)**: Conditioning numbers, FP16/FP32/fixed-point quantization error, WCET (worst-case execution time) guarantees.
5. **Firm 5 (*Empirical Ablation & Adversarial Benchmark Lab*)**: Designing falsifiable synthetic + hardware-in-the-loop (HIL) experiments to prove the algorithm beats SOTA baselines.
