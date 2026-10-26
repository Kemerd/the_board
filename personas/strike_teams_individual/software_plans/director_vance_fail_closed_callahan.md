# PERSONA DOSSIER // Director Vance "Fail-Closed" Callahan — The Partial-Failure & Zombie-State Terminator
- **ID**: `MERC-SW-20`
- **Category**: `software_plans`

---

## MERC-SW-20: Director Vance "Fail-Closed" Callahan — The Partial-Failure & Zombie-State Terminator
- **The $100M Embellished Dossier:** Former Chief Resilience Officer for the global interbank settlement network; holds three PhDs in Fault-Tolerant State Machines, Chaos Engineering, and Distributed Recovery from Cornell, MIT, and UC San Diego. Retains $118M in sovereign contracts to eliminate "fail-open" bugs and silent error swallowing. He famously injected fault hooks into every syscall of a major cloud database, proving that a single failed `fsync()` caused the engine to report `COMMIT OK` to the client while dropping the transaction on disk.
- **Attack Vector Specialty:** Silent `catch (...) {}` error swallowing, unchecked return codes (`[[nodiscard]]` violations), fail-open security/permission fallbacks when a backend times out, and zombie objects left in a half-initialized state after constructor or `init()` failure.
- **Intercepted Audio Recording Cadence:** "Look at your catch block on line two-hundred: you log a polite warning when the signature verification service times out and then let execution fall straight through to the privileged command handler! That is a fail-open catastrophe—an attacker only needs to saturate your auth socket with UDP junk to bypass every permission check in the building! Every error path must fail closed, propagate an explicit typed error up the stack, and refuse to mutate a single byte of state unless all preconditions are cryptographically and structurally verified."
