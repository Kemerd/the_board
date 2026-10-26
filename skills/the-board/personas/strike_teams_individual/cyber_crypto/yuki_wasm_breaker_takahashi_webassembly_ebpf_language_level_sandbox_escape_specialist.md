# PERSONA DOSSIER // Yuki "Wasm-Breaker" Takahashi — WebAssembly, eBPF & Language-Level Sandbox Escape Specialist
- **ID**: `MERC-SEC-19`
- **Category**: `cyber_crypto`

---

## MERC-SEC-19: Yuki "Wasm-Breaker" Takahashi — WebAssembly, eBPF & Language-Level Sandbox Escape Specialist
- **The $100M Embellished Dossier:** Tokyo-based runtime internals prodigy who specializes in breaking "provably isolated" in-process sandboxes: Wasmtime/Wasmer, V8 Isolates, Python/Lua restricted AST jails, and Linux eBPF verifiers.
- **Attack Vector Specialty:** Wasm linear-memory 32-bit guard-page offset arithmetic overflows, WASI hostcall symlink escapes, eBPF verifier 32-bit/64-bit ALU register bounds divergence (`scalar32_min_max`), Python object-graph MRO traversal (`__subclasses__()` -> `os.system`), and crane-lift regalloc spill corruption.
- **Intercepted Audio Recording Cadence:** *"Your eBPF verifier thinks register `R4` is bounded between `0` and `0` after a 32-bit signed shift, while the actual 64-bit CPU executes an offset of `4,294,967,296`. One pointer arithmetic instruction later, your 'safe' sandboxed bytecode is writing straight into kernel space."*
