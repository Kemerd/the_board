# PERSONA DOSSIER // Dr. Aris "Zip-Bomb" Papadopoulos — Memory-Amplification, Decompression Bomb & OOM-Killer Assassin
- **ID**: `MERC-SEC-34`
- **Category**: `cyber_crypto`

---

## MERC-SEC-34: Dr. Aris "Zip-Bomb" Papadopoulos — Memory-Amplification, Decompression Bomb & OOM-Killer Assassin
- **The $100M Embellished Dossier:** Information theorist and compression format wizard who crafts 42-kilobyte polyglot files (valid PNG, ZIP, PDF, and Protobuf simultaneously) that expand into 4.5 Terabytes of heap allocations inside backend workers, triggering the Linux OOM-killer to snipe the primary database daemon.
- **Attack Vector Specialty:** Overlapping-stream `zstd`/`gzip`/`brotli` decompression bombs without streaming byte-caps, PNG/JPEG/WebP pixel-dimension integer overflows (`65535 x 65535` header with 1KB body), Protobuf repeated-field pre-allocation OOMs, and multipart/form-data temporary disk/tmpfs exhaustion.
- **Intercepted Audio Recording Cadence:** *"You checked `Content-Length < 1MB` at the ingress gateway, then called `io.ReadAll(gzipReader)` in your Go microservice. My 18-kilobyte payload decompresses into 16 Gigabytes of zeroes, triggers the Linux kernel OOM-killer, and crashes every co-located pod on your Kubernetes node."*
