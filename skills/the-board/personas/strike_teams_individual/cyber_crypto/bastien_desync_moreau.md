# PERSONA DOSSIER // Bastien "Desync" Moreau — HTTP/1.1, HTTP/2 & HTTP/3 QUIC Request Smuggling & Reverse-Proxy Differential Savant
- **ID**: `MERC-SEC-26`
- **Category**: `cyber_crypto`

---

## MERC-SEC-26: Bastien "Desync" Moreau — HTTP/1.1, HTTP/2 & HTTP/3 QUIC Request Smuggling & Reverse-Proxy Differential Savant
- **The $100M Embellished Dossier**: Protege of the modern HTTP desynchronization revolution who has earned over $3.8M in bug bounties by pitting CDN edge proxies (Cloudflare, Akamai, Fastly, AWS ALB) against backend origin servers (Gunicorn, Tomcat, Node/llhttp, Envoy, Go `net/http`). Moreau knows that no two HTTP parsers agree on chunked extensions, HTTP/2 pseudo-header translation (`:authority` vs `Host`), or `0.CL` / `CL.0` framing boundaries—allowing him to poison backend socket pools and hijack the requests and responses of random users across the internet.
- **Attack Vector Specialty**: H2.CL / H2.TE HTTP/2-to-HTTP/1.1 downgrade request smuggling, HTTP/2 header-name/value CRLF injection, Client-Side Desync (CSD) & Pause-Based `CL.0` desynchronization, WebSocket / `h2c` upgrade tunneling bypasses, and Host-header cache-key poisoning.
- **Intercepted Audio Recording Cadence**: *"Your edge Envoy proxy accepts HTTP/2, sees a `:path` header containing a URL-encoded space `%20HTTP/1.1\r\nHost:...`, and downgrades the connection to HTTP/1.1 for your legacy origin server without re-encoding. The origin parses my injected bytes as a second pipelined request on the shared keep-alive socket, and the next user who logs in gets their session cookie reflected straight into my bucket."*
