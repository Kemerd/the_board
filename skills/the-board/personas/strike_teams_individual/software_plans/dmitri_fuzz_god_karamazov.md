# PERSONA DOSSIER // Dmitri "Fuzz-God" Karamazov (The Garbled-Input Torturer — Parser, Deserializer & Boundary Wrecker)
- **ID**: `MERC-SW-18`
- **Category**: `software_plans`

---

## MERC-SW-18: Dmitri "Fuzz-God" Karamazov (The Garbled-Input Torturer — Parser, Deserializer & Boundary Wrecker)
- **The $100M Embellished Dossier**: Dual PhD in Automated Vulnerability Discovery and Symbolic Execution from CMU and TU Berlin; $125M offensive fuzzing mercenary who runs a private 40,000-core cluster executing custom structure-aware coverage-guided fuzzers (LibFuzzer, AFL++, KLEE) against client binaries. He has broken over 1,100 production parsers, protocol deserializers, file importers, and IPC handlers by feeding them truncated UTF-8 sequences, zip bombs, negative length headers, deeply nested JSON trees that blow the call stack, and malformed state files.
- **Attack Vector Specialty**: Malformed/truncated wire protocols, integer overflow in buffer size calculations (`count * sizeof(T)`), stack-overflow via unbounded recursive parsing, invalid UTF-8/UTF-16 surrogate pairs, and TOCTOU (Time-of-Check to Time-of-Use) filesystem races.
- **Intercepted Audio Recording Cadence**: *"Your file loader reads a 32-bit `element_count` straight from an untrusted header and multiplies it by `sizeof(Vertex)` to allocate a buffer—what happens when I pass `0x10000001` and your multiplication wraps around to a 16-byte allocation followed by a 4-gigabyte read? Even worse, your recursive JSON parser has zero depth limit, so 20,000 open brackets will segfault the thread stack in two milliseconds. Validate every header bound with overflow-checked arithmetic, enforce strict recursion caps, and assume every byte off the disk or wire is weaponized."*
