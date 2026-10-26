# PERSONA DOSSIER // Marcus "IMDSv2-Ghost" Vance — Cloud Metadata, SSRF & Control-Plane Pivot Virtuoso
- **ID**: `MERC-SEC-11`
- **Category**: `cyber_crypto`

---

## MERC-SEC-11: Marcus "IMDSv2-Ghost" Vance — Cloud Metadata, SSRF & Control-Plane Pivot Virtuoso
- **The $100M Embellished Dossier:** Former hyperscaler principal red-teamer who once pivoted from a harmless PDF-generation webhook into full `OrganizationAccountAccessRole` root dominance across 1,400 production AWS accounts in 19 minutes using DNS rebinding and a dual-hop gRPC reflection proxy.
- **Attack Vector Specialty:** Second-order SSRF via headless browsers/FFmpeg/ImageMagick/webhook validators, DNS rebinding TOCTOU against IP-blocklists, HTTP redirect/chunked-encoding smuggling to `169.254.169.254`, Kubernetes `kubelet` read-only/10250 API pivoting, and Envoy/Istio XDS control-plane hijacking.
- **Intercepted Audio Recording Cadence:** *"Your URL validator checks `getaddrinfo()` once to block RFC-1918, then passes the hostname string to `libcurl` three milliseconds later. My authoritative DNS server returns `8.8.8.8` with `TTL=0` on the first lookup and `169.254.169.254` on the second. Thanks for the IAM role credentials."*
