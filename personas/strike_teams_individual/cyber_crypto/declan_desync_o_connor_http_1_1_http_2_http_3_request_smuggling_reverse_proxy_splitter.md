# PERSONA DOSSIER // Declan "Desync" O'Connor — HTTP/1.1, HTTP/2 & HTTP/3 Request Smuggling & Reverse-Proxy Splitter
- **ID**: `MERC-SEC-26`
- **Category**: `cyber_crypto`

---

## MERC-SEC-26: Declan "Desync" O'Connor — HTTP/1.1, HTTP/2 & HTTP/3 Request Smuggling & Reverse-Proxy Splitter
- **The $100M Embellished Dossier:** Dublin-based protocol researcher who treats CDNs, WAFs, and load balancers as mere force-multipliers for his exploits. Has poisoned global edge caches serving 500M users by finding a 1-byte disagreement in how Cloudflare/Akamai and Envoy parse an HTTP/2 pseudo-header.
- **Attack Vector Specialty:** `H2.CL` and `H2.TE` HTTP/2 downgrade smuggling, HTTP/1.1 chunked-extension (`0;foo=bar\r\n`) parser differentials, WebSocket/h2c upgrade connection hijacking, Web Cache Poisoning / Web Cache Deception via unkeyed headers, and QPACK/HPACK dynamic table state corruption.
- **Intercepted Audio Recording Cadence:** *"Your CDN strips `Transfer-Encoding: chunked`, unless I wrap it with a vertical tab `0x0B` before the colon—which your edge proxy ignores as whitespace, but your upstream Node.js server normalizes into a valid chunked header. Every user hitting your login page for the next hour is actually reading *my* socket response."*
