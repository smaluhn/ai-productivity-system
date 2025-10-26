#!/bin/bash

# Script to add issues to GitHub Projects
# Run this after refreshing your GitHub auth with project scopes:
# gh auth refresh -s read:project,write:org -h github.com

set -e

echo "Adding issues to Printora Projects..."
echo ""

# First, refresh auth (you'll need to do this interactively)
echo "Step 1: Refresh GitHub auth with project scopes"
echo "Run this command first:"
echo "  gh auth refresh -s read:project,write:org -h github.com"
echo ""
read -p "Press Enter after you've refreshed auth..."

echo ""
echo "=== Adding issues to Project #5 (Operations) ==="
echo ""

# Add issues from printora repo
echo "Adding printora #4..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/4

echo "Adding printora #5..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/5

echo "Adding printora #6..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/6

echo "Adding printora #7..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/7

# Add issues from printora-marketing repo
echo "Adding printora-marketing #1..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/1

echo "Adding printora-marketing #2..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/2

echo "Adding printora-marketing #3..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/3

# Add issue from printora-spec-docs repo
echo "Adding printora-spec-docs #4..."
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/4

echo ""
echo "✅ Project #5 (Operations) - 8 issues added!"
echo ""

echo "=== Adding issues to Project #2 (Development) ==="
echo ""

# Add issues from printora repo
for issue_num in 2 3 8 9 10 11 12 13 14 15 16 17 18 19 20 21; do
    echo "Adding printora #$issue_num..."
    gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/$issue_num
done

# Add issues from printora-spec-docs repo
for issue_num in 1 2 3; do
    echo "Adding printora-spec-docs #$issue_num..."
    gh project item-add 2 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/$issue_num
done

echo ""
echo "✅ Project #2 (Development) - 19 issues added!"
echo ""

echo "=== Summary ==="
echo "✅ Project #5 (Operations): 8 issues"
echo "✅ Project #2 (Development): 19 issues"
echo ""
echo "Check your projects:"
echo "  - Operations: https://github.com/orgs/Printora/projects/5"
echo "  - Development: https://github.com/orgs/Printora/projects/2"
echo ""
echo "Done! 🚀"
