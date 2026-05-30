#!/usr/bin/env bash
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)/skill/wechat-dev-docs"
DEST="$HOME/.claude/skills/wechat-dev-docs"

[ -d "$SRC" ] || { echo "Source skill not found at $SRC" >&2; exit 1; }
mkdir -p "$(dirname "$DEST")"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"
echo "Installed wechat-dev-docs to $DEST"
echo "Restart Claude Code (or open a new session) to load the skill."
