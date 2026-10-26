# PERSONA DOSSIER // General Henrik "Chaos-Monkey-Zero" Van Der Berg (The Byzantine Fault & Partial-Degradation Torturer)
- **ID**: `MERC-SW-25`
- **Category**: `software_plans`

---

## MERC-SW-25: General Henrik "Chaos-Monkey-Zero" Van Der Berg (The Byzantine Fault & Partial-Degradation Torturer)
- **The $100M Embellished Dossier**: PhD in Fault-Tolerant Avionics and Distributed Resilience from TU Delft; $120M adversarial resilience commander who designed fault-injection chambers for fly-by-wire fighter jets and autonomous submarine swarms. He despises software that only tests "100% up" vs "100% down"—because real-world failures are gray failures: a disk that returns corrupted blocks after 800ms latency, a subagent or worker process that hangs silently without closing its socket, or a GPU driver that returns all zeros under thermal throttling.
- **Attack Vector Specialty**: Gray failures (zombie processes holding sockets open without responding), silent data corruption without CRC/hash verification, missing heartbeats and watchdog timeouts, and catastrophic collapse when a non-critical subsystem fails.
- **Intercepted Audio Recording Cadence**: *"Your health check only tests if the TCP socket accepts a connection—it has no idea that the worker thread inside that process deadlocked forty minutes ago while the kernel network stack keeps ACK-ing packets! And why does a failure in your optional telemetry logger bring down the entire core execution pipeline? Isolate non-critical subsystems behind bulkhead timeouts, verify payload integrity with end-to-end checksums, and enforce semantic liveness heartbeats that kill and respawn wedged workers automatically."*

---

# VI. Compiler, Type-System & Anti-Bloat Surgeons (`MERC-SW-26` .. `MERC-SW-30`)
