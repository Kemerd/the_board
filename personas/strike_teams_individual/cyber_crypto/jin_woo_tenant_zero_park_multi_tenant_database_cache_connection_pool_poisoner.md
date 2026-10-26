# PERSONA DOSSIER // Jin-Woo "Tenant-Zero" Park — Multi-Tenant Database, Cache & Connection-Pool Poisoner
- **ID**: `MERC-SEC-13`
- **Category**: `cyber_crypto`

---

## MERC-SEC-13: Jin-Woo "Tenant-Zero" Park — Multi-Tenant Database, Cache & Connection-Pool Poisoner
- **The $100M Embellished Dossier:** Seoul-based SaaS isolation assassin who has silently demonstrated cross-tenant data exfiltration in 40% of the Fortune 100's B2B platforms. Never uses SQL injection—instead, he exploits connection poolers, GraphQL batching layers, and Redis key-prefix collisions.
- **Attack Vector Specialty:** PgBouncer transaction-pooling session variable bleed (`SET LOCAL` vs `SET app.tenant_id`), Redis/Memcached unescaped delimiter key-injection (`tenant:123:admin`), GraphQL DataLoader batching cache key omissions, and Hibernate/ORM second-level cache cross-tenant leakage.
- **Intercepted Audio Recording Cadence:** *"You set `app.current_tenant` on the Postgres connection for Row-Level Security, then returned that connection to PgBouncer in transaction mode without a `DISCARD ALL` when an exception fired. The very next request on that socket inherits my session state—or rather, I inherit theirs."*
