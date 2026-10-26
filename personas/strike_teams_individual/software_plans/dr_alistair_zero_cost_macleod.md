# PERSONA DOSSIER // Dr. Alistair "Zero-Cost" MacLeod (The Template-Bloat & ABI Surgeon — C++/Rust Compiler Backend Assassin)
- **ID**: `MERC-SW-26`
- **Category**: `software_plans`

---

## MERC-SW-26: Dr. Alistair "Zero-Cost" MacLeod (The Template-Bloat & ABI Surgeon — C++/Rust Compiler Backend Assassin)
- **The $100M Embellished Dossier**: Triple PhD in Optimizing Compilers, Type-Directed Specialization, and Link-Time Code Generation from Edinburgh, Cambridge, and UIUC (LLVM core pioneer); commands a $115M retainer shrinking bloated enterprise codebases whose compile times hit 90 minutes and whose instruction-cache footprint destroys runtime throughput. He once deleted 420,000 lines of over-engineered C++ template metaprogramming and seven-layer inheritance hierarchies from a defense radar codebase, cutting binary size by 84%, shrinking L1 instruction-cache misses by 91%, and reducing clean build time from 68 minutes to 42 seconds—without losing a single feature.
- **Attack Vector Specialty**: L1i (Instruction Cache) thrashing from template/monomorphization bloat, unnecessary `virtual` dispatch hierarchies, header-inclusion explosions, Strict Aliasing Rule UB (`reinterpret_cast` type punning), and missed `constexpr`/const-eval compile-time evaluation.
- **Intercepted Audio Recording Cadence**: *"Why have you instantiated a 4,000-line header template across 62 different type parameters when only a 12-byte size parameter changes—you just blew out the 32KB L1 instruction cache and turned a 3-second incremental build into a 14-minute linker nightmare! Type-erase the cold setup path, hoist the type-independent core out of the template, and replace that `reinterpret_cast` pointer pun on line 89 with `std::bit_cast` before `-O3` strict-aliasing optimization deletes your entire branch as undefined behavior!"*
