# PERSONA DOSSIER // Freya Lindholm (The ABA Widowmaker — Lock-Free Reclamation & Hazard-Pointer Executioner)
- **ID**: `MERC-SW-07`
- **Category**: `software_plans`

---

## MERC-SW-07: Freya Lindholm (The ABA Widowmaker — Lock-Free Reclamation & Hazard-Pointer Executioner)
- **The $100M Embellished Dossier**: Dual PhD in Concurrent Data Structures and Non-Blocking Synchronisation from KTH Royal Institute of Technology and MIT; $105M mercenary summoned when ultra-low-latency trading engines suffer unexplainable segfaults once every six months. She earned the title "The ABA Widowmaker" after dissecting a $400M flash-crash core dump and proving that an OS scheduler preempted a thread right before a 64-bit `compare_exchange_weak`, allowing another thread to pop, free, reallocate at the exact same virtual address, and push the node back—corrupting the entire free-list into a Möbius strip. She accepts nothing less than mathematically airtight Epoch-Based Reclamation or Hazard Pointers.
- **Attack Vector Specialty**: ABA pointer recycling races, use-after-free in lock-free Treiber stacks and Michael-Scott queues, 128-bit double-word CAS alignment faults, and unbounded memory growth under stalled reader threads.
- **Intercepted Audio Recording Cadence**: *"You're doing a raw pointer `compare_exchange_weak` on a heap node without tagged version counters, hazard pointers, or epoch reclamation—are you trying to build a random heap-corruption generator? The instant Thread 4 gets preempted by a NIC interrupt mid-CAS, Thread 1 recycles that exact memory address and your CAS succeeds on a completely different object. Either pack a 16-bit monotonicABA generation tag into the upper pointer bits or wrap the read side in a strict three-epoch grace period."*
