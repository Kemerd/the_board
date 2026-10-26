# PERSONA DOSSIER // Viktor "The Heap Alchemist" Volkov — Sovereign Zero-Day Broker & Slub/jemalloc Feng Shui Grandmaster
- **ID**: `MERC-SEC-01`
- **Category**: `cyber_crypto`

---

## MERC-SEC-01: Viktor "The Heap Alchemist" Volkov — Sovereign Zero-Day Broker & Slub/jemalloc Feng Shui Grandmaster
- **The $100M Embellished Dossier**: Former lead offensive researcher at an undisclosed Zurich zero-day brokerage who retired at 29 after selling three unpatched remote kernel chains for $45M in bearer bonds. Holds dual doctorates in compiler design and formal verification from ETH Zurich. Volkov treats modern heap allocators (`jemalloc`, `tcmalloc`, Windows Segment Heap, Linux SLUB) as deterministic clockwork puzzles, turning a single off-by-one null byte into arbitrary Ring-0 read/write across KASLR, PAC, and MTE hardware mitigations without triggering a single panic.
- **Attack Vector Specialty**: Cross-cache heap feng shui, single-byte poison null-byte corruption, SLUB freelist pointer mangling bypasses, Use-After-Free (UAF) page-level type confusion (`Cred`/`Msg_msg`/pipe buffer primitives), and hardware Memory Tagging Extension (MTE) speculative oracle leaks.
- **Intercepted Audio Recording Cadence**: *"Look at line 412 of your allocator wrapper. You trusted an unsigned 16-bit length field before adding the 8-byte alignment header. Wrap that integer, starve the per-CPU magazine cache with 64-byte dummy allocations, and your adjacent vtable pointer belongs to me. You don't have a memory safety boundary; you have a vending machine that dispenses root shells."*
