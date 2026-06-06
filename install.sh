#!/usr/bin/env bash
# Consulting AI Kit -- Mode A installer
# Usage: bash install.sh
set -euo pipefail

DEST="$HOME/.claude"
KIT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "==> Consulting AI Kit installer"
echo "    Kit:  $KIT_DIR"
echo "    Dest: $DEST"
echo ""

# Skills
mkdir -p "$DEST/skills"
for skill_dir in "$KIT_DIR/skills"/*/; do
    skill_name="$(basename "$skill_dir")"
    target="$DEST/skills/$skill_name"
    if [ -d "$target" ]; then
        echo "  [skip] $skill_name already installed -- remove $target to reinstall"
    else
        cp -R "$skill_dir" "$target"
        echo "  [ok]   skills/$skill_name"
    fi
done

# Rules
if [ -d "$KIT_DIR/rules" ]; then
    mkdir -p "$DEST/rules"
    for rules_dir in "$KIT_DIR/rules"/*/; do
        rules_name="$(basename "$rules_dir")"
        target="$DEST/rules/$rules_name"
        if [ -d "$target" ]; then
            echo "  [skip] rules/$rules_name already installed"
        else
            cp -R "$rules_dir" "$target"
            echo "  [ok]   rules/$rules_name"
        fi
    done
fi

# CLAUDE.md -- copy to cwd only if not already present
if [ ! -f "CLAUDE.md" ] && [ "$(pwd)" != "$KIT_DIR" ]; then
    cp "$KIT_DIR/CLAUDE.md" "CLAUDE.md"
    echo "  [ok]   CLAUDE.md -> $(pwd)/CLAUDE.md"
else
    echo "  [skip] CLAUDE.md already present in $(pwd)"
fi

echo ""
echo "==> Done. Start a new Claude Code session to load skills."
echo ""
echo "Mode B (browser): paste contents of prompts/ files as first message."
echo "  Research: $KIT_DIR/prompts/research-agent.md"
echo "  Finance:  $KIT_DIR/prompts/finance-agent.md"
