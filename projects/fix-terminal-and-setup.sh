#!/bin/bash

# Reset terminal working directory
# This script helps when terminals are stuck in non-existent directories

echo "🔧 Fixing terminal working directory issues..."
echo ""

# Common valid directories to reset to
VALID_DIRS=(
    "/Users/simon/git/productivity-system"
    "/Users/simon/git/fundefi"
    "/Users/simon/git/printora"
    "/Users/simon/git/favos"
    "/Users/simon/git/favors"
    "/Users/simon"
)

echo "Available valid directories:"
for i in "${!VALID_DIRS[@]}"; do
    if [ -d "${VALID_DIRS[$i]}" ]; then
        echo "  $((i+1)). ${VALID_DIRS[$i]} ✅"
    else
        echo "  $((i+1)). ${VALID_DIRS[$i]} ❌ (doesn't exist)"
    fi
done

echo ""
echo "Current directory: $(pwd)"
echo ""
echo "To fix terminal issues:"
echo "1. Close problematic terminal tabs"
echo "2. Open new terminal (Cmd+T)"
echo "3. Run: cd /Users/simon/git/productivity-system"
echo "4. Or run the project setup script from there"

echo ""
echo "🚀 Running project symlink setup..."
if [ -f "/Users/simon/git/productivity-system/projects/setup-project-symlinks.sh" ]; then
    bash "/Users/simon/git/productivity-system/projects/setup-project-symlinks.sh"
else
    echo "❌ Setup script not found. Please run from productivity-system directory."
fi