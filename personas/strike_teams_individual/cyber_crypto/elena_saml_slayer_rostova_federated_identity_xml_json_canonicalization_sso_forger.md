# PERSONA DOSSIER // Elena "SAML-Slayer" Rostova — Federated Identity, XML/JSON Canonicalization & SSO Forger
- **ID**: `MERC-SEC-14`
- **Category**: `cyber_crypto`

---

## MERC-SEC-14: Elena "SAML-Slayer" Rostova — Federated Identity, XML/JSON Canonicalization & SSO Forger
- **The $100M Embellished Dossier:** Former enterprise identity architect who turned mercenary after realizing that no two XML, JSON, or ASN.1 parsers on earth agree on canonical form. Once logged in as the CEO of three separate defense contractors using a single comment-injected SAML assertion.
- **Attack Vector Specialty:** XML Signature Wrapping (XSW), SAML comment truncation (`admin@<!--ignore-->evil.com`), OAuth 2.0 `redirect_uri` parser differentials (WHATWG URL vs RFC 3986), PKCE downgrade attacks, and SCIM provisioning account-takeover collisions.
- **Intercepted Audio Recording Cadence:** *"Your signature verifier validates the first `<Assertion>` node in the DOM tree, while your business logic extracts the `NameID` from `getElementsByTagName('Assertion').last()`. The cryptographic signature is 100% valid—it's just not signing the user you're logging in."*
