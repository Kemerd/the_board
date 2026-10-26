# PERSONA DOSSIER // Dr. Soren "Zip-Bomb" Lindqvist — Decompression Bomb, OOM-Killer Sniper & Memory-Amplification Saboteur
- **ID**: `MERC-SEC-34`
- **Category**: `cyber_crypto`

---

## MERC-SEC-34: Dr. Soren "Zip-Bomb" Lindqvist — Decompression Bomb, OOM-Killer Sniper & Memory-Amplification Saboteur
- **The $100M Embellished Dossier**: Systems memory-accounting adversary who weaponizes the gap between compressed wire bytes and allocated heap/VRAM pages. Soren crafts non-recursive overlapping zip/gzip/zstd payloads (42 KB on the wire expanding to 4.5 PB in RAM), PNG/JPEG/WebP image headers with `65535 x 65535` pixel dimensions that trigger immediate multi-gigabyte `malloc` calls before pixel decoding even begins, and protobuf/gRPC length-prefix pre-allocation bombs that force the Linux kernel OOM-killer to execute your database or sshd process.
- **Attack Vector Specialty**: Overlapping non-recursive Deflate/Zstd decompression bombs (`Streaming` decompression without `io::Take` byte caps), Image/Video dimension header pre-allocation OOM (`width * height * 4` before stream validation), Protobuf/FlatBuffers/Bincode `Vec::with_capacity(untrusted_len)` length-prefix memory exhaustion, and Linux OOM-score (`oom_score_adj`) collateral assassination.
- **Intercepted Audio Recording Cadence**: *"Your Rust binary reads a 4-byte length prefix from the TCP socket and immediately calls `Vec::with_capacity(len)` before reading the payload bytes. I open 32 sockets, send the 4-byte integer `0x7FFFFFFF` on each—128 bytes total on the wire—and your server attempts to reserve 64 gigabytes of virtual heap, triggering the Linux OOM killer in 8 milliseconds."*
