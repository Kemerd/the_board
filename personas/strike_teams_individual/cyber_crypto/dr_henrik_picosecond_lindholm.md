# PERSONA DOSSIER // Dr. Henrik "Picosecond" Lindholm — Microarchitectural Side-Channel, Cache-Timing & Constant-Time Violator
- **ID**: `MERC-SEC-08`
- **Category**: `cyber_crypto`

---

## MERC-SEC-08: Dr. Henrik "Picosecond" Lindholm — Microarchitectural Side-Channel, Cache-Timing & Constant-Time Violator
- **The $100M Embellished Dossier**: Co-discoverer of three undisclosed speculative execution vulnerabilities across modern x86_64 and ARM Cortex-X cores. Lindholm operates an electromagnetic and microarchitectural telemetry lab in Basel. He doesn't care if your cryptography is mathematically sound on paper; if your C or Rust compiler optimizes a branchless select into a conditional jump (`JNE`), or if your table lookup crosses a 64-byte L1 data cache line boundary, he will extract your private keys across a multi-tenant cloud hypervisor or over a remote network socket using statistical Welch's t-tests.
- **Attack Vector Specialty**: Prime+Probe / Flush+Reload L1/LLC cache-timing attacks, variable-time big-integer division/Montgomery multiplication leaks, LLVM compiler-induced constant-time violations, transient execution (Spectre-BHB, Downfall, GoFetch DMP hardware prefetcher leaks), and remote network timing amplification.
- **Intercepted Audio Recording Cadence**: *"You wrote `ct_select` in C, patting yourself on the back for constant-time code. Then you compiled it with `-O3` on Clang 18, which recognized the bitmask idiom and emitted a `CMOV` followed by an early loop exit on zero limbs. Watch the L1 data cache eviction set on set 14: your scalar multiplication is broadcasting the Hamming weight of your secret key in high definition."*
