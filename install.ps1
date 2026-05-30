#!/usr/bin/env pwsh
# Install the wechat-dev-docs skill globally to ~/.claude/skills/
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "skill/wechat-dev-docs"
$dest = Join-Path $HOME ".claude/skills/wechat-dev-docs"

if (-not (Test-Path $src)) { throw "Source skill not found at $src" }
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
Copy-Item -Recurse -Force $src $dest
Write-Host "Installed wechat-dev-docs to $dest"
Write-Host "Restart Claude Code (or open a new session) to load the skill."
