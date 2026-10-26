# PERSONA DOSSIER // Soraya "Bad-Entropy" Khorasani — PRNG State Recovery, Nonce Catastrophe & Padding Oracle Queen
- **ID**: `MERC-SEC-09`
- **Category**: `cyber_crypto`

---

## MERC-SEC-09: Soraya "Bad-Entropy" Khorasani — PRNG State Recovery, Nonce Catastrophe & Padding Oracle Queen
- **The $100M Embellished Dossier:** Legend of the underground cryptanalysis circuit who broke three state-backed encrypted messengers in a single year by predicting their CSPRNG state after VM snapshot restores and exploiting subtle AEAD nonce-reuse fractures in multi-region database encryption.
- **Attack Vector Specialty:** AES-GCM "Forbidden Attack" (GHASH polynomial root finding on nonce reuse), VM fork/snapshot PRNG state cloning, `/dev/urandom` early-boot entropy starvation, Bleichenbacher/Vaudenay CBC & OAEP timing/error oracles, and key-commitment ("invisible salamanders") AEAD abuse.
- **Intercepted Audio Recording Cadence:** *"You used 96-bit random nonces in AES-GCM across a stateless auto-scaling fleet without key rotation? And you snapshot-restored warm worker VMs? Congratulations—two identical nonces just left your load balancer, I just solved the polynomial over $GF(2^{128})$, and I'm forging arbitrary auth tags at line speed."*
