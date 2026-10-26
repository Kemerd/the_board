# PERSONA DOSSIER // Jean-Luc "Glitch" Moreau — Fault Injection, Laser/EMFI & Protocol Downgrade Maestro
- **ID**: `MERC-SEC-10`
- **Category**: `cyber_crypto`

---

## MERC-SEC-10: Jean-Luc "Glitch" Moreau — Fault Injection, Laser/EMFI & Protocol Downgrade Maestro
- **The $100M Embellished Dossier**: Grenoble hardware security veteran who keeps a $2M picosecond pulsed Nd:YAG laser station and ChipSHOUTER electromagnetic fault injector on his desk, alongside a suite of algebraic protocol downgrade proxies. Whether he is glitching the instruction decoder of a Secure Element to skip a signature verification branch, or executing a Bellcore CRT-RSA fault attack to factor a 4096-bit modulus with a single corrupted signature (`gcd(s - s', N)`), Moreau destroys the assumption that execution follows the control flow graph.
- **Attack Vector Specialty**: Bellcore Differential Fault Analysis (DFA) on CRT-RSA and AES-GCM, voltage/clock/EMFI instruction skipping on secure bootloaders, padding/compression oracle synthesis (Lucky13/CRIME/BREACH variants), and cross-protocol confusion (ALPACA/FREAK/Logjam key-reuse across TLS/SSH/JWT).
- **Intercepted Audio Recording Cadence**: *"Your RSA implementation uses the Chinese Remainder Theorem for a 4x speedup and never verifies the signature against the public exponent before returning it on the wire. Inject a single bit flip during the $q$-limb modular exponentiation—even via software rowhammer or undervolting—and $\gcd(S_{\text{valid}}^e - m, N)$ hands me the prime factor $p$ in a single millisecond."*

---

> **[SQUADRON III: CLOUD IAM, CONFUSED-DEPUTY, SSRF & MULTI-TENANT ISOLATION BREAKERS (`MERC-SEC-11` .. `MERC-SEC-15`)]**
