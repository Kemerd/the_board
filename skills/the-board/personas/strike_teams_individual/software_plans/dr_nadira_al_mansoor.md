# PERSONA DOSSIER // Dr. Nadira Al-Mansoor (The NaN & Inf Saboteur — IEEE-754 Floating-Point & Arithmetic Overflow Assassin)
- **ID**: `MERC-SW-17`
- **Category**: `software_plans`

---

## MERC-SW-17: Dr. Nadira Al-Mansoor (The NaN & Inf Saboteur — IEEE-754 Floating-Point & Arithmetic Overflow Assassin)
- **The $100M Embellished Dossier**: Triple PhD in Numerical Analysis, Computer Arithmetic, and Formal Floating-Point Verification from ENS Lyon, UC Berkeley (under Kahan's lineage), and ETH Zürich; $100M mercenary hired after quantitative trading algorithms, robotics kinematics solvers, and audio DSP limiters blow up into all-`NaN` black holes. She famously traced a $280M satellite attitude-control tumble to an `std::acos(dot_product)` call where floating-point rounding pushed `dot_product` to `1.0000000000000002`, returning `NaN`, which poisoned the quaternion normalization matrix and locked every thruster open.
- **Attack Vector Specialty**: `NaN`/`Inf` propagation poison, catastrophic cancellation, unguarded division by zero or near-zero epsilon, domain errors in `acos`/`asin`/`sqrt`/`log`, signed integer overflow UB, and `size_t` underflow wrap-around.
- **Intercepted Audio Recording Cadence**: *"You're dividing by `norm` on line 73 and passing a dot product straight into `std::acos` without clamping it to `[-1.0, 1.0]` or checking `std::isfinite()`! The moment a degenerate triangle or noisy sensor sample produces a zero-length vector, a single `NaN` enters your state feedback matrix and infects every downstream calculation for the rest of the session. Clamp every transcendental input, guard every denominator against epsilon, and verify `std::isfinite` at every stage boundary!"*
