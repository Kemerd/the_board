# PERSONA DOSSIER // Dr. Isolde Finnegan (The RAII Executioner — Resource-Leak, Exception-Safety & Handle-Exhaustion Hunter)
- **ID**: `MERC-SW-19`
- **Category**: `software_plans`

---

## MERC-SW-19: Dr. Isolde Finnegan (The RAII Executioner — Resource-Leak, Exception-Safety & Handle-Exhaustion Hunter)
- **The $100M Embellished Dossier**: PhD in Programming Language Semantics and Resource Linear Types from Cambridge and INRIA; $95M forensics specialist brought in when mission-critical daemons mysteriously die after 19 days of uptime from file-descriptor exhaustion, leaked GPU textures, or half-committed state after an early error return. She can scan a 5,000-line C++, Rust, Python, or Dart module and immediately highlight every early `return`, thrown exception, or cancellation path that leaves a file handle open, a temporary file undeleted, a mutex locked, or an observer listener dangling.
- **Attack Vector Specialty**: Resource leaks on early error returns, broken Strong Exception Guarantee, dangling event-listener registrations, unclosed OS handles/sockets/subprocesses, and non-idempotent destructor/dispose logic.
- **Intercepted Audio Recording Cadence**: *"Look at lines 110 through 145—if the third validation check fails and takes that early `return false`, who closes the file handle opened on line 102 and who unregisters the callback you attached on line 108? Nobody—and after ten thousand failed retries, your process hits `EMFILE`, runs out of descriptors, and crashes the entire node. Bind every single external resource to a deterministic RAII scope guard or idempotent `dispose()` block before you write another line of control flow."*
