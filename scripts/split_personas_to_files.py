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
  - `personas/strike_teams/<category>/<mercenary_slug>.md`
plus master `INDEX.md` manifests so Boardroom selections are simply lists of
individual `.md` files to load.
===============================================================================
"""

import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Tuple


# -----------------------------------------------------------------------------
# Windows Console UTF-8 Compatibility Guard
# Ensures clean UTF-8 output on Windows PowerShell and Command Prompt.
# -----------------------------------------------------------------------------
def configure_utf8_console() -> None:
    """Reconfigure stdout and stderr to UTF-8 on Windows platforms."""
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


def extract_persona_blocks(markdown_text: str) -> List[Tuple[str, str, str]]:
    """
    Extract `(persona_id, persona_name, block_content)` tuples from a repertoire
    Markdown file. Matches `## ` or `### ` headers containing `REAL-...`, `MERC-...`,
    or numbered persona headings.
    """
    if not markdown_text:
        return []

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

        # Determine where this persona's markdown block ends
        start_pos = match.start()
        end_pos = len(markdown_text)
        for next_match in matches[idx + 1 :]:
            next_heading = next_match.group(2).strip().strip("*")
            next_is_persona = bool(
                re.search(r"(?:REAL|MERC)-[A-Z0-9\-]+", next_heading)
                or re.match(r"^#?\d{1,2}[\.\:\)\s\-]+", next_heading)
            )
            if next_is_persona or len(next_match.group(1)) <= len(level_hashes):
                end_pos = next_match.start()
                break

        block_body = markdown_text[start_pos:end_pos].strip()

        # Extract ID if present, otherwise synthesize one
        id_match = re.search(r"((?:REAL|MERC)-[A-Z]+-\d+)", heading_text)
        persona_id = id_match.group(1) if id_match else f"ENTRY-{idx+1:02d}"

        # Extract human-readable name after the colon or number prefix
        name_part = re.sub(r"^.*?(?:REAL|MERC)-[A-Z]+-\d+\s*[:\-–—]\s*", "", heading_text)
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

        index_lines.append(f"\n## Category: `{cat_slug}` ({len(entries)} Personas)\n")
        index_lines.append("| ID | Persona | Individual `.md` File |")
        index_lines.append("| :--- | :--- | :--- |")

        for persona_id, persona_name, block_body in entries:
            file_slug = slugify_persona_name(persona_name)
            out_file = cat_dir / f"{file_slug}.md"

            # Wrap the individual persona file with a clean header
            file_content = (
                f"# PERSONA DOSSIER // {persona_name}\n"
                f"- **ID**: `{persona_id}`\n"
                f"- **Category**: `{cat_slug}`\n\n"
                f"---\n\n"
                f"{block_body}\n"
            )
            out_file.write_text(file_content, encoding="utf-8")
            rel_link = f"./{cat_slug}/{file_slug}.md"
            index_lines.append(f"| `{persona_id}` | **{persona_name}** | [`{rel_link}`]({rel_link}) |")
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

    print(f"[SPLIT COMPLETE] Generated {board_count} Board Member .md files and {strike_count} Strike-Team .md files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
