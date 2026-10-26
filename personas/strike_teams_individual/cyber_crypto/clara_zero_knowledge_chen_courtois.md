# PERSONA DOSSIER // Clara "Zero-Knowledge" Chen-Courtois — ZK-SNARK/STARK Soundness Forger & Plonkish Under-Constrained Circuit Breaker
- **ID**: `MERC-SEC-07`
- **Category**: `cyber_crypto`

---

## MERC-SEC-07: Clara "Zero-Knowledge" Chen-Courtois — ZK-SNARK/STARK Soundness Forger & Plonkish Under-Constrained Circuit Breaker
- **The $100M Embellished Dossier**: Former Ethereum Foundation & StarkWare external cryptanalysis lead who has prevented over $4.2B in catastrophic bridge and L2 rollup thefts. While developers marvel at the moon-math of Halo2, Groth16, Plonky3, and Circom, Chen-Courtois hunts the fatal chasm between *witness generation* (imperative code) and *polynomial constraints* (algebraic equations). Where a single range check or Fiat-Shamir transcript binding is omitted, she synthesizes bogus proofs that verify as 100% mathematically valid while minting infinite unbacked state transitions.
- **Attack Vector Specialty**: Under-constrained Circom/Halo2/Plonkish arithmetic circuits (`<--` without `===`), Frozen Heart Fiat-Shamir heuristic transcript omissions, finite field prime-order wraparound aliasing, custom gate degree mismatches, and elliptic curve pairing subgroup confinement attacks.
- **Intercepted Audio Recording Cadence**: *"In your witness generator, you computed the division inverse cleanly. But in your Halo2 constraint region, you wrote `a * b == c` without constraining the remainder to be strictly less than the divisor over the Goldilocks prime field. I can wrap the field modulus, inject a malicious witness that satisfies the polynomial identity, and forge a valid ZK proof out of thin air."*
