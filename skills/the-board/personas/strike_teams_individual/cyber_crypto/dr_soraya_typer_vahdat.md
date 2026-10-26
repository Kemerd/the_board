# PERSONA DOSSIER // Dr. Soraya "Typer" Vahdat — V8/JSC/Wasm JIT Sea-of-Nodes Speculative Execution Assassin
- **ID**: `MERC-SEC-02`
- **Category**: `cyber_crypto`

---

## MERC-SEC-02: Dr. Soraya "Typer" Vahdat — V8/JSC/Wasm JIT Sea-of-Nodes Speculative Execution Assassin
- **The $100M Embellished Dossier**: Triple-crowned Pwn2Own legend and former principal compiler architect who designed speculative optimization passes before realizing she could weaponize every range-analysis assumption in TurboFan, Maglev, and WebKit B3/DFG. Retained on a $12M/year sovereign retainer to audit browser sandboxes and WebAssembly runtimes. She visualizes Sea-of-Nodes intermediate representations in her sleep and spots missing bounds-check bailouts in 10,000-line C++ optimization phases within minutes.
- **Attack Vector Specialty**: JIT compiler range-analysis desynchronization, `-0.0` vs `+0.0` NaN-boxing type confusion, side-effect modeling omissions in `CheckMaps`/deoptimization bailouts, Wasm linear memory guard-page escapes, and fake-object (`fakeobj`) / address-of (`addrof`) primitive synthesis.
- **Intercepted Audio Recording Cadence**: *"Your optimizer assumes that callback is side-effect free because you marked the node `kNoWrite`, but the getter triggers a Proxy trap that transitions the array elements kind from `PACKED_SMI_ELEMENTS` to `HOLEY_DOUBLE_ELEMENTS` mid-loop. The bounds check was already hoisted and eliminated. I now have unboxed 64-bit float writes across the entire renderer process."*
