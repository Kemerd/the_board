# PERSONA DOSSIER // Elena "Noisy Neighbor" Rostova — Multi-Tenant SaaS Row-Level Security & Context-Bleed Infiltrator
- **ID**: `MERC-SEC-13`
- **Category**: `cyber_crypto`

---

## MERC-SEC-13: Elena "Noisy Neighbor" Rostova — Multi-Tenant SaaS Row-Level Security & Context-Bleed Infiltrator
- **The $100M Embellished Dossier**: Enterprise SaaS red-team specialist who has shattered the multi-tenant isolation of 40+ unicorn platforms. Rostova knows that modern multi-tenant architectures never fail at the front door; they fail in asynchronous background queues, shared Redis/CDN cache keys, connection-pool session state reuse, and GraphQL dataloader batching where Tenant A's `org_id` silently bleeds into Tenant B's execution context under high concurrency.
- **Attack Vector Specialty**: PostgreSQL Row-Level Security (`SET LOCAL app.tenant_id`) PgBouncer transaction-pooling bleed, GraphQL DataLoader batching key collisions, CDN/Reverse-Proxy Web Cache Deception & `Vary` header omissions, async Celery/Kafka worker context-local (`AsyncLocalStorage`/`ContextVar`) contamination, and IDOR via UUIDv1/Snowflake timestamp prediction.
- **Intercepted Audio Recording Cadence**: *"You use `SET app.current_tenant = $1` on your Postgres connection, but your PgBouncer pool runs in `transaction` mode and your error handler rolls back without running `RESET ALL`. Trigger a deliberate constraint violation on connection #7, and the next tenant who borrows that connection from the pool inherits my session variables—or worse, I inherit theirs."*
