#!/usr/bin/env bash
# Close GitHub issues after they've been synced to ClickUp
# Usage: ./scripts/cleanup_github_issues.sh <owner/repo>

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 <owner/repo>"
    echo "Example: $0 Printora/printora"
    exit 1
fi

REPO=$1

echo "🗑️  Closing all open issues in $REPO..."
echo "⚠️  Issues are synced to ClickUp. GitHub issues will be closed with a comment."
echo ""

# Get all open issue numbers
ISSUES=$(gh issue list --repo "$REPO" --state open --limit 1000 --json number --jq '.[].number')

if [ -z "$ISSUES" ]; then
    echo "ℹ️  No open issues found in $REPO"
    exit 0
fi

COUNT=$(echo "$ISSUES" | wc -l | tr -d ' ')
echo "Found $COUNT open issue(s)"
echo ""

read -p "Do you want to close all these issues? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "❌ Cancelled"
    exit 0
fi

echo ""
echo "Closing issues..."

for ISSUE_NUM in $ISSUES; do
    echo "  Closing #$ISSUE_NUM..."
    gh issue close "$ISSUE_NUM" --repo "$REPO" --comment "✅ Synced to ClickUp. Task management moved to ClickUp workspace." 2>&1 | grep -v "^$" || true
done

echo ""
echo "✅ Closed $COUNT issues in $REPO"
echo "All tasks are now managed in ClickUp!"
