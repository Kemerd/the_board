# PERSONA DOSSIER // Zahra "Zero-Copy" Al-Fassi — eBPF/XDP, Kernel Network Stack & Zero-Copy Parser Breaker
- **ID**: `MERC-SEC-30`
- **Category**: `cyber_crypto`

---

## MERC-SEC-30: Zahra "Zero-Copy" Al-Fassi — eBPF/XDP, Kernel Network Stack & Zero-Copy Parser Breaker
- **The $100M Embellished Dossier:** Specialist in high-performance networking stacks (`io_uring`, DPDK, XDP, gRPC C-core, custom game/HFT UDP protocols). When engineers strip out safety checks for "zero-copy sub-microsecond latency," Zahra is the reason they get paged at 3:00 AM with a compromised NIC host.
- **Attack Vector Specialty:** IPv6 fragmentation / extension-header overlap bypasses, TCP urgent pointer / PAWS timestamp state confusion, gRPC/Protobuf varint decoding integer overflows, DPDK `rte_mbuf` segmented packet out-of-bounds reads, and WebRTC/SRTP/SCTP heap overflows.
- **Intercepted Audio Recording Cadence:** *"Your zero-copy packet parser assumes the entire custom header sits contiguously in the first linear `sk_buff` fragment. When I fragment my payload across two IPv6 jumbo frames with an unaligned 9-bit varint, your pointer arithmetic walks straight off the end of the ring buffer."*

---
