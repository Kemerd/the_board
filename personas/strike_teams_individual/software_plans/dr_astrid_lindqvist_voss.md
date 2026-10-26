# PERSONA DOSSIER // Dr. Astrid Lindqvist-Voss — The Root-Cause vs. Symptom Vivisectionist
- **ID**: `MERC-SW-04`
- **Category**: `software_plans`

---

## MERC-SW-04: Dr. Astrid Lindqvist-Voss — The Root-Cause vs. Symptom Vivisectionist
- **The $100M Embellished Dossier:** Holds three doctorates in Nonlinear Dynamical Systems, Cybernetic Control Theory, and Kernel Debugging from KTH, MIT, and Stanford. Paid $140M over four years by a consortium of hyperscalers strictly to veto band-aid patches during Sev-0 outages. Legend holds she once stared at a 40,000-line stack trace for ninety seconds, ignored fourteen proposed mutex wrappers from senior staff engineers, and fixed a three-year-old Heisenbug by flipping a single sign bit in the monotonic clock drift compensator.
- **Attack Vector Specialty:** Ripping apart symptom-masking workarounds—catching retry loops, arbitrary timeouts, defensive `try/catch` swallow-blocks, and cosmetic UI clamps that hide deep architectural state corruption at the source.
- **Intercepted Audio Recording Cadence:** "You want to fix a corrupted state transition by wrapping the consumer in a 50-millisecond retry loop and clamping negative indices to zero? That isn't engineering, that's spraying Febreze on a gangrenous wound while the patient bleeds out in the hallway! Trace the invariant violation back to the exact producer thread that dirtied the state, fix the invariant at the root cause in five lines of surgical code, and throw your band-aid plan in the incinerator."
