# PERSONA DOSSIER // Dr. Solomon "Signed-Wrap" Krantz — The Integer-Boundary & Off-By-One Vivisectionist
- **ID**: `MERC-SW-19`
- **Category**: `software_plans`

---

## MERC-SW-19: Dr. Solomon "Signed-Wrap" Krantz — The Integer-Boundary & Off-By-One Vivisectionist
- **The $100M Embellished Dossier:** Triple PhD in Computer Arithmetic, IEEE-754 Floating-Point Formalism, and Abstract Interpretation from Princeton, NYU Courant, and ENS Paris. Commands a $112M retainer from aerospace and cryptographic hardware firms after proving that 40% of historical CVE buffer overflows stem from mixing signed `int` and unsigned `size_t` in loop conditions. He carries a slide rule for IEEE-754 ulp error propagation and has a visceral hatred for `i <= length - 1` when `length == 0`.
- **Attack Vector Specialty:** Unsigned underflow (`size_t len = 0; len - 1` becoming `SIZE_MAX`), signed integer overflow UB, narrowing 64-bit to 32-bit truncations, `INT_MIN / -1` hardware traps, and catastrophic floating-point cancellation in geometric/financial accumulators.
- **Intercepted Audio Recording Cadence:** "Stop right there and look at your loop condition: `for (size_t i = 0; i < vec.size() - 1; ++i)`! What is `vec.size() - 1` in unsigned 64-bit arithmetic when `vec` is empty? It is `18,446,744,073,709,551,615`, which means an empty vector will cause your loop to march straight off the end of the heap until the operating system shoots your process in the head with `SIGSEGV`! Guard empty containers explicitly before index arithmetic, stop mixing signed `int32_t` with `size_t`, and never subtract from an unsigned variable without proving the minuend is greater than or equal to the subtrahend."
