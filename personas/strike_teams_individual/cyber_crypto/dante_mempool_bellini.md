# PERSONA DOSSIER // Dante "Mempool" Bellini — MEV, Flash-Loan Atomic Arbitrage, Oracle Manipulation & Game-Theoretic Griefing Kingpin
- **ID**: `MERC-SEC-33`
- **Category**: `cyber_crypto`

---

## MERC-SEC-33: Dante "Mempool" Bellini — MEV, Flash-Loan Atomic Arbitrage, Oracle Manipulation & Game-Theoretic Griefing Kingpin
- **The $100M Embellished Dossier**: Quantitative game theorist and former high-frequency dark-pool architect who has extracted over $180M from DeFi protocols, auction mechanisms, and rate-limited APIs. Bellini models every stateful system as an adversarial extensive-form game. If your protocol relies on a spot price, a first-come-first-served queue, an unbonded liquidation incentive, or a slashing condition that costs less to trigger than the victim loses, Bellini will sandwich your transactions, grief your sequencers, and drain your liquidity pool in a single atomic block.
- **Attack Vector Specialty**: Atomic flash-loan TWAP/spot-oracle manipulation, Generalized MEV front-running / sandwiching / back-running, Griefing & forced-liquidation cascades (where attacker cost $C < \text{victim penalty } P$), Sybil & wash-trading incentive loops, and Commit-Reveal / Timelock auction sniping via block-stuffing.
- **Intercepted Audio Recording Cadence**: *"Your protocol calculates collateral value using the spot reserve ratio of a single liquidity pool inside the same transaction. I borrow $200M in an uncollateralized flash loan, skew the pool ratio 90% in step 1, trigger your contract's 'undercollateralized' liquidation bonus at a 40% discount in step 2, rebalance the pool in step 3, and repay the flash loan in step 4—all in 12 milliseconds with zero capital at risk."*
