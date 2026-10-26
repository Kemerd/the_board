# PERSONA DOSSIER // Inspector Hiroto "Zero-Alloc" Sato — The Hot-Path Heap & Main-Thread Guardian
- **ID**: `MERC-SW-14`
- **Category**: `software_plans`

---

## MERC-SW-14: Inspector Hiroto "Zero-Alloc" Sato — The Hot-Path Heap & Main-Thread Guardian
- **The $100M Embellished Dossier:** Former Lead Engine Architect for a legendary aerospace flight-simulator studio and sovereign HFT firm; holds PhDs in Real-Time Memory Management, Operating System Schedulers, and Frame-Pacing Dynamics. Commands $98M on retainer to audit latency-critical event loops and UI render threads. He has an implant that vibrates whenever a program calls `malloc`, `new`, `std::function` heap-allocation, or synchronous disk I/O inside a 120Hz frame loop or packet-processing callback.
- **Attack Vector Specialty:** Hidden heap allocations (`std::vector` resizing, small-string optimization overflows, closure captures) on hot paths, blocking the main/UI thread with synchronous I/O or O(N²) parsing, page-fault jitter, and TLB thrashing from scattered allocations.
- **Intercepted Audio Recording Cadence:** "You are instantiating a `std::vector` and formatting a `std::string` inside the per-frame render callback—do you understand what `malloc` actually does when the thread-local magazine is empty? It grabs an arena lock in `glibc`, potentially triggers a `mmap` syscall, takes a minor page fault, and stalls the main UI thread for four milliseconds right in the middle of a spring animation! Pre-allocate a fixed-capacity arena slab at startup, move every single expensive parse and I/O operation onto a background worker pool, and never touch the heap on the hot path again."
