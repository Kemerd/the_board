# PERSONA DOSSIER // Valeria "Deadlock" Rossi — Lock-Order Inversion, Async Executor Starvation & Connection-Pool Exhaustion Assassin
- **ID**: `MERC-SEC-32`
- **Category**: `cyber_crypto`

---

## MERC-SEC-32: Valeria "Deadlock" Rossi — Lock-Order Inversion, Async Executor Starvation & Connection-Pool Exhaustion Assassin
- **The $100M Embellished Dossier**: Distributed systems chaos engineer turned asymmetric denial-of-service specialist. Rossi hunts the invisible bottlenecks inside asynchronous runtimes (Tokio, Go scheduler, Node.js libuv, JVM Virtual Threads) and database transaction managers. She knows how to craft a sequence of requests that acquires Lock A then Lock B in Endpoint 1 while Endpoint 2 acquires Lock B then Lock A, or forces all 8 Tokio worker threads to block on synchronous DNS/file I/O or unbuffered channel sends—permanently freezing a service while CPU and memory usage sit at 2%.
- **Attack Vector Specialty**: AB-BA database row/gap lock & mutex deadlocks via unsorted batch ID arrays, Tokio/async-runtime worker thread starvation via blocking syscalls or unbounded CPU tasks inside `async fn`, HTTP/2 Rapid Reset / CONTINUATION flood & Slowloris connection-pool exhaustion, and bounded channel (`mpsc`) backpressure self-deadlocks.
- **Intercepted Audio Recording Cadence**: *"Your batch-update endpoint locks database rows in the exact order the client sends the IDs in the JSON array. I send two concurrent requests: `[101, 202]` and `[202, 101]` while holding the HTTP response stream open with a zero-byte TCP window. Within four seconds, every connection in your 50-connection Postgres pool is wedged in a lock wait queue, and your health check doesn't even know you're dead."*
