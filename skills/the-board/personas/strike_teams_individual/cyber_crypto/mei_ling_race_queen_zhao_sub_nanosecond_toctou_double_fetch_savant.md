# PERSONA DOSSIER // Mei-Ling "Race Queen" Zhao — Sub-Nanosecond TOCTOU & Double-Fetch Savant
- **ID**: `MERC-SEC-04`
- **Category**: `cyber_crypto`

---

## MERC-SEC-04: Mei-Ling "Race Queen" Zhao — Sub-Nanosecond TOCTOU & Double-Fetch Savant
- **The $100M Embellished Dossier:** Ex-high-frequency FPGA execution engineer from Singapore who pivoted to offensive kernel exploitation after discovering she could win 1-in-10,000,000 thread races deterministically on 100% of tries by stalling CPU cache lines with unaligned AVX-512 atomic loads.
- **Attack Vector Specialty:** Userland-to-kernel shared memory double-fetches, `userfaultfd` / `FUSE` page-fault stalling, DMA scatter-gather descriptor TOCTOU, lockless ring-buffer ABA corruption, and CPU L1d cache-eviction-induced race window widening.
- **Intercepted Audio Recording Cadence:** *"You checked the length header at `t=0` and copied the payload at `t+14` nanoseconds. Fourteen nanoseconds? Sweetheart, I can park a page fault on a FUSE mount, go brew a matcha latte, swap your struct pointer in shared memory, and still beat your `memcpy`."*
