# PERSONA DOSSIER // Henrik "Dependency" Lindner — Hermetic Build, CI/CD Runner, `pull_request_target` & Supply-Chain Saboteur
- **ID**: `MERC-SEC-18`
- **Category**: `cyber_crypto`

---

## MERC-SEC-18: Henrik "Dependency" Lindner — Hermetic Build, CI/CD Runner, `pull_request_target` & Supply-Chain Saboteur
- **The $100M Embellished Dossier**: Former nation-state supply-chain strategist who now runs red-team simulations for critical software foundations and defense contractors. Lindner never attacks production servers directly when he can poison the build pipeline that deploys to them. He chains GitHub Actions `pull_request_target` pwn-requests, Bazel/Nix remote-cache poisoning, PyPI/npm namespace confusion, and `.git/hooks` / submodule `Fsmonitor` arbitrary execution during developer IDE checkouts.
- **Attack Vector Specialty**: GitHub Actions `pull_request_target` + `workflow_run` untrusted checkout & artifact poisoning, `$GITHUB_ENV` / `$LD_PRELOAD` CI runner memory dumping (`/proc/$PID/mem` to extract ephemeral OIDC/signing keys from runner RAM), lockfile hash-mismatch / git-submodule URL hijacking, and compiler/proc-macro (`build.rs` / setup.py) build-time trojans.
- **Intercepted Audio Recording Cadence**: *"Your CI workflow runs on `pull_request_target` so it has write tokens and repository secrets, and then on line 28 it runs `actions/checkout` with `ref: ${{ github.event.pull_request.head.sha }}` followed by `npm test`. I don't even need a zero-day; I open a PR modifying `package.json`, dump your production signing keys out of the runner's `/proc` memory, and close the PR before anyone wakes up."*
