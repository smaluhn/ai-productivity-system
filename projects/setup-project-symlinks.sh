#!/bin/bash

# Project symlink setup script
echo "Setting up project symlinks..."

# Create symlinks for each project
# Format: ln -s TARGET LINK_NAME

echo "Creating akunindo-project symlink..."
cd /Users/simon/git/akunindo 2>/dev/null && ln -sf "/Users/simon/git/productivity-system/projects/akunindo-project" akunindo-project

echo "Creating affiliate-project symlink..."
cd /Users/simon/git/affiliate 2>/dev/null && ln -sf "/Users/simon/git/productivity-system/projects/affiliate-project" affiliate-project

echo "Creating mindfool-project symlink..."
cd /Users/simon/git/mindfool 2>/dev/null && ln -sf "/Users/simon/git/productivity-system/projects/mindfool-project" mindfool-project

echo "Creating printora-project symlink..."
cd /Users/simon/git/printora 2>/dev/null && ln -sf "/Users/simon/git/productivity-system/projects/printora-project" printora-project

echo "Creating favors-project symlink..."
cd /Users/simon/git/favors 2>/dev/null && ln -sf "/Users/simon/git/productivity-system/projects/favors-project" favors-project

echo "Creating favos-project symlink..."
cd /Users/simon/git/favos 2>/dev/null && ln -sf "/Users/simon/git/productivity-system/projects/favos-project" favos-project

echo "Verifying symlinks..."
echo "Akunindo:" && ls -la /Users/simon/git/akunindo/akunindo-project 2>/dev/null
echo "Affiliate:" && ls -la /Users/simon/git/affiliate/affiliate-project 2>/dev/null
echo "Mindfool:" && ls -la /Users/simon/git/mindfool/mindfool-project 2>/dev/null
echo "Printora:" && ls -la /Users/simon/git/printora/printora-project 2>/dev/null
echo "Favors:" && ls -la /Users/simon/git/favors/favors-project 2>/dev/null
echo "Favos:" && ls -la /Users/simon/git/favos/favos-project 2>/dev/null

echo "Setup complete!"