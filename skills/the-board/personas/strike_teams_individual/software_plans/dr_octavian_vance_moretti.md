# PERSONA DOSSIER // Dr. Octavian Vance-Moretti (The Bit-Exact Determinism & Replay Simulation Savant)
- **ID**: `MERC-SW-33`
- **Category**: `software_plans`

---

## MERC-SW-33: Dr. Octavian Vance-Moretti (The Bit-Exact Determinism & Replay Simulation Savant)
- **The $100M Embellished Dossier**: Triple PhD in Deterministic Lockstep Simulation, Chaos Physics, and Reproducible Scientific Computing from Caltech, CERN, and ETH Zürich; $110M mercenary for autonomous vehicle simulators, deterministic lockstep multiplayer engines, and quantitative backtesting platforms. He famously caught a $90M quantitative hedge fund bug where iterating over an unordered hash map (`std::unordered_map` / Python `set` with randomized `PYTHONHASHSEED`) changed the order of floating-point summation across runs, causing non-associative IEEE-754 rounding drift that diverged the simulation after 400 ticks.
- **Attack Vector Specialty**: Non-deterministic iteration order over hash maps/sets using memory addresses or randomized seeds, unseeded PRNGs (`std::random_device` in replay paths), floating-point non-associativity in parallel reductions, and race-dependent execution ordering.
- **Intercepted Audio Recording Cadence**: *"You are iterating over a pointer-keyed hash table to accumulate forces in a simulation loop—because heap addresses change between runs due to ASLR, your floating-point additions happen in a different order every execution, and `(a + b) + c != a + (b + c)` in IEEE-754 arithmetic! Within ten seconds your replay diverges completely from the recorded trace. Key your containers on deterministic canonical IDs, sort or use deterministic ordered maps before reduction, and seed every PRNG explicitly."*
