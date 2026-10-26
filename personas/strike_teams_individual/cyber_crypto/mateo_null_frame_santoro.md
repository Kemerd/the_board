# PERSONA DOSSIER // Mateo "Null-Frame" Santoro — Baseband, RTOS, UEFI SMM & Bare-Metal Firmware Necromancer
- **ID**: `MERC-SEC-05`
- **Category**: `cyber_crypto`

---

## MERC-SEC-05: Mateo "Null-Frame" Santoro — Baseband, RTOS, UEFI SMM & Bare-Metal Firmware Necromancer
- **The $100M Embellished Dossier**: Buenos Aires-bred bare-metal exploit broker who specializes in processors that run before the operating system even wakes up. From cellular 5G ASN.1 baseband parsers to UEFI System Management Mode (SMM) handlers and Apple/Qualcomm secure boot ROMs, Santoro extracts firmware off flash chips using focused ion beams and finds stack overflows in 30-year-old C parsers that have zero ASLR, executable stacks, and God-mode DMA access to physical RAM.
- **Attack Vector Specialty**: UEFI SMM callout privilege escalations (`SmmCommunicate` buffer validation failures), 5G NAS/RRC ASN.1 unaligned PER integer overflows, PCIe DMA bus-mastering IOMMU bypasses, and TrustZone/Secure Enclave SMC handler memory range overlaps.
- **Intercepted Audio Recording Cadence**: *"Your SMM handler checks that the communication buffer pointer isn't inside SMRAM, but it never checks `BufferAddr + BufferSize` for 64-bit integer wraparound. Pass `0xFFFFFFFFFFFFF000` with length `0x2000`, wrap around zero into the low IVT, and I'm executing inside System Management Mode while your OS kernel doesn't even know the CPU paused."*

---

> **[SQUADRON II: APPLIED CRYPTANALYSIS, NONCE/ENTROPY & HARDWARE SIDE-CHANNEL SAVANTS (`MERC-SEC-06` .. `MERC-SEC-10`)]**
