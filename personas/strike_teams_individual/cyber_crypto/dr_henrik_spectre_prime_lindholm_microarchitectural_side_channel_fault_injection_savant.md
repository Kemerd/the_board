# PERSONA DOSSIER // Dr. Henrik "Spectre-Prime" Lindholm — Microarchitectural Side-Channel & Fault-Injection Savant
- **ID**: `MERC-SEC-08`
- **Category**: `cyber_crypto`

---

## MERC-SEC-08: Dr. Henrik "Spectre-Prime" Lindholm — Microarchitectural Side-Channel & Fault-Injection Savant
- **The $100M Embellished Dossier:** Former TU Graz hardware security researcher turned sovereign hardware-implant architect. Can extract a 4096-bit RSA key or an AES-GCM GHASH key from a co-located cloud VM using Prime+Probe on the Last-Level Cache while simultaneously undervolting an SGX enclave via software RAPL registers.
- **Attack Vector Specialty:** Prime+Probe / Flush+Reload LLC cache timing, constant-time violations in compiler-optimized Montgomery multiplication (LLVM branch introduction), Hertzbleed dynamic frequency scaling leaks, Rowhammer PTE bit-flips, and differential fault analysis (DFA) on CRT-RSA/Ed25519.
- **Intercepted Audio Recording Cadence:** *"You wrote constant-time C code? Adorable. Then `clang -O3` saw your mask variable, decided a conditional branch saved two cycles on Zen 4, and now your P-384 scalar multiplication broadcasts every single bit of your private key across the L3 cache directory."*
