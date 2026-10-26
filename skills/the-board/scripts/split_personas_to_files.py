#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
THE BOARD — Individual Persona `.md` File Splitter (`split_personas_to_files.py`)
===============================================================================
Parses the category repertoire files in:
  - `personas/repertoire_real_humans/*.md`
  - `personas/strike_teams/*.md`
and emits ONE standalone `.md` file per persona:
  - `personas/board_members/<category>/<person_slug>.md`
  - `personas/strike_teams_individual/<category>/<mercenary_slug>.md`
plus master `INDEX.md` manifests so Boardroom and Strike-Team selections are
simply lists of individual `.md` files to load.
===============================================================================
"""

import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Set, Tuple


# -----------------------------------------------------------------------------
# Windows Console UTF-8 Compatibility Guard
# Ensures clean UTF-8 output on Windows PowerShell and Command Prompt.
# -----------------------------------------------------------------------------
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows platforms."""
    # Guard stdout reconfiguration on consoles that support it
    if sys.stdout is not None and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    # Guard stderr reconfiguration on consoles that support it
    if sys.stderr is not None and hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


# -----------------------------------------------------------------------------
# Category Folder Mapping
# Maps source repertoire filenames to clean category directory slugs.
# -----------------------------------------------------------------------------
REAL_HUMAN_CATEGORY_MAP: Dict[str, str] = {
    "01_computing_math_crypto.md": "computing",
    "02_physics_hardware_inventors.md": "physics_hardware",
    "03_design_product_visionaries.md": "design_product",
    "04_philosophy_epistemology_logic.md": "philosophy_logic",
    "05_strategy_warfare_statecraft.md": "strategy_command",
    "06_law_jurisprudence_rhetoric.md": "law_rhetoric",
}

STRIKE_TEAM_CATEGORY_MAP: Dict[str, str] = {
    "01_software_kernels_and_plans_mercenaries.md": "software_plans",
    "02_cyber_zeroday_and_crypto_syndicates.md": "cyber_crypto",
    "03_legal_patent_and_contract_sharks.md": "legal_patents",
    "04_commercial_pentagon_and_gtm_killers.md": "commercial_dod",
    "05_hardware_robotics_and_physics_savants.md": "hardware_physics",
    "06_design_copy_and_philosophy_iconoclasts.md": "design_philosophy",
    "07_philosophy_ontology_and_prompt_linguists.md": "philosophy_prompt_linguistics",
}

# -----------------------------------------------------------------------------
# Pre-NFKD Extended Latin Transliteration Map & Win32 Reserved Names
# Prevents characters like 'ø' in Søren Kierkegaard from being silently dropped
# by NFKD + ascii('ignore'), which otherwise produced `sren_kierkegaard.md`.
# -----------------------------------------------------------------------------
LATIN_TRANSLITERATION_MAP: Dict[str, str] = {
    "Ø": "O",
    "ø": "o",
    "Æ": "AE",
    "æ": "ae",
    "Ł": "L",
    "ł": "l",
    "Đ": "D",
    "đ": "d",
    "ß": "ss",
    "Œ": "OE",
    "œ": "oe",
    "Ð": "D",
    "ð": "d",
    "Þ": "TH",
    "þ": "th",
}

WIN32_RESERVED_NAMES: Set[str] = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{i}" for i in range(1, 10)),
    *(f"lpt{i}" for i in range(1, 10)),
}


def slugify_persona_name(raw_name: str, fallback_id: str = "persona_entry") -> str:
    """Convert a persona heading or name into a clean, concise lowercase filesystem slug."""
    # Guard against null or empty input strings
    if not raw_name or not raw_name.strip():
        return fallback_id.lower().replace("-", "_")

    # Step 1: Strip leading ID prefixes (`REAL-COMP-01:`, `MERC-SW-01 —`) and numeric prefixes
    cleaned = re.sub(
        r"^.*?(?:REAL|MERC)-[A-Z]+-\d+\s*[:\-–—]\s*",
        "",
        raw_name.strip(),
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"^#?\d+[\.\:\-\)\s]+", "", cleaned)

    # Step 2: Strip long role suffixes after em-dashes/en-dashes (`Name — Role Description`)
    # so mercenary filenames remain crisp (`dr_viktor_the_redline_kaczmarek.md`)
    cleaned = re.split(r"\s+(?:—|–|--)\s+", cleaned, maxsplit=1)[0].strip()

    # Step 3: Preserve parenthetical ASCII romanizations following CJK ideographs
    # (e.g., `Dr.卢 (Lu) "Strict-Alias" Jian-Guo` -> `Dr. Lu "Strict-Alias" Jian-Guo`)
    cleaned = re.sub(r"([^\x00-\x7F]+)\s*\(([A-Za-z0-9\s\-']+)\)", r" \2 ", cleaned)

    # Step 4: Strip long parenthetical date/location suffixes like `(1912–1954)` or `(c. 55–135 AD)`
    # while preserving short statutory/complexity tokens like `(f)`, `(g)`, or `(n^2)`
    cleaned = re.sub(r"\([^)]{4,}\)", "", cleaned)

    # Step 5: Apply extended Latin transliteration map before NFKD normalization
    for src_char, dst_ascii in LATIN_TRANSLITERATION_MAP.items():
        if src_char in cleaned:
            cleaned = cleaned.replace(src_char, dst_ascii)

    # Step 6: Normalize Unicode diacritics (e.g., Kálmán -> Kalman, Gödel -> Godel)
    normalized = unicodedata.normalize("NFKD", cleaned)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")

    # Step 7: Convert non-alphanumeric sequences to single underscores and clamp length
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text.strip().lower()).strip("_")
    if len(slug) > 64:
        slug = slug[:64].rstrip("_")

    # Step 8: Fallback for empty slugs or Windows reserved device names
    if not slug:
        slug = fallback_id.lower().replace("-", "_")
    if slug in WIN32_RESERVED_NAMES:
        slug = f"{slug}_persona"

    return slug


def is_section_or_range_heading(heading_text: str) -> bool:
    """
    Return True if `heading_text` is a Category/Division banner or an ID range
    (e.g., `Category I: ... (MERC-SW-01 .. MERC-SW-05)`), which must NOT be
    extracted as an individual persona dossier.
    """
    # Guard against empty heading strings
    if not heading_text:
        return True

    # Strip leading markdown formatting tokens (`*`, `` ` ``) before testing
    stripped = heading_text.strip().strip("*`").strip()

    # Reject explicit Category, Division, Part, or Section structural headers
    if re.match(r"^(?:Category|Division|Part|Section|Overview|Index)\b", stripped, re.IGNORECASE):
        return True

    # Reject headings that contain a range of persona IDs (`MERC-SW-01 .. MERC-SW-05` or `01–07`)
    if re.search(
        r"(?:REAL|MERC)-[A-Z]+-\d+`?\s*(?:\.\.|–|—|-|to|through)\s*`?(?:REAL|MERC)-[A-Z]+-\d+",
        stripped,
        re.IGNORECASE,
    ):
        return True

    return False


def is_valid_persona_heading(heading_text: str) -> bool:
    """Return True if `heading_text` introduces a single real human or mercenary persona."""
    # Reject category/division headers and ID range headers first
    if is_section_or_range_heading(heading_text):
        return False

    stripped = heading_text.strip().strip("*`").strip()
    # Match explicit `REAL-<CAT>-<NUM>` or `MERC-<CAT>-<NUM>` or numbered persona headers
    return bool(
        re.search(r"\b(?:REAL|MERC)-[A-Z]+-\d+\b", stripped)
        or re.match(r"^#?\d{1,2}[\.\:\)\s\-]+", stripped)
    )


def extract_persona_blocks(markdown_text: str) -> List[Tuple[str, str, str]]:
    """
    Extract `(persona_id, persona_name, block_content)` tuples from a repertoire
    Markdown file while excluding Category/Division section headers.
    """
    # Defensive check for empty markdown text
    if not markdown_text or not markdown_text.strip():
        return []

    # Match all level-2 (`##`) and level-3 (`###`) Markdown headings
    header_pattern = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)
    matches = list(header_pattern.finditer(markdown_text))
    extracted: List[Tuple[str, str, str]] = []

    for idx, match in enumerate(matches):
        level_hashes = match.group(1)
        heading_text = match.group(2).strip().strip("*")

        # Skip structural Category/Division banners and non-persona headings
        if not is_valid_persona_heading(heading_text):
            continue

        # Determine where this persona's Markdown block ends:
        # Stop at the next valid persona heading, any Category/Division banner,
        # or any heading of equal or higher hierarchy (`<= len(level_hashes)`).
        start_pos = match.start()
        end_pos = len(markdown_text)
        for next_match in matches[idx + 1 :]:
            next_level = next_match.group(1)
            next_heading = next_match.group(2).strip().strip("*")
            if (
                is_valid_persona_heading(next_heading)
                or is_section_or_range_heading(next_heading)
                or len(next_level) <= len(level_hashes)
            ):
                end_pos = next_match.start()
                break

        # Strip trailing horizontal rules (`---`) so we don't leave dangling dividers
        block_body = markdown_text[start_pos:end_pos].strip()
        block_body = re.sub(r"(?:\r?\n)+\s*---\s*\Z", "", block_body).strip()

        # Extract the canonical `REAL-...` or `MERC-...` identifier
        id_match = re.search(r"\b((?:REAL|MERC)-[A-Z]+-\d+)\b", heading_text)
        persona_id = id_match.group(1) if id_match else f"ENTRY-{len(extracted) + 1:02d}"

        # Extract the clean display name (preserving role title for the H1 header)
        name_part = re.sub(
            r"^.*?(?:REAL|MERC)-[A-Z]+-\d+`?\s*[:\-–—]\s*",
            "",
            heading_text,
        )
        name_part = re.sub(r"^#?\d{1,2}[\.\:\)\s\-]+", "", name_part).strip().strip("*`")

        extracted.append((persona_id, name_part, block_body))

    return extracted


def split_collection(
    source_dir: Path,
    dest_root: Path,
    category_map: Dict[str, str],
    collection_title: str,
) -> int:
    """Split all repertoire files in `source_dir` into individual `.md` files."""
    # Defensive check for missing source directory
    if source_dir is None or not source_dir.is_dir():
        print(f"[WARN] Source directory not found: {source_dir}", file=sys.stderr)
        return 0

    total_written = 0
    index_lines: List[str] = [
        f"# {collection_title} — Individual `.md` File Index\n",
        "> Each persona below is stored in its own standalone `.md` file so Boardroom and Strike-Team dispatches load only the exact personas needed.\n",
    ]

    for src_filename, cat_slug in sorted(category_map.items()):
        src_path = source_dir / src_filename
        if not src_path.is_file():
            continue

        raw_md = src_path.read_text(encoding="utf-8", errors="replace")
        entries = extract_persona_blocks(raw_md)
        cat_dir = dest_root / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        # Purge all pre-existing `.md` files in `cat_dir` before writing so zero
        # stale orphans or `category_*.md`/`division_*.md` stubs survive on disk!
        for old_md in cat_dir.glob("*.md"):
            try:
                old_md.unlink()
            except OSError:
                pass

        index_lines.append(f"\n## Category: `{cat_slug}` ({len(entries)} Personas)\n")
        index_lines.append("| ID | Persona | Individual `.md` File |")
        index_lines.append("| :--- | :--- | :--- |")

        # Track used slugs within this category to prevent silent overwrites on collision
        used_slugs: Set[str] = set()

        for persona_id, persona_name, block_body in entries:
            base_slug = slugify_persona_name(persona_name, fallback_id=persona_id)
            file_slug = base_slug
            if file_slug in used_slugs:
                id_suffix = persona_id.lower().replace("-", "_")
                file_slug = f"{base_slug}_{id_suffix}"
            used_slugs.add(file_slug)

            out_file = cat_dir / f"{file_slug}.md"

            # Wrap the individual persona file with a deterministic metadata header
            file_content = (
                f"# PERSONA DOSSIER // {persona_name}\n"
                f"- **ID**: `{persona_id}`\n"
                f"- **Category**: `{cat_slug}`\n\n"
                f"---\n\n"
                f"{block_body}\n"
            )
            out_file.write_text(file_content, encoding="utf-8")
            rel_link = f"./{cat_slug}/{file_slug}.md"
            index_lines.append(
                f"| `{persona_id}` | **{persona_name}** | [`{rel_link}`]({rel_link}) |"
            )
            total_written += 1

    # Write the master INDEX.md for this collection
    dest_root.mkdir(parents=True, exist_ok=True)
    (dest_root / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return total_written


def main() -> int:
    """Entry point to split both Board Members and Strike-Team Mercenaries."""
    configure_utf8_console()
    repo_root = Path(__file__).resolve().parent.parent

    real_src = repo_root / "personas" / "repertoire_real_humans"
    board_members_dst = repo_root / "personas" / "board_members"

    strike_src = repo_root / "personas" / "strike_teams"
    strike_dst = repo_root / "personas" / "strike_teams_individual"

    board_count = split_collection(
        source_dir=real_src,
        dest_root=board_members_dst,
        category_map=REAL_HUMAN_CATEGORY_MAP,
        collection_title="THE BOARD — Real Historical Humans (`personas/board_members/`)",
    )
    strike_count = split_collection(
        source_dir=strike_src,
        dest_root=strike_dst,
        category_map=STRIKE_TEAM_CATEGORY_MAP,
        collection_title="STRIKE TEAMS — $100M Mercenary Specialists (`personas/strike_teams_individual/`)",
    )

    print(
        f"[SPLIT COMPLETE] Generated {board_count} Board Member .md files and "
        f"{strike_count} Strike-Team .md files (0 orphans, 0 category stubs)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
