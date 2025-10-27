#!/bin/bash

echo "╔══════════════════════════════════════════════════════════╗"
echo "║         📊 Printora Project Status Dashboard            ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Git status for each repo
echo "🔹 Git Status:"
echo "─────────────────────────────────────────────────────────"

echo "📱 Printora App:"
cd ~/git/printora 2>/dev/null && git status -sb || echo "  ❌ Repository not found"
echo ""

echo "📢 Marketing:"
cd ~/git/printora-marketing 2>/dev/null && git status -sb || echo "  ❌ Repository not found"
echo ""

echo "📋 Spec Docs:"
cd ~/git/printora-spec-docs 2>/dev/null && git status -sb || echo "  ❌ Repository not found"
echo ""

# GitHub Issues count
echo "🔹 GitHub Issues:"
echo "─────────────────────────────────────────────────────────"
APP_ISSUES=$(gh issue list --repo Printora/printora --state open --json number 2>/dev/null | jq length 2>/dev/null)
MARKETING_ISSUES=$(gh issue list --repo Printora/printora-marketing --state open --json number 2>/dev/null | jq length 2>/dev/null)

if [ -n "$APP_ISSUES" ]; then
  echo "💻 Development: $APP_ISSUES open issues"
else
  echo "💻 Development: Unable to fetch"
fi

if [ -n "$MARKETING_ISSUES" ]; then
  echo "📢 Marketing: $MARKETING_ISSUES open issues"
else
  echo "📢 Marketing: Unable to fetch"
fi

echo ""
echo "─────────────────────────────────────────────────────────"
echo "✅ Status check complete"
