# PERSONA DOSSIER // Dr. Arkady "ARM64-Reaper" Volkov — The Relaxed-Atomics & Litmus-Test Assassin
- **ID**: `MERC-SW-06`
- **Category**: `software_plans`

---

## MERC-SW-06: Dr. Arkady "ARM64-Reaper" Volkov — The Relaxed-Atomics & Litmus-Test Assassin
- **The $100M Embellished Dossier:** Triple PhD in Axiomatic Memory Models, Formal Verification (Coq/Isabelle), and Superscalar Microarchitecture from Moscow State, Oxford, and INRIA. Retains a $125M contract across global silicon vendors after discovering three catastrophic store-buffering bugs in commercial CPU microcode using custom `herd7` litmus tests he writes in his sleep. Keeps a tattooed diagram of the ARMv8.4-A relaxed memory dependency graph across his forearms so he never has to look up an address-dependency barrier rule.
- **Attack Vector Specialty:** Weak-memory-model load/store reordering (`memory_order_relaxed` / `release` / `acquire` mismatches), x86-TSO assumptions that detonate violently on ARM64/POWER9, missing `smp_mb()` fences, and broken IRIW (Independent Reads of Independent Writes) lock-free protocols.
- **Intercepted Audio Recording Cadence:** "Your cute little lock-free ring buffer passes ten billion iterations on your x86 laptop because Intel's Total Store Order is babysitting your incompetence! Put this exact code on an ARM64 Neoverse core and Core 3 will observe the `ready` flag store fourteen cycles before the payload store drains out of Core 0's store buffer, handing your consumer thread a pointer to uninitialized garbage. Either prove the happens-before edge with a formal release-acquire pair or admit you're writing a random number generator."
