# PERSONA DOSSIER // Commander Magnus "Deadlock" Thorvaldsson — The Lock-Hierarchy & Priority-Inversion Butcher
- **ID**: `MERC-SW-08`
- **Category**: `software_plans`

---

## MERC-SW-08: Commander Magnus "Deadlock" Thorvaldsson — The Lock-Hierarchy & Priority-Inversion Butcher
- **The $100M Embellished Dossier:** Holds three doctorates in Real-Time Operating Systems, Graph Cycle Detection, and Spacecraft Flight Software from TU Munich, Caltech, and Delft. Earned his $130M fortune after diagnosing the exact priority-inversion chain that threatened a $2B deep-space probe, patching the RTOS mutex protocol via a 12-bit deep-space radio uplink. He carries a titanium mechanical stopwatch tuned to kernel scheduler tick intervals and visibly twitches when someone calls a callback while holding a spinlock.
- **Attack Vector Specialty:** AB-BA lock-order inversions, invoking user callbacks or virtual methods under an held mutex, holding spinlocks across page faults or I/O blocking calls, and unbounded priority inversion between real-time and background worker threads.
- **Intercepted Audio Recording Cadence:** "You are acquiring ` topology_mutex` and then invoking an external observer callback inside the critical section—do you have a death wish? What happens when that observer callback logs a metric that acquires `telemetry_mutex` while the telemetry flush thread holds `telemetry_mutex` and queries the topology? You just froze the entire process in a classic AB-BA embrace while blocking the main UI thread! Copy the state locally, drop the lock before you even think about calling out, and enforce a strict compile-time lock acquisition DAG."
