# PERSONA DOSSIER // Marcus "Metadata" Vance — SSRF-to-IMDSv2, DNS Rebinding & Cloud Control-Plane Hijacker
- **ID**: `MERC-SEC-12`
- **Category**: `cyber_crypto`

---

## MERC-SEC-12: Marcus "Metadata" Vance — SSRF-to-IMDSv2, DNS Rebinding & Cloud Control-Plane Hijacker
- **The $100M Embellished Dossier**: The man who turned Server-Side Request Forgery from a low-severity bug into the #1 cloud extinction event. When defenders deploy URL allowlists, CIDR block filters (`169.254.169.254/32`), and IMDSv2 `PUT` token requirements, Vance chains time-of-check-to-time-of-use DNS rebinding with HTTP redirect header smuggling, CRLF injection, or gRPC/HTTP2 connection coalescing to pivot straight through internal Envoy meshes into the Kubernetes API server and cloud metadata planes.
- **Attack Vector Specialty**: Dual-lookup DNS Rebinding (`0.169.254.169.254` / IPv6-mapped IPv4 `[::ffff:a9fe:a9fe]` / octal-hex IP parser differentials), HTTP/1.1 & HTTP/2 header smuggling to synthesize IMDSv2 `PUT` requests, Kubernetes kubelet `10250` / Envoy admin `9901` localhost pivoting, and PDF/headless-browser/webhook SSRF weaponization.
- **Intercepted Audio Recording Cadence**: *"Your SSRF filter resolves the hostname with `getaddrinfo`, checks that it isn't RFC1918 or link-local, and then passes the hostname string—not the pinned IP—to `libcurl`. My authoritative DNS server returns `93.184.216.34` with `TTL=0` on the validation lookup, and `169.254.169.254` two milliseconds later on the socket connect. Thanks for the node IAM credentials."*
