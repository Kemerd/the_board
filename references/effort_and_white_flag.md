```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  [REF // 03]  EFFORT DIAL, BENCH ROTATION, RATCHET & WHITE-FLAG PROTOCOL     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## [01] THE EFFORT DIAL (`1` TO `20` WAVES) & TEAM TOPOLOGY

| Effort Tier | Wave Cap | Strike Team Count & Rotation Strategy | Ideal Target |
| :--- | :---: | :--- | :--- |
| **`strike`** | `1–2` waves | `1–2` (or `5`) Strike Teams + 1 Boardroom pass | Fast PR reviews, tactical memos, quick Pre-Code Plan sanity checks |
| **`standard`** | `3–5` waves | `5` Persistent Strike Teams + Boardroom across `v1..v5` (optional Bench Rotation) | Production features, API architectures, commercial B2B/DoD playbooks |
| **`deep`** | `6–10` waves | `5` Persistent Strike Teams + **Default Bench Replacement** on early White Flags + Two-Tier Compression every 3 waves | Lock-free/SIMD kernels, zero-day security audits, M&A/licensing contracts |
| **`white-flag` / `relentless`** | `Up to 20 waves` (halts upon `5/5` White Flags or Wave 20 ceiling) | `5` Persistent Strike Teams + **Default Bench Replacement** on early White Flags + Cross-Pillar Diff Re-Verification | Flagship patent filings (`v1->v16`), flight/medical/crypto systems, foundational skills |

---

## [02] PERSISTENT ADVERSARIAL MEMORY, BENCH ROTATION & CROSS-PILLAR RE-VERIFICATION

Across multi-wave runs (`v2..v20`), **The Lead** enforces three laws over Strike Team continuity:

1. **Persistent Adversarial Memory (`send_message` / `resume`)**:
   - Keep the exact same 5 Strike Team subagent instances alive across waves whenever open vectors remain in their pillar.
   - Because Firm 2 remembers how its Wave `v1..v3` attacks were foreclosed by The Board, it cannot repeat dead ideas and is forced to invent genuine **Nth-order paradigm shifts**.
2. **White-Flag Bench Replacement (`Fresh Blood Protocol` — Default in `deep` and `white-flag`/`relentless`)**:
   - When a Firm raises an early White Flag while `< 5/5` Firms have converged, **The Lead** benches that Firm and drafts a **fresh reserve Strike Team** from [`personas/strike_teams/`](../personas/strike_teams/) (or selects 3 new individual mercenary `.md` dossiers from [`personas/strike_teams_individual/INDEX.md`](../personas/strike_teams_individual/INDEX.md)) to audit that pillar with fresh eyes—confirming the White Flag was earned and not premature.
3. **Cross-Pillar Diff Re-Verification Law**:
   - Whenever a Wave `vN` patch modifies a shared file touched by a previously White-Flagged pillar, that pillar's Strike Team must re-audit the diff in Wave `v(N+1)` to verify zero cross-pillar regressions before its White Flag is retained.

---

## [03] THREE STRUCTURAL SAFEGUARDS ACROSS `v1 -> v20`

### Safeguard 1: The Non-Regression Ratchet
Every defense added in Wave `vN` is logged in `CONVERGENCE_TRACKER.md` (`DEF-v1-01`, `DEF-v2-04`, ...).
- **Rule**: No patch in Wave `vN` may delete, weaken, or regress a defense established in Waves `v1..v(N-1)`.
- **Enforcement**: `CONVERGENCE_TRACKER.md` is passed directly into Template `[D]` on every wave so **The Board** audits every proposed patch against the cumulative Defense Ledger before issuing the Patch Spec, and **The Lead** appends the new `DEF-vN-XX` rows in Phase 3.

### Safeguard 2: Two-Tier Anti-Bloat Compression
Naive patching over 15 waves turns code into spaghetti and legal/patent claims or plans into bloated walls of text.
- **Rule**: Every 3 waves (and mandatorily before final sign-off), **The Board** enforces a **Two-Tier Compression Pass**:
  - **In Code & Plans**: Factor invariants, validation helpers, and protocol tables into clean **Tier-2 modules/headers** so **Tier-1 hot-path logic and core architecture** stay minimal and fast.
  - **In Skills & Prompts**: Keep `SKILL.md` brutally selective (zero redundant synonyms) while housing deep persona dossiers in modular `.md` files (`personas/board_members/<category>/<person>.md`).
  - **In Legal & Patents**: Keep **Tier-1 Independent Claims** short and structural while housing broad equivalents in a **Tier-2 Specification Lexicon**.

### Safeguard 3: Earned White-Flag Verification & Board Revocation Authority (`0` Surviving Vectors)
A Strike Team is forbidden from raising a lazy or straw-man White Flag. The Board and [`scripts/verify_convergence.py`](../scripts/verify_convergence.py) accept `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]` **only** when the Firm's saved transcript demonstrates:
1. Line-by-line verification (`4-State Disposition Table`) proving that every vector from Wave `v(N-1)` is `[DEAD / CHECKMATED (Verified at File:Line)]`.
2. At least **3 non-suicidal, steel-manned Nth-order candidate attacks** anchored to exact file/line citations and proven mathematically, physically, or statutorily foreclosed by Mask 2 (`The Literal Purist`). Suicidal straw-men are strictly prohibited.
3. Zero `CRITICAL`, `HIGH`, or `MEDIUM` vectors remaining in the Firm's ledger, and full compliance with minimum line (`>= 250`) and dialogue turn (`>= 10`) thresholds.
4. **Board White-Flag Revocation Authority (`[WHITE FLAG REVOKED BY BOARD]`)**: If The Board detects that a Firm surrendered using weak straw-men or missed a live vulnerability in its pillar, The Board revokes that Firm's White Flag and orders immediate remediation.
