<#
.SYNOPSIS
    Installs "The Board" (`the-board`) skill into Claude Code, Google Antigravity (agy),
    Gemini CLI, and/or the current workspace `.agents/skills/` directory.
#>

param(
    [ValidateSet("all", "agy", "claude", "workspace")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

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

if ($Target -eq "all" -or $Target -eq "agy") {
    $AgySkillsDir = Join-Path $HOME ".gemini\config\skills\the-board"
    Install-SkillToDir -DestDir $AgySkillsDir -Label "Google Antigravity & Gemini CLI"
}

if ($Target -eq "all" -or $Target -eq "claude") {
    $ClaudeSkillsDir = Join-Path $HOME ".claude\skills\the-board"
    Install-SkillToDir -DestDir $ClaudeSkillsDir -Label "Claude Code (~/.claude/skills)"

    $ClaudeCommandsDir = Join-Path $HOME ".claude\commands"
    New-Item -ItemType Directory -Force -Path $ClaudeCommandsDir | Out-Null
    Copy-Item -Force (Join-Path $RepoRoot "commands\board.md") (Join-Path $ClaudeCommandsDir "board.md")
    Write-Host "🏛️⚔️  Installed [/board] command -> Claude Code ($ClaudeCommandsDir\board.md)" -ForegroundColor Green
}

if ($Target -eq "workspace") {
    $WorkspaceSkillsDir = Join-Path (Get-Location) ".agents\skills\the-board"
    Install-SkillToDir -DestDir $WorkspaceSkillsDir -Label "Workspace (.agents/skills/the-board)"
}
