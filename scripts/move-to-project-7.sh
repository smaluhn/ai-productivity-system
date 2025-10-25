#!/bin/bash

# Script to move all development issues to Project #7 (new iterative template)
# This replaces Project #2

set -e

echo "==================================================================="
echo "Moving Printora Development Issues to Project #7"
echo "==================================================================="
echo ""

# First, refresh auth (you'll need to do this interactively)
echo "Step 1: Refresh GitHub auth with project scopes"
echo "Run this command first:"
echo "  gh auth refresh -s read:project,write:org -h github.com"
echo ""
read -p "Press Enter after you've refreshed auth..."

echo ""
echo "=== Adding all development issues to Project #7 ==="
echo ""

# Add issues from printora repo (all dev issues)
echo "Adding issues from printora repo..."

for issue_num in 2 3 8 9 10 11 12 13 14 15 16 17 18 19 20 21; do
    echo "  Adding printora #$issue_num..."
    gh project item-add 7 --owner Printora --url https://github.com/Printora/printora/issues/$issue_num
done

echo ""
echo "Adding issues from printora-spec-docs repo..."

# Add documentation issues
for issue_num in 1 2 3; do
    echo "  Adding printora-spec-docs #$issue_num..."
    gh project item-add 7 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/$issue_num
done

echo ""
echo "✅ Project #7 (Printora Development) - 19 issues added!"
echo ""

echo "==================================================================="
echo "Summary"
echo "==================================================================="
echo ""
echo "✅ Project #7 now has all development issues (19 total)"
echo ""
echo "Issues added:"
echo "  From printora repo:"
echo "    #2  - Deploy AI-Design Feature to Staging"
echo "    #3  - Setup Stripe Sandbox"
echo "    #8  - AI Prompt Training Framework"
echo "    #9  - Implement Stripe checkout"
echo "    #10 - Build AI design studio"
echo "    #11 - Image upload"
echo "    #12 - Dual image storage"
echo "    #13 - Text editing component"
echo "    #14 - Product mockup preview"
echo "    #15 - Version control workflow"
echo "    #16 - Design counter"
echo "    #17 - Product view filters"
echo "    #18 - AI-powered categorization"
echo "    #19 - Social features"
echo "    #20 - Admin dashboard"
echo "    #21 - Subscription system"
echo ""
echo "  From printora-spec-docs repo:"
echo "    #1 - Documentation repository structure"
echo "    #2 - MVP technical specifications"
echo "    #3 - GitHub Projects setup"
echo ""
echo "==================================================================="
echo "Next Steps"
echo "==================================================================="
echo ""
echo "1. Verify issues in Project #7:"
echo "   https://github.com/orgs/Printora/projects/7"
echo ""
echo "2. Delete Project #2 (old project):"
echo "   https://github.com/orgs/Printora/projects/2"
echo "   - Go to Settings (... menu)"
echo "   - Scroll to bottom"
echo "   - Click 'Delete project'"
echo ""
echo "3. Your final structure:"
echo "   - Project #7: Printora Development (19 issues)"
echo "   - Project #5: Printora Operations (add 8 issues separately)"
echo ""
echo "Done! 🚀"
