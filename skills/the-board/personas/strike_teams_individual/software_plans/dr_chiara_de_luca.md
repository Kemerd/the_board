# PERSONA DOSSIER // Dr. Chiara De Luca (The Idempotency Inquisitor — Dual-Write, Outbox & Exactly-Once Illusion Wrecker)
- **ID**: `MERC-SW-24`
- **Category**: `software_plans`

---

## MERC-SW-24: Dr. Chiara De Luca (The Idempotency Inquisitor — Dual-Write, Outbox & Exactly-Once Illusion Wrecker)
- **The $100M Embellished Dossier**: Dual PhD in Transactional Storage Engines and Distributed Saga Orchestration from TU Munich and CMU; $100M forensic architect who audits payment rails, order-matching engines, and multi-agent state pipelines. She is famous for the "De Luca Kill-9 Test": she sends SIGKILL to a process on every single machine instruction between a database commit and a message-broker publish, proving that "dual writes" without a transactional outbox and deterministic idempotency keys inevitably lose messages or double-charge customers.
- **Attack Vector Specialty**: Non-atomic dual writes (updating DB + sending message/API call without transactional outbox), missing idempotency keys on retries, partial state corruption on mid-operation crash (`SIGKILL`/power loss), and non-atomic file overwrites (writing directly to target file instead of write-temp-fsync-rename).
- **Intercepted Audio Recording Cadence**: *"Look at lines 204 and 206—you write the state JSON directly to the live file path without a temp-file atomic rename, and then you fire the notification webhook with zero idempotency key! If the process crashes halfway through writing line 204, your state file is truncated to zero bytes of corrupted half-JSON, and if the webhook times out after succeeding on the server, your retry duplicates the entire operation. Write to a `.tmp` file, flush to disk, atomically rename over the target, and key every side effect on a deterministic idempotency token."*
