# INTERCEPTED STRIKE-TEAM RECORDING // FIRM 4: CROSS-RUNTIME PACKAGING, LINK RESOLUTION & CONTEXT HYGIENE

```diff
@@ ╔══════════════════════════════════════════════════════════════════════════════╗ @@
!  ║  [AUDIO RECORDING ACTIVE // STOCKHOLM HERMETIC PACKAGING LAB — SUB-LEVEL 4]  ║
!  ║  FIRM 04        // HERMETIC-GUILLOTINE SYNDICATE (PILLAR IV)                 ║
-  ║  BOUNTY RETAINER// $100,000,000 + 20% KILL-FEE BONUS (WAVE v1)               ║
+  ║  ASSIGNED PILLAR// BROKEN LINKS, ROOT-VS-SUBFOLDER DRIFT & PLUGIN MANIFESTS  ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

- **Timestamp**: `2026-10-26T06:44:10Z`
- **Target Repository**: `L:\Dev\the_board`
- **Primary Target Artifacts Audited**:
  - `L:\Dev\the_board\SKILL.md` (`119 lines`, `13,471 bytes`)
  - `L:\Dev\the_board\skills\the-board\SKILL.md` (`143 lines`, `15,333 bytes`)
  - `L:\Dev\the_board\plugin.json` (`6 lines`, `300 bytes`)
  - `L:\Dev\the_board\gemini-extension.json` (`5 lines`, `202 bytes`)
  - `L:\Dev\the_board\.claude-plugin\plugin.json` (`8 lines`, `318 bytes`)
  - `L:\Dev\the_board\README.md` (`219 lines`, `20,867 bytes`)
  - `L:\Dev\the_board\commands\board.md` (`59 lines`, `6,077 bytes`)
  - `L:\Dev\the_board\personas\boardrooms\*.md` (`8 Boardroom manifests` + `README.md`)
  - `L:\Dev\the_board\personas\board_members\INDEX.md` (`249 lines`, `26,901 bytes`)
  - `L:\Dev\the_board\personas\strike_teams_individual\INDEX.md` (`319 lines`, `95,779 bytes`)
  - `L:\Dev\the_board\scripts\split_personas_to_files.py` (`227 lines`, `9,595 bytes`)
  - `L:\Dev\the_board\scripts\install.ps1` (`50 lines`, `2,019 bytes`) & `L:\Dev\the_board\scripts\install.sh` (`38 lines`, `1,740 bytes`)
  - `L:\Dev\the_board\scripts\init_board_workspace.py` (`252 lines`, `8,771 bytes`) & `L:\Dev\the_board\scripts\verify_convergence.py` (`223 lines`, `8,479 bytes`)
  - `L:\Dev\the_board\personas\*.md` (`8 legacy domain files`) & `L:\Dev\the_board\references\*.md` (`4 reference files`)
- **Active Mercenary Triad**:
  1. **Freja "Hermetic" Lindström (`MERC-SW-32` — The $100M Principal)**: Dual PhD in Build-Graph Theory & Cryptographic Supply-Chain Verification (Chalmers / TU Munich). Manifest, Link-Resolution & Packaging Inquisitor.
  2. **Dr. Viktor Krol (`MERC-SW-01` — The Literal Purist)**: Triple PhD in Formal Methods, Program Synthesis & Systems Architecture (ETH Zürich). Cross-Runtime Systems Architect & Pre-Commit Guillotine.
  3. **Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26` — The Lateral Breaker)**: Triple PhD in Optimizing Compilers, Type-Directed Specialization & Link-Time Code Generation (Edinburgh / Cambridge / UIUC). Context-Window & Repository Hygiene Surgeon.

---

## PART 1: VERBATIM WAR-ROOM AUDIO TRANSCRIPT (`[AUDIO RECORDING ACTIVE]`)

**[00:00:01] [SOUND OF HEAVY PNEUMATIC AIRLOCK SEALING; COOLING FANS HUMMING AT 42 dBA; THREE 8K ULTRA-WIDE MONITORS ILLUMINATING THE DIRECTORY TREE OF `L:\Dev\the_board`]**

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Lock the doors and pin the filesystem snapshot. Nobody touches a coffee cup until we have hashed every byte in `L:\Dev\the_board` and traced every Markdown link, JSON manifest, and installer copy path to its physical inode on disk. We are on a `$100,000,000` retainer with a 20% kill-fee bonus to audit **Pillar IV: Cross-Runtime Packaging, Markdown Link Resolution, Root-vs-Subfolder Skill Drift, and Context-Window Hygiene**. Look at `README.md` line 67:
> `[SECT // 02] TEN-SECOND INSTALLATION (ONE SKILL.MD RULES THEM ALL)`

**Freja "Hermetic" Lindström (`MERC-SW-32`):** "One `SKILL.md` rules them all," they brag! And yet when I run a recursive file tree across `L:\Dev\the_board`, there are *two* `SKILL.md` files, *three* plugin manifests (`plugin.json`, `.claude-plugin/plugin.json`, `gemini-extension.json`), *two* `references/` trees, *two* `scripts/` trees, *two* `examples/` trees, and five overlapping subdirectories under `personas/` (`board_members/`, `boardrooms/`, `repertoire_real_humans/`, `strike_teams/`, `strike_teams_individual/`) plus eight loose `.md` files sitting in the root of `personas/`. Let's start with blood on the floor: I want to check `personas/boardrooms/*.md` first. Look at `scripts/split_personas_to_files.py` lines 67–85 (`slugify_persona_name`). It strips parentheticals, strips `REAL-XXX-NN:`, normalizes NFKD, and converts non-alphanumerics to underscores. I'm betting $20M right now that the 8 Boardroom manifests in `personas/boardrooms/*.md` have broken links whenever a historical figure has quotation marks, military ranks, noble titles, or accents—like `Clarence "Kelly" Johnson`, `Sir Jony Ive`, `Rudolf E. Kálmán`, `Adm. Hyman G. Rickover`, `Col. John Boyd`, `Niccolò Machiavelli`, or `The Self-Aware Ghost of Steve Jobs`!

**Dr. Viktor Krol (`MERC-SW-01`):** *[Taps mechanical pencil against the glass table; pulls up `personas/boardrooms/*.md` side-by-side with `personas/board_members/` directory listings]* Hold your fire, Freja. Put the $20M back in your pocket before you embarrass this syndicate in front of The Board. I do not guess at broken links; I resolve every path against the actual filesystem. Look at Monitor 2. I just parsed every single Markdown link `[label](target)` across all 9 files in `L:\Dev\the_board\personas\boardrooms\`:
1. `personas/boardrooms/README.md` (lines 15–22, 28)
2. `personas/boardrooms/the_godfather_board.md` (lines 14–19)
3. `personas/boardrooms/software_and_plans_board.md` (lines 12–17)
4. `personas/boardrooms/hardware_and_physics_board.md` (lines 12–17)
5. `personas/boardrooms/design_and_product_board.md` (lines 12–17)
6. `personas/boardrooms/cybersecurity_board.md` (lines 12–17)
7. `personas/boardrooms/legal_and_patents_board.md` (lines 12–17)
8. `personas/boardrooms/philosophy_and_strategy_board.md` (lines 12–17)
9. `personas/boardrooms/commercial_and_dod_board.md` (lines 12–17)

**Dr. Viktor Krol (`MERC-SW-01`):** Let us check your specific suspects against the exact filenames generated on disk in `personas/board_members/<category>/`:
- In `personas/boardrooms/hardware_and_physics_board.md` line 12: links to `../board_members/physics_hardware/clarence_kelly_johnson.md`. On disk at `L:\Dev\the_board\personas\board_members\physics_hardware\clarence_kelly_johnson.md`? **Exists (`1,945 bytes`)**. `slugify_persona_name("Clarence \"Kelly\" Johnson")` turned the quotes and spaces into single underscores: `clarence_kelly_johnson`.
- In `personas/boardrooms/hardware_and_physics_board.md` line 15: links to `../board_members/physics_hardware/rudolf_e_kalman.md`. On disk at `L:\Dev\the_board\personas\board_members\physics_hardware\rudolf_e_kalman.md`? **Exists (`1,908 bytes`)**. `NFKD` decomposed `á` into `a` + combining acute accent, and `.encode("ascii", "ignore")` stripped the accent cleanly.
- In `personas/boardrooms/design_and_product_board.md` line 14: links to `../board_members/design_product/sir_jony_ive.md`. On disk at `L:\Dev\the_board\personas\board_members\design_product\sir_jony_ive.md`? **Exists (`1,781 bytes`)**.
- In `personas/boardrooms/software_and_plans_board.md` line 17, `hardware_and_physics_board.md` line 17, and `commercial_and_dod_board.md` line 15: links to `../board_members/strategy_command/adm_hyman_g_rickover.md`. On disk? **Exists (`1,996 bytes`)**.
- In `personas/boardrooms/commercial_and_dod_board.md` line 14: links to `../board_members/strategy_command/col_john_boyd.md`. On disk? **Exists (`1,953 bytes`)**.
- In `personas/boardrooms/philosophy_and_strategy_board.md` line 17: links to `../board_members/strategy_command/niccolo_machiavelli.md`. On disk? **Exists (`1,887 bytes`)**.
- In `personas/boardrooms/the_godfather_board.md` line 14: links to `../board_members/design_product/the_self_aware_ghost_of_steve_jobs.md`. On disk? **Exists (`2,115 bytes`)**.

**Dr. Viktor Krol (`MERC-SW-01`):** Every single one of the **48 Board member links** across all 8 `personas/boardrooms/*.md` manifests and `personas/boardrooms/README.md` resolves to a valid, non-empty `.md` file on disk. Your first theory is **dead on arrival**. If we walk into The Boardroom claiming `personas/boardrooms/*.md` has broken links to `clarence_kelly_johnson.md` or `sir_jony_ive.md`, Dennis Ritchie and Alan Turing will throw us out the window.

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** *[Leans forward, eyes narrowing at the terminal output]* Wait a second, Viktor. Don't let Freja off the hook on `personas/boardrooms/README.md`, because while the 8 Boardroom files in `personas/boardrooms/*.md` have valid links, look two directories up at **`L:\Dev\the_board\commands\board.md`**! Read **line 42** of `commands/board.md` out loud right now!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** *[Pulls `L:\Dev\the_board\commands\board.md` onto Monitor 1, zooming in on lines 41–44]*
```markdown
3. **🏛️ EXECUTIVE BOARDROOM ROSTER**:
   - **`[A] THE GODFATHER OF BOARDS`** (`ghost_of_steve_jobs.md`, `epictetus.md`, `alan_turing.md`, `nikola_tesla.md`, `albert_einstein.md`, `claude_shannon.md`)
```
Aha!! Look at line 42 of `commands/board.md`: it tells the agent to load **`ghost_of_steve_jobs.md`**! There is NO `ghost_of_steve_jobs.md` anywhere in `L:\Dev\the_board`! On disk (`personas/board_members/design_product/the_self_aware_ghost_of_steve_jobs.md`), in `README.md` line 181, and in `personas/boardrooms/the_godfather_board.md` line 14, the file is named **`the_self_aware_ghost_of_steve_jobs.md`**! When a user invokes the `/board` slash command in Claude Code and selects Option `[A] THE GODFATHER OF BOARDS`, `commands/board.md` instructs the agent to look for `ghost_of_steve_jobs.md`—which does not exist!

**Dr. Viktor Krol (`MERC-SW-01`):** Good catch, Freja—and look twelve lines lower in that exact same file, `L:\Dev\the_board\commands\board.md`, at **line 55**:
```markdown
2. Follow the exact protocol in [`SKILL.md`](../SKILL.md):
```
In the repository root, `commands/board.md` sits at `L:\Dev\the_board\commands\board.md`, so `../SKILL.md` resolves to `L:\Dev\the_board\SKILL.md`. In the repo, that link works. **HOWEVER**, look at what `scripts/install.ps1` (lines 41–43) and `scripts/install.sh` (lines 31–32) do when installing `/board` for Claude Code:
```powershell
    $ClaudeCommandsDir = Join-Path $HOME ".claude\commands"
    New-Item -ItemType Directory -Force -Path $ClaudeCommandsDir | Out-Null
    Copy-Item -Force (Join-Path $RepoRoot "commands\board.md") (Join-Path $ClaudeCommandsDir "board.md")
```
When `commands/board.md` is copied to `~/.claude/commands/board.md`, where does `../SKILL.md` resolve?! It resolves to **`~/.claude/SKILL.md`**! Not `~/.claude/skills/the-board/SKILL.md`! So in every installed Claude Code environment on Earth, the `[SKILL.md](../SKILL.md)` link on line 55 of `~/.claude/commands/board.md` points to a non-existent file `~/.claude/SKILL.md`!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Hold on—Before we even get to `install.ps1`, let me test my second hypothesis on the root `SKILL.md` and `README.md`. In `SKILL.md` lines 53–119 and `README.md` lines 180–188, they link to `./personas/strike_teams/`, `./personas/board_members/`, `./personas/boardrooms/`, and `./scripts/init_board_workspace.py`. And what about the `.claude-plugin/plugin.json` vs root `plugin.json` schema mismatch? In root `plugin.json` line 5:
```json
  "author": "Donald Everett Hinton III"
```
Whereas in `.claude-plugin/plugin.json` lines 5–7:
```json
  "author": {
    "name": "Donald Everett Hinton III"
  }
```
Surely one of those two `plugin.json` files fails schema validation, or root `SKILL.md` has a broken relative path!

**Dr. Viktor Krol (`MERC-SW-01`):** *[Shakes head firmly, pulling up the link-verification matrix and JSON schema specs]* No, Freja. I am shooting down both of those false alarms right now so we don't waste ammunition on phantoms:
1. **False Alarm Shot Down — Root `SKILL.md` and `README.md` Relative Links**: I ran a full AST link resolver across `L:\Dev\the_board\SKILL.md` (all 16 relative Markdown links on lines 53, 60, 62, 80, 82, 85, 89, 101, 113, 114, 115, 116, 117, 118, 119) and `L:\Dev\the_board\README.md` (all 6 relative links on lines 181–186). When evaluated from the repository root `L:\Dev\the_board\`, **100% of the links in root `SKILL.md` and `README.md` resolve cleanly on disk**.
2. **False Alarm Shot Down — `author` String vs. Object in `plugin.json` vs `.claude-plugin/plugin.json`**: Both JSON files are syntactically valid UTF-8 JSON. In Claude Code's `.claude-plugin/plugin.json` specification, `"author"` is an object `{"name": "...", "email": "...", "url": "..."}`, whereas generic/Cursor/npm-style `plugin.json` manifests accept `"author"` as a string shorthand. That difference is intentional cross-runtime adaptation, **not** a bug.

**Dr. Viktor Krol (`MERC-SW-01`):** **HOWEVER**, while you were looking at the `"author"` field in `plugin.json`, look at what the plugin manifests and the `skills/the-board/` subdirectory *actually* do when Claude Code, Gemini CLI, or Google Antigravity loads this repository! Alistair, pull up the diff between `L:\Dev\the_board\SKILL.md` and `L:\Dev\the_board\skills\the-board\SKILL.md`!

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** *[Slams `Enter` on the keyboard; a massive red-and-green diff fills Monitor 3]* Mother of God. Look at this. The repository contains **two completely different versions of `the-board` living side-by-side**!
- Root `L:\Dev\the_board\SKILL.md` is **119 lines (`13,471 bytes`)**—the **v2.0 architecture** featuring:
  - The ASCII diff boot banner (lines 13–26) and `[00] TERMINAL BOOT & INTERACTIVE INTAKE` (lines 28–34).
  - Four operating modes including **`plan` (Pre-Code / Pre-Execution Plan Siege)** (lines 32, 69).
  - Section `[02] TWO-TIER PERSONA ARCHITECTURE` (lines 48–64): `$100M` Mercenary Strike Teams in `personas/strike_teams/` + 6 Real Historical Humans on The Board in `personas/board_members/<category>/<person>.md` selected via `personas/boardrooms/*.md` with closed-door choreography (`[DOORS SEALED // EXECUTIVE SESSION RECORDING]`).
- Meanwhile, `L:\Dev\the_board\skills\the-board\SKILL.md` is **143 lines (`15,333 bytes`)**—an **un-updated v1.0 fossil**! Let's read `skills/the-board/SKILL.md` lines 14–21 and 72–76:
  - No ASCII boot banner! No interactive intake!
  - Lines 59 and 72–76: Only lists **3 operating modes** (`red`, `blue`, `purple`). **`plan` mode does not exist anywhere in `skills/the-board/SKILL.md`!**
  - Lines 96–101 and 135–143: **Zero mention of `personas/board_members/`, `personas/boardrooms/`, `personas/strike_teams/`, or real historical humans on The Board!** Instead, line 100 and line 139 instruct the agent to load `[references/domain_playbooks.md](./references/domain_playbooks.md)`!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Wait—it gets ten times worse! Look at the directory contents of `L:\Dev\the_board\skills\the-board\` that we just listed:
```text
L:\Dev\the_board\skills\the-board\SKILL.md                                     (15,333 bytes — Stale v1!)
L:\Dev\the_board\skills\the-board\personas\                                    (EMPTY DIRECTORY — 0 FILES!)
L:\Dev\the_board\skills\the-board\references\domain_playbooks.md               (11,072 bytes — Legacy v1)
L:\Dev\the_board\skills\the-board\references\effort_and_white_flag.md          (5,818 bytes — Stale v1 vs root 4,475 bytes!)
L:\Dev\the_board\skills\the-board\references\persona_mask_theory.md            (7,779 bytes — Stale v1 vs root 4,573 bytes!)
L:\Dev\the_board\skills\the-board\references\prompt_templates.md               (9,046 bytes — Stale v1 vs root 10,041 bytes!)
```
Look at `L:\Dev\the_board\skills\the-board\personas\`: **IT IS AN EMPTY FOLDER (`0` files, `0` subdirectories)**!
And look at `L:\Dev\the_board\skills\the-board\references\prompt_templates.md` **line 9**:
```markdown
Use this template when spawning each of the 5 parallel Red-Team subagents in Wave `v1`. Assign each firm its unique Pillar (`Pillar 1..5`) and 3-Persona Triad from [`domain_playbooks.md`](file:///L:/Dev/the_board/skills/the-board/references/domain_playbooks.md).
```
They hardcoded **`file:///L:/Dev/the_board/skills/the-board/references/domain_playbooks.md`**—a local Windows `L:` drive path from the author's workstation—directly inside `skills/the-board/references/prompt_templates.md` line 9! On macOS, Linux, or any Windows machine where the repo isn't mounted on `L:\Dev\the_board`, that link is 100% dead!

**Dr. Viktor Krol (`MERC-SW-01`):** Let us trace the exact cross-runtime consequence of this split-brain (`Vector F4-V1`). Why does `skills/the-board/` exist in a repository that also has `.claude-plugin/plugin.json`, `plugin.json`, and `gemini-extension.json`?
Because in **Claude Code's plugin loader** (`.claude-plugin/plugin.json`) and standard multi-skill repository discovery (`.agents/skills/` or plugin root), the runtime discovers skills by globbing **`skills/*/SKILL.md`**!
When a user installs `the_board` as a Claude Code plugin or points an agent skill scanner at the repository, the scanner finds `skills/the-board/SKILL.md`! And what happens when `skills/the-board/SKILL.md` is loaded?
1. The agent has **no `plan` mode** (`skills/the-board/SKILL.md` lines 72–76).
2. The agent has **no ASCII boot banner or interactive intake**.
3. The agent has **an empty `skills/the-board/personas/` directory (`0` files)**—none of the 215 real historical Board members, none of the 8 Boardrooms, and none of the 245 `$100M` mercenaries exist inside `skills/the-board/`!
4. The agent loads stale v1 `skills/the-board/references/prompt_templates.md` (which lacks the 6-Board-member `.md` loader in `[D]` and contains the broken `file:///L:/Dev/...` link on line 9), stale v1 `persona_mask_theory.md`, and stale v1 `effort_and_white_flag.md`!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Now let's check what happens if the user does *not* use the plugin loader, and instead runs the automated installation scripts touted in `README.md` lines 84–93:
```powershell
# Windows (PowerShell)
pwsh -File .\the_board\scripts\install.ps1 -Target all
```
or:
```bash
# macOS / Linux
bash ./the_board/scripts/install.sh all
```
Read `L:\Dev\the_board\scripts\install.ps1` lines 15–30 and `L:\Dev\the_board\scripts\install.sh` lines 14–23 right now!

**Dr. Viktor Krol (`MERC-SW-01`):** *[Reads `L:\Dev\the_board\scripts\install.ps1` lines 15–30 aloud]*
```powershell
function Install-SkillToDir {
    param([string]$DestDir, [string]$Label)

    New-Item -ItemType Directory -Force -Path $DestDir | Out-Null
    Copy-Item -Force (Join-Path $RepoRoot "SKILL.md") (Join-Path $DestDir "SKILL.md")

    foreach ($Sub in @("references", "examples", "scripts")) {
        $SrcSub = Join-Path $RepoRoot $Sub
        $DstSub = Join-Path $DestDir $Sub
        if (Test-Path $SrcSub) {
            New-Item -ItemType Directory -Force -Path $DstSub | Out-Null
            Copy-Item -Force -Recurse (Join-Path $SrcSub "*") $DstSub
        }
    }
    Write-Host "🏛️⚔️  Installed [the-board] skill -> $Label ($DestDir)" -ForegroundColor Green
}
```
And in `L:\Dev\the_board\scripts\install.sh` lines 14–23:
```bash
install_skill_dir() {
    local dest_dir="$1"
    local label="$2"
    mkdir -p "${dest_dir}/references" "${dest_dir}/examples" "${dest_dir}/scripts"
    cp -f "${REPO_ROOT}/SKILL.md" "${dest_dir}/SKILL.md"
    cp -rf "${REPO_ROOT}/references/"* "${dest_dir}/references/"
    cp -rf "${REPO_ROOT}/examples/"* "${dest_dir}/examples/"
    cp -rf "${REPO_ROOT}/scripts/"* "${dest_dir}/scripts/"
    echo "🏛️⚔️  Installed [the-board] skill -> ${label} (${dest_dir})"
}
```
*[Silence in the room for three seconds]*

**Freja "Hermetic" Lindström (`MERC-SW-32`):** **NEITHER `install.ps1` NOR `install.sh` COPIES `personas/`!**
Look at line 21 of `install.ps1`: `@("references", "examples", "scripts")`!
Look at line 17 of `install.sh`: `mkdir -p "${dest_dir}/references" "${dest_dir}/examples" "${dest_dir}/scripts"`!
They copy root `SKILL.md` into `~/.gemini/config/skills/the-board/`, `~/.claude/skills/the-board/`, and `.agents/skills/the-board/`—and they **completely forget to copy `personas/` (`personas/board_members/`, `personas/boardrooms/`, `personas/strike_teams/`, `personas/strike_teams_individual/`, `personas/repertoire_real_humans/`)**!
Every single link in `SKILL.md`:
- Line 53: `[personas/strike_teams/](./personas/strike_teams/)`
- Line 60: `[personas/board_members/<category>/<person>.md](./personas/board_members/)`
- Line 62: `[personas/boardrooms/*.md](./personas/boardrooms/)`
- Line 82: `[personas/boardrooms/](./personas/boardrooms/)` and `[personas/board_members/<category>/](./personas/board_members/)`
- Line 85: `[personas/strike_teams/](./personas/strike_teams/)`
- Line 89: `[personas/strike_teams/](./personas/strike_teams/)`
- Line 113: `[personas/board_members/](./personas/board_members/)`
- Line 114: `[personas/boardrooms/](./personas/boardrooms/)` and `[the_godfather_board.md](./personas/boardrooms/the_godfather_board.md)`
- Line 115: `[personas/strike_teams/](./personas/strike_teams/)`
**ALL NINE OF THOSE LINKS BREAK INSTANTLY (`FileNotFoundError`) THE MOMENT A USER INSTALLS THE SKILL VIA `install.ps1` OR `install.sh`!** That is a catastrophic `CRITICAL` packaging failure (`Vector F4-V2`)!

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** Now let's talk about what is sitting *inside* `personas/` in the repository, because I just audited `scripts/split_personas_to_files.py` (`227 lines`), `personas/board_members/INDEX.md` (`249 lines`), and `personas/strike_teams_individual/INDEX.md` (`319 lines`), and what I found is a masterclass in both parser bugs and un-garbage-collected filesystem pollution.
First, Viktor—remember how you told us who we are in the briefing?
- Mask 1: `MERC-SW-32` — **Freja "Hermetic" Lindström**
- Mask 2: `MERC-SW-01` — **Dr. Viktor Krol**
- Mask 3: `MERC-SW-26` — **Dr. Alistair "Zero-Cost" MacLeod**
Look at `personas/strike_teams_individual/software_plans/` on disk right now:
- `personas/strike_teams_individual/software_plans/freja_hermetic_lindstrom.md` (`ID: MERC-SW-32`)
- `personas/strike_teams_individual/software_plans/dr_viktor_krol.md` (`ID: MERC-SW-01`)
- `personas/strike_teams_individual/software_plans/dr_alistair_zero_cost_macleod.md` (`ID: MERC-SW-26`)
Now open `personas/strike_teams_individual/INDEX.md` and `personas/strike_teams/01_software_kernels_and_plans_mercenaries.md` and look up `MERC-SW-01`, `MERC-SW-26`, and `MERC-SW-32`!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** *[Scrolls to lines 10–11, 40–41, and 48 of `personas/strike_teams_individual/INDEX.md`]*
Wait a minute! In `personas/strike_teams_individual/INDEX.md`:
- Line 11: `| MERC-SW-01 | **Dr. Viktor "The Redline" Kaczmarek — Sovereign Pre-Code Spec Executioner** | [./software_plans/dr_viktor_the_redline_kaczmarek_sovereign_pre_code_spec_executioner.md](...) |`
- Line 41: `| MERC-SW-26 | **Dr.卢 (Lu) "Strict-Alias" Jian-Guo — The Undefined-Behavior & LLVM-IR Grand Surgeon** | [./software_plans/dr_strict_alias_jian_guo_the_undefined_behavior_llvm_ir_grand_surgeon.md](...) |`
- Line 48: `| MERC-SW-32 | **Dr. Svetlana "Bit-for-Bit" Koroleva — The Hermetic-Build & Determinism Tyrant** | [./software_plans/dr_svetlana_bit_for_bit_koroleva_the_hermetic_build_determinism_tyrant.md](...) |`
Why are *both* `freja_hermetic_lindstrom.md` AND `dr_svetlana_bit_for_bit_koroleva_the_hermetic_build_determinism_tyrant.md` sitting in `personas/strike_teams_individual/software_plans/` claiming `ID: MERC-SW-32`?!

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** Because `scripts/split_personas_to_files.py` (`split_collection`, lines 168–190) calls `cat_dir.mkdir(parents=True, exist_ok=True)` and writes `.md` files **without ever deleting old `.md` files from previous versions of the repertoire**!
When the repertoire files in `personas/repertoire_real_humans/*.md` and `personas/strike_teams/*.md` were edited or regenerated across commits, `split_personas_to_files.py` left every single old `.md` file sitting on disk as an **unindexed orphan**!
Look at the exact numbers from our filesystem audit:
1. In `personas/board_members/`:
   - `personas/board_members/INDEX.md` links to **215** `.md` files (`40` computing + `40` physics_hardware + `35` design_product + `35` philosophy_logic + `35` strategy_command + `30` law_rhetoric = `215`).
   - But on disk inside `personas/board_members/<category>/`, there are **221** `.md` files!
   - Here are the **6 unindexed orphan duplicate Board Member `.md` files** sitting in `personas/board_members/`:
     1. `physics_hardware/albert_einstein_19021909_bern_patent_examiner_class_iii.md` (orphan duplicate of `physics_hardware/albert_einstein.md`, both `REAL-PHYS-02`)
     2. `physics_hardware/charles_proteus_steinmetz_the_forger_of_thunderbolts.md` (orphan duplicate of `physics_hardware/charles_proteus_steinmetz.md`, both `REAL-PHYS-38`)
     3. `physics_hardware/lord_kelvin_william_thomson.md` (orphan duplicate of `physics_hardware/lord_kelvin.md`, both `REAL-PHYS-40`)
     4. `physics_hardware/robert_noyce_the_mayor_of_silicon_valley.md` (orphan duplicate of `physics_hardware/robert_noyce.md`, both `REAL-PHYS-32`)
     5. `physics_hardware/sergei_korolev_the_chief_designer.md` (orphan duplicate of `physics_hardware/sergei_korolev.md`, both `REAL-PHYS-20`)
     6. `strategy_command/talleyrand.md` (orphan duplicate of `strategy_command/charles_maurice_de_talleyrand_perigord.md`, both `REAL-STRAT-21`)
2. In `personas/strike_teams_individual/`:
   - `personas/strike_teams_individual/INDEX.md` links to **280** `.md` files.
   - But on disk inside `personas/strike_teams_individual/<category>/`, there are **464** `.md` files!
   - There are **184 unindexed orphan `.md` files** from an earlier persona generation run sitting on disk alongside the new files (including a malformed filename `commercial_dod/ideon_intel_inside_mercer.md` next to `gideon_intel_inside_mercer.md`)!

**Dr. Viktor Krol (`MERC-SW-01`):** Wait—why did you say `personas/strike_teams_individual/INDEX.md` links to **280** `.md` files when there are 7 categories of 35 mercenaries (`7 × 35 = 245` mercenaries)? Where did the extra `35` entries (`280 - 245 = 35`) in `personas/strike_teams_individual/INDEX.md` come from?!
Look at `personas/strike_teams_individual/INDEX.md` lines 10–11:
```markdown
| `MERC-SW-01` | **Category I: Pre-Code Implementation-Plan Wreckers (`MERC-SW-01` .. `MERC-SW-05`)** | [`./software_plans/category_i_pre_code_implementation_plan_wreckers.md`](./software_plans/category_i_pre_code_implementation_plan_wreckers.md) |
| `MERC-SW-01` | **Dr. Viktor "The Redline" Kaczmarek — Sovereign Pre-Code Spec Executioner** | [`./software_plans/dr_viktor_the_redline_kaczmarek_sovereign_pre_code_spec_executioner.md`](./software_plans/dr_viktor_the_redline_kaczmarek_sovereign_pre_code_spec_executioner.md) |
```
And look at the contents of `L:\Dev\the_board\personas\strike_teams_individual\software_plans\category_i_pre_code_implementation_plan_wreckers.md` (`lines 1–7`):
```markdown
# PERSONA DOSSIER // Category I: Pre-Code Implementation-Plan Wreckers (`MERC-SW-01` .. `MERC-SW-05`)
- **ID**: `MERC-SW-01`
- **Category**: `software_plans`

---

## Category I: Pre-Code Implementation-Plan Wreckers (`MERC-SW-01` .. `MERC-SW-05`)
```
It is a **7-line empty section-header stub** pretending to be persona `MERC-SW-01`!

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** Trace the exact bug in `L:\Dev\the_board\scripts\split_personas_to_files.py` lines 108–134 (`extract_persona_blocks`):
```python
        # Filter out generic section headers (e.g., "Category 1:", "Overview")
        is_persona_header = bool(
            re.search(r"(?:REAL|MERC)-[A-Z0-9\-]+", heading_text)
            or re.match(r"^#?\d{1,2}[\.\:\)\s\-]+", heading_text)
        )
        if not is_persona_header:
            continue
```
The author wrote a comment on line 108: `# Filter out generic section headers (e.g., "Category 1:", "Overview")`.
Why did that filter fail on 5 of the 7 Strike Team files (`01_software_kernels_and_plans_mercenaries.md`, `03_legal_patent_and_contract_sharks.md`, `05_hardware_robotics_and_physics_savants.md`, `06_design_copy_and_philosophy_iconoclasts.md`, `07_philosophy_ontology_and_prompt_linguists.md`)?
Because those 5 files include the ID range in parentheses inside the Category/Division heading—for example:
- `## Category I: Pre-Code Implementation-Plan Wreckers (\`MERC-SW-01\` .. \`MERC-SW-05\`)`
- `## DIVISION I: WITTGENSTEINIAN LEXICAL SURGEONS & SYNONYM ASSASSINS (\`MERC-PHIL-01\` – \`MERC-PHIL-05\`)`
Because `re.search(r"(?:REAL|MERC)-[A-Z0-9\-]+", heading_text)` searches *anywhere* in `heading_text`, it matches `MERC-SW-01` inside the parenthetical range of the `## Category I` header! And then line 132 (`id_match = re.search(r"((?:REAL|MERC)-[A-Z]+-\d+)", heading_text)`) assigns the first ID in the range (`MERC-SW-01`, `MERC-SW-06`, `MERC-SW-11`, `MERC-SW-16`, `MERC-SW-21`, `MERC-SW-26`, `MERC-SW-31`) to the Category header itself!
That creates **35 bogus `.md` files** (`7` per category across `software_plans`, `legal_patents`, `hardware_physics`, `design_philosophy`, and `philosophy_prompt_linguistics`) and **35 duplicate ID collisions** in `personas/strike_teams_individual/INDEX.md`!
And if The Lead follows `references/effort_and_white_flag.md` line 26 (*"randomize 3 new mercenary `.md` files from `personas/strike_teams_individual/`"*) and picks one of those 35 `category_*.md` or `division_*.md` files, the subagent gets a 7-line empty header with zero persona data!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Look at `scripts/split_personas_to_files.py` line 12 while we're in that file:
```python
and emits ONE standalone `.md` file per persona:
  - `personas/board_members/<category>/<person_slug>.md`
  - `personas/strike_teams/<category>/<mercenary_slug>.md`
```
The docstring on line 12 says it outputs to `personas/strike_teams/<category>/<mercenary_slug>.md`, while line 207 (`strike_dst = repo_root / "personas" / "strike_teams_individual"`) outputs to `personas/strike_teams_individual/`! And in root `SKILL.md` (lines 53, 85, 89, 115), `personas/strike_teams_individual/` is never linked or mentioned once!
Now look closer at `slugify_persona_name(raw_name: str)` on lines 67–85 of `scripts/split_personas_to_files.py`:
```python
def slugify_persona_name(raw_name: str) -> str:
    """Convert a persona heading or name into a clean lowercase filesystem slug."""
    # Guard against null or empty strings
    if not raw_name or not raw_name.strip():
        return "unknown_persona"

    # Strip parenthetical dates like (1912-1954) or role suffixes
    cleaned = re.sub(r"\([^)]*\)", "", raw_name)
    cleaned = re.sub(r"^(?:REAL|MERC)-[A-Z]+-\d+\s*:\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^#?\d+[\.\:\-\s]+", "", cleaned)

    # Normalize unicode accents (e.g., Kálmán -> Kalman, Gödel -> Godel)
    normalized = unicodedata.normalize("NFKD", cleaned)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")

    # Convert non-alphanumeric sequences to single underscores
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text.strip().lower()).strip("_")
    return slug if slug else "persona_entry"
```
Look at three separate slugification bugs in those 15 lines (`Vector F4-V5`):
1. **The `Søren Kierkegaard` -> `sren_kierkegaard.md` Unicode Stroke-Letter Deletion Bug**:
   Open `personas/board_members/INDEX.md` to **line 162**:
   ```markdown
   | `REAL-PHIL-23` | **Søren Kierkegaard** | [`./philosophy_logic/sren_kierkegaard.md`](./philosophy_logic/sren_kierkegaard.md) |
   ```
   Why is Søren Kierkegaard's file named **`sren_kierkegaard.md`** instead of `soren_kierkegaard.md`?!
   Because in Unicode Standard Annex #15, `NFKD` decomposes *combining diacritical marks* (like `ö` -> `o` + `\u0308`), but **diagonally stroked or ligature Latin letters (`ø`/`Ø`, `æ`/`Æ`, `ł`/`Ł`, `ß`, `đ`/`Đ`, `ð`, `þ`) do NOT have an `NFKD` decomposition**! When `.encode("ascii", "ignore")` runs on `"Søren"`, it deletes `ø` outright and produces `"Sren"` -> `sren_kierkegaard.md`! If The Lead assembles a custom Boardroom (as instructed in `SKILL.md` line 82 and `commands/board.md` line 44) and writes `personas/board_members/philosophy_logic/soren_kierkegaard.md`, the file does not exist!
2. **The `Dr.卢 (Lu) "Strict-Alias" Jian-Guo` Surname Erasure Bug**:
   Open `personas/strike_teams_individual/INDEX.md` to **line 41**:
   ```markdown
   | `MERC-SW-26` | **Dr.卢 (Lu) "Strict-Alias" Jian-Guo — The Undefined-Behavior & LLVM-IR Grand Surgeon** | [`./software_plans/dr_strict_alias_jian_guo_the_undefined_behavior_llvm_ir_grand_surgeon.md`](...) |
   ```
   In `01_software_kernels_and_plans_mercenaries.md` line 153, the author helpfully provided the ASCII pinyin `(Lu)` right after the Chinese character `卢`. Then `slugify_persona_name` ran `re.sub(r"\([^)]*\)", "", raw_name)` on line 74—which **deleted `(Lu)`**—and then `.encode("ascii", "ignore")` on line 80 **deleted `卢`**! So his family name `Lu` was completely erased from the filename (`dr_strict_alias_jian_guo_...`)!
3. **The Parenthetical Technical-Term & Em-Dash Title Bloat Bug**:
   In `personas/strike_teams_individual/INDEX.md`:
   - Line 87: `Dr. Magnus "O(n^2)" Lindqvist` becomes `dr_magnus_o_lindqvist_...` because `(n^2)` was inside parentheses!
   - Lines 112–114: `Marcus "271(f)-Dodge"`, `Dr. Priya ... § 271(b)/(c)`, `Baron Henrik "271(g)-Process"` lose `(f)`, `(b)/(c)`, and `(g)`!
   - And because `extract_persona_blocks` does not strip the `— <Long Title>` suffix before calling `slugify_persona_name`, every mercenary filename is 75–105 characters long (`chief_warrant_officer_roy_smoke_test_miller_the_fault_containment_harness_chafing_pyro_fuse_brutalist.md`), risking Windows `MAX_PATH` (`260` char) limits when nested inside deep workspace directories!

**Dr. Viktor Krol (`MERC-SW-01`):** Now let us move to Alistair's third surgical target: **Legacy File Contradictions (`Vector F4-V7`)**. Look at the top level of `L:\Dev\the_board\personas\`. Sitting right next to `board_members/` and `boardrooms/` are **8 legacy Markdown files**:
1. `personas/the_godfather_board.md` (`8,947 bytes`)
2. `personas/software_and_plans.md` (`4,208 bytes`)
3. `personas/hardware_and_physics.md` (`3,920 bytes`)
4. `personas/design_and_product.md` (`3,885 bytes`)
5. `personas/commercial_and_action_plans.md` (`4,292 bytes`)
6. `personas/legal_and_patents.md` (`4,460 bytes`)
7. `personas/philosophy_and_strategy.md` (`3,994 bytes`)
8. `personas/security_and_redteam.md` (`3,934 bytes`)
Plus `references/domain_playbooks.md` (`11,072 bytes`).
Alistair, walk us through the exact architectural and roster contradictions between those 8 legacy `personas/*.md` files, `references/domain_playbooks.md`, and the new `personas/boardrooms/*.md` manifests!

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** Look at Monitor 3. I built a complete diff table comparing the new `personas/boardrooms/<domain>_board.md` manifests against the legacy `personas/<domain>.md` files and `references/domain_playbooks.md`:

| Domain | New Canonical Boardroom (`personas/boardrooms/*.md`) | Legacy File (`personas/*.md`) | Exact Contradiction Found |
| :--- | :--- | :--- | :--- |
| **Software & Plans** | `personas/boardrooms/software_and_plans_board.md` (lines 12–17):<br>1. `dennis_ritchie.md`<br>2. `edsger_w_dijkstra.md`<br>3. `seymour_cray.md`<br>4. `margaret_hamilton.md`<br>5. **`linus_torvalds.md`**<br>6. `adm_hyman_g_rickover.md` | `personas/software_and_plans.md` (lines 24–29):<br>1. Dennis Ritchie<br>2. Edsger W. Dijkstra<br>3. Seymour Cray<br>4. Margaret Hamilton<br>5. **The Self-Aware Ghost of Steve Jobs**<br>6. Adm. Hyman G. Rickover | **Seat 5 Contradiction** (`Linus Torvalds` vs. `Ghost of Steve Jobs`). Worse, lines 13–17 put real historical humans (`Turing`, `Hamilton`, `von Neumann`, `Cray`, `Dijkstra`, `Ritchie`, `Shannon`, `Popper`, `Hopper`) inside the **5 Strike Teams**, violating `SKILL.md` Section `[02]`! |
| **Hardware & Physics** | `personas/boardrooms/hardware_and_physics_board.md` (lines 12–17):<br>1. `clarence_kelly_johnson.md`<br>2. `richard_feynman.md`<br>3. `nikola_tesla.md`<br>4. `rudolf_e_kalman.md`<br>5. **`jim_williams.md`**<br>6. `adm_hyman_g_rickover.md` | `personas/hardware_and_physics.md` (lines 21–26):<br>1. Clarence "Kelly" Johnson<br>2. Richard Feynman<br>3. Nikola Tesla<br>4. Rudolf E. Kálmán<br>5. **Albert Einstein**<br>6. Adm. Hyman G. Rickover | **Seat 5 Contradiction** (`Jim Williams` vs. `Albert Einstein`). Also puts `Tesla`, `Kálmán`, `Bode`, `Einstein`, `Feynman`, `Shannon`, `Nyquist`, `Kelly Johnson`, `Rickover` inside the 5 Strike Teams (lines 11–15)! |
| **Design & Product** | `personas/boardrooms/design_and_product_board.md` (lines 12–17):<br>1. `the_self_aware_ghost_of_steve_jobs.md`<br>2. `dieter_rams.md`<br>3. `sir_jony_ive.md`<br>4. `bret_victor.md`<br>5. `don_norman.md`<br>6. **`lee_clow.md`** | `personas/design_and_product.md` (lines 21–26):<br>1. Ghost of Steve Jobs<br>2. Dieter Rams<br>3. Jony Ive<br>4. Bret Victor<br>5. Don Norman<br>6. **Andy Hertzfeld** | **Seat 6 Contradiction** (`Lee Clow` vs. `Andy Hertzfeld`). Also puts `Jobs`, `Land`, `Rams`, `Ive`, `Victor`, `Hertzfeld`, `Kare`, `Norman`, `Clow`, `Ogilvy` inside the 5 Strike Teams (lines 11–15)! |
| **Commercial & DoD** | `personas/boardrooms/commercial_and_dod_board.md` (lines 12–17):<br>1. `andrew_grove.md`<br>2. `charlie_munger.md`<br>3. `col_john_boyd.md`<br>4. `adm_hyman_g_rickover.md`<br>5. `the_self_aware_ghost_of_steve_jobs.md`<br>6. **`claude_c_hopkins.md`** | `personas/commercial_and_action_plans.md` (lines 21–26):<br>1. Andrew Grove<br>2. Charlie Munger<br>3. Adm. Hyman G. Rickover<br>4. Ghost of Steve Jobs<br>5. Col. John Boyd<br>6. **Clarence "Kelly" Johnson** | **Seat 6 Contradiction** (`Claude C. Hopkins` vs. `Clarence "Kelly" Johnson`). Also mixes real humans into the 5 Strike Teams (lines 11–15)! |
| **Legal & Patents** | `personas/boardrooms/legal_and_patents_board.md` (lines 12–17):<br>1. `judge_giles_sutherland_rich.md`<br>2. `judge_learned_hand.md`<br>3. `albert_einstein.md`<br>4. `justice_oliver_wendell_holmes_jr.md`<br>5. **`justice_antonin_scalia.md`**<br>6. **`judge_pauline_newman.md`** | `personas/legal_and_patents.md` (lines 21–26):<br>1. Judge Giles Sutherland Rich<br>2. Judge Learned Hand<br>3. Albert Einstein<br>4. Justice Oliver Wendell Holmes Jr.<br>5. **Hon. Judge Miller (Ret.)** *(fictional)*<br>6. **Victoria Sterling** *(fictional)* | **Seats 5 & 6 Contradiction**: Legacy file puts *fictional* characters (`Hon. Judge Miller` and `Victoria Sterling`) on The Board instead of `Justice Antonin Scalia` and `Judge Pauline Newman`, directly violating the "6 Real Historical Humans on The Board" law in `SKILL.md` line 59! |
| **Philosophy & Strategy** | `personas/boardrooms/philosophy_and_strategy_board.md` (lines 12–17):<br>1. `epictetus.md`<br>2. `socrates.md`<br>3. `ludwig_wittgenstein.md`<br>4. `karl_popper.md`<br>5. `sun_tzu.md`<br>6. **`niccolo_machiavelli.md`** | `personas/philosophy_and_strategy.md` (lines 21–26):<br>1. Epictetus<br>2. Socrates<br>3. Ludwig Wittgenstein<br>4. Karl Popper<br>5. Sun Tzu<br>6. **Charlie Munger** | **Seat 6 Contradiction** (`Niccolò Machiavelli` vs. `Charlie Munger`). |
| **All 5 Domains in `references/domain_playbooks.md`** | `SKILL.md` Section `[02]` (lines 48–64): Two-Tier split (`$100M` Mercenaries in `personas/strike_teams/` + 6 Real Humans in `personas/board_members/`) | `references/domain_playbooks.md` (lines 1–91): Unlinked in root `SKILL.md`, linked in `skills/the-board/SKILL.md` lines 100 & 139 | Uses 100% v1 generic fictional 1-liners (`Viktor K.`, `Sarah L.`) and generic unnamed Board roles (`Arbiter 2: Principal Security & Memory-Safety Engineer`). |

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** Think about what happens in an LLM's context window when those 8 legacy `personas/*.md` files and `references/domain_playbooks.md` sit in the repository! Even if root `SKILL.md` doesn't link to them, `personas/the_godfather_board.md` line 71 literally says:
> `If a user's task involves a specialized niche not covered in personas/*.md, The Lead must dynamically construct each Firm's 3-Persona Triad...`
When The Lead globs `personas/*.md`, it finds the 8 legacy files instead of `personas/boardrooms/*.md` and `personas/strike_teams/*.md`!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Wait—let's check the three plugin manifests (`plugin.json`, `.claude-plugin/plugin.json`, and `gemini-extension.json`) and the two Python automation scripts (`scripts/init_board_workspace.py` and `scripts/verify_convergence.py`) before we lock our ledger!
First, look at `L:\Dev\the_board\gemini-extension.json` (`lines 1–5`):
```json
{
  "name": "the-board",
  "version": "1.0.0",
  "description": "Multi-Agent Persona-Conditioned Red-Team, Blue-Team, and Board-of-Directors Iterative Convergence Engine (v1 -> vN until White Flag)."
}
```
What happens when a user installs this repo as a Gemini CLI extension (`gemini extensions install ...`)?
In Gemini CLI's extension loader specification, `gemini-extension.json` looks for `GEMINI.md` by default unless `"contextFileName": "SKILL.md"` is explicitly specified in `gemini-extension.json`! Because there is no `GEMINI.md` in `L:\Dev\the_board` and `"contextFileName": "SKILL.md"` is missing from `gemini-extension.json`, Gemini CLI loads the extension with **zero context instructions**!
And in `.claude-plugin/plugin.json` (`lines 1–8`) and `plugin.json` (`lines 1–6`), neither manifest includes `"commands": ["./commands/board.md"]` or `"skills": ["./SKILL.md"]` (or a synchronized `skills/the-board/`), nor do their `description` strings mention `plan` mode (`Pre-Code Plan Siege`)!

**Dr. Viktor Krol (`MERC-SW-01`):** And look at `L:\Dev\the_board\scripts\init_board_workspace.py`—this is a deterministic CLI crash (`Vector F4-V9`) that I just verified on lines 206–212:
```python
    parser.add_argument(
        "--mode",
        type=str,
        choices=["red", "blue", "purple"],
        default="red",
        help="Operating mode: red (Red-Team), blue (Blue-Team Tournament), or purple (Hybrid)",
    )
```
Read `L:\Dev\the_board\SKILL.md` lines 32, 69, and 80:
- Line 32: `mode (plan | red | blue | purple)`
- Line 69: `- plan (Pre-Code / Pre-Execution Plan Siege): Run The Board on an Implementation Plan, Architecture Spec, or Action Plan before executing or writing production code.`
- Line 80: `2. Run scripts/init_board_workspace.py (or create .board/v1/ and .board/CONVERGENCE_TRACKER.md).`
If The Lead follows `SKILL.md` Phase 0 Step 2 in `plan` mode and executes:
`python scripts/init_board_workspace.py --mode plan`
`argparse` throws a fatal **`SystemExit: 2` (`error: argument --mode: invalid choice: 'plan' (choose from 'red', 'blue', 'purple')`)** because `"plan"` was never added to `choices=["red", "blue", "purple"]` on line 209 of `scripts/init_board_workspace.py`!
And look at `L:\Dev\the_board\scripts\verify_convergence.py` lines 50–53 and 80–85:
```python
CRITICAL_HIGH_SURVIVING_RE = re.compile(
    r"\|\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL|HIGH)`?\s*\|",
    re.IGNORECASE,
)
```
In `references/effort_and_white_flag.md` line 48 (Safeguard 3: Earned White-Flag Verification), the law states:
> `3. Zero CRITICAL, HIGH, or MEDIUM vectors remaining in the Firm's ledger.`
And in `references/prompt_templates.md` line 37, the Surviving Vector Ledger columns are:
> `| Vector ID | Severity (CRITICAL/HIGH/MEDIUM) | Exact Location | Exploit / Failure Mechanism | Required Root-Cause Fix |`
Yet `verify_convergence.py` line 50 only checks `(CRITICAL|HIGH)` and completely ignores `MEDIUM`! Even worse, if a Firm writes `| F4-V1 | **CRITICAL** |` (with Markdown bold asterisks around `CRITICAL`), `r"\|\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL|HIGH)`?\s*\|"` **fails to match** because it only allows optional backticks `` `? `` and not asterisks `\**`!

**Dr. Alistair "Zero-Cost" MacLeod (`MERC-SW-26`):** Let's also check `scripts/verify_convergence.py` line 164:
```python
    for idx in range(1, 6):
```
And line 181:
```python
    converged = (missing_firms == 0) and (white_flag_count == 5) and board_exists
```
Look at `SKILL.md` line 40 and line 81:
- Line 40: `Call invoke_subagent (TypeName: "self") K times (K=5 default; K=1..2 for strike) in one turn`
- Line 81: `Partition the target into 5 strictly orthogonal pillars (Pillars I–V) (or 1–2 pillars for quick strike runs).`
If a user runs `/board red strike` with `1–2` Strike Teams (`firm1_*.md`, `firm2_*.md`) as explicitly permitted by `SKILL.md` lines 40 and 81, `verify_convergence.py` hardcodes `range(1, 6)` and `white_flag_count == 5`, so it unconditionally fails and reports `Firm 3..5 ❌ MISSING` on every 1–2 team `strike` run!

**Freja "Hermetic" Lindström (`MERC-SW-32`):** Let's review our internal pushback log and our surviving vector ledger to make sure every single citation is bit-for-bit surgical before we seal the tape:
- **False Alarms Tested & Shot Down by Viktor (`MERC-SW-01`)**:
  1. **Rejected Hypothesis 1**: Suspected broken links inside `personas/boardrooms/*.md` (`the_godfather_board.md`, `software_and_plans_board.md`, `hardware_and_physics_board.md`, `design_and_product_board.md`, `cybersecurity_board.md`, `legal_and_patents_board.md`, `philosophy_and_strategy_board.md`, `commercial_and_dod_board.md`, and `personas/boardrooms/README.md`) for names with quotes, titles, or diacritics (`clarence_kelly_johnson.md`, `sir_jony_ive.md`, `rudolf_e_kalman.md`, `adm_hyman_g_rickover.md`, `the_self_aware_ghost_of_steve_jobs.md`). **Falsified**: All 48 links in `personas/boardrooms/*.md` resolve 100% cleanly on disk.
  2. **Rejected Hypothesis 2**: Suspected dead relative Markdown links in root `SKILL.md` (lines 53–119) and `README.md` (lines 181–186) when evaluated in-place at the repo root. **Falsified**: All 22 relative links in root `SKILL.md` and `README.md` resolve cleanly when evaluated at the repo root (they only break *after* running `install.ps1` / `install.sh` because the installers omit `personas/`).
  3. **Rejected Hypothesis 3**: Suspected JSON syntax/schema incompatibility between `"author": "Donald Everett Hinton III"` in `plugin.json` and `"author": {"name": "Donald Everett Hinton III"}` in `.claude-plugin/plugin.json`. **Falsified**: Both are valid per their respective runtime conventions.

**Dr. Viktor Krol (`MERC-SW-01`):** And our **9 Surviving Vectors (`F4-V1` through `F4-V9`)** are 100% verified against the disk state of `L:\Dev\the_board`, with exact line numbers, byte counts, and root-cause fixes. Compile the ledger and seal the recording.

**[00:38:42] [AUDIO RECORDING SEALED // TRANSMITTING VERBATIM PAYLOAD TO THE BOARDROOM]**

---

## PART 2: SURVIVING VECTOR LEDGER (`PILLAR IV — FIRM 4`)

| Vector ID | Severity | Exact Target File & Line Numbers | Exploit / Failure Mechanism | Required Root-Cause Fix |
| :--- | :---: | :--- | :--- | :--- |
| **`F4-V1`** | **`CRITICAL`** | - `L:\Dev\the_board\skills\the-board\SKILL.md` (`lines 1–143`, `15,333B` vs. root `SKILL.md` `lines 1–119`, `13,471B`)<br>- `L:\Dev\the_board\skills\the-board\personas\` (`0 files` vs. root `personas\` `712 files`)<br>- `L:\Dev\the_board\skills\the-board\references\prompt_templates.md` (`line 9`, `9,046B` vs. root `10,041B`)<br>- `L:\Dev\the_board\skills\the-board\references\effort_and_white_flag.md` (`5,818B` vs. root `4,475B`)<br>- `L:\Dev\the_board\skills\the-board\references\persona_mask_theory.md` (`7,779B` vs. root `4,573B`) | **Root-vs-Subfolder Skill Split-Brain & Hardcoded `L:` Drive URI**:<br>1. `skills/the-board/SKILL.md` is an un-updated v1 file missing `plan` mode, missing the ASCII boot banner & interactive intake, and missing the Two-Tier Persona Architecture (`personas/board_members/`, `personas/boardrooms/`, `personas/strike_teams/`).<br>2. `skills/the-board/personas/` is completely empty (`0` files).<br>3. `skills/the-board/references/prompt_templates.md:9` contains a hardcoded local machine URI (`file:///L:/Dev/the_board/skills/the-board/references/domain_playbooks.md`).<br>4. Any plugin/skill scanner that loads `skills/the-board/SKILL.md` gets a broken v1 skill. | Synchronize `skills/the-board/` 100% with root (`SKILL.md`, `references/*.md`, `scripts/*.py`, `commands/board.md`, and `personas/`), or eliminate duplicate drift by having `split_personas_to_files.py` / a sync step mirror root `SKILL.md`, `references/`, `scripts/`, and `personas/` into `skills/the-board/` (and remove the hardcoded `file:///L:/...` URI on line 9 of `prompt_templates.md`). |
| **`F4-V2`** | **`CRITICAL`** | - `L:\Dev\the_board\scripts\install.ps1` (`lines 21–28`)<br>- `L:\Dev\the_board\scripts\install.sh` (`lines 17–21`)<br>- `L:\Dev\the_board\skills\the-board\scripts\install.ps1` (`lines 21–28`)<br>- `L:\Dev\the_board\skills\the-board\scripts\install.sh` (`lines 17–21`) | **Installers Omit `personas/` and `commands/`, Breaking All Persona Links Post-Install**:<br>`install.ps1` (`foreach ($Sub in @("references", "examples", "scripts"))`) and `install.sh` (`mkdir -p "${dest_dir}/references" "${dest_dir}/examples" "${dest_dir}/scripts"`) copy `SKILL.md` to `~/.gemini/config/skills/the-board`, `~/.claude/skills/the-board`, and `.agents/skills/the-board`, but **never copy `personas/` or `commands/`**. Every link in installed `SKILL.md` to `./personas/boardrooms/`, `./personas/board_members/`, and `./personas/strike_teams/` (`lines 53, 60, 62, 82, 85, 89, 113–115`) fails with `FileNotFoundError`. | Update `install.ps1` (`line 21`) and `install.sh` (`lines 17–21`) to include `"personas"` and `"commands"` in the copied subdirectories list (`@("personas", "references", "examples", "scripts", "commands")`). |
| **`F4-V3`** | **`CRITICAL`** | - `L:\Dev\the_board\scripts\split_personas_to_files.py` (`lines 12, 97–140, 207`)<br>- `L:\Dev\the_board\personas\strike_teams_individual\INDEX.md` (`lines 10, 16, 22, 28, 34, 40, 46, 97, 103, 109, 115, 121, 127, 133, 184, 190, 196, 202, 208, 214, 220, 231, 237, 243, 249, 255, 261, 267, 278, 284, 290, 296, 302, 308, 314`) | **Splitter Regex Extracts 35 Bogus "Category/Division" Stub `.md` Files with Duplicate IDs + Docstring Path Mismatch**:<br>1. In `split_personas_to_files.py:109–114`, `re.search(r"(?:REAL|MERC)-[A-Z0-9\-]+", heading_text)` matches parenthetical ID ranges inside section headers like `## Category I: ... (MERC-SW-01 .. MERC-SW-05)` and `## DIVISION I: ... (MERC-PHIL-01 – MERC-PHIL-05)`.<br>2. This generates **35 bogus 7-line `.md` files** (`category_i_*.md`, `division_i_*.md`) and **35 duplicate primary IDs** in `personas/strike_teams_individual/INDEX.md` (`280` rows instead of `245`).<br>3. Line 12 docstring says output is `personas/strike_teams/<category>/` while line 207 writes to `personas/strike_teams_individual/`, which is never linked in `SKILL.md`. | 1. Fix `extract_persona_blocks` (`lines 108–126`) in `scripts/split_personas_to_files.py` to require the heading to *start* with `(?:REAL|MERC)-[A-Z]+-\d+` (or `#?\d+`) and explicitly exclude headings starting with `Category\s+[IVX0-9]+` or `DIVISION\s+[IVX0-9]+`.<br>2. Update line 12 docstring and link `personas/strike_teams_individual/INDEX.md` in `SKILL.md` Section `[05]`. |
| **`F4-V4`** | **`HIGH`** | - `L:\Dev\the_board\scripts\split_personas_to_files.py` (`lines 168–194`)<br>- `L:\Dev\the_board\personas\board_members\` (`221 files on disk` vs. `215 in INDEX.md` — `6 orphans`)<br>- `L:\Dev\the_board\personas\strike_teams_individual\` (`464 files on disk` vs. `280 in INDEX.md` — `184 orphans`) | **190 Unindexed Orphan `.md` Files Polluting `personas/board_members/` and `personas/strike_teams_individual/`**:<br>`split_collection()` creates category directories with `exist_ok=True` and writes new `.md` files without removing stale `.md` files from prior versions. This left **6 duplicate historical human files** in `personas/board_members/` (e.g., `albert_einstein_19021909_bern_patent_examiner_class_iii.md` alongside `albert_einstein.md`, `talleyrand.md` alongside `charles_maurice_de_talleyrand_perigord.md`) and **184 orphan mercenary files** in `personas/strike_teams_individual/` (including `ideon_intel_inside_mercer.md`, `dr_viktor_krol.md`, `freja_hermetic_lindstrom.md`, etc.) with colliding IDs. | In `scripts/split_personas_to_files.py` (`split_collection`, `line 169`), purge existing `*.md` files in `cat_dir` before writing the newly split persona files, and re-run `python scripts/split_personas_to_files.py` so disk contents match `INDEX.md` 1-to-1 (`215` Board Member files and `245` Strike-Team Mercenary files). |
| **`F4-V5`** | **`HIGH`** | - `L:\Dev\the_board\scripts\split_personas_to_files.py` (`lines 67–85`, `135–138`)<br>- `L:\Dev\the_board\personas\board_members\INDEX.md` (`line 162`: `sren_kierkegaard.md`)<br>- `L:\Dev\the_board\personas\strike_teams_individual\INDEX.md` (`line 41`: `dr_strict_alias_jian_guo...`; `line 87`: `dr_magnus_o_lindqvist...`) | **Unicode Stroke-Letter Deletion (`sren_kierkegaard.md`) & Parenthetical Surname/Math Erasure in `slugify_persona_name`**:<br>1. `unicodedata.normalize("NFKD", "Søren")` does not decompose stroked/ligature letters (`ø`, `æ`, `ł`, `ß`, `đ`), so `.encode("ascii", "ignore")` deletes `ø`, turning **Søren Kierkegaard** into `sren_kierkegaard.md`.<br>2. `re.sub(r"\([^)]*\)", "", raw_name)` strips `(Lu)` from `Dr.卢 (Lu) "Strict-Alias" Jian-Guo` before ASCII encoding strips `卢`, erasing his surname `lu` (`dr_strict_alias_jian_guo_...`), and strips `(n^2)` from `O(n^2)` and `(f)`/`(g)` from `271(f)`/`271(g)`.<br>3. `MERC` headings retain `— <Role Description>` in the filename slug, creating 95+ char filenames. | In `scripts/split_personas_to_files.py` (`slugify_persona_name`, `lines 67–85`):<br>1. Map non-NFKD Latin characters (`ø->o`, `æ->ae`, `ł->l`, `ß->ss`, `đ->d`, `ð->d`, `þ->th`) before ASCII encoding so Søren Kierkegaard becomes `soren_kierkegaard.md`.<br>2. Strip the `— <Role Suffix>` (`\s*[—–-]\s+.*$`) from the slug source while preserving short parenthetical transliterations/clauses like `(Lu)` or `(f)` when preceded by CJK or statute numbers. |
| **`F4-V6`** | **`HIGH`** | - `L:\Dev\the_board\commands\board.md` (`line 42` & `line 55`) | **Broken Filename `ghost_of_steve_jobs.md` & Broken Post-Install Relative Link `../SKILL.md` in `commands/board.md`**:<br>1. Line 42 lists `ghost_of_steve_jobs.md` instead of the actual filename `the_self_aware_ghost_of_steve_jobs.md` (`personas/board_members/design_product/the_self_aware_ghost_of_steve_jobs.md`).<br>2. Line 55 links to `[SKILL.md](../SKILL.md)`, which resolves in-repo but breaks when `install.ps1`/`install.sh` copies `board.md` to `~/.claude/commands/board.md` (where `../SKILL.md` resolves to non-existent `~/.claude/SKILL.md` instead of `~/.claude/skills/the-board/SKILL.md`). | 1. In `commands/board.md:42`, replace `ghost_of_steve_jobs.md` with `the_self_aware_ghost_of_steve_jobs.md`.<br>2. In `commands/board.md:55`, reference `SKILL.md` in the `the-board` skill directory (`~/.claude/skills/the-board/SKILL.md` or repo `../SKILL.md`). |
| **`F4-V7`** | **`HIGH`** | - `L:\Dev\the_board\personas\software_and_plans.md` (`lines 13–29`)<br>- `L:\Dev\the_board\personas\hardware_and_physics.md` (`lines 11–26`)<br>- `L:\Dev\the_board\personas\design_and_product.md` (`lines 11–26`)<br>- `L:\Dev\the_board\personas\commercial_and_action_plans.md` (`lines 11–26`)<br>- `L:\Dev\the_board\personas\legal_and_patents.md` (`lines 11–26`)<br>- `L:\Dev\the_board\personas\philosophy_and_strategy.md` (`lines 11–26`)<br>- `L:\Dev\the_board\personas\security_and_redteam.md` (`lines 11–26`)<br>- `L:\Dev\the_board\personas\the_godfather_board.md` (`lines 1–74`)<br>- `L:\Dev\the_board\references\domain_playbooks.md` (`lines 1–91`) | **Legacy `personas/*.md` & `references/domain_playbooks.md` Contradict `personas/boardrooms/*.md` Rosters & Two-Tier Architecture**:<br>1. Six of the legacy `personas/<domain>.md` files contradict the 6-member rosters in `personas/boardrooms/<domain>_board.md` (e.g., `software_and_plans.md` seats Steve Jobs instead of Linus Torvalds; `hardware_and_physics.md` seats Einstein instead of Jim Williams; `design_and_product.md` seats Andy Hertzfeld instead of Lee Clow; `commercial_and_action_plans.md` seats Kelly Johnson instead of Claude Hopkins; `legal_and_patents.md` seats fictional Judge Miller & Victoria Sterling instead of Scalia & Newman; `philosophy_and_strategy.md` seats Charlie Munger instead of Machiavelli).<br>2. Legacy `personas/*.md` files put Real Historical Humans inside the 5 Strike Teams, and `references/domain_playbooks.md` uses 100% generic fictional arbiters on The Board—both contradicting `SKILL.md` Section `[02]`. | Either remove/archive the 8 legacy top-level `personas/*.md` files and update `references/domain_playbooks.md`, OR update all 8 `personas/*.md` files and `references/domain_playbooks.md` so their 6-member Board rosters match `personas/boardrooms/*.md` 1-to-1 and their 5 Strike Teams reference the `$100M` mercenaries in `personas/strike_teams/*.md`. |
| **`F4-V8`** | **`HIGH`** | - `L:\Dev\the_board\gemini-extension.json` (`lines 1–5`)<br>- `L:\Dev\the_board\plugin.json` (`lines 1–6`)<br>- `L:\Dev\the_board\.claude-plugin\plugin.json` (`lines 1–8`) | **Incomplete Cross-Runtime Plugin Manifests (`gemini-extension.json`, `plugin.json`, `.claude-plugin/plugin.json`)**:<br>1. `gemini-extension.json` omits `"contextFileName": "SKILL.md"`, causing Gemini CLI to look for a non-existent `GEMINI.md` and load zero instructions.<br>2. `plugin.json` and `.claude-plugin/plugin.json` omit `"commands": ["./commands/board.md"]`, `"skills"`, and `"license": "MIT"`, and their descriptions omit `plan` mode (`Pre-Code Plan Siege`). | 1. Add `"contextFileName": "SKILL.md"` to `gemini-extension.json`.<br>2. Add `"license": "MIT"`, updated `description` (including `Pre-Code Plan`), and explicit skill/command pointers to `plugin.json` and `.claude-plugin/plugin.json`. |
| **`F4-V9`** | **`MEDIUM`** | - `L:\Dev\the_board\scripts\init_board_workspace.py` (`line 209`)<br>- `L:\Dev\the_board\scripts\verify_convergence.py` (`lines 50–53, 164, 181`) | **Automation Script CLI Crash on `--mode plan` & Regex/Team-Count Mismatch in `verify_convergence.py`**:<br>1. `init_board_workspace.py:209` restricts `--mode` to `choices=["red", "blue", "purple"]`, crashing with `SystemExit: 2` when invoked with `--mode plan` (the primary mode in `SKILL.md:32, 69`).<br>2. `verify_convergence.py:50` ignores `MEDIUM` surviving vectors (`CRITICAL|HIGH` only) and fails to match bolded severities (`**CRITICAL**`), violating `references/effort_and_white_flag.md:48`.<br>3. `verify_convergence.py:164, 181` hardcodes 5 firms (`range(1, 6)`), failing on `1–2` team `strike` runs allowed by `SKILL.md:40, 81`. | 1. Add `"plan"` to `choices=["plan", "red", "blue", "purple"]` in `scripts/init_board_workspace.py:209`.<br>2. Update `CRITICAL_HIGH_SURVIVING_RE` in `scripts/verify_convergence.py:50` to match `(CRITICAL|HIGH|MEDIUM)` with optional `\*` or `` ` `` wrappers, and support dynamic `--expected-firms` (or auto-detect 1..5 firms for `strike` mode). |
