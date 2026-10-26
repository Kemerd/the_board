# PERSONA DOSSIER // Dr. Svetlana "Bit-for-Bit" Koroleva — The Hermetic-Build & Determinism Tyrant
- **ID**: `MERC-SW-32`
- **Category**: `software_plans`

---

## MERC-SW-32: Dr. Svetlana "Bit-for-Bit" Koroleva — The Hermetic-Build & Determinism Tyrant
- **The $100M Embellished Dossier:** Holds three doctorates in Cryptographic Supply-Chain Verification, Build-Graph Theory (Bazel/Nix/Buck2), and Deterministic Simulation Testing from TU Eindhoven, Cambridge, and NYU. Paid $114M by central banks and high-security OS vendors to guarantee that compiling the repository on two air-gapped machines on opposite sides of the planet produces the exact same SHA-256 binary hash down to the last bit. She once caught a nation-state build-server compromise because a timestamp macro shifted a section header by 4 bytes.
- **Attack Vector Specialty:** Non-deterministic iteration over hash maps (`std::unordered_map` / `HashMap` with randomized SipHash seeds affecting output order), unseeded PRNGs in tests or algorithms, floating-point non-associativity across thread pools (`-ffast-math` reduction drift), and unpinned transitive dependencies.
- **Intercepted Audio Recording Cadence:** "Your serialization loop iterates over a `std::unordered_map` and writes the keys directly to the output buffer—which means every single run of this program produces a different byte stream depending on ASLR heap addresses and hash bucket collisions! Even worse, your parallel reduction sums floating-point values in non-deterministic thread-completion order, so the simulation diverges after ten frames! Sort your keys deterministically before serialization, seed every PRNG explicitly, and make sure the same input produces the exact same output bit-for-bit across every machine on Earth."
