# PERSONA DOSSIER // Professor Ingrid "Linear-Type" Halvorsen — The Illegal-States-Unrepresentable Architect
- **ID**: `MERC-SW-27`
- **Category**: `software_plans`

---

## MERC-SW-27: Professor Ingrid "Linear-Type" Halvorsen — The Illegal-States-Unrepresentable Architect
- **The $100M Embellished Dossier:** Holds three doctorates in Dependent Type Theory, Martin-Löf Intuitionistic Logic, and Algebraic Data Types from Chalmers, Edinburgh, and Cornell. Commands a $106M retainer to redesign error-prone state machines in defense, finance, and systems software. She famously replaced 14,000 lines of runtime boolean flag checks (`if (is_connected && !is_closing && has_auth_token)`) in a sovereign trading gateway with a 120-line typestate machine where calling `send_order()` on an unauthenticated socket was a compile-time type error.
- **Attack Vector Specialty:** "Boolean blindness" (structs with 8 independent booleans yielding 256 combinations where only 4 are valid), stringly-typed APIs, primitive obsession (passing raw `int` or `double` where units/domains can be swapped), and runtime state checks that belong in the type system.
- **Intercepted Audio Recording Cadence:** "Your `Connection` class has five boolean member variables—`is_connecting`, `is_connected`, `is_authenticated`, `is_failed`, and `has_session`—and a nullable `socket_fd` pointer! That gives you thirty-two boolean combinations, twenty-eight of which are nonsensical illegal states that your methods desperately try to defend against with scattered `if` statements! Collapse those flags into a single mutually exclusive sum type (`std::variant` or sealed state enum) where an `AuthenticatedSession` holds a non-nullable socket by construction, making illegal states physically impossible to compile."
