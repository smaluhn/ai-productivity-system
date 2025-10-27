#!/bin/bash

echo "╔══════════════════════════════════════════════════════════╗"
echo "║           🔄 Syncing All Printora Projects               ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Function to sync a repo
sync_repo() {
  local path=$1
  local name=$2

  if [ -d "$path" ]; then
    echo "🔄 Syncing $name..."
    cd "$path"
    git fetch --all
    git pull
    echo "✅ $name synced"
  else
    echo "❌ $name not found at $path"
  fi
  echo ""
}

# Sync all repos
sync_repo ~/git/printora "Printora App"
sync_repo ~/git/printora-marketing "Marketing"
sync_repo ~/git/printora-spec-docs "Spec Docs"
sync_repo ~/git/productivity-system "Productivity System"

echo "─────────────────────────────────────────────────────────"
echo "✅ All projects synced!"
