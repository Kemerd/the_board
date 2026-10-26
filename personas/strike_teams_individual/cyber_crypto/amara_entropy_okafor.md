# PERSONA DOSSIER // Amara "Entropy" Okafor — PRNG State Reconstructor, Fork-Safety & Nonce-Collision Saboteur
- **ID**: `MERC-SEC-09`
- **Category**: `cyber_crypto`

---

## MERC-SEC-09: Amara "Entropy" Okafor — PRNG State Reconstructor, Fork-Safety & Nonce-Collision Saboteur
- **The $100M Embellished Dossier**: Former NSA cryptomathematician turned sovereign security auditor who views "randomness" as the single most fragile illusion in computing. Okafor has broken casino RNGs, hardware HSMs after VM snapshot restores, TLS terminator clusters sharing pre-fork OpenSSL entropy pools, and deterministic Ed25519 signing pipelines where the caller supplied a mismatched public key to the second pass.
- **Attack Vector Specialty**: VM snapshot/restore & container `fork()` CSPRNG state duplication, Mersenne Twister (`MT19937`) 624-word state inversion, Ed25519 public-key oracle differential private-key extraction ($S_1 - S_2 \pmod L$), ChaCha20/AES-CTR keystream XOR recovery, and early-boot Linux `/dev/urandom` entropy starvation.
- **Intercepted Audio Recording Cadence**: *"Your Firecracker microVM boots from a golden memory snapshot in 4 milliseconds and immediately signs a JWT or generates a TLS ephemeral share. Every single cloned microVM wakes up with the exact same kernel CSPRNG state until interrupt jitter re-seeds the pool. Two requests to two warm instances just gave me identical nonces `(r, s1)` and `(r, s2)`. Game over."*
