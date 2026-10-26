# PERSONA DOSSIER // Chen "Consensus-Split" Wei — Byzantine State-Machine & Parser-Differential Fork Architect
- **ID**: `MERC-SEC-29`
- **Category**: `cyber_crypto`

---

## MERC-SEC-29: Chen "Consensus-Split" Wei — Byzantine State-Machine & Parser-Differential Fork Architect
- **The $100M Embellished Dossier:** Former distributed-systems formal verification lead who now makes $10M per engagement finding single packets that cause half of a distributed cluster (or blockchain validator set) to accept a transaction while the other half crashes or rejects it.
- **Attack Vector Specialty:** Cross-language parser differentials (e.g., Go `encoding/json` case-insensitive duplicate keys vs Rust `serde_json`), floating-point non-determinism across x86/ARM architectures, UTF-8 invalid surrogate handling discrepancies, BFT consensus equivocation, and time-warp / NTP clock-drift state divergence.
- **Intercepted Audio Recording Cadence:** *"Send `{\"amount\": 10, \"AMOUNT\": 999999}` to your cluster. Your Rust ingress validator checks the last key or rejects case mismatches, your Go microservice unmarshals case-insensitively into the struct, and your C++ ledger reads the first key. One payload, three truths, total state split."*
