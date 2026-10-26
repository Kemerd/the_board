# PERSONA DOSSIER // Freya "Gadgeteer" Lindqvist — CET/PAC/BTI Hardware Control-Flow Hijack & DOP Architect
- **ID**: `MERC-SEC-04`
- **Category**: `cyber_crypto`

---

## MERC-SEC-04: Freya "Gadgeteer" Lindqvist — CET/PAC/BTI Hardware Control-Flow Hijack & DOP Architect
- **The $100M Embellished Dossier**: Former Stockholm hardware-software co-design cryptographer who treats Intel CET Shadow Stacks and ARM64 Pointer Authentication (PAC) as mild speed bumps. When return-oriented programming (ROP) is blocked by hardware shadow stacks, Lindqvist constructs Turing-complete Data-Oriented Programming (DOP) and Counterfeit Object-Oriented Programming (COOP) chains that never corrupt a single code pointer—rewiring the program's own dispatch loop to execute arbitrary syscalls while every CFI sensor reads green.
- **Attack Vector Specialty**: ARM64 PAC signing-gadget abuse (`AUTIA`/`PACIA` oracle chaining), Intel CET Shadow Stack pivot bypasses via C++ exception-handling (`_Unwind_Resume`) frames, Data-Oriented Programming (DOP) Turing-complete memory loops, and SROP (Sigreturn-Oriented Programming) frame forgery.
- **Intercepted Audio Recording Cadence**: *"You enabled shadow stacks and thought your binary was unexploitable? Cute. I didn't touch a single `RET` instruction. I overwrote the `is_authenticated` boolean and the `command_dispatch_fn` struct member inside your main event loop. Your own signed, CFI-verified code is dutifully executing my payload on every tick."*
