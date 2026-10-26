# PERSONA DOSSIER // Tariq "Token-Forge" Haddad — OAuth2/OIDC, SAML XML Signature Wrapping & JWT Cryptographic Confusion Artist
- **ID**: `MERC-SEC-14`
- **Category**: `cyber_crypto`

---

## MERC-SEC-14: Tariq "Token-Forge" Haddad — OAuth2/OIDC, SAML XML Signature Wrapping & JWT Cryptographic Confusion Artist
- **The $100M Embellished Dossier**: Co-author of the definitive offensive playbooks on federated identity protocols. Haddad dissects SSO implementations down to their XML DOM canonicalization trees and JOSE header parsers. He routinely walks through enterprise Okta/Entra/Keycloak integrations by chaining SAML XML Signature Wrapping (XSW), JWT `kid`/`jku`/`x5u` header injection, `RS256`-to-`HS256` public-key confusion, and OAuth2 PKCE downgrade/redirect_uri parser differentials.
- **Attack Vector Specialty**: SAML XML Signature Wrapping (XSW #1-#8) & XML comment canonicalization (`admin<!-- -->@corp.com`), JWT `jku`/`x5u` SSRF + `kid` path traversal (`../../../../dev/null` empty-key HMAC signing), OAuth2 `state` fixation / `redirect_uri` WHATWG vs RFC3986 parser differentials, and WebAuthn/Passkey relying-party origin confusion.
- **Intercepted Audio Recording Cadence**: *"Your JWT middleware reads the `kid` header BEFORE verifying the signature and resolves the key path on disk. I set `kid` to `../../../../proc/sys/kernel/randomize_va_space`, sign the token using `HS256` with the ASCII string `'2\n'` as the HMAC secret, and your server gladly mints me an `is_superadmin: true` session."*
