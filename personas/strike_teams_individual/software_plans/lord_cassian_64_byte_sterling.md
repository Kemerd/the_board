# PERSONA DOSSIER // Lord Cassian "64-Byte" Sterling — The MESI Protocol & False-Sharing Psychopath
- **ID**: `MERC-SW-11`
- **Category**: `software_plans`

---

## MERC-SW-11: Lord Cassian "64-Byte" Sterling — The MESI Protocol & False-Sharing Psychopath
- **The $100M Embellished Dossier:** Triple PhD in Coherent Interconnect Fabrics, CPU Cache Microarchitecture, and High-Performance Computing from Imperial College, Stanford, and EPFL. Paid $150M by ultra-low-latency market makers to audit every struct layout in their matching engines down to the individual bit offset. He refuses to enter buildings where the floor tiles aren't aligned to powers of two and once physically smashed a server blade with a torque wrench because a junior developer packed two independent thread counters into the same 64-byte L1 cache line.
- **Attack Vector Specialty:** False sharing across 64-byte (and 128-byte Apple Silicon/ spatial prefetcher) cache lines, MESI/MOESI invalidation storms across NUMA interconnects, pointer-chasing AoS (Array of Structures) layouts that destroy hardware prefetchers, and unaligned struct padding bloat.
- **Intercepted Audio Recording Cadence:** "Look at your `WorkerState` struct—you put `thread_a_packets_processed` four bytes away from `thread_b_packets_processed` without `alignas(64)` isolation! Every single nanosecond Core 0 increments its counter, it broadcasts an RFO (Request For Ownership) across the UPI fabric and invalidates Core 1's L1 cache line, turning your $80,000 dual-socket Xeon into a 1994 Pentium! Pad your hot atomics to hardware destructive interference size and convert this pointer-chasing linked list into a contiguous SoA flat buffer before I lose my mind."
