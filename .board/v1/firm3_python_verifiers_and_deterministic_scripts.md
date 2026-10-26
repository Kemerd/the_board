# 🏛️⚔️ FIRM 3 WAR-ROOM RECORDING (WAVE `v1`) — DETERMINISTIC TOOLING, VERIFIER SOUNDNESS & CROSS-PLATFORM INSTALLERS

```diff
@@ ╔══════════════════════════════════════════════════════════════════════════════╗ @@
!  ║  [AUDIO RECORDING ACTIVE // BUNKER-03 SANITIZER LAB // ZURICH SUB-LEVEL 4]   ║
-  ║  FIRM 3: DETERMINISTIC PYTHON VERIFIERS, REGEX SOUNDNESS & INSTALLER AUDIT   ║
+  ║  ASSIGNED ORTHOGONAL PILLAR: PILLAR III (SCRIPTS & AUTOMATION TOOLING)       ║
!  ║  BOUNTY RETAINER: $100,000,000 + 20% KILL-FEE BONUS (WAVE v1)                ║
@@ ╚══════════════════════════════════════════════════════════════════════════════╝ @@
```

- **Target Artifacts Under Forensic Vivisection**:
  1. [`L:\Dev\the_board\scripts\verify_convergence.py`](file:///L:/Dev/the_board/scripts/verify_convergence.py) (`223` lines)
  2. [`L:\Dev\the_board\scripts\init_board_workspace.py`](file:///L:/Dev/the_board/scripts/init_board_workspace.py) (`252` lines)
  3. [`L:\Dev\the_board\scripts\split_personas_to_files.py`](file:///L:/Dev/the_board/scripts/split_personas_to_files.py) (`227` lines)
  4. [`L:\Dev\the_board\scripts\install.ps1`](file:///L:/Dev/the_board/scripts/install.ps1) (`50` lines)
  5. [`L:\Dev\the_board\scripts\install.sh`](file:///L:/Dev/the_board/scripts/install.sh) (`38` lines)
- **Triad Roster**:
  - **Mask 1 (`The $100M Principal`)**: **Cassian "Schema-Lock" Vane (`MERC-SEC-23`)** — Regex-Bypass, Formal Verifier Soundness & False-Convergence Executioner.
  - **Mask 2 (`The Literal Purist`)**: **General Cassius "Zero-Trust" Sterling (`MERC-SW-16`)** — Defensive-Programming Paranoid, Line-by-Line Ground-Truth Auditor & False-Claim Terminator.
  - **Mask 3 (`The Lateral Breaker`)**: **Renzo "Unicode-Hell" Takahashi-Cruz (`MERC-SEC-25`)** — Cross-Platform Installer, NFKD Canonicalization, Slug-Collision & Filesystem Saboteur.

---

## PART I: BUNKER-03 VERBATIM WAR-ROOM TRANSCRIPT (`[AUDIO RECORDING ACTIVE // BUNKER-03 SANITIZER LAB]`)

**Cassian "Schema-Lock" Vane**: `[00:00:04]` Lock the blast doors and kill the external telemetry feed. We have 790 total lines of Python, PowerShell, and Bash sitting on the table across five scripts: `verify_convergence.py`, `init_board_workspace.py`, `split_personas_to_files.py`, `install.ps1`, and `install.sh`. These five files are the deterministic spine of `the-board`. If `verify_convergence.py` can be spoofed into returning exit code `0` (`CONVERGED`), the entire multi-wave adversarial loop short-circuits on Wave `v1` while catastrophic vulnerabilities are still bleeding on the floor. I want the $20M kill-fee bonus wired before sunrise. Let's start by tearing apart Windows console encoding in `verify_convergence.py` and `init_board_workspace.py`—Look at line 196 of `verify_convergence.py`: `print(f"🏛️⚔️  [THE BOARD] Wave Audit: {wave_dir.resolve()}")`. On a default Windows `cp1252` console, printing surrogate-pair emojis like `🏛️` and `🏳️` without UTF-8 stream wrapping throws `UnicodeEncodeError: 'charmap' codec can't encode characters` and crashes the verifier before it prints a single row! And if you run it headless under `pythonw.exe` where `sys.stdout` is `None`, calling `.reconfigure()` crashes with `AttributeError: 'NoneType' object has no attribute 'reconfigure'`!

**General Cassius "Zero-Trust" Sterling**: `[00:00:51]` Put the champagne back on ice, Cassian. You skipped lines 27 through 38 of `verify_convergence.py`, lines 27 through 38 of `init_board_workspace.py`, and lines 29 through 40 of `split_personas_to_files.py`. Read the actual file before you hallucinate a crash vector. Every single one of the three Python scripts defines `configure_utf8_console()` and invokes it as the very first statement in `main()` (`verify_convergence.py:127`, `init_board_workspace.py:188`, `split_personas_to_files.py:200`). Let me read `verify_convergence.py` lines 27–38 verbatim onto the tape:

```python
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows consoles."""
    if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    if sys.stderr is not None and hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
```

**General Cassius "Zero-Trust" Sterling**: `[00:01:28]` Look at line 29: `if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):`. Look at line 31: `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` wrapped in a `try / except Exception: pass`. And look at file ingestion at `verify_convergence.py` line 71 and line 175: `file_path.read_text(encoding="utf-8", errors="replace")`. Even if a Strike Team writes malformed `0xFF 0xFE` byte sequences into a Markdown transcript, `read_text` replaces them with `U+FFFD` without throwing `UnicodeDecodeError`, and `stdout` prints UTF-8 with `errors="replace"` and explicit `None` guards. Your Windows `cp1252` crash and `pythonw` `NoneType` theory is dead on arrival. Strike it from the ledger.

**Cassian "Schema-Lock" Vane**: `[00:02:02]` Fair kill on the console wrapper, Cassius. The author actually guarded `sys.stdout` and `read_text`. Now watch what happens when we move seven lines down in `verify_convergence.py` to lines 45 through 53. This is where the verifier's brain lives—and it is a target-rich disaster. Read lines 45–53 of `verify_convergence.py`:

```python
DIALOGUE_SPEAKER_RE = re.compile(r"^\s*(?:\*\*|\*|-)?\s*\**[A-Z][A-Za-z0-9\.\-\s\(\)]{2,45}\**\s*:\s+.+", re.MULTILINE)
WHITE_FLAG_RE = re.compile(
    r"(WHITE[\s\-]+FLAG\s+RAISED|FORMAL\s+WHITE[\s\-]+FLAG|UNCONDITIONAL\s+SURRENDER|SURVIVING\s+(?:NON-SUICIDAL\s+)?VECTORS\s*:\**\s*0\b|0\s+SURVIVING\s+VECTORS)",
    re.IGNORECASE,
)
CRITICAL_HIGH_SURVIVING_RE = re.compile(
    r"\|\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL|HIGH)`?\s*\|",
    re.IGNORECASE,
)
```

**Cassian "Schema-Lock" Vane**: `[00:02:44]` Let's dissect `WHITE_FLAG_RE` at lines 46–49 and how `audit_single_firm_file()` uses it at lines 82–84:

```python
    # Determine if a formal White Flag was raised and no open CRITICAL/HIGH vectors remain
    has_white_flag_phrase = bool(WHITE_FLAG_RE.search(text))
    is_white_flag = has_white_flag_phrase and (active_vectors == 0)
```

**Cassian "Schema-Lock" Vane**: `[00:03:09]` Do you see what `WHITE_FLAG_RE.search(text)` does? It performs an **unanchored, context-free, negation-blind substring search** across the entire Markdown file! Let me give you three ways this blows up in production during Wave `v1`:
1. **Negation Spoofing**: Suppose Firm 1 writes in their conclusion: `"STATUS: NO WHITE FLAG RAISED. We reject unconditional surrender—there are NOT 0 surviving vectors."` What does `WHITE_FLAG_RE.search(text)` return? It matches `"WHITE FLAG RAISED"`, `"UNCONDITIONAL SURRENDER"`, and `"0 surviving vectors"` right inside the negated sentence and returns `True`!
2. **Prompt / Rule Quote Spoofing**: Every Strike Team is instructed by `SKILL.md` line 90: `A Firm may output [STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS] only after testing and falsifying at least 3 new candidate Nth-order vectors in dialogue.` When a mercenary in the transcript quotes the rule—for instance, `"Cassius: Remember the briefing law: we cannot declare WHITE FLAG RAISED or claim 0 SURVIVING VECTORS while the parser is broken"`—`WHITE_FLAG_RE.search(text)` matches the dialogue quote and sets `has_white_flag_phrase = True`!
3. **Combined with a non-matching table format, it triggers a False White Flag (`is_white_flag = True`) on an active attack transcript**: Look at line 84: `is_white_flag = has_white_flag_phrase and (active_vectors == 0)`. If a Firm quotes `"WHITE FLAG RAISED"` anywhere in dialogue and either (a) has only `MEDIUM` vectors, or (b) puts **bold** formatting around its vector IDs (`| **F1-V1** | **CRITICAL** |`), or (c) puts the Vector Title column before the Severity column (`| F1-V1 | Regex Bypass | CRITICAL |`), then `active_vectors` is `0`, `has_white_flag_phrase` is `True`, and `verify_convergence.py` certifies a hostile Red-Team report as `🏳️ WHITE FLAG`!

**General Cassius "Zero-Trust" Sterling**: `[00:04:18]` Hold on—let me verify whether `audit_single_firm_file()` or `main()` has any secondary gate that would catch that or block convergence. Let me trace `verify_convergence.py` from line 56 to line 191. In `audit_single_firm_file(file_path: Path, min_lines: int)` (lines 56–94):
- Line 73: `line_count = len(lines)`
- Line 76–77: `dialogue_matches = DIALOGUE_SPEAKER_RE.findall(text); dialogue_count = len(dialogue_matches)`
- Line 80: `active_vectors = len(CRITICAL_HIGH_SURVIVING_RE.findall(text))`
- Line 83: `has_white_flag_phrase = bool(WHITE_FLAG_RE.search(text))`
- Line 84: `is_white_flag = has_white_flag_phrase and (active_vectors == 0)`
- Line 93: `"meets_length": line_count >= min_lines`

**General Cassius "Zero-Trust" Sterling**: `[00:05:03]` Wait a second. Look at line 93, and now look at lines 164 through 182 in `main()`:

```python
    for idx in range(1, 6):
        f_path = firm_map.get(idx)
        res = audit_single_firm_file(f_path, args.min_lines)
        firm_results[idx] = res
        if not res["exists"]:
            missing_firms += 1
        elif res["white_flag"]:
            white_flag_count += 1

    board_exists = len(board_files) > 0
    board_lines = (
        len(board_files[0].read_text(encoding="utf-8", errors="replace").splitlines())
        if board_exists
        else 0
    )

    # Convergence requires all 5 firms present, 5/5 White Flags, and a Board report
    converged = (missing_firms == 0) and (white_flag_count == 5) and board_exists
```

**General Cassius "Zero-Trust" Sterling**: `[00:05:42]` By the gods of defensive C++. `res["meets_length"]` is computed on line 93 and **NEVER READ ANYWHERE IN THE ENTIRE FILE**! Not in `is_white_flag` at line 84, not in the `elif res["white_flag"]:` branch at line 170, not in `converged` at line 181, not even in the CLI table status column at lines 202–206!
And look at `res["dialogue_turns"]` (line 90) and `board_lines` (line 174):
1. Look at the module docstring at lines 7–11 of `verify_convergence.py`:
   `Audits a completed wave directory (vN/) to verify:`
   `1. All 5 Firm reports (firm1_*.md .. firm5_*.md) and the Board report exist`
   `2. Each report meets the verbatim persona dialogue density threshold`
   `3. How many Firms raised a verified Formal White Flag (0 surviving vectors)`
   `4. Whether the wave has achieved 5/5 White-Flag Convergence`
2. Look at the CLI flag at lines 138–143:
   `parser.add_argument("--min-lines", type=int, default=250, help="Minimum line count expected per Firm transcript (default: 250)")`
3. Even if a user passes `--min-lines 400`, if `firm1.md` through `firm5.md` are **1-line files** containing the 17 bytes `WHITE FLAG RAISED` (`lines = 1`, `meets_length = False`, `dialogue_turns = 0`), and `BOARD_ADJUDICATION_v1.md` is a **0-byte empty file** (`board_lines = 0`), `audit_single_firm_file()` sets `res["white_flag"] = True` for all 5 firms, `white_flag_count` becomes `5`, `board_exists` is `True`, `converged` at line 181 evaluates to `True`, and `verify_convergence.py` exits with return code `0` (`Verdict : 🏳️ CONVERGED (5/5 WHITE FLAGS RAISED!)`)!

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:06:35]` That is a Grade-A soundness collapse. A verifier that advertises `--min-lines` and "verbatim persona dialogue density threshold" in its own docstring and `argparse` help text, calculates `"meets_length": line_count >= min_lines` at line 93, and then throws the boolean in the garbage without gating `is_white_flag` or `converged` on it is a dead man's switch with the wire cut. That's Vector `F3-V1` (the unanchored/negation-blind `WHITE_FLAG_RE` spoofing) and Vector `F3-V2` (`meets_length`, `dialogue_turns`, and `board_lines` completely disconnected from `is_white_flag` and `converged`).

**Cassian "Schema-Lock" Vane**: `[00:07:19]` Don't move off `verify_convergence.py` yet! Look closer at `CRITICAL_HIGH_SURVIVING_RE` on lines 50–53:

```python
CRITICAL_HIGH_SURVIVING_RE = re.compile(
    r"\|\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL|HIGH)`?\s*\|",
    re.IGNORECASE,
)
```

**Cassian "Schema-Lock" Vane**: `[00:07:45]` Count the ways `CRITICAL_HIGH_SURVIVING_RE` fails both soundness (false negatives—missing real open vectors) and completeness (false positives—blocking valid White Flags in Wave `v2+`):
1. **False Negative #1 — `MEDIUM` (and `LOW`) Vectors Are Invisible**: Every briefing in `the-board` (and `SKILL.md` line 70 & 90) defines convergence as `0 SURVIVING VECTORS` and mandates logging `CRITICAL / HIGH / MEDIUM` bugs in the Surviving Vector Ledger. Because line 51 only matches `(CRITICAL|HIGH)`, a Firm with 12 unpatched `MEDIUM` vulnerabilities in its ledger has `active_vectors == 0`!
2. **False Negative #2 — Markdown Bold/Italic Formatting Bypass**: In Markdown tables, agents routinely format vector IDs or severities in bold or bold-code: `| **F3-V1** | **CRITICAL** |` or `| **`F3-V1`** | `CRITICAL` |` or `| F3-V1 | 🔴 CRITICAL |`. Because line 51 only permits `\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL|HIGH)`?\s*\|`, a single asterisk `*` or emoji `🔴` around `F3-V1` or `CRITICAL` causes `CRITICAL_HIGH_SURVIVING_RE` to return **zero matches**!
3. **False Negative #3 — Column-Order Rigidity**: What if a Firm formats its table as `| Vector ID | Target File | Severity | Fix |` (`| F3-V1 | verify_convergence.py:46 | CRITICAL | ... |`)? Because `CRITICAL_HIGH_SURVIVING_RE` demands that `(CRITICAL|HIGH)` be in the **immediately adjacent second column** right after `F[1-5]-V\d+`, putting the file name or vector title in column 2 makes every single `CRITICAL` bug invisible to `verify_convergence.py`!
4. **False Negative #4 — Blue/Purple Firm Letter IDs (`FA-V1` .. `FE-V1`)**: Look at `locate_firm_files` on lines 113–116 of `verify_convergence.py`:
   ```python
   for idx, letter in enumerate(["a", "b", "c", "d", "e"], start=1):
       if (
           re.search(rf"firm[\s_\-]*0?{idx}\b", name_lower)
           or re.search(rf"firm[\s_\-]*{letter}\b", name_lower)
   ```
   `locate_firm_files` explicitly supports Firms `A` through `E` (`firm_a` .. `firm_e`), or even numeric IDs with leading zeros (`F01-V01`), yet `CRITICAL_HIGH_SURVIVING_RE` hardcodes `F[1-5]-V\d+`!
5. **False Positive #5 — Wave `v2..vN` Historical / Closed Vector Table Trap**: Suppose in Wave `v2`, Firm 3 verifies that `F3-V1` through `F3-V5` from Wave `v1` were fixed and writes a verification table:
   `| F3-V1 | CRITICAL | VERIFIED FIXED IN v2 |`
    followed by `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]`. What does `CRITICAL_HIGH_SURVIVING_RE.findall(text)` do? It scans the entire file text, matches `| F3-V1 | CRITICAL |` in the "Verified Fixed" table, sets `active_vectors = 5`, and **refuses to grant the White Flag**!

**General Cassius "Zero-Trust" Sterling**: `[00:09:32]` Every single one of those five points on `CRITICAL_HIGH_SURVIVING_RE` is 100% verified against lines 50–53 and 80 of `verify_convergence.py`. Especially #5: in a multi-wave convergence engine (`v1 -> v2 -> vN`), Wave `v2` transcripts are *required* to audit the Wave `v1` patches before raising a White Flag. If mentioning `| F3-V1 | CRITICAL | FIXED |` in Wave `v2` permanently poisons `active_vectors > 0`, the wave loop can never converge unless Firms delete their audit trail! That's Vector `F3-V3`.

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:10:15]` Now look at line 45 of `verify_convergence.py`—`DIALOGUE_SPEAKER_RE`:

```python
DIALOGUE_SPEAKER_RE = re.compile(r"^\s*(?:\*\*|\*|-)?\s*\**[A-Z][A-Za-z0-9\.\-\s\(\)]{2,45}\**\s*:\s+.+", re.MULTILINE)
```

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:10:34]` Cassian, Cassius, test this regex against our own names and against the header of this very file!
First, what are our speaker prefixes in this transcript?
`**Cassian "Schema-Lock" Vane**:`
`**General Cassius "Zero-Trust" Sterling**:`
`**Renzo "Unicode-Hell" Takahashi-Cruz**:`
Or what if a Firm includes the persona ID in the speaker tag as shown in the prompt briefing:
`**Cassian "Schema-Lock" Vane (`MERC-SEC-23` — The $100M Principal)**:`
Or what if The Board or a Strike Team includes `**Kurt Gödel**:`, `**Rudolf E. Kálmán**:`, `**Erwin Schrödinger**:`, `**Fernando Corbató**:`, `**Madame Hélène "RAII-Ironclad" Moreau**:`, or `**Liam "Supply-Chain-Blitz" O'Connor**:`?
Look at the character class in `DIALOGUE_SPEAKER_RE` at line 45:
`[A-Z][A-Za-z0-9\.\-\s\(\)]{2,45}`
- Are double quotes `"` in that character class? **NO!** Every single mercenary in `personas/strike_teams/` has a callsign in double quotes (`"Schema-Lock"`, `"Zero-Trust"`, `"Unicode-Hell"`, `"The Redline"`, `"ARM64-Reaper"`). Every single dialogue line spoken by a mercenary with their callsign in quotes is **completely ignored (`0` matches)** by `DIALOGUE_SPEAKER_RE`!
- Are apostrophes `'` in that character class (`O'Connor`, `Chesterton's-Bulldozer`, `Occam's-Razor`)? **NO!**
- Are Unicode letters like `ö`, `á`, `é`, `ü`, `ó`, `卢` in `[A-Za-z...]`? **NO!** `Kurt Gödel`, `Rudolf E. Kálmán`, `Erwin Schrödinger`, and `Madame Hélène Moreau` fail to match!
- Are backticks `` ` ``, slashes `/`, `$`, or em-dashes `—` in that character class? **NO!**

**General Cassius "Zero-Trust" Sterling**: `[00:11:50]` Wait—it gets worse! Look at the other side of `DIALOGUE_SPEAKER_RE` on line 45:
`^\s*(?:\*\*|\*|-)?\s*\**[A-Z][A-Za-z0-9\.\-\s\(\)]{2,45}\**\s*:\s+.+`
Because both `(?:\*\*|\*|-)?` and `\**` are optional (`?` and `*`), **no bolding (`**`) is required at all**! Any plain line or bullet point starting with an uppercase word followed by a colon within 45 characters matches as a "persona dialogue turn":
- `- **Target Artifacts**:` -> Matches!
- `- **Assigned Orthogonal Pillar (Pillar III)**:` -> Matches!
- `- **Saved Recording Path**:` -> Matches!
- `- **Project / Target**: **Untitled Target**` -> Matches!
- `Step 1: Run the script` -> Matches!
- `Warning: File not found` -> Matches!
So `DIALOGUE_SPEAKER_RE` at line 45 **rejects** real verbatim dialogue from `**Cassian "Schema-Lock" Vane**:` and `**Kurt Gödel**:`, while **counting** YAML frontmatter, Markdown metadata bullets, and `Step 1:` list items as "Persona Dialogue Turns"! That is a complete inversion of the regex's specification. Log that as Vector `F3-V4`.

**Cassian "Schema-Lock" Vane**: `[00:12:55]` And look at `locate_firm_files(wave_dir: Path)` at lines 97–122 of `verify_convergence.py`:

```python
    # Scan all Markdown files in the wave directory
    for md_file in sorted(wave_dir.glob("*.md")):
        name_lower = md_file.name.lower()
        if "board" in name_lower:
            board_files.append(md_file)
            continue
        # Match firm1..firm5 or blue_firm_a..e
        for idx, letter in enumerate(["a", "b", "c", "d", "e"], start=1):
            if (
                re.search(rf"firm[\s_\-]*0?{idx}\b", name_lower)
                or re.search(rf"firm[\s_\-]*{letter}\b", name_lower)
                or re.search(rf"^0?{idx}_", name_lower)
            ):
                firm_map[idx] = md_file
                break
```

**Cassian "Schema-Lock" Vane**: `[00:13:33]` Look at lines 109–111:
`if "board" in name_lower: board_files.append(md_file); continue`
That check runs **BEFORE** the `firm1..firm5` loop!
What happens when Firm 1 or Firm 2 names its file after its assigned pillar, just like `SKILL.md` line 55 instructs (`.board/vN/firmK_<pillar>.md`)?
- Suppose we are auditing this very repository (`the_board`) and Firm 1 writes `firm1_boardroom_manifests_and_personas.md` or `firm2_init_board_workspace_audit.md`!
- Or suppose we are auditing a hardware or UI project where Firm 3 writes `firm3_motherboard_power_rails.md`, `firm4_dashboard_layout.md`, `firm5_onboarding_flow.md`, or `firm1_clipboard_sanitization.md`!
Every single one of those filenames contains the 5-letter substring `"board"` (`boardroom`, `init_board_workspace`, `motherboard`, `dashboard`, `onboarding`, `clipboard`)!
Because `if "board" in name_lower:` runs first at line 109 and executes `continue` at line 111:
1. `firm1_boardroom_manifests_and_personas.md` is hijacked into `board_files` and **never enters `firm_map[1]`**, so `verify_convergence.py` reports `Firm 1 | MISSING | ❌ MISSING` and `converged = False`!
2. Even worse: if `board_files` gets `clipboard_firm1.md` sorted alphabetically before `firm5`, or if `BOARD_ADJUDICATION_v1.md` is missing entirely, `firm1_boardroom_manifests.md` is treated as the Board Adjudication report (`board_exists = len(board_files) > 0` becomes `True` at line 173)!
3. And look at lines 164 and 181: `for idx in range(1, 6):` and `converged = (missing_firms == 0) and (white_flag_count == 5) and board_exists`. What if the user ran `--effort strike`, which `SKILL.md` line 41 and line 80 explicitly defines as spawning `K=1..2` Strike Teams instead of `5`? `verify_convergence.py` hardcodes `5` firms with no `--firms` CLI flag and no lookup of `board_config.json`, making `--effort strike` mathematically impossible to pass `verify_convergence.py`! Log that as Vector `F3-V5`.

---

**General Cassius "Zero-Trust" Sterling**: `[00:15:10]` Let's move to the second target script: `L:\Dev\the_board\scripts\init_board_workspace.py` (252 lines).
Before you two start swinging wildly at `init_board_workspace.py`, let me test Cassian's earlier instinct about integer overflow or negative `--max-waves` DOS attacks on `init_board_workspace.py`.

**Cassian "Schema-Lock" Vane**: `[00:15:32]` Right—in `init_board_workspace.py`, `build_convergence_tracker_markdown()` at line 71 runs `for w in range(1, max_waves + 1):`. If a user or agent passes `--max-waves 10000000` on the CLI, doesn't that allocate a 10-million-row Markdown table in memory and hang the scaffolder, or if they pass `--max-waves -5` or `0`, generate an empty wave table with zero rows?

**General Cassius "Zero-Trust" Sterling**: `[00:15:58]` **Shot down.** Read lines 123 through 132 of `init_board_workspace.py` before you speak, Cassian:

```python
    # Normalize effort string and resolve wave ceiling
    norm_effort = (effort or "standard").strip().lower()
    if norm_effort not in EFFORT_DEFAULT_WAVES:
        print(f"[WARN] Unknown effort '{norm_effort}', defaulting to 'standard'.")
        norm_effort = "standard"

    # Determine final max_waves count with bounds clamping (1..30)
    resolved_waves = max_waves if (max_waves is not None and max_waves > 0) else EFFORT_DEFAULT_WAVES[norm_effort]
    resolved_waves = max(1, min(resolved_waves, 30))
```

**General Cassius "Zero-Trust" Sterling**: `[00:16:31]` Look at lines 130–131:
If `max_waves` is `None`, `0`, or `-5`, `max_waves is not None and max_waves > 0` is `False`, so it falls back to `EFFORT_DEFAULT_WAVES[norm_effort]`.
If `max_waves` is `10000000`, line 131 clamps `resolved_waves = max(1, min(resolved_waves, 30))`, and line 171 passes `max_waves=resolved_waves` into `build_convergence_tracker_markdown()`. And `board_dir is None` is explicitly checked at line 119, and `OSError` on `mkdir` is caught at line 137. So your `--max-waves` memory-exhaustion and negative-wave theories are completely neutralized by existing defenses. That's two lazy theories of yours I've buried today.

**Cassian "Schema-Lock" Vane**: `[00:17:08]` Fine, line 131 clamps `resolved_waves` to `[1, 30]`. Now look at what `init_board_workspace.py` *actually* breaks at lines 206–212 when The Lead follows `SKILL.md`!

**General Cassius "Zero-Trust" Sterling**: `[00:17:22]` Oh, I already circled lines 206–212 in red ink. Look at `SKILL.md` line 32 and Section `[03] FOUR OPERATING MODES` at lines 67–73:
- `SKILL.md` line 32: `mode (plan | red | blue | purple)`
- `SKILL.md` line 69: `- plan (Pre-Code / Pre-Execution Plan Siege): Run The Board on an Implementation Plan, Architecture Spec, or Action Plan before executing or writing production code.`
- `SKILL.md` lines 79–80:
  `1. Read target files (or draft the initial Implementation Plan if in plan mode).`
  `2. Run scripts/init_board_workspace.py (or create .board/v1/ and .board/CONVERGENCE_TRACKER.md).`
Now read `init_board_workspace.py` lines 206–212:

```python
    parser.add_argument(
        "--mode",
        type=str,
        choices=["red", "blue", "purple"],
        default="red",
        help="Operating mode: red (Red-Team), blue (Blue-Team Tournament), or purple (Hybrid)",
    )
```

**General Cassius "Zero-Trust" Sterling**: `[00:18:10]` `"plan"` is **MISSING** from `choices=["red", "blue", "purple"]` at line 209!
When The Lead or a user runs `python scripts/init_board_workspace.py --mode plan --project "My Plan"`, `argparse` immediately aborts with exit code `2`:
`init_board_workspace.py: error: argument --mode: invalid choice: 'plan' (choose from 'red', 'blue', 'purple')`!
And look at `commands/board.md` or `SKILL.md`—`plan` mode is one of the four headline operating modes of the entire skill (it's even in the YAML description at `SKILL.md` line 4: `Multi-agent persona-conditioned Red-Team, Blue-Team, Pre-Code Plan, and Executive Boardroom iterative convergence engine`), yet the workspace initializer rejects `--mode plan` as an illegal argument! And what if the user invokes `--mode boardroom` or `--mode executive`? At minimum, `choices` at line 209 MUST include `"plan"` (`choices=["plan", "red", "blue", "purple"]`). That's Vector `F3-V6`.

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:19:01]` Look also at `init_board_workspace.py` lines 160–175 inside `init_workspace()`:

```python
    config_path = board_dir / "board_config.json"
    config_path.write_text(json.dumps(config_payload, indent=2), encoding="utf-8")

    # Write `CONVERGENCE_TRACKER.md` if it does not already exist
    tracker_path = board_dir / "CONVERGENCE_TRACKER.md"
    if not tracker_path.exists():
        tracker_md = build_convergence_tracker_markdown(
            project_name=project_name,
            mode=mode,
            domain=domain,
            effort=norm_effort,
            max_waves=resolved_waves,
            targets=targets,
        )
        tracker_path.write_text(tracker_md, encoding="utf-8")
```

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:19:38]` Look at the asymmetry between line 161 and line 165:
- Line 165 carefully checks `if not tracker_path.exists():` before writing `CONVERGENCE_TRACKER.md` so that re-running `init_board_workspace.py` during an active multi-wave session doesn't wipe out the Wave-by-Wave White-Flag Convergence Matrix and Non-Regression Ratchet Ledger.
- Line 161 (`config_path.write_text(...)`) has **NO `if not config_path.exists():` guard and no `--force` flag**! If `init_board_workspace.py` is run a second time on an existing `.board/` directory (for example, when resuming a session or scaffolding a new wave), line 161 **unconditionally overwrites `board_config.json`**, wiping out `"current_wave"`, resetting `"converged": False`, and erasing all 6 persisted `"subagent_ids"` (`firm1..5`, `board`), leaving `board_config.json` out of sync with `CONVERGENCE_TRACKER.md`!
- Also look at line 8 of the docstring (`1. Wave directories (v1 .. vN)`) versus line 136 (`(board_dir / "v1").mkdir(parents=True, exist_ok=True)`): it only creates `v1`, and `init_workspace` at line 168 & 178 calls `mode.upper()` directly without guarding `if mode is None` (even though line 144 guarded `(mode or "red").lower()`, line 178 does `print(f"    • Mode      : {mode.upper()}")` and line 81 does `{mode.upper()}`, which will throw `AttributeError: 'NoneType' object has no attribute 'upper'` if `init_workspace` is imported and called programmatically with `mode=None`!).

**General Cassius "Zero-Trust" Sterling**: `[00:20:42]` Good catch on `mode.upper()` at lines 81 and 178! Look at line 144 of `init_board_workspace.py`:
`"mode": (mode or "red").lower(),`
The author anticipated `mode` could be `None` or empty at line 144 (`(mode or "red").lower()`) and `domain` could be `None` at line 145 (`(domain or "coding").lower()`), yet forgot to normalize `norm_mode = (mode or "red").strip().lower()` and `norm_domain = (domain or "coding").strip().lower()` at the top of `init_workspace()`, passing raw `mode` to `mode.upper()` at lines 81 and 178! That's a classic half-finished defensive check. We'll bundle the `board_config.json` overwrite protection and `norm_mode` / `norm_domain` normalization into Vector `F3-V7`.

---

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:21:30]` Now step into my domain: `L:\Dev\the_board\scripts\split_personas_to_files.py` (227 lines).
Wait—first, let me check `slugify_persona_name(raw_name: str)` at lines 67–85. When we feed European names like `Kurt Gödel`, `Rudolf E. Kálmán`, `Fernando Corbató`, `Erwin Schrödinger`, `Jürgen Habermas-Arrow`, or `Madame Hélène Moreau` into `slugify_persona_name`, doesn't stripping non-ASCII characters corrupt their names into `kurt_gdel` or `rudolf_e_klmn`?!

**General Cassius "Zero-Trust" Sterling**: `[00:22:02]` **Shot down—that's Shootdown #3!** Read lines 78 through 80 of `split_personas_to_files.py`, Renzo:

```python
    # Normalize unicode accents (e.g., Kálmán -> Kalman, Gödel -> Godel)
    normalized = unicodedata.normalize("NFKD", cleaned)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
```

**General Cassius "Zero-Trust" Sterling**: `[00:22:25]` Because line 79 runs `unicodedata.normalize("NFKD", cleaned)` *before* `.encode("ascii", "ignore")`, Latin precomposed characters with diacritics (`ö` = `U+00F6`, `á` = `U+00E1`, `é` = `U+00E9`) are canonically decomposed into their base ASCII letter (`o`, `a`, `e`) plus a combining diacritical mark (`U+0308`, `U+0301`). Then `.encode("ascii", "ignore")` drops only the combining mark and preserves the base ASCII letter! Look at `personas/board_members/INDEX.md` lines 25, 36, 68, 75:
- `Kurt Gödel` -> `kurt_godel.md`
- `Fernando Corbató` -> `fernando_corbato.md`
- `Erwin Schrödinger` -> `erwin_schrodinger.md`
- `Rudolf E. Kálmán` -> `rudolf_e_kalman.md`
So Latin diacritics under `NFKD` are already handled cleanly at lines 79–80!

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:23:08]` Hold on, Cassius! Look at why I brought up Unicode normalization—because what works for Latin `NFKD` (`Gödel -> Godel`) **catastrophically fails on CJK ideographs and non-Latin scripts (`卢`, `孫子`, `Łukasiewicz`) when combined with line 74 of `split_personas_to_files.py`**!
Read lines 73–84 of `split_personas_to_files.py` in exact execution order:

```python
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

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:23:55]` Look at what actually happened in this repository when `split_personas_to_files.py` ran on `MERC-SW-26` (`personas/strike_teams_individual/INDEX.md` line 41):
The persona's name in `01_software_kernels_and_plans_mercenaries.md` is:
`Dr.卢 (Lu) "Strict-Alias" Jian-Guo — The Undefined-Behavior & LLVM-IR Grand Surgeon`
Trace that string through lines 74–80 of `slugify_persona_name()`:
1. Line 74 (`cleaned = re.sub(r"\([^)]*\)", "", raw_name)`) strips `(Lu)` because it is inside parentheses! Now the string is `Dr.卢 "Strict-Alias" Jian-Guo...`.
2. Line 79 (`unicodedata.normalize("NFKD", cleaned)`) does nothing to `卢` (`U+5362`) because CJK ideographs do not decompose into Latin ASCII under `NFKD`!
3. Line 80 (`normalized.encode("ascii", "ignore")`) deletes `卢` completely!
4. Result on disk (`personas/strike_teams_individual/INDEX.md` line 41):
   `dr_strict_alias_jian_guo_the_undefined_behavior_llvm_ir_grand_surgeon.md` — **Dr. Lu's surname (`卢 / Lu`) was completely erased from the filename!**
5. What if a persona is named `孫子 (Sun Tzu)` or `韓非子 (Han Feizi)`? Line 74 deletes `(Sun Tzu)` and `(Han Feizi)`, line 80 deletes `孫子` and `韓非子`, `slug` becomes `""`, and line 84 returns `"persona_entry"` for **both** of them, silently overwriting `persona_entry.md`!
6. And what about Polish `Ł` (`Jan Łukasiewicz`), Nordic `Ø` (`Ørsted`), or German `ß`? `NFKD` does **NOT** decompose `Ł -> L` or `Ø -> O` (`unicodedata.normalize("NFKD", "ŁØ").encode("ascii", "ignore")` returns `b""`!), so `Łukasiewicz` becomes `ukasiewicz`!

**Cassian "Schema-Lock" Vane**: `[00:25:12]` Wait—look at `personas/strike_teams_individual/INDEX.md` again! Renzo just quoted line 41 of `personas/strike_teams_individual/INDEX.md`, and while looking at that file, I just saw something 10x worse in `split_personas_to_files.py`.
Look at `personas/strike_teams_individual/INDEX.md` lines 6–19:

```markdown
## Category: `software_plans` (42 Personas)

| ID | Persona | Individual `.md` File |
| :--- | :--- | :--- |
| `MERC-SW-01` | **Category I: Pre-Code Implementation-Plan Wreckers (`MERC-SW-01` .. `MERC-SW-05`)** | [`./software_plans/category_i_pre_code_implementation_plan_wreckers.md`](./software_plans/category_i_pre_code_implementation_plan_wreckers.md) |
| `MERC-SW-01` | **Dr. Viktor "The Redline" Kaczmarek — Sovereign Pre-Code Spec Executioner** | [`./software_plans/dr_viktor_the_redline_kaczmarek_sovereign_pre_code_spec_executioner.md`](./software_plans/dr_viktor_the_redline_kaczmarek_sovereign_pre_code_spec_executioner.md) |
...
| `MERC-SW-06` | **Category II: Weak-Memory-Model & Lock-Free Kernel Assassins (`MERC-SW-06` .. `MERC-SW-10`)** | [`./software_plans/category_ii_weak_memory_model_lock_free_kernel_assassins.md`](./software_plans/category_ii_weak_memory_model_lock_free_kernel_assassins.md) |
| `MERC-SW-06` | **Dr. Arkady "ARM64-Reaper" Volkov — The Relaxed-Atomics & Litmus-Test Assassin** | [`./software_plans/dr_arkady_arm64_reaper_volkov_the_relaxed_atomics_litmus_test_assassin.md`](./software_plans/dr_arkady_arm64_reaper_volkov_the_relaxed_atomics_litmus_test_assassin.md) |
```

**Cassian "Schema-Lock" Vane**: `[00:25:58]` Look at that output! Why does `software_plans` say `(42 Personas)` when there are only `35` mercenaries (`MERC-SW-01` .. `MERC-SW-35`), and why does `MERC-SW-01` appear **TWICE**—first as `Category I: Pre-Code Implementation-Plan Wreckers (MERC-SW-01 .. MERC-SW-05)` in a bogus file `category_i_pre_code_implementation_plan_wreckers.md`, and second as `Dr. Viktor "The Redline" Kaczmarek`?!
Let's trace `extract_persona_blocks(markdown_text: str)` at lines 87–141 of `split_personas_to_files.py`:

```python
    # Match markdown headings that introduce an individual persona entry
    header_pattern = re.compile(
        r"^(#{2,3})\s+(.+?)\s*$",
        re.MULTILINE,
    )
    matches = list(header_pattern.finditer(markdown_text))
    extracted: List[Tuple[str, str, str]] = []

    for idx, match in enumerate(matches):
        level_hashes = match.group(1)
        heading_text = match.group(2).strip().strip("*")

        # Filter out generic section headers (e.g., "Category 1:", "Overview")
        is_persona_header = bool(
            re.search(r"(?:REAL|MERC)-[A-Z0-9\-]+", heading_text)
            or re.match(r"^#?\d{1,2}[\.\:\)\s\-]+", heading_text)
        )
        if not is_persona_header:
            continue
```

**Cassian "Schema-Lock" Vane**: `[00:26:49]` Look at the comment on line 108:
`# Filter out generic section headers (e.g., "Category 1:", "Overview")`
The author *intended* to filter out `Category` and `Division` section headers!
Why did the filter on lines 109–112 fail on **35 section headers** across `software_plans`, `legal_patents`, `hardware_physics`, `design_philosophy`, and `philosophy_prompt_linguistics`?!
Because in those five repertoire files, the `## Category` and `## DIVISION` headers include the ID range in parentheses:
- `## Category I: Pre-Code Implementation-Plan Wreckers (\`MERC-SW-01\` .. \`MERC-SW-05\`)`
- `## Category II: PTAB IPR Invalidity & Prior-Art Combinatorics Assassins (\`MERC-LAW-06\` .. \`MERC-LAW-10\`)`
- `## DIVISION I: WITTGENSTEINIAN LEXICAL SURGEONS & SYNONYM ASSASSINS (\`MERC-PHIL-01\` – \`MERC-PHIL-05\`)`
Because the header text contains `MERC-SW-01` inside `(\`MERC-SW-01\` .. \`MERC-SW-05\`)`, `re.search(r"(?:REAL|MERC)-[A-Z0-9\-]+", heading_text)` at line 110 returns **`True`**!
And what if a section header is written `## Category 1: Overview` (the exact example in the author's comment on line 108)? Doesn't `Category` fail `re.match(r"^#?\d{1,2}[\.\:\)\s\-]+", heading_text)` only if it starts with `Category`, whereas if someone writes `## 1. Category Overview` it matches `^\d{1,2}\.` too?!
And once `## Category I: ... (\`MERC-SW-01\` .. \`MERC-SW-05\`)` passes `is_persona_header` at line 109:
1. Line 132 (`id_match = re.search(r"((?:REAL|MERC)-[A-Z]+-\d+)", heading_text)`) extracts the first ID in the range (`MERC-SW-01`), creating a **duplicate ID collision** with the actual `MERC-SW-01` persona!
2. Line 187 writes a bogus `.md` file (`category_i_pre_code_implementation_plan_wreckers.md`, `division_i_wittgensteinian_lexical_surgeons_synonym_assassins.md`, etc.) containing nothing but the 1-line category heading!
3. Across the 5 files (`software_plans`, `legal_patents`, `hardware_physics`, `design_philosophy`, `philosophy_prompt_linguistics`), `split_personas_to_files.py` generated **35 bogus Category/Division `.md` files** on disk (`280` files emitted instead of `245`), polluting `personas/strike_teams_individual/` and its `INDEX.md`!

**General Cassius "Zero-Trust" Sterling**: `[00:28:15]` That is an indisputable, smoking-gun bug with 35 corrupted artifacts currently sitting on disk in `personas/strike_teams_individual/` to prove it!
Let's trace the exact root cause in `extract_persona_blocks()` (`split_personas_to_files.py` lines 97–140):
Why did `extract_persona_blocks` match `## Category I: ...`?
1. In all repertoire files (`personas/repertoire_real_humans/*.md` and `personas/strike_teams/*.md`), `## ` (level 2) is used for **Category / Division section headers** (or in some files persona headers when not nested), while individual personas either start with `### ` or start with their ID/number right at the beginning of the heading (not inside a parenthetical range like `(MERC-SW-01 .. MERC-SW-05)`), and **never** begin with `Category ` or `Division `!
2. Look at what happens if we check:
   - First, reject any heading that starts with `Category` or `Division` (`re.match(r"^(?:Category|Division)\b", heading_text, re.IGNORECASE)`) OR contains an ID range (`re.search(r"(?:REAL|MERC)-[A-Z]+-\d+`?\s*(?:\.\.|–|—|-|to)\s*`?(?:REAL|MERC)-[A-Z]+-\d+", heading_text)`).
   - Second, in `split_collection()` (lines 168–190), before writing the `.md` files into `cat_dir`, clean any stale `.md` files in `cat_dir` (`for old_md in cat_dir.glob("*.md"): old_md.unlink()`) so the 35 bogus `category_*.md` and `division_*.md` files are purged when `split_personas_to_files.py` is re-run!
Log the bogus Category/Division persona extraction and duplicate ID bug as Vector `F3-V8`.

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:29:40]` And look at the filenames `split_personas_to_files.py` generates for the remaining 245 Strike Team mercenaries!
Look at line 73 of `split_personas_to_files.py`:
`# Strip parenthetical dates like (1912-1954) or role suffixes`
Read lines 74–76 right underneath that comment:

```python
    # Strip parenthetical dates like (1912-1954) or role suffixes
    cleaned = re.sub(r"\([^)]*\)", "", raw_name)
    cleaned = re.sub(r"^(?:REAL|MERC)-[A-Z]+-\d+\s*:\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^#?\d+[\.\:\-\s]+", "", cleaned)
```

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:30:12]` Where is the regex that strips `or role suffixes`?! **The comment on line 73 says `or role suffixes`, and the author completely forgot to write the line of code that strips ` — <Role Suffix>`!**
Look at the consequence in `personas/strike_teams_individual/`:
Every Strike-Team heading has the format:
`### MERC-LAW-35: Lord Conrad "Lear-Breaker" Ravenscroft — No-Challenge Clauses, *Lear v. Adkins* Settlement Locks & Bankruptcy IP Stripper (London / Delaware / SDNY)`
Because `slugify_persona_name` never strips the ` — <Role Suffix>` after the em-dash (`—` or `–` or ` - `), the generated filename is:
`lord_conrad_lear_breaker_ravenscroft_no_challenge_clauses_lear_v_adkins_settlement_locks_bankruptcy_ip_stripper.md` (**114 characters** just for the filename!).
Combined with the directory path:
`C:\Users\Donny\.gemini\config\skills\the-board\personas\strike_teams_individual\philosophy_prompt_linguistics\inquisitor_torquemada_goodhart_campbell_the_metric_gaming_fake_white_flag_executioner.md`
That's **202+ characters** in the home directory, and if installed into `.agents/skills/the-board` inside a nested Windows workspace (`L:\Dev\SomeProject\submodules\...\`), it blows right past the Win32 `MAX_PATH` (`260`-character) limit!
And look at the three additional bugs in `slugify_persona_name` (lines 67–85) and `split_collection` (lines 175–188):
1. **Parenthetical Romanization Destruction (`Dr.卢 (Lu)`)**: If `raw_name` contains non-ASCII CJK characters followed by a parenthetical ASCII romanization like `Dr.卢 (Lu)`, stripping `\([^)]*\)` at line 74 deletes `(Lu)` before NFKD normalization at line 79, erasing the name! Instead, parentheticals should only be stripped if they are dates/locations/ranges or after preserving ASCII romanizations adjacent to CJK characters, AND role suffixes after ` — ` / ` – ` should be stripped so the slug is `dr_lu_strict_alias_jian_guo.md` instead of `dr_strict_alias_jian_guo_the_undefined_behavior_llvm_ir_grand_surgeon.md`!
2. **Extended Latin Transliteration (`Ł`, `Ø`, `ß`, `Æ`, `Œ`)**: `unicodedata.normalize("NFKD", ...)` does not decompose stroke/ligature letters like `Ł/ł`, `Ø/ø`, `Đ/đ`, `ß`, `Æ/æ`, `Œ/œ`. A small pre-NFKD translation table (`str.maketrans({"Ł": "L", "ł": "l", "Ø": "O", "ø": "o", "Đ": "D", "đ": "d", "ß": "ss", "Æ": "AE", "æ": "ae", "Œ": "OE", "œ": "oe"})`) prevents silent character deletion.
3. **Windows Reserved Device Names & Duplicate Slug Collisions**: On Windows, creating `con.md`, `prn.md`, `aux.md`, `nul.md`, `com1.md`..`com9.md`, or `lpt1.md`..`lpt9.md` is a reserved Win32 device name hazard, and if two personas in the same category produce the same `file_slug`, line 177 (`out_file = cat_dir / f"{file_slug}.md"`) silently overwrites the first file without appending `_{persona_id.lower()}`!
Log that as Vector `F3-V9`.

**General Cassius "Zero-Trust" Sterling**: `[00:32:18]` Also check `split_personas_to_files.py` line 12 vs line 207:
- Line 12 (docstring): `- personas/strike_teams/<category>/<mercenary_slug>.md`
- Line 207 (`main()`): `strike_dst = repo_root / "personas" / "strike_teams_individual"`
Why did `main()` write to `personas/strike_teams_individual` instead of `personas/strike_teams/<category>/`? Because `personas/strike_teams/` holds the source repertoire files (`01_software_kernels_and_plans_mercenaries.md`, etc.)! That's fine, except:
1. The module docstring at line 12 lies about the destination path (`personas/strike_teams/<category>/<mercenary_slug>.md` instead of `personas/strike_teams_individual/<category>/<mercenary_slug>.md`).
2. `SKILL.md` (lines 53, 85, 89, 115) never mentions `personas/strike_teams_individual/INDEX.md`!
Log that docstring/manifest desync and stale-file cleanup in `split_collection()` as Vector `F3-V10`.

---

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:33:10]` Now let's open the final two target artifacts: [`L:\Dev\the_board\scripts\install.ps1`](file:///L:/Dev/the_board/scripts/install.ps1) (50 lines) and [`L:\Dev\the_board\scripts\install.sh`](file:///L:/Dev/the_board/scripts/install.sh) (38 lines).
Read `install.ps1` lines 15–30 verbatim:

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

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:33:48]` And now read `install.sh` lines 14–23 verbatim:

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

**Cassian "Schema-Lock" Vane**: `[00:34:15]` WAIT A SECOND! Look at line 21 of `install.ps1`:
`foreach ($Sub in @("references", "examples", "scripts"))`
And look at lines 17–21 of `install.sh`:
`mkdir -p "${dest_dir}/references" "${dest_dir}/examples" "${dest_dir}/scripts"`
**WHERE IS `personas`?! WHERE IS `commands`?!**

**General Cassius "Zero-Trust" Sterling**: `[00:34:40]` Hold everything. Let me check `SKILL.md` to see every relative path `SKILL.md` instructs the agent to read when `the-board` is activated from its installed location (`~/.gemini/config/skills/the-board` or `~/.claude/skills/the-board` or `.agents/skills/the-board`):
- `SKILL.md` line 53: `[personas/strike_teams/](./personas/strike_teams/)`
- `SKILL.md` line 60: `[personas/board_members/<category>/<person>.md](./personas/board_members/)`
- `SKILL.md` line 62: `[personas/boardrooms/*.md](./personas/boardrooms/)`
- `SKILL.md` line 82: `Pick a Boardroom manifest from [personas/boardrooms/](./personas/boardrooms/) (e.g., the_godfather_board.md)—or assemble a custom list of 6 .md files from [personas/board_members/<category>/](./personas/board_members/)`
- `SKILL.md` line 85: `persona dossiers from [personas/strike_teams/](./personas/strike_teams/)`
- `SKILL.md` line 94: `Instruct The Board subagent to read the 6 selected Board member .md files (personas/board_members/...)`
- `SKILL.md` lines 113–115:
  - `[personas/board_members/](./personas/board_members/)`
  - `[personas/boardrooms/](./personas/boardrooms/)`
  - `[personas/strike_teams/](./personas/strike_teams/)`
- And what does `scripts/split_personas_to_files.py` (which *is* copied into `scripts/`) look for when run from the installed skill directory (`repo_root = Path(__file__).resolve().parent.parent` at line 201)? It looks for `repo_root / "personas" / "repertoire_real_humans"` and `repo_root / "personas" / "strike_teams"`!

**General Cassius "Zero-Trust" Sterling**: `[00:35:52]` Neither `install.ps1` (line 21) nor `install.sh` (lines 17–21) copies `personas/` or `commands/` into `$DestDir`!
When a user runs `.\scripts\install.ps1` or `./scripts/install.sh` to install `the-board` into Google Antigravity (`~/.gemini/config/skills/the-board`), Claude Code (`~/.claude/skills/the-board`), or a project workspace (`.agents/skills/the-board`):
1. The entire `personas/` directory (`board_members/`, `boardrooms/`, `repertoire_real_humans/`, `strike_teams/`, `strike_teams_individual/`) is **100% MISSING** from the installed skill directory!
2. When an agent activates `the-board` from `~/.gemini/config/skills/the-board/SKILL.md` in any workspace other than `L:\Dev\the_board`, every single Board member `.md` file, every Boardroom manifest (`the_godfather_board.md`), and every Strike Team dossier is **non-existent (`FileNotFoundError`)**!
3. And `commands/` (`commands/board.md`) is never copied into `$DestDir/commands` (nor into `.claude/commands/board.md` when `$Target` is `"workspace"`).
That is a `CRITICAL` installer completeness failure (`F3-V11`). The skill literally amputates its own 500-persona library during installation!

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:36:55]` And look closely at `install.sh` vs `install.ps1` for three more cross-platform defects (`F3-V12`):
1. **Silent No-Op on Invalid Target Argument in `install.sh` (lines 10 & 25–38)**:
   In `install.ps1` line 8, PowerShell enforces `[ValidateSet("all", "agy", "claude", "workspace")]`.
   In `install.sh` line 10, `TARGET="${1:-all}"` is checked by three independent `if` statements (`if [[ "${TARGET}" == "all" || "${TARGET}" == "agy" ]]`, `if [[ "${TARGET}" == "all" || "${TARGET}" == "claude" ]]`, `if [[ "${TARGET}" == "workspace" ]]`).
   If a user runs `./scripts/install.sh --help`, `./scripts/install.sh gemini`, or `./scripts/install.sh claud`, **none of the `if` branches match, nothing is printed, nothing is installed, and `install.sh` exits with return code `0` (success)!**
   It needs a `case "${TARGET}" in all|agy|claude|workspace) ;; *) echo "[ERROR] Invalid target '${TARGET}'. Expected: all | agy | claude | workspace" >&2; exit 1 ;; esac` guard!
2. **Unquoted Glob Expansion & Stale File Accumulation in `install.sh` (lines 17–21) and `install.ps1` (lines 21–28)**:
   In `install.sh` lines 19–21:
   `cp -rf "${REPO_ROOT}/references/"* "${dest_dir}/references/"`
   If any subdirectory happens to be empty, in bash with `failglob` or `nullglob` unset, `"${REPO_ROOT}/subdir/"*` passes a literal `"*"` to `cp`, which crashes under `set -euo pipefail`! Using `cp -rf "${REPO_ROOT}/${sub}/." "${dest_dir}/${sub}/"` in a loop over `personas references examples scripts commands` avoids glob expansion pitfalls and copies nested directory trees cleanly.
   Furthermore, if old files exist in `${dest_dir}/personas` (such as the 35 bogus `category_*.md` files from `F3-V8`), `cp -rf` / `Copy-Item` merges on top of the destination without removing deleted/renamed files unless `${dest_dir}/${sub}` is cleaned before copying!

**Cassian "Schema-Lock" Vane**: `[00:38:40]` Let's do a complete audit check across all five scripts to see if any other subtle edge cases remain in `verify_convergence.py`, `init_board_workspace.py`, `split_personas_to_files.py`, `install.ps1`, or `install.sh`.
Let's check `verify_convergence.py` lines 173–178:

```python
    board_exists = len(board_files) > 0
    board_lines = (
        len(board_files[0].read_text(encoding="utf-8", errors="replace").splitlines())
        if board_exists
        else 0
    )
```

**Cassian "Schema-Lock" Vane**: `[00:39:08]` Look at `board_files[0]` at line 175 and line 211 (`board_label = board_files[0].name if board_exists else "MISSING"`).
What if a wave directory has multiple files containing `"board"`, or what if we tighten `locate_firm_files`?
In `locate_firm_files(wave_dir: Path)` (lines 97–122):
1. We should match Firm files (`firm1..5`, `firm_a..e`, `^0?[1-5]_`) **FIRST** before checking for the Board Adjudication file, OR only match `board_files` when the filename starts with `board` (`^board\b`, `board_adjudication`, `board_report`, `executive_patch`) and is **not** a `firm1..5` file! That completely prevents `firm1_boardroom_personas.md` or `firm3_dashboard_ui.md` from being misclassified as a `board_file`.
2. What if there are multiple `BOARD*` files in `wave_dir` (e.g., `BOARD_ADJUDICATION_v1.md` and `board_notes.md`)? Prefer `BOARD_ADJUDICATION*.md` (or the largest/latest matching `BOARD*.md` file) instead of blindly taking `board_files[0]`.
3. What about `board_lines`? `SKILL.md` line 96 specifies that `BOARD_ADJUDICATION_vN.md` records `400–700+` lines of verbatim closed-door deliberation plus the Binding Executive Patch Specification. At minimum, `verify_convergence.py` should enforce that `board_lines >= min_board_lines` (e.g., `--min-board-lines`, default `100`, or `max(50, args.min_lines // 2)`) so a 0-byte `touch .board/v1/BOARD_ADJUDICATION_v1.md` cannot satisfy `converged = True`!

**General Cassius "Zero-Trust" Sterling**: `[00:40:25]` Let's check the exact arithmetic and logic we want in `verify_convergence.py` so there is zero ambiguity when The Board reviews our patch specification:
1. **In `verify_convergence.py`**:
   - **`DIALOGUE_SPEAKER_RE`**: Must match real Markdown bold speaker turns (`**Speaker Name**: ...` or `- **Speaker Name (Role)**: ...`) including double quotes `"..."`, single quotes `'`, Unicode letters (`\w` in Python 3 `re` matches all Unicode word characters including `ö`, `á`, `é`, `卢`, etc.!), backticks, slashes, `$`, and em-dashes, while **excluding** non-dialogue metadata bullets like `- **Target Artifacts**:`, `- **Saved Recording Path**:`, `- **Assigned Orthogonal Pillar**:`, `- **Project / Target**:`, `- **Operating Mode**:`, `- **ID**:`, `- **Category**:`, `- **Status**:`, `- **Verdict**:`, etc.
     Specifically: require bold speaker formatting `^\s*(?:[-*]\s+)?\*\*([^*\n]{2,90}?)\*\*\s*:\s+\S+` and filter out known metadata keys (`Target Artifacts`, `Assigned Orthogonal Pillar`, `Saved Recording Path`, `Triad Roster`, `Mask [123]`, `Project / Target`, `Operating Mode`, `Domain Playbook`, `Effort Level`, `Initialized`, `ID`, `Category`, `Status`, `Verdict`, `Rule`, `Fix`, `Vector`, `Severity`, `File`, `Summary`).
   - **`WHITE_FLAG_RE` & Negation Guard**:
     Instead of an unanchored substring search that triggers on `"NO WHITE FLAG RAISED"` or quoted prompt instructions, check two tiers:
     1. Look for the canonical status block `[STATUS: WHITE FLAG RAISED // 0 SURVIVING VECTORS]` (or line-anchored heading/status line containing `WHITE FLAG RAISED`, `FORMAL WHITE FLAG`, `UNCONDITIONAL SURRENDER`, or `0 SURVIVING VECTORS`).
     2. Reject any line that contains negation tokens (`\b(?:no|not|never|cannot|can't|without|withheld|false|reject|denied|pending|if|until|unless)\b`) before or after the phrase on that line, OR where the phrase is enclosed in inline code/quotes inside a dialogue turn explaining the rules!
     3. Explicitly reject if the file contains `[STATUS: OPEN VECTORS REMAIN` or `WHITE FLAG WITHHELD`.
   - **`SURVIVING_VECTOR_RE` (replacing `CRITICAL_HIGH_SURVIVING_RE`)**:
     1. Match `CRITICAL`, `HIGH`, **and `MEDIUM`** severities (`CRITICAL|HIGH|MEDIUM`).
     2. Allow optional Markdown bold/italic/code/emoji formatting around the Vector ID (`F[1-5A-E]-V\d+` or `F0?[1-5]-V\d+`) and around the Severity (`CRITICAL|HIGH|MEDIUM`), and allow Severity to appear in **any column** of that Markdown table row (`^\s*\|[^|\n]*`?\**F(?:0?[1-5]|[A-E])-V\d+\**`?\s*\|[^\n]*\b(CRITICAL|HIGH|MEDIUM)\b[^\n]*\|`), **unless** the row explicitly marks the vector as closed/fixed/resolved (`\b(?:FIXED|RESOLVED|CLOSED|NEUTRALIZED|REMEDIATED|VERIFIED\s+FIXED)\b`)!
   - **Enforcing `meets_length`, `meets_dialogue`, and `board_meets_length` in `is_white_flag` and `converged`**:
     - Add `--min-turns` (default: `10`) and `--min-board-lines` (default: `100`) and `--expected-firms` (default: `5`, or auto-read from `board_config.json` if present) to `argparse`.
     - In `audit_single_firm_file()`:
       `meets_length = line_count >= min_lines`
       `meets_turns = dialogue_count >= min_turns`
       `is_white_flag = has_white_flag_phrase and (active_vectors == 0) and meets_length and meets_turns`
     - In `main()`:
       `board_ok = board_exists and (board_lines >= args.min_board_lines)`
       `converged = (missing_firms == 0) and (white_flag_count == expected_firms) and board_ok`
     - And in the human-readable table Status column (lines 202–206), if `not r["meets_length"]` or `not r["meets_turns"]`, clearly display `⚠️ SHORT ({r['lines']}L/{r['dialogue_turns']}T)` so The Lead immediately sees why a stub report was rejected!

**Renzo "Unicode-Hell" Takahashi-Cruz**: `[00:42:40]` Look how clean that is. Every single lie in `verify_convergence.py`'s docstring becomes a true, mechanically enforced invariant.
Now let's review our exact fixes for the other four scripts:
2. **In `init_board_workspace.py`**:
   - Line 209: Change `choices=["red", "blue", "purple"]` to `choices=["plan", "red", "blue", "purple"]` and update help text to `"Operating mode: plan (Pre-Code Plan Siege), red (Red-Team), blue (Blue-Team Tournament), or purple (Hybrid)"`.
   - Lines 123–128: Normalize `norm_mode = (mode or "red").strip().lower()` and `norm_domain = (domain or "coding").strip().lower()` right alongside `norm_effort`, and use `norm_mode` and `norm_domain` everywhere (lines 81, 82, 144, 145, 168, 169, 178, 179) so `mode=None` or `domain=None` can never raise `AttributeError`.
   - Lines 160–162: Add `--force` CLI flag (`action="store_true"`). Only write `board_config.json` if `not config_path.exists() or force`, or if `config_path.exists()` and not `force`, preserve existing `current_wave`, `converged`, and `subagent_ids` while updating metadata!
3. **In `split_personas_to_files.py`**:
   - In `extract_persona_blocks()` (lines 108–115):
     Reject any heading that starts with `Category`, `Division`, `Part`, or `Section` (`re.match(r"^(?:Category|Division|Part|Section)\b", heading_text, re.IGNORECASE)`) OR contains an ID range (`re.search(r"(?:REAL|MERC)-[A-Z]+-\d+`?\s*(?:\.\.|–|—|-|to)\s*`?(?:REAL|MERC)-[A-Z]+-\d+", heading_text)`).
   - In `slugify_persona_name()` (lines 67–85):
     1. Strip the `^(?:REAL|MERC)-[A-Z]+-\d+\s*[:\-–—]\s*` and `^#?\d+[\.\:\-\s]+` prefixes first.
     2. Strip the role description suffix after ` — `, ` – `, or ` - ` (`re.split(r"\s+(?:—|–|--)\s+", cleaned, maxsplit=1)[0]`) so filenames are concise, human-readable persona names (`dr_viktor_the_redline_kaczmarek.md` instead of 120-character biographies that risk `MAX_PATH` overflow!).
     3. Before stripping parentheses, if a parenthetical immediately follows a non-ASCII CJK character (e.g. `Dr.卢 (Lu)`), unwrap the parenthetical into ASCII (`re.sub(r"([^\x00-\x7F]+)\s*\(([A-Za-z0-9\s\-']+)\)", r" \2 ", cleaned)`) so `Dr.卢 (Lu)` becomes `Dr. Lu` instead of deleting both `卢` and `(Lu)`! Then strip remaining parenthetical dates/locations (`re.sub(r"\([^)]*\)", "", cleaned)`).
     4. Apply an extended Latin transliteration map (`Ł->L`, `ł->l`, `Ø->O`, `ø->o`, `Đ->D`, `đ->d`, `ß->ss`, `Æ->AE`, `æ->ae`, `Œ->OE`, `œ->oe`) before `unicodedata.normalize("NFKD", cleaned)`.
     5. Guard against Windows reserved device names (`{"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}`) by appending `_persona`, and cap slug length at `64` characters.
   - In `split_collection()` (lines 168–190):
     1. Before writing files into `cat_dir`, remove stale `.md` files (`for old_file in cat_dir.glob("*.md"): old_file.unlink()`) so the 35 bogus `category_*.md` and `division_*.md` files are automatically purged.
     2. Track `used_slugs: Set[str] = set()` per category and if `file_slug in used_slugs`, append `_{persona_id.lower().replace('-', '_')}` so two personas can never silently overwrite each other.
     3. Update the docstring at line 12 to accurately state `personas/strike_teams_individual/<category>/<mercenary_slug>.md`.
4. **In `install.ps1` and `install.sh`**:
   - In `install.ps1` line 21: Expand `@("references", "examples", "scripts")` to `@("personas", "references", "examples", "scripts", "commands")` and remove stale destination subdirectories before copying (`if (Test-Path $DstSub) { Remove-Item -Recurse -Force $DstSub }`) so no zombie files survive across upgrades.
   - In `install.sh` lines 10 & 14–23:
     1. Validate `TARGET` with a `case "${TARGET}" in all|agy|claude|workspace) ;; *) ... exit 1 ;; esac` block so typos or `--help` fail fast with exit code `1` and usage instructions.
     2. In `install_skill_dir()`, loop over `for sub in personas references examples scripts commands; do` and copy the full directory tree (`rm -rf "${dest_dir}/${sub}" && mkdir -p "${dest_dir}/${sub}" && cp -rf "${REPO_ROOT}/${sub}/." "${dest_dir}/${sub}/"`) so all 500+ persona `.md` files, Boardroom manifests, references, examples, scripts, and commands are installed intact!

**Cassian "Schema-Lock" Vane**: `[00:45:12]` Let's compile the formal **Surviving Vector Ledger (`F3-V1` .. `F3-V12`)** with exact file paths, line numbers, severity classifications, and complete drop-in code fixes. We are withholding our White Flag in Wave `v1`—12 verified bugs (`3 CRITICAL`, `5 HIGH`, `4 MEDIUM`) are on the slab. Seal the tape and transmit to The Board!

---

## PART II: INTERNAL PUSHBACK SUMMARY (MASK 2 FALSIFICATION LOG)

To maintain strict compliance with Mandatory Recording Law #2, the following three initial attack hypotheses raised in Bunker-03 were **falsified and rejected** by **General Cassius "Zero-Trust" Sterling (`MERC-SW-16`)** upon line-by-line inspection of the target scripts:

1. **Rejected Hypothesis #1 (Windows `cp1252` Console Emoji Crash & `pythonw` `sys.stdout is None` Crash)**:
   - *Initial Claim*: Printing `🏛️⚔️` and `🏳️` in `verify_convergence.py:196` and `init_board_workspace.py:177` crashes on Windows default `cp1252` consoles, or `.reconfigure()` crashes when `sys.stdout` is `None`.
   - *Ground-Truth Falsification*: All three Python scripts (`verify_convergence.py:27-38`, `init_board_workspace.py:27-38`, `split_personas_to_files.py:29-40`) implement `configure_utf8_console()` with explicit `if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):` guards, `encoding="utf-8", errors="replace"`, and `try / except Exception: pass`, plus `errors="replace"` on all `read_text()` calls (`verify_convergence.py:71,175`, `split_personas_to_files.py:166`).
2. **Rejected Hypothesis #2 (`--max-waves` Memory Exhaustion / Negative Wave Count in `init_board_workspace.py`)**:
   - *Initial Claim*: Passing `--max-waves 10000000` or `--max-waves -5` causes `build_convergence_tracker_markdown()` (`init_board_workspace.py:71`) to hang allocating millions of table rows or emit a broken 0-row table.
   - *Ground-Truth Falsification*: `init_board_workspace.py` lines 130–131 explicitly guard `max_waves is not None and max_waves > 0` and clamp `resolved_waves = max(1, min(resolved_waves, 30))` before invoking `build_convergence_tracker_markdown()`.
3. **Rejected Hypothesis #3 (Latin Diacritic Corruption in `split_personas_to_files.py`)**:
   - *Initial Claim*: European names with diacritics (`Kurt Gödel`, `Rudolf E. Kálmán`, `Erwin Schrödinger`, `Fernando Corbató`) have their accented letters stripped into `kurt_gdel` or throw `UnicodeEncodeError`.
   - *Ground-Truth Falsification*: `split_personas_to_files.py` lines 79–80 run `unicodedata.normalize("NFKD", cleaned)` prior to `.encode("ascii", "ignore")`, which cleanly decomposes precomposed Latin accents into base ASCII letters (`kurt_godel.md`, `rudolf_e_kalman.md`, `erwin_schrodinger.md`, `fernando_corbato.md`). Only non-NFKD-decomposable characters (`卢`, `Ł`, `Ø`, `ß`) and parenthetical romanizations stripped prematurely at line 74 (`Dr.卢 (Lu)`) fail.

---

## PART III: SURVIVING VECTOR LEDGER (`FIRM 3` — WAVE `v1`)

| Vector ID | Severity | Target File & Exact Line Numbers | Vulnerability / Soundness Failure Summary | Exact Code Fix Required |
| :--- | :---: | :--- | :--- | :--- |
| `F3-V1` | `CRITICAL` | `scripts/verify_convergence.py` (Lines `46–49`, `82–84`) | **Unanchored & Negation-Blind `WHITE_FLAG_RE` Spoofing**: `WHITE_FLAG_RE.search(text)` matches anywhere in the file, triggering `has_white_flag_phrase = True` when a Firm writes `"NO WHITE FLAG RAISED"`, `"We do NOT have 0 surviving vectors"`, or quotes the prompt rule `"WHITE FLAG RAISED"` in dialogue. | Replace `WHITE_FLAG_RE` with a line-anchored certificate matcher `WHITE_FLAG_CERT_RE` + negation/withheld guard (`WHITE_FLAG_NEGATION_RE` / `OPEN_STATUS_RE`) so negated lines, prompt quotes, or `[STATUS: OPEN VECTORS REMAIN // WHITE FLAG WITHHELD]` never trigger `has_white_flag_phrase = True`. |
| `F3-V2` | `CRITICAL` | `scripts/verify_convergence.py` (Lines `6–12`, `84`, `93`, `138–143`, `164–182`) | **Dead `meets_length`, `dialogue_turns`, and `board_lines` Checks in `is_white_flag` & `converged`**: `audit_single_firm_file()` computes `"meets_length": line_count >= min_lines` (line 93) and `"dialogue_turns": dialogue_count` (line 90), and `main()` computes `board_lines` (line 174), but **never checks any of them** in `is_white_flag` (line 84) or `converged` (line 181). Five 1-line stub files + a 0-byte `BOARD.md` pass with exit code `0` (`CONVERGED`). | Add `--min-turns` (default `10`) and `--min-board-lines` (default `100`). Gate `is_white_flag` on `meets_length and meets_turns`, and gate `converged` on `board_exists and (board_lines >= args.min_board_lines)`. Show `⚠️ SHORT` in table status when length/turn checks fail. |
| `F3-V3` | `HIGH` | `scripts/verify_convergence.py` (Lines `50–53`, `80`) | **`CRITICAL_HIGH_SURVIVING_RE` Misses `MEDIUM` Vectors, Bold/Formatted Cells, Multi-Column Layouts, Letter Firm IDs (`FA..FE`), and False-Matches Closed Wave `v1` Vectors**: Line 51 (`\|\s*`?F[1-5]-V\d+`?\s*\|\s*`?(CRITICAL\|HIGH)`?\s*\|`) ignores `MEDIUM` bugs, fails if cells use bold `**F3-V1**` or `**CRITICAL**`, fails if Severity is in column 3+, fails on `FA-V1`, and falsely counts rows marked `FIXED` / `RESOLVED` in Wave `v2+`. | Replace with line-level table scanner `extract_open_vectors(text)` that matches `F[1-5A-E]-V\d+` with `CRITICAL\|HIGH\|MEDIUM` in any column of the table row (`**`, `` ` ``, or plain), while excluding rows containing `FIXED`, `RESOLVED`, `CLOSED`, `NEUTRALIZED`, or `REMEDIATED`. |
| `F3-V4` | `HIGH` | `scripts/verify_convergence.py` (Line `45`, `76–77`) | **`DIALOGUE_SPEAKER_RE` Rejects Quoted Callsigns & Unicode Names While Matching Metadata Bullets**: Line 45 (`[A-Z][A-Za-z0-9\.\-\s\(\)]{2,45}`) rejects double quotes (`**Cassian "Schema-Lock" Vane**:`), apostrophes (`O'Connor`), backticks, em-dashes, and accented characters (`Kurt Gödel`, `Rudolf E. Kálmán`), while optional `\**` causes plain metadata lines (`- **Target Artifacts**: ...`) to be counted as dialogue turns. | Require bold speaker syntax `^\s*(?:[-*]\s+)?\*\*([^*\n]{2,90}?)\*\*\s*:\s+\S+` allowing quotes, Unicode word chars, apostrophes, and role tags, and filter out non-speaker metadata headers (`Target Artifacts`, `Saved Recording Path`, `Assigned Orthogonal Pillar`, `ID`, `Category`, etc.). |
| `F3-V5` | `MEDIUM` | `scripts/verify_convergence.py` (Lines `107–121`, `164`, `181`) | **`locate_firm_files` Substring Collision on `"board"` & Hardcoded 5-Firm Count**: Checking `if "board" in name_lower:` (line 109) *before* checking `firm1..5` causes files like `firm1_boardroom_personas.md`, `firm2_dashboard_ui.md`, or `firm3_motherboard.md` to be misclassified as `board_files` and marked `MISSING` in `firm_map`. Hardcoding `5` firms also breaks `--effort strike` (`1–2` firms). | Match `firm1..5` / `firm_a..e` first in `locate_firm_files()`, restrict `board_files` to filenames matching `r"(?:^|[_\-])board(?:[_\-\.]|$)"` that are not Firm files, and support `--expected-firms` (auto-reading `board_config.json` when available). |
| `F3-V6` | `HIGH` | `scripts/init_board_workspace.py` (Lines `206–212`) | **`--mode plan` Rejected by `argparse` Despite Being Mode #1 in `SKILL.md`**: `SKILL.md` (lines 32, 69, 79–80) defines four operating modes (`plan`, `red`, `blue`, `purple`), but `init_board_workspace.py` line 209 sets `choices=["red", "blue", "purple"]`, crashing with exit code `2` whenever `--mode plan` is passed. | Update `choices=["plan", "red", "blue", "purple"]` at line 209 and update `--mode` help text. |
| `F3-V7` | `MEDIUM` | `scripts/init_board_workspace.py` (Lines `81`, `143–179`) | **Unconditional Overwrite of `board_config.json` & Unguarded `mode.upper()`**: Line 161 overwrites `board_config.json` unconditionally even when `CONVERGENCE_TRACKER.md` is preserved (line 165), wiping live `current_wave` and `subagent_ids`. Also `mode.upper()` at lines 81 & 178 uses raw `mode` instead of normalized `norm_mode`. | Normalize `norm_mode = (mode or "red").strip().lower()` and `norm_domain = (domain or "coding").strip().lower()` at the start of `init_workspace()`, add `--force`, and preserve existing `board_config.json` state unless `--force` is passed. |
| `F3-V8` | `CRITICAL` | `scripts/split_personas_to_files.py` (Lines `108–140`) | **`extract_persona_blocks` Matches `## Category ...` and `## DIVISION ...` Headers Containing ID Ranges, Generating 35 Bogus `.md` Files & Duplicate IDs**: Section headers like `## Category I: ... (\`MERC-SW-01\` .. \`MERC-SW-05\`)` match `re.search(r"(?:REAL\|MERC)-[A-Z0-9\-]+", heading_text)` at line 110, creating 35 bogus `.md` files (`category_i_*.md`, `division_i_*.md`) with duplicate IDs (`MERC-SW-01` twice in `INDEX.md`). | Reject headings starting with `Category`, `Division`, `Part`, or `Section` (`re.match(r"^(?:Category\|Division\|Part\|Section)\b", heading_text, re.IGNORECASE)`) or containing ID ranges (`..`, `–`, `—` between two IDs). |
| `F3-V9` | `HIGH` | `scripts/split_personas_to_files.py` (Lines `67–85`, `136–137`) | **`slugify_persona_name` Deletes Parenthetical Romanizations (`Dr.卢 (Lu)`), Fails to Strip Role Suffixes (120+ Char Filenames), Drops `Ł/Ø/ß`, and Lacks Windows Reserved-Name / Collision Guards**: Line 74 strips `(Lu)` before line 80 strips `卢`, erasing `Lu` (`MERC-SW-26`). Missing ` — <Role>` stripping creates 110–126 char filenames risking Windows `MAX_PATH` overflow. | Unwrap ASCII romanizations after CJK chars before stripping parentheticals, strip ` — <Role>` suffixes in `slugify_persona_name()`, transliterate `Ł/Ø/Đ/ß/Æ/Œ`, cap slug length, guard Win32 reserved names (`con`, `prn`, `aux`, `nul`, `com1..9`, `lpt1..9`), and deduplicate colliding slugs in `split_collection()`. |
| `F3-V10` | `MEDIUM` | `scripts/split_personas_to_files.py` (Lines `12`, `168–190`, `207`) | **Stale Zombie `.md` Files Never Purged on Re-Split & Docstring Path Mismatch**: `split_collection()` writes into `cat_dir` without unlinking old `.md` files, leaving the 35 bogus `category_*.md` / `division_*.md` files on disk forever. Line 12 docstring says `personas/strike_teams/<category>/` instead of `personas/strike_teams_individual/<category>/`. | Unlink existing `*.md` files in `cat_dir` before writing fresh persona files in `split_collection()`, and update line 12 docstring to `personas/strike_teams_individual/<category>/<mercenary_slug>.md`. |
| `F3-V11` | `CRITICAL` | `scripts/install.ps1` (Line `21`) & `scripts/install.sh` (Lines `17–21`) | **Both Installers Completely Omit the `personas/` and `commands/` Directories**: `install.ps1` line 21 and `install.sh` lines 17–21 only copy `references`, `examples`, and `scripts`. All 500+ persona `.md` files (`personas/board_members/`, `personas/boardrooms/`, `personas/strike_teams/`, `personas/strike_teams_individual/`) and `commands/` are omitted, breaking every persona path in `SKILL.md`! | Add `"personas"` and `"commands"` to the directory list in both `install.ps1` and `install.sh` so the complete `personas/` hierarchy and `commands/` directory are recursively copied into every target skill directory. |
| `F3-V12` | `MEDIUM` | `scripts/install.sh` (Lines `10`, `14–38`) & `scripts/install.ps1` (Lines `21–28`) | **`install.sh` Exits `0` Silently on Invalid Target Argument & Uncleaned Destination Directories Retain Stale Files**: Passing an invalid target (e.g. `./install.sh claud` or `--help`) matches no `if` block and exits `0` silently. Both installers also merge-copy over old directories without cleaning stale removed files. | Add a `case "${TARGET}" in all\|agy\|claude\|workspace) ;; *) ... exit 1 ;; esac` validation block in `install.sh`, and clean destination subdirectories before copying in both `install.sh` and `install.ps1`. |

---

## PART IV: EXACT DROP-IN PATCH SPECIFICATIONS FOR PILLAR III (`SCRIPTS/`)

### 1. Patch for `scripts/verify_convergence.py` (`F3-V1`, `F3-V2`, `F3-V3`, `F3-V4`, `F3-V5`)

```python
# Replace lines 45-122 of scripts/verify_convergence.py with:
DIALOGUE_SPEAKER_RE = re.compile(
    r"^\s*(?:[-*]\s+)?\*\*([^*\n]{2,90}?)\*\*\s*:\s+\S+",
    re.MULTILINE,
)
NON_SPEAKER_METADATA_KEYS = {
    "target artifacts",
    "target artifacts under forensic vivisection",
    "target artifacts under review",
    "assigned orthogonal pillar",
    "saved recording path",
    "triad roster",
    "mask 1",
    "mask 2",
    "mask 3",
    "project / target",
    "operating mode",
    "domain playbook",
    "effort level",
    "initialized",
    "id",
    "category",
    "status",
    "verdict",
    "rule",
    "fix",
    "vector",
    "severity",
    "file",
    "summary",
    "initial claim",
    "ground-truth falsification",
}

WHITE_FLAG_CERT_RE = re.compile(
    r"^\s*(?:#+\s*|>+\s*|\*\*|\[)*\s*(?:STATUS\s*:\s*)?(?:WHITE[\s\-]+FLAG\s+RAISED|FORMAL\s+WHITE[\s\-]+FLAG|UNCONDITIONAL\s+SURRENDER|SURVIVING\s+(?:NON-SUICIDAL\s+)?VECTORS\s*:\**\s*0\b|0\s+SURVIVING\s+(?:NON-SUICIDAL\s+)?VECTORS)\b",
    re.IGNORECASE | re.MULTILINE,
)
WHITE_FLAG_NEGATION_RE = re.compile(
    r"\b(?:no|not|never|cannot|can't|without|withheld|false|reject|rejected|denies|denied|pending|until|unless|if)\b",
    re.IGNORECASE,
)
OPEN_STATUS_RE = re.compile(
    r"WHITE[\s\-]+FLAG\s+WITHHELD|OPEN\s+VECTORS\s+REMAIN",
    re.IGNORECASE,
)
SURVIVING_VECTOR_ROW_RE = re.compile(
    r"^\s*\|[^|\n]*`?\**F(?:0?[1-5]|[A-E])-V\d+\**`?\s*\|[^\n]*\b(CRITICAL|HIGH|MEDIUM)\b[^\n]*\|",
    re.IGNORECASE | re.MULTILINE,
)
CLOSED_VECTOR_ROW_RE = re.compile(
    r"\b(?:FIXED|RESOLVED|CLOSED|NEUTRALIZED|REMEDIATED|VERIFIED\s+FIXED)\b",
    re.IGNORECASE,
)


def count_dialogue_turns(text: str) -> int:
    """Count authentic persona dialogue turns while filtering out metadata bullets."""
    if not text:
        return 0
    count = 0
    for match in DIALOGUE_SPEAKER_RE.finditer(text):
        speaker_raw = match.group(1).strip()
        speaker_norm = re.sub(r"\([^)]*\)", "", speaker_raw).strip().lower()
        if speaker_norm in NON_SPEAKER_METADATA_KEYS or speaker_raw.lower() in NON_SPEAKER_METADATA_KEYS:
            continue
        if speaker_norm.startswith(("mask 1", "mask 2", "mask 3", "part ", "step ", "phase ", "wave ")):
            continue
        count += 1
    return count


def count_open_vectors(text: str) -> int:
    """Count open CRITICAL, HIGH, or MEDIUM vector rows in Markdown tables."""
    if not text:
        return 0
    open_count = 0
    for match in SURVIVING_VECTOR_ROW_RE.finditer(text):
        row_text = match.group(0)
        if not CLOSED_VECTOR_ROW_RE.search(row_text):
            open_count += 1
    return open_count


def has_verified_white_flag_certificate(text: str) -> bool:
    """Verify an affirmative, un-negated White-Flag certificate line is present."""
    if not text or OPEN_STATUS_RE.search(text):
        return False
    for match in WHITE_FLAG_CERT_RE.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.end())
        if line_end == -1:
            line_end = len(text)
        full_line = text[line_start:line_end]
        if not WHITE_FLAG_NEGATION_RE.search(full_line):
            return True
    return False
```

### 2. Patch for `scripts/init_board_workspace.py` (`F3-V6`, `F3-V7`)

- Add `"plan"` to `choices=["plan", "red", "blue", "purple"]` at line 209.
- Normalize `norm_mode = (mode or "red").strip().lower()` and `norm_domain = (domain or "coding").strip().lower()` at the top of `init_workspace()`.
- Guard `board_config.json` writes when `config_path.exists()` unless `--force` is specified, preserving `current_wave`, `converged`, and `subagent_ids`.

### 3. Patch for `scripts/split_personas_to_files.py` (`F3-V8`, `F3-V9`, `F3-V10`)

- Filter out `Category` / `Division` section headings and ID-range headings (`MERC-SW-01 .. MERC-SW-05`) in `extract_persona_blocks()`.
- In `slugify_persona_name()`, strip ` — <Role Suffix>`, preserve parenthetical ASCII romanizations following CJK ideographs (`Dr.卢 (Lu)` -> `Dr. Lu`), transliterate `Ł/Ø/Đ/ß/Æ/Œ`, cap slug length, and guard Windows reserved filenames (`con`, `prn`, `aux`, `nul`, `com1..9`, `lpt1..9`).
- In `split_collection()`, unlink stale `*.md` files in `cat_dir` prior to writing and deduplicate any colliding slugs.

### 4. Patch for `scripts/install.ps1` and `scripts/install.sh` (`F3-V11`, `F3-V12`)

- Copy `personas`, `references`, `examples`, `scripts`, and `commands` in both `install.ps1` and `install.sh`.
- Add target validation (`all | agy | claude | workspace`) to `install.sh` so invalid targets fail with exit code `1`.

---

`[STATUS: OPEN VECTORS REMAIN // WHITE FLAG WITHHELD // 12 SURVIVING VECTORS (3 CRITICAL, 5 HIGH, 4 MEDIUM)]`
`[END OF BUNKER-03 RECORDING // TRANSMITTING TO THE BOARD]`
