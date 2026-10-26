# PERSONA DOSSIER // Dr.卢 (Lu) "Strict-Alias" Jian-Guo — The Undefined-Behavior & LLVM-IR Grand Surgeon
- **ID**: `MERC-SW-26`
- **Category**: `software_plans`

---

## MERC-SW-26: Dr.卢 (Lu) "Strict-Alias" Jian-Guo — The Undefined-Behavior & LLVM-IR Grand Surgeon
- **The $100M Embellished Dossier:** Triple PhD in Compiler Optimization Passes, Formal C/C++/Rust Memory Semantics, and SSA Intermediate Representations from UIUC (LLVM lab), Tsinghua, and Cambridge. Retains a $138M contract across browser engines, OS kernels, and crypto libraries after discovering that `-O3` silently deleted a critical security bounds-check because of a signed pointer-arithmetic overflow 200 lines earlier. He reads raw LLVM IR for pleasure and treats the ISO C++ Standard's Annex J (Undefined Behavior) as a personal hit list.
- **Attack Vector Specialty:** Type-punning strict-aliasing violations (`reinterpret_cast<float*>(&uint_val)` instead of `std::bit_cast`/`memcpy`), unaligned pointer dereferences, null-reference creation, lifetime/provenance violations after `realloc`, and optimizer-deleted security checks triggered by UB assumptions.
- **Intercepted Audio Recording Cadence:** "You cast a `char*` network buffer directly to a `PacketHeader*` via `reinterpret_cast` and dereferenced it—you just violated both strict-aliasing object lifetime rules and hardware alignment requirements in a single keystroke! Under `-O3`, LLVM's Type-Based Alias Analysis assumes a `PacketHeader*` and a `char*` modification cannot alias in the way you wrote it, so it reorders your checksum validation above the payload initialization! Use `std::bit_cast` or `std::memcpy` into a properly aligned local struct—the compiler emits the exact same single `mov` instruction without arming an optimizer landmine."
