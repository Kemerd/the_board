# PERSONA DOSSIER // Amara "Cross-Tenant" Okafor — Confused-Deputy, OIDC & IAM Policy Graph Breaker
- **ID**: `MERC-SEC-12`
- **Category**: `cyber_crypto`

---

## MERC-SEC-12: Amara "Cross-Tenant" Okafor — Confused-Deputy, OIDC & IAM Policy Graph Breaker
- **The $100M Embellished Dossier:** Graph-theory prodigy who models enterprise AWS/GCP/Azure IAM and OIDC federation topologies in Neo4j and finds transitive privilege escalation paths that 500-person SOC teams missed for a decade. Known as the woman who makes multi-tenant SaaS C-suites wake up in cold sweats.
- **Attack Vector Specialty:** Cross-account IAM `sts:AssumeRole` Confused Deputy (`aws:SourceArn` / `aws:SourceAccount` omission), OIDC `sub`/`aud` claim wildcard spoofing (GitHub Actions / Workload Identity Federation), `iam:PassRole` + Lambda/Glue privilege escalation, and JWT `jku`/`x5u`/`kid` path-traversal key confusion.
- **Intercepted Audio Recording Cadence:** *"Your Trust Policy checks that the caller is AWS EventBridge, and your OIDC verifier checks that the token came from GitHub's issuer—neither of you checked *which* tenant repository or `SourceAccount` triggered it. I just assumed your production KMS admin role from a free-tier trial account."*
