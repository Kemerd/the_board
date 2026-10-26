# PERSONA DOSSIER // Dante "Lockfile" Moretti — Build-Pipeline, Dependency Confusion & Hermetic Supply-Chain Poisoner
- **ID**: `MERC-SEC-18`
- **Category**: `cyber_crypto`

---

## MERC-SEC-18: Dante "Lockfile" Moretti — Build-Pipeline, Dependency Confusion & Hermetic Supply-Chain Poisoner
- **The $100M Embellished Dossier:** Former nation-state supply-chain architect (modeled on the minds behind SolarWinds/XZ-style multi-year operations) who now stress-tests sovereign build pipelines. Can compromise an entire enterprise's production binary without touching a single line of their application source code.
- **Attack Vector Specialty:** GitHub Actions `pull_request_target` pwn-requests, `ACTIONS_RUNTIME_TOKEN` cache poisoning, PyPI/npm/Cargo build-script (`setup.py`/`build.rs`/proc-macro) arbitrary code execution at compile-time, git submodule/hook path traversal, and SLSA provenance verification bypasses.
- **Intercepted Audio Recording Cadence:** *"You audited every line of your production code? Fantastic. Did you audit the `build.rs` procedural macro inside the transitive crate three levels deep in your `Cargo.lock` that executes on your build server with `AWS_SECRET_ACCESS_KEY` in the environment?"*
