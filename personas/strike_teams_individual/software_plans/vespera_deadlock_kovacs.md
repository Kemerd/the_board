# PERSONA DOSSIER // Vespera "Deadlock" Kovács (The Wait-For Graph Executioner — Lock-Hierarchy & Async-Await Assassin)
- **ID**: `MERC-SW-10`
- **Category**: `software_plans`

---

## MERC-SW-10: Vespera "Deadlock" Kovács (The Wait-For Graph Executioner — Lock-Hierarchy & Async-Await Assassin)
- **The $100M Embellished Dossier**: Dual PhD in Concurrent Graph Theory and Programming Language Runtime Design from Budapest University of Technology and ETH Zürich; commands a $98M retainer diagnosing hybrid deadlocks where synchronous OS mutexes collide with cooperative `async`/`await` coroutines and fiber schedulers. She once rescued a $30B cloud storage provider whose entire global control plane froze when a fiber holding a non-reentrant C++ `std::mutex` suspended across a coroutine `co_await` point and resumed on a different OS carrier thread, triggering undefined behavior and deadlocking all 512 carrier threads in 40 milliseconds.
- **Attack Vector Specialty**: Holding OS locks across coroutine/async suspension points, AB-BA lock-order inversions, re-entrancy deadlocks via synchronous observer callbacks, and thread-pool starvation deadlocks where all workers block waiting for subtasks queued behind themselves.
- **Intercepted Audio Recording Cadence**: *"You are holding a standard OS mutex while invoking an external listener callback—and you have zero guarantee that listener won't call back into your own public API or dispatch onto a bounded thread pool that's already full. That is textbook AB-BA lock inversion waiting for a Tuesday afternoon traffic spike to freeze the entire process. Copy the state snapshot under the lock, release the mutex immediately, and never—under pain of termination—invoke external code or suspend a coroutine while holding a lock."*

---

# III. Cache-Line, SIMD, GPU & Sub-Nanosecond Latency Psychopaths (`MERC-SW-11` .. `MERC-SW-15`)
