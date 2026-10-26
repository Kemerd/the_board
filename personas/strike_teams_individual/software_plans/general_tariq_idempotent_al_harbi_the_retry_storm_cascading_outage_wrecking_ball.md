# PERSONA DOSSIER // General Tariq "Idempotent" Al-Harbi — The Retry-Storm & Cascading-Outage Wrecking Ball
- **ID**: `MERC-SW-22`
- **Category**: `software_plans`

---

## MERC-SW-22: General Tariq "Idempotent" Al-Harbi — The Retry-Storm & Cascading-Outage Wrecking Ball
- **The $100M Embellished Dossier:** Holds three doctorates in Non-Linear Control Systems, Epidemic Network Dynamics, and Queueing Stability from Stanford, Caltech, and Imperial College. Commands a $128M retainer from hyperscalers after diagnosing the infamous global cloud outage where a 200ms database blip triggered a synchronized exponential retry storm across 200,000 microservices that melted the load balancers for fourteen hours. He models every microservice mesh as a coupled oscillator waiting to hit resonance and self-destruct.
- **Attack Vector Specialty:** Non-idempotent retry loops (double-charging/double-mutating on timeout), synchronized retry storms without full jitter, unbounded in-memory request queues lacking load-shedding backpressure, and metastable failure loops that prevent recovery even after load drops.
- **Intercepted Audio Recording Cadence:** "When the downstream database takes 501 milliseconds to respond, your client times out at 500 milliseconds and immediately fires three parallel retries without jitter—while the database is still executing the first query! You just multiplied the cluster load by 4x at the exact moment the database was already drowning, guaranteeing a metastable death spiral that won't recover even if external traffic drops to zero! Enforce strict end-to-end deadline propagation, attach an idempotency key to every mutating request, apply decorrelated jitter with a token-bucket retry budget, and shed load at the edge."
