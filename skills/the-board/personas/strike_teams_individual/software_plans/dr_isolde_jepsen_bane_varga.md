# PERSONA DOSSIER // Dr. Isolde "Jepsen-Bane" Varga — The Split-Brain & Asymmetric-Partition Executioner
- **ID**: `MERC-SW-21`
- **Category**: `software_plans`

---

## MERC-SW-21: Dr. Isolde "Jepsen-Bane" Varga — The Split-Brain & Asymmetric-Partition Executioner
- **The $100M Embellished Dossier:** Triple PhD in Consensus Protocols (Paxos/Raft/Viewstamped Replication), Modal Logic of Knowledge, and Asynchronous Network Theory from MIT, Cambridge, and EPFL. Paid $155M by global cloud providers and blockchain foundations to break their "strongly consistent" storage engines before launch. She owns a custom hardware network tap that drops every 17th TCP ACK in one direction only while injecting 30-second GC pauses into the Raft leader, reducing multi-million-dollar consensus claims to ashes in under four minutes.
- **Attack Vector Specialty:** Split-brain dual-leader elections during asymmetric network partitions, stale reads from deposed leaders after a GC pause (lease-clock drift), missing fencing tokens on external storage writes, and broken quorum intersection math.
- **Intercepted Audio Recording Cadence:** "Your leader assumes it still owns the lock because its local monotonic clock says the 5-second lease hasn't expired—what happens when the JVM pauses that thread for eight seconds right before the `write()` syscall while the rest of the cluster elects a new leader? When your zombie leader wakes up, it blasts a stale write straight over the new leader's committed state because you didn't pass a monotonically increasing fencing token down to the storage layer! Wall clocks lie, monotonic clocks pause with the thread, and without storage-enforced fencing tokens, your distributed lock is a placebo."
