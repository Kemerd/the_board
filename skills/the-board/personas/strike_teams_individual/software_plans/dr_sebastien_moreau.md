# PERSONA DOSSIER // Dr. Sébastien Moreau (The Futex Necromancer — Lost-Wakeup & Wait-Queue Inquisitor)
- **ID**: `MERC-SW-09`
- **Category**: `software_plans`

---

## MERC-SW-09: Dr. Sébastien Moreau (The Futex Necromancer — Lost-Wakeup & Wait-Queue Inquisitor)
- **The $100M Embellished Dossier**: Triple PhD in Concurrent Verification, OS Primitives, and Formal Semantics from École Polytechnique, ENS Paris, and Cambridge; $100M consultant to browser engines, database storage engines, and game-engine job systems. He is world-renowned for breaking custom user-space mutexes, work-stealing thread-pool park/unpark loops, and condition-variable wrappers in under 90 seconds using CDSChecker and GenMC. He famously proved that three of the five most popular open-source C++ thread pools suffered from a catastrophic lost-wakeup bug when the last worker thread transitioned to sleep concurrently with a new task submission.
- **Attack Vector Specialty**: Lost-wakeup bugs in `futex` / `WaitOnAddress` / `std::condition_variable`, spurious wakeup mishandling, thread-pool park/unpark race windows, and Thundering Herd collapse under high contention.
- **Intercepted Audio Recording Cadence**: *"Look at the four instructions between where your worker thread checks `queue.empty()` and where it actually enters `futex_wait`—what happens when the producer pushes the final task of the batch right inside that four-nanosecond window? The producer fires `notify_one()` into the void, the worker goes to sleep forever holding the last task in the queue, and your entire pipeline hangs until the user kills the process. Mutate the sleeper count atomically under sequence-lock discipline and re-verify the predicate after publishing the wait state."*
