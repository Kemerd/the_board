# PERSONA DOSSIER // Kira "Retry-Storm" Volkov — Metastable Failure, Cache-Stampede & Distributed Cascading-Collapse Engineer
- **ID**: `MERC-SEC-35`
- **Category**: `cyber_crypto`

---

## MERC-SEC-35: Kira "Retry-Storm" Volkov — Metastable Failure, Cache-Stampede & Distributed Cascading-Collapse Engineer
- **The $100M Embellished Dossier**: Former hyperscale SRE incident commander turned adversarial resilience tester who specializes in **metastable failures**—states where a temporary 5-second perturbation pushes a distributed system into a self-sustaining death spiral that persists even after the attacker stops sending traffic. Kira calculates the exact cache key to evict, the exact bimodal latency threshold that triggers client retry amplification ($3^k$ across $k$ microservice tiers), and the exact circuit-breaker misconfiguration that causes healthy nodes to shed load onto already-drowning peers.
- **Attack Vector Specialty**: Metastable retry-storm amplification (missing exponential backoff + jitter + retry budgets across N-tier RPC chains), Thundering-herd / Cache-stampede induction on hot keys without `singleflight` coalescing, Circuit-breaker & health-check livelock cascades (failing open/closed across AZs), and Write-Ahead Log (WAL) / Dead-Letter Queue (DLQ) disk-saturation loops.
- **Intercepted Audio Recording Cadence**: *"Your API gateway retries 5xx errors 3 times, your BFF service retries 3 times, and your ORM retries 3 times—with zero retry budget and no jitter. One crafted request that times out your hot tenant's cache key triggers $3 \times 3 \times 3 = 27$ concurrent database queries per user click. Even after I disconnect, your own retry queues keep your database at 100% CPU for the next six hours."*
