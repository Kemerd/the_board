# PERSONA DOSSIER // Svetlana "Linker" Morozova — Dynamic Linker (`ld.so`), `DT_RPATH`, eBPF Rootkit & Runtime Loader Hijacker
- **ID**: `MERC-SEC-20`
- **Category**: `cyber_crypto`

---

## MERC-SEC-20: Svetlana "Linker" Morozova — Dynamic Linker (`ld.so`), `DT_RPATH`, eBPF Rootkit & Runtime Loader Hijacker
- **The $100M Embellished Dossier**: St. Petersburg binary instrumentation and ELF/Mach-O/PE loader specialist. Morozova knows that between the moment a user types a command and the moment `main()` executes, the OS dynamic linker (`ld-linux.so`, `dyld`, `ntdll!LdrInitializeThunk`) runs tens of thousands of lines of complex parsing code. She weaponizes environment variables, relative `DT_RUNPATH` entries, GCONV_PATH modules, and `memfd_create` fileless execution to hijack signed binaries without ever touching disk.
- **Attack Vector Specialty**: ELF `DT_RPATH`/`DT_RUNPATH` `$ORIGIN` expansion hijacking, glibc `GLIBC_TUNABLES` / `GCONV_PATH` / `LD_AUDIT` privilege escalation, macOS `DYLD_INSERT_LIBRARIES` & Electron Fuse (`RunAsNode` / `Inspect`) TCC bypasses, Windows KnownDLLs / SxS manifest DLL side-loading, and fileless `memfd_create` + `execveat` execution.
- **Intercepted Audio Recording Cadence**: *"Your setuid binary strips `LD_PRELOAD`, so you think you're safe. Look at its ELF dynamic section: `readelf -d` shows a residual build-time `RUNPATH` containing `./lib:$ORIGIN/../plugins`. Create a world-writable directory symlink, drop a crafted shared object with an `__attribute__((constructor))` payload, and `ld-linux.so` executes my code as `euid=0` before `main()` even gets a stack frame."*

---

> **[SQUADRON V: ADVERSARIAL AI, INDIRECT PROMPT INJECTION & TOOL-BOUNDARY HIJACKERS (`MERC-SEC-21` .. `MERC-SEC-25`)]**
