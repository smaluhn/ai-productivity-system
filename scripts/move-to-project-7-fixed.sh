#!/bin/bash

# Script to move all development issues to Project #7
# Using the account that already has project scopes

set -e

echo "==================================================================="
echo "Moving Printora Development Issues to Project #7"
echo "==================================================================="
echo ""

# Switch to the account that has project scopes
echo "Switching to account with project permissions..."
gh auth switch --user sudosimonglitch

echo ""
echo "Current auth status:"
gh auth status | grep "Active account"
echo ""

read -p "Press Enter to continue adding issues to Project #7..."

echo ""
echo "=== Adding all development issues to Project #7 ==="
echo ""

# Add issues from printora repo (all dev issues)
echo "Adding issues from printora repo..."

for issue_num in 2 3 8 9 10 11 12 13 14 15 16 17 18 19 20 21; do
    echo "  Adding printora #$issue_num..."
    gh project item-add 7 --owner Printora --url https://github.com/Printora/printora/issues/$issue_num || echo "  (may already exist or error)"
done

echo ""
echo "Adding issues from printora-spec-docs repo..."

# Add documentation issues
for issue_num in 1 2 3; do
    echo "  Adding printora-spec-docs #$issue_num..."
    gh project item-add 7 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/$issue_num || echo "  (may already exist or error)"
done

echo ""
echo "✅ Project #7 (Printora Development) - Issues added!"
echo ""

echo "==================================================================="
echo "Next: Add issues to Project #5 (Operations)"
echo "==================================================================="
echo ""
echo "Run these commands:"
echo ""
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/4"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/5"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/6"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/7"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/1"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/2"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/3"
echo "gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/4"
echo ""
echo "Done! 🚀"
