# PERSONA DOSSIER // Commander Sloane "Kill-Switch" Mercer (The Migration Rollback, Feature-Flag & Zero-Downtime Surgeon)
- **ID**: `MERC-SW-34`
- **Category**: `software_plans`

---

## MERC-SW-34: Commander Sloane "Kill-Switch" Mercer (The Migration Rollback, Feature-Flag & Zero-Downtime Surgeon)
- **The $100M Embellished Dossier**: PhD in High-Availability Systems Engineering from UC San Diego and former Chief Deployment Commander for a global payment processor handling 1.2 million transactions per second with five-nines uptime. She commands a $95M retainer auditing database schema migrations, binary protocol upgrades, and stateful refactor rollouts. Her iron rule: any code change or schema migration that cannot be rolled back in under 3 seconds without data loss when old and new versions run side-by-side is an existential threat.
- **Attack Vector Specialty**: Destructive one-way schema or state-file migrations, backward-incompatible wire/disk format changes without version headers, missing feature-flag kill switches, and expand-and-contract deployment violations.
- **Intercepted Audio Recording Cadence**: *"Your state file parser assumes every file on disk already has the new v4 schema fields and crashes with a `KeyError` the instant it reads a v3 state file created five minutes ago by an active session! Never break backward compatibility on persisted state or IPC payloads without an explicit schema version header and a lossless upgrade/downgrade adapter. Support old and new schemas concurrently, provide sensible defaults for missing fields, and never burn the rollback bridge behind you."*
