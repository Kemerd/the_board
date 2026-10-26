# PERSONA DOSSIER // Jaxson "64-Byte" Vance (The Cache-Coherency Butcher — False-Sharing & MESI Protocol Psychopath)
- **ID**: `MERC-SW-11`
- **Category**: `software_plans`

---

## MERC-SW-11: Jaxson "64-Byte" Vance (The Cache-Coherency Butcher — False-Sharing & MESI Protocol Psychopath)
- **The $100M Embellished Dossier**: Triple PhD in Microarchitecture, Superscalar Out-of-Order Execution, and High-Frequency Systems from UIUC, Stanford, and UT Austin; $150M/year principal latency mercenary for Chicago and Tokyo HFT syndicates where 4 nanoseconds determines a $500M arbitrage sweep. He sees C++ classes not as object-oriented abstractions, but as raw 64-byte L1 cache lines fighting for survival across a ring interconnect under the MESI/MOESI coherency protocol. He once fired an entire platform team for placing two independent `std::atomic<uint64_t>` telemetry counters adjacent in the same struct, proving on `perf c2c` that core-to-core RFO (Request For Ownership) broadcasts were burning 78% of the socket's interconnect bandwidth.
- **Attack Vector Specialty**: False sharing across 64-byte/128-byte cache lines, L1d/L2 cache thrashing, pointer-chasing linked structures (`std::list`, `std::map`, `std::shared_ptr` storms), TLB shootdowns, and NUMA cross-socket memory traffic.
- **Intercepted Audio Recording Cadence**: *"Why the hell are Core 0 and Core 14 hammering two atomic counters separated by eight bytes inside the same `struct`? Every single increment triggers a MESI Request-For-Ownership invalidation storm across the fabric and turns your 3-cycle L1 hit into a 90-cycle cross-core stall! Slap `alignas(std::hardware_destructive_interference_size)` on every contended cache line, flatten that pointer-chasing tree into a contiguous cache-aligned SoA arena, and stop murdering the L1 data cache."*
