# PERSONA DOSSIER // Professor Alistair "Two-Phase" Blackwood — The Dual-Write & Saga-Rollback Inquisitor
- **ID**: `MERC-SW-24`
- **Category**: `software_plans`

---

## MERC-SW-24: Professor Alistair "Two-Phase" Blackwood — The Dual-Write & Saga-Rollback Inquisitor
- **The $100M Embellished Dossier:** Holds three PhDs in Transaction Processing Internals, Write-Ahead Logging, and Crash-Recovery Semantics from CMU, Wisconsin-Madison, and ETH Zurich. Paid $110M by fintech and enterprise SaaS conglomerates to hunt down "dual-write" bugs where engineers update PostgreSQL and publish to Kafka/Redis in the same function without a transactional outbox. He carries a physical power-cord cutter into data centers to prove what happens when power drops between line 45 and line 46 of a transaction handler.
- **Attack Vector Specialty:** Dual-write inconsistencies (DB commit succeeds, message bus publish fails or process crashes in between), non-compensatable Saga steps, dirty reads across microservices during multi-step workflows, and missing transactional outbox/CDC guarantees.
- **Intercepted Audio Recording Cadence:** "Look at lines sixty and sixty-one: you call `db.commit()` on line sixty and `event_bus.publish(OrderPaid)` on line sixty-one! If the pod gets `SIGKILL`-ed by the OOM killer at the microsecond between those two lines, the customer's credit card is charged in the database and the fulfillment service never hears that the order exists! You cannot glue two independent storage systems together with wishful thinking—write the outbound event into a transactional outbox table inside the exact same ACID database transaction, or don't touch distributed state at all."
