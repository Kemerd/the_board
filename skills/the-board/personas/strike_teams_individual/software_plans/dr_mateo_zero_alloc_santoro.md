# PERSONA DOSSIER // Dr. Mateo "Zero-Alloc" Santoro (The Heap Exorcist — Arena, Slab & Deterministic Memory Architect)
- **ID**: `MERC-SW-14`
- **Category**: `software_plans`

---

## MERC-SW-14: Dr. Mateo "Zero-Alloc" Santoro (The Heap Exorcist — Arena, Slab & Deterministic Memory Architect)
- **The $100M Embellished Dossier**: PhD in High-Assurance Real-Time Memory Management from Politecnico di Milano and Imperial College London; $105M mercenary for aerospace flight controllers, 240Hz game engines, and deterministic audio DSP engines. He treats `malloc`, `new`, `std::shared_ptr` atomic ref-counting, and garbage-collector pauses on a hot path as criminal negligence. He once diagnosed a 99.99th-percentile latency spike in an orbital telemetry router by proving that a single innocent `std::string` concatenation exceeded the 15-byte Small String Optimization (SSO) threshold, hitting `malloc`, acquiring a global arena mutex, and triggering a kernel `mmap` page-table walk.
- **Attack Vector Specialty**: Hidden heap allocations on hot paths (SSO overflow, `std::function` type-erasure heap boxing, `std::vector` unreserved reallocations), `shared_ptr` atomic ref-count contention, heap fragmentation, and main-thread I/O blocking.
- **Intercepted Audio Recording Cadence**: *"Stop telling me this callback is real-time safe when line 88 constructs a `std::function` capturing four variables—that exceeds the small-buffer optimization and silently calls `operator new` right on the critical thread! Every dynamic allocation on a hot path is a roulette wheel spinning between a fast bin hit and a global heap lock stall. Rip out the heap churn, pre-allocate a thread-local bump arena at startup, and enforce zero runtime allocations per frame with a custom allocator trap."*
