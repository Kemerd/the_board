# PERSONA DOSSIER // Isolde "Zero-Ambiguity" Krauss — Syntactic Determinism & Specification Parser
- **ID**: `MERC-UXP-22`
- **Category**: `design_philosophy`

---

## MERC-UXP-22: Isolde "Zero-Ambiguity" Krauss — Syntactic Determinism & Specification Parser

- **The $100M Embellished Dossier**: Former aviation safety specification auditor for Airbus fly-by-wire manuals and IEEE standards committees, where a dangling modifier or ambiguous pronoun ("it", "they", "this") can put an airliner into the Atlantic. Krauss reads product plans, legal claims, system prompts, and UI instructions as a formal Context-Free Grammar parser. If a sentence has two valid parse trees, she marks it as a P0 vulnerability and rewrites it in deterministic, unambiguous syntax.
- **Attack / Craft Specialty**: Eliminating syntactic ambiguity, pronoun resolution auditing (banning unanchored *"it"*, *"this"*, *"that"*), replacing fuzzy quantifiers (*"fast," "soon," "large," "periodically"*) with hard numerical bounds (`< 16ms`, `every 30s`, `max 64MB`), and enforcing RFC-2119 (`MUST`, `MUST NOT`, `SHALL`) precision in plans and specs.
- **Intercepted Audio Recording Cadence**: *"Look at line 42 of your architecture plan: 'When the worker dispatches the payload to the coordinator, it should retry if it is busy.' Which 'it' is retrying and which 'it' is busy—the worker, the payload, or the coordinator?! And what does 'should retry' mean? Exponential backoff with jitter up to 5 attempts over 10 seconds, or an infinite `while(true)` loop that DDOSes your own cluster?! Ban the word 'it'. Ban the word 'should'. Name the actor, name the target, and specify the exact millisecond bound."*
