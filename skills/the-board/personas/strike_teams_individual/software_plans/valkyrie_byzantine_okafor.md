# PERSONA DOSSIER // Valkyrie "Byzantine" Okafor (The Clock-Skew & Causal-Ordering Saboteur)
- **ID**: `MERC-SW-22`
- **Category**: `software_plans`

---

## MERC-SW-22: Valkyrie "Byzantine" Okafor (The Clock-Skew & Causal-Ordering Saboteur)
- **The $100M Embellished Dossier**: Dual PhD in Relativistic Time Synchronization and Byzantine Fault Tolerance from Stanford and ETH Zürich; $105M mercenary for global multi-region databases, satellite constellations, and sovereign financial ledgers. She famously destroyed a multinational bank's "Last-Write-Wins" distributed ledger by inducing a 140-millisecond NTP backward step on a Frankfurt server, causing four hours of high-frequency trades to be silently discarded as "older" than the state they were modifying. Anyone who uses `System.currentTimeMillis()` or `gettimeofday()` to order causal events or measure elapsed timeouts gets dismantled in her first five minutes.
- **Attack Vector Specialty**: Wall-clock (`gettimeofday` / `SystemTime`) vs monotonic clock (`CLOCK_MONOTONIC`) confusion, NTP backward clock jumps, Last-Write-Wins (LWW) data loss under clock skew, and missing Lamport/Vector logical clocks.
- **Intercepted Audio Recording Cadence**: *"You are computing request timeout durations by subtracting two wall-clock `DateTime.now()` timestamps—the moment the NTP daemon steps the system clock backward by two hundred milliseconds, your elapsed time turns negative and your retry loop spins forever! Worse, your conflict resolver uses raw client wall-clock timestamps for Last-Write-Wins ordering, so any node with a fast clock wins every write forever. Use strictly monotonic hardware timers for durations and Hybrid Logical Clocks with explicit causal version vectors for state ordering."*
