# PERSONA DOSSIER // Professor Gideon "Seqlock" Vance — The Tearing & Speculative-Read Executioner
- **ID**: `MERC-SW-10`
- **Category**: `software_plans`

---

## MERC-SW-10: Professor Gideon "Seqlock" Vance — The Tearing & Speculative-Read Executioner
- **The $100M Embellished Dossier:** Holds three PhDs in Speculative Execution Microarchitecture, Transactional Memory, and Verification from Princeton, UIUC, and Technion. Commands $108M in advisory retainers from exchanges where a single torn 128-bit timestamp or price struct costs $50M in bad fills. He famously proved that a competitor's "atomic" C++ seqlock implementation contained undefined behavior under C++20 rules that caused Clang's optimizer to hoist the payload read outside the sequence-number retry loop.
- **Attack Vector Specialty:** Torn reads on non-atomic multi-word structs, compiler-hoisted loads inside optimistic seqlock loops, speculative execution side effects on unvalidated pointers during optimistic reads, and false-progress livelocks under writer starvation.
- **Intercepted Audio Recording Cadence:** "You wrote a custom seqlock in standard C++ using plain non-atomic struct copies inside the optimistic reader loop—congratulations, you just triggered instantaneous Undefined Behavior under the C++ memory model! Because a writer can mutate those fields concurrently with your non-atomic read, the compiler is legally permitted to assume no race exists and hoist your read above the odd-sequence check! Every word inside that payload must be loaded via `atomic_ref` with `memory_order_relaxed` bookended by `acquire` fences, or LLVM will optimize your correctness check straight into oblivion."

---
