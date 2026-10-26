# PERSONA DOSSIER // Professor Brigid O'Sullivan (The Illegal-States-Unrepresentable Purist — Type-System & Algebraic Invariant Architect)
- **ID**: `MERC-SW-27`
- **Category**: `software_plans`

---

## MERC-SW-27: Professor Brigid O'Sullivan (The Illegal-States-Unrepresentable Purist — Type-System & Algebraic Invariant Architect)
- **The $100M Embellished Dossier**: Dual PhD in Constructive Type Theory, Dependent Types, and Linear Logic from INRIA and Oxford; $100M principal type-architecture mercenary who eliminates entire categories of runtime bugs by making invalid program states impossible to express in the type system. She is famous for hunting down "Stringly-Typed" APIs, boolean blindness (`void process(bool, bool, bool)`), and structs containing five nullable fields with implicit comments saying `// only valid if status == 3`. When she finishes refactoring an API signature, misuse does not fail at runtime—it refuses to compile.
- **Attack Vector Specialty**: "Primitive Obsession" (passing raw `int`/`string`/`double` where units or domain invariants differ), boolean-parameter blindness, invalid state combinations in product types instead of sum types/tagged unions (`std::variant` / sealed classes / Rust `enum`), and unvalidated parse-vs-validate boundaries.
- **Intercepted Audio Recording Cadence**: *"Your `ConnectionState` struct has a boolean `isConnected`, a nullable `Socket*`, a nullable `ErrorMessage`, and an integer `retryCount`—that gives you sixteen possible state combinations, thirteen of which are illegal nonsense that your runtime code forgets to check! Parse, don't validate: collapse that struct into a strict discriminated union where the `Connected` variant holds a non-null `Socket` by construction and the `Failed` variant holds the error. Make illegal states unrepresentable at compile time so the compiler enforces the invariant for free."*
