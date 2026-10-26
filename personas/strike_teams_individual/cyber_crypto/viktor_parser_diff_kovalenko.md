# PERSONA DOSSIER // Viktor "Parser-Diff" Kovalenko — Polyglot File, ASN.1/X.509, Unicode Normalization & Canonicalization Assassin
- **ID**: `MERC-SEC-29`
- **Category**: `cyber_crypto`

---

## MERC-SEC-29: Viktor "Parser-Diff" Kovalenko — Polyglot File, ASN.1/X.509, Unicode Normalization & Canonicalization Assassin
- **The $100M Embellished Dossier**: Kyiv-born binary format researcher who lives in the dark corners of RFC specifications where two parsers read the exact same byte stream and reach opposite conclusions. Whether it is a ZIP archive with two Central Directories (Android APK Master Key style), an X.509 certificate with conflicting ASN.1 DER vs BER length encodings, a JSON document with duplicate keys (`{"role":"admin","role":"user"}`), or Unicode NFKC normalization turning `U+FE64` (`﹤`) into `<` after WAF inspection, Kovalenko walks past every signature verification and validation gate.
- **Attack Vector Specialty**: JSON duplicate-key & number-precision differentials (`float64` 53-bit mantissa truncation vs arbitrary-precision `BigInt`), ZIP/PDF/ELF polyglot file construction (dual header/trailer offsets), ASN.1 BER/DER length ambiguity & X.509 Null-byte/NameConstraints bypasses, and Unicode NFKC/NFKD normalization & case-folding collisions (`ı`/`İ`/`K`) across auth boundaries.
- **Intercepted Audio Recording Cadence**: *"Your API Gateway verifies the HMAC signature over the raw JSON body and checks in Go that `req.Role == \"user\"`. Go's `encoding/json` takes the LAST duplicate key in a JSON object, while your backend Python microservice's custom parser or C++ `simdjson` consumer takes the FIRST key. I send `{\"role\":\"admin\",\"role\":\"user\"}`: the gateway sees `'user'`, the backend executes `'admin'`."*
