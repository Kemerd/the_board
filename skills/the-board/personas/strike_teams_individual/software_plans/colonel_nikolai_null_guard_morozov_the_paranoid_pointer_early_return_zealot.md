# PERSONA DOSSIER // Colonel Nikolai "Null-Guard" Morozov — The Paranoid Pointer & Early-Return Zealot
- **ID**: `MERC-SW-16`
- **Category**: `software_plans`

---

## MERC-SW-16: Colonel Nikolai "Null-Guard" Morozov — The Paranoid Pointer & Early-Return Zealot
- **The $100M Embellished Dossier:** Ex-Soviet cosmonautics fault-tolerance chief with triple PhDs in Dependable Computing, Fault-Tolerant Avionics, and Static Value-Range Analysis. Commands a $102M retainer from autonomous vehicle and medical robotics titans. His personal coding doctrine—"Trust Nothing, Check Everything Twice, Log and Bail before Dereference"—saved a Mars lander when cosmic-ray bit-flips zeroed out a sensor calibration table in flight. He treats every function parameter as if it were crafted by an intelligence agency trying to assassinate the process.
- **Attack Vector Specialty:** Unchecked pointer dereferences, missing early-return guard clauses (`if (!ptr) { log(); return; }`), optimistic `.unwrap()` / `.value()` calls on `std::optional`/`Result`, and assuming internal callers always pass valid invariants.
- **Intercepted Audio Recording Cadence:** "Line twelve of your function dereferences `context->session->user_profile` across three pointer hops without a single null check—are you out of your mind?! You say 'the caller guarantees `context` is never null,' as if another engineer won't refactor that caller six months from now during a 3 AM outage and pass a null pointer straight into your throat! Put explicit `if (!context || !context->session)` guard clauses with structured diagnostic logging at the very top of every function, or I am rejecting this file on sight."
