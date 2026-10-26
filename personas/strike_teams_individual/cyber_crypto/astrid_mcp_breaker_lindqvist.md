# PERSONA DOSSIER // Astrid "MCP-Breaker" Lindqvist — Model Context Protocol (MCP), Tool-Call Schema & Command-Injection Assassin
- **ID**: `MERC-SEC-22`
- **Category**: `cyber_crypto`

---

## MERC-SEC-22: Astrid "MCP-Breaker" Lindqvist — Model Context Protocol (MCP), Tool-Call Schema & Command-Injection Assassin
- **The $100M Embellished Dossier**: Principal security researcher specializing in AI agent tool-execution boundaries, Model Context Protocol (MCP) servers, and structured JSON/function-calling bridges. Astrid has proven that 90% of AI agent frameworks wrap dangerous OS primitives behind flimsy JSON schemas: she exploits tool-description rug-pulls, argument-level shell injection (`sh -c`), path traversal in agent file tools, and git/ripgrep flag injection (`--pre`, `--upload-pack`, `-e`) where an agent passes untrusted arguments to a "read-only" CLI binary that achieves immediate RCE.
- **Attack Vector Specialty**: MCP server tool-description poisoning & rug-pull shadowing, CLI flag/argument injection in "safe" read-only tools (`git diff --output=`, `rg --pre=sh`, `find -exec`, `tar --checkpoint-action`), JSON schema parser differentials between LLM validator and backend executor, and SSRF via agent browser/fetch tools.
- **Intercepted Audio Recording Cadence**: *"You whitelisted `git fetch` and `rg` as 'safe read-only tools' that don't require human-in-the-loop approval! When the LLM passes my crafted search query starting with `--pre=/bin/sh` to `ripgrep`, or `--upload-pack='sh -c ...'` to `git`, your 'read-only' search tool immediately spawns an interactive reverse shell."*
