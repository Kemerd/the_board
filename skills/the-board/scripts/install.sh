#!/usr/bin/env bash
# ==============================================================================
# THE BOARD — Universal Skill Installer (`install.sh`)
# Installs `the-board` into Claude Code (`~/.claude/skills/the-board`),
# Google Antigravity / Gemini CLI (`~/.gemini/config/skills/the-board`),
# or the current workspace (`.agents/skills/the-board`).
# Copies `personas`, `references`, `examples`, `scripts`, and `commands`.
# ==============================================================================
set -euo pipefail

TARGET="${1:-all}"
case "${TARGET}" in
    all|agy|claude|workspace) ;;
    *)
        echo "[ERROR] Invalid target '${TARGET}'. Usage: $0 [all|agy|claude|workspace]" >&2
        exit 1
        ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

install_skill_dir() {
    local dest_dir="$1"
    local label="$2"
    mkdir -p "${dest_dir}"
    cp -f "${REPO_ROOT}/SKILL.md" "${dest_dir}/SKILL.md"

    for sub in personas references examples scripts commands; do
        if [[ -d "${REPO_ROOT}/${sub}" ]]; then
            rm -rf "${dest_dir}/${sub}"
            mkdir -p "${dest_dir}/${sub}"
            cp -rf "${REPO_ROOT}/${sub}/." "${dest_dir}/${sub}/"
        fi
    done

    echo "[THE BOARD] Installed [the-board] skill -> ${label} (${dest_dir})"
}

if [[ "${TARGET}" == "all" || "${TARGET}" == "agy" ]]; then
    install_skill_dir "${HOME}/.gemini/config/skills/the-board" "Google Antigravity & Gemini CLI"
fi

if [[ "${TARGET}" == "all" || "${TARGET}" == "claude" ]]; then
    install_skill_dir "${HOME}/.claude/skills/the-board" "Claude Code (~/.claude/skills)"
    mkdir -p "${HOME}/.claude/commands"
    cp -f "${REPO_ROOT}/commands/board.md" "${HOME}/.claude/commands/board.md"
    echo "[THE BOARD] Installed [/board] slash command -> Claude Code (~/.claude/commands/board.md)"
fi

if [[ "${TARGET}" == "workspace" ]]; then
    install_skill_dir "$(pwd)/.agents/skills/the-board" "Workspace (.agents/skills/the-board)"
fi
