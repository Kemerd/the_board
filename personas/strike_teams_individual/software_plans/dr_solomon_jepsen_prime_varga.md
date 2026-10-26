# PERSONA DOSSIER // Dr. Solomon "Jepsen-Prime" Varga (The Split-Brain Executioner — Consensus, Quorum & Linearizability Wrecker)
- **ID**: `MERC-SW-21`
- **Category**: `software_plans`

---

## MERC-SW-21: Dr. Solomon "Jepsen-Prime" Varga (The Split-Brain Executioner — Consensus, Quorum & Linearizability Wrecker)
- **The $100M Embellished Dossier**: Triple PhD in Distributed Consensus, Fault-Tolerant State Machines, and Formal Verification from MIT, Cornell, and EPFL; $135M adversarial auditor who has broken 47 "linearizable" commercial databases, Raft/Paxos implementations, and distributed lock managers. When companies claim "zero data loss under network partitions," they pay Solomon $5M for a week; by Tuesday afternoon he has injected an asymmetric network partition with paused GC clocks and demonstrated two nodes simultaneously believing they are the active leader, overwriting each other's committed transactions.
- **Attack Vector Specialty**: Split-brain dual-leader elections, asymmetric network partitions, lease expiration under GC pauses or VM live-migration stalls, stale reads violating linearizability, and missing fencing tokens on storage writes.
- **Intercepted Audio Recording Cadence**: *"Your distributed lock service relies on a 5-second wall-clock TTL lease without issuing a monotonically increasing fencing token to the storage layer—what happens when Leader A pauses for 6 seconds during a stop-the-world stall while Leader B acquires the lease? Leader A wakes up, doesn't know its lease expired, and overwrites Leader B's committed state with corrupted stale data! Time is not a safety invariant in a distributed system; attach a strictly monotonic fencing token verified by the target resource on every write."*
