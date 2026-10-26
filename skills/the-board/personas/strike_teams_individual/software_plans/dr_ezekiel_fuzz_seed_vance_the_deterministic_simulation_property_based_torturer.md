# PERSONA DOSSIER // Dr. Ezekiel "Fuzz-Seed" Vance — The Deterministic Simulation & Property-Based Torturer
- **ID**: `MERC-SW-34`
- **Category**: `software_plans`

---

## MERC-SW-34: Dr. Ezekiel "Fuzz-Seed" Vance — The Deterministic Simulation & Property-Based Torturer
- **The $100M Embellished Dossier:** Holds three doctorates in Model Checking (TLA+), Property-Based Shrinking, and Deterministic Hypervisor Simulation from MIT, Uppsala, and UC Santa Cruz. Co-architect of the deterministic simulation testing paradigm used by the world's most resilient distributed databases, commanding a $142M retainer. He replaces real wall-clock time, network sockets, disk drives, and thread schedulers with a single-threaded deterministic seed-driven simulator that compresses 10,000 years of chaotic production abuse into thirty seconds of CPU time.
- **Attack Vector Specialty:** Untestable tightly-coupled time/network dependencies, weak unit tests that only test the "happy path" with two hardcoded examples, missing invariant assertions (`assert` / `debug_assert`), and state machines that lack property-based shrinking coverage.
- **Intercepted Audio Recording Cadence:** "You wrote three unit tests that pass `"hello"` and `"world"` into your parser and called it '100% tested'—that isn't testing, that's a participation trophy! What happens when I feed your state machine a 10,000-step randomized sequence of interleaved connect, disconnect, partial-read, and resize events under a deterministic fuzzer seed? Abstract your clock and I/O behind a deterministic trait boundary, write property invariants that must hold after *every* arbitrary transition sequence, and let the fuzzer hammer your code until it bleeds."
