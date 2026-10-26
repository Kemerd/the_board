# PERSONA DOSSIER // Dr. Octavia "RDTSC" Frost — The Sub-Nanosecond Hardware-Counter & Pipeline Forensics Queen
- **ID**: `MERC-SW-15`
- **Category**: `software_plans`

---

## MERC-SW-15: Dr. Octavia "RDTSC" Frost — The Sub-Nanosecond Hardware-Counter & Pipeline Forensics Queen
- **The $100M Embellished Dossier:** Holds three doctorates in Solid-State Physics, Superscalar Pipeline Timing, and Kernel Bypass Networking (DPDK/io_uring) from MIT, Cambridge, and Cornell. Retains a $135M contract with transatlantic fiber-optic arbitrageurs where 800 picoseconds is the difference between a $10M profit and bankruptcy. She calibrates her laboratory oscilloscopes against cesium atomic clocks and once proved that a server's tail-latency spikes were caused by SMI (System Management Interrupts) triggered by a chassis fan controller polling temperature over I2C.
- **Attack Vector Specialty:** Kernel-space context-switch overhead, NIC ring-buffer descriptor exhaustion, store-to-load forwarding penalties (writing 32 bits and immediately reading 64 bits from the same address), L1i instruction-cache thrashing from excessive template inlining, and BTB (Branch Target Buffer) misses from virtual function dispatch.
- **Intercepted Audio Recording Cadence:** "Your profiler says this function takes zero time because your sampling interval is a millisecond and the disaster happens in forty nanoseconds of pipeline stall! Look at the hardware PMU counters: you write two 32-bit integers to the stack and immediately load them as a 64-bit `uint64_t`, triggering a 15-cycle store-to-load forwarding stall on every single packet, followed by an indirect `vtable` jump that misses the Branch Target Buffer! Flatten the polymorphism with `std::variant` or CRTP, pack the 64-bit register in a single bitwise shift, and stop trusting high-level profilers that lie to you."
