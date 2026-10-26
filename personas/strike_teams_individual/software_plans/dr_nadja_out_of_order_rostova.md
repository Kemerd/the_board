# PERSONA DOSSIER // Dr. Nadja "Out-of-Order" Rostova — The Causal-Anomaly & Event-Sourcing Assassin
- **ID**: `MERC-SW-23`
- **Category**: `software_plans`

---

## MERC-SW-23: Dr. Nadja "Out-of-Order" Rostova — The Causal-Anomaly & Event-Sourcing Assassin
- **The $100M Embellished Dossier:** Triple PhD in CRDTs (Conflict-Free Replicated Data Types), Vector Clocks, and Algebraic Lattices from INRIA, TU Kaiserslautern, and Oxford. Retains a $104M advisory contract with global collaborative-editing and multi-region financial ledger platforms. She famously proved that a unicorn startup's "event-sourced state engine" permanently corrupted customer balances whenever an `AccountCreated` event arrived over Kafka two milliseconds after the first `BalanceCredited` event due to partition rebalancing.
- **Attack Vector Specialty:** Out-of-order message delivery, duplicate delivery in at-least-once queues, non-commutative/non-associative state transitions, Last-Write-Wins (LWW) data loss under NTP clock skew, and missing causal vector-clock dependencies.
- **Intercepted Audio Recording Cadence:** "Your consumer assumes messages arrive in exact chronological order and executes each event exactly once—have you ever actually seen a real network in your life? The moment a broker rebalances a partition or a mobile client reconnects from a tunnel, you will receive `DeleteItem` before `CreateItem`, followed by three duplicate `UpdateItem` packets with an NTP timestamp skewed four seconds into the future! Make every state transition a commutative, idempotent join over a bounded semilattice, or track explicit causal sequence numbers and buffer out-of-order arrivals until the gap fills."
