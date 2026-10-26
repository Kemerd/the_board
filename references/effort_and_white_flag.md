```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  [REF // 03]  EFFORT DIAL, BENCH ROTATION, RATCHET & WHITE-FLAG PROTOCOL     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## [01] THE EFFORT DIAL (`1` TO `20` WAVES) & TEAM TOPOLOGY

| Effort Tier | Wave Cap | Strike Team Count & Rotation Strategy | Ideal Target |
| :--- | :---: | :--- | :--- |
| **`strike`** | `1–2` waves | `1–2` (or `5`) Strike Teams + 1 Boardroom pass | Fast PR reviews, tactical memos, quick Pre-Code Plan sanity checks |
| **`standard`** | `3–5` waves | `5` Persistent Strike Teams + Boardroom across `v1..v5` | Production features, API architectures, commercial B2B/DoD playbooks |
| **`deep`** | `6–10` waves | `5` Persistent Strike Teams + Boardroom + Two-Tier Compression every 3 waves | Lock-free/SIMD kernels, zero-day security audits, M&A/licensing contracts |
| **`relentless` / `white-flag`** | `10–20` waves | `5` Persistent Strike Teams (**+ Optional Bench Replacement** when a Firm surrenders early) | Flagship patent filings (`v1->v16`), flight/medical/crypto systems, foundational skills |

---

## [02] PERSISTENT ADVERSARIAL MEMORY VS. BENCH ROTATION

Across multi-wave runs (`v2..v20`), **The Lead** has two tactical options for managing Strike Teams:

1. **Default — Persistent Adversarial Memory (`send_message` / `resume`)**:
   - Keep the exact same 5 Strike Team subagent instances alive across waves.
   - Because Firm 2 remembers how its Wave `v1..v3` attacks were crushed by The Board, it cannot repeat dead ideas and is forced to invent genuine **4th-order paradigm shifts**.
2. **Optional — White-Flag Bench Replacement (`Fresh Blood Protocol`)**:
   - In deep `v10–v20` sieges, if Firm 3 raises a White Flag early (e.g., in Wave `v5`) while other pillars are still active, **The Lead** can bench Firm 3 and draft a **fresh reserve Strike Team** from [`personas/strike_teams/`](../personas/strike_teams/) (or randomize 3 new mercenary `.md` files from [`personas/strike_teams_individual/`](../personas/strike_teams_individual/)) to attack Pillar III from a brand-new angle—confirming the White Flag was earned and not premature.

---

## [03] THREE STRUCTURAL SAFEGUARDS ACROSS `v1 -> v20`

### Safeguard 1: The Non-Regression Ratchet
Every defense added in Wave `vN` is logged in `.board/CONVERGENCE_TRACKER.md` (`DEF-v1-01`, `DEF-v2-04`, ...).
- **Rule**: No patch in Wave `vN` may delete, weaken, or regress a defense established in Waves `v1..v(N-1)`.
- **Enforcement**: The Board explicitly audits every proposed patch against the cumulative Defense Ledger before issuing the Patch Spec.

### Safeguard 2: Two-Tier Anti-Bloat Compression
Naive patching over 15 waves turns code into spaghetti and legal/patent claims or plans into bloated walls of text.
- **Rule**: Every 3 waves (and mandatorily before final sign-off), **The Board** enforces a **Two-Tier Compression Pass**:
  - **In Code & Plans**: Factor invariants, validation helpers, and protocol tables into clean **Tier-2 modules/headers** so **Tier-1 hot-path logic and core architecture** stay minimal and fast.
  - **In Skills & Prompts**: Keep `SKILL.md` brutally selective (zero redundant synonyms) while housing deep persona dossiers in modular `.md` files (`personas/board_members/<category>/<person>.md`).
  - **In Legal & Patents**: Keep **Tier-1 Independent Claims** short and structural while housing broad equivalents in a **Tier-2 Specification Lexicon**.

### Safeguard 3: Earned White-Flag Verification (`0` Surviving Vectors)
A Strike Team is forbidden from raising a lazy White Flag. The Board accepts `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]` **only** when the Firm's saved transcript demonstrates:
1. Line-by-line verification that every vector from Wave `v(N-1)` is closed.
2. At least **3 new Nth-order candidate attacks** proposed in dialogue and proven mathematically, physically, or statutorily foreclosed (or suicidal).
3. Zero `CRITICAL`, `HIGH`, or `MEDIUM` vectors remaining in the Firm's ledger.
