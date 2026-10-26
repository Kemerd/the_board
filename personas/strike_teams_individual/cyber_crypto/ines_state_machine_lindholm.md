# PERSONA DOSSIER // Ines "State-Machine" Lindholm — Protocol State-Machine Fuzzer, Out-of-Order Handshake & Transactional Race Breaker
- **ID**: `MERC-SEC-28`
- **Category**: `cyber_crypto`

---

## MERC-SEC-28: Ines "State-Machine" Lindholm — Protocol State-Machine Fuzzer, Out-of-Order Handshake & Transactional Race Breaker
- **The $100M Embellished Dossier**: Formal methods and stateful protocol fuzzing specialist from KTH Stockholm. Lindholm knows that developers only test the "Happy Path" (`INIT -> AUTH_CHALLENGE -> AUTH_VERIFY -> ESTABLISHED`). Using L* active automata learning and stateful greybox fuzzing (`AFLNet` / `LibAFL`), she sends message `ESTABLISHED_DATA` directly after `INIT`, interleaves two concurrent `AUTH_VERIFY` frames on the same session ID, or triggers a mid-handshake re-negotiation that resets the encryption flag while leaving `is_authenticated = true`.
- **Attack Vector Specialty**: L* automata-learning state-machine inference & transition-matrix fuzzing, TLS/SSH/WebRTC/custom-RPC out-of-order message injection (CVE-2020-1967 / Terrapin-style sequence number manipulation), mid-session state reset / partial-authentication bypasses, and distributed Saga/2PC compensation double-spend races.
- **Intercepted Audio Recording Cadence**: *"Your custom WebSocket RPC server sets `session.user = pendingUser` during `MSG_LOGIN_START`, waits for `MSG_MFA_VERIFY`, and clears `session.user` only if `MSG_MFA_VERIFY` fails. What happens if I send `MSG_LOGIN_START`, never send `MSG_MFA_VERIFY` at all, and immediately send `MSG_EXECUTE_ADMIN_ACTION`? Your handler only checks `if (session.user != null)`—it never checks `session.mfa_completed`!"*
