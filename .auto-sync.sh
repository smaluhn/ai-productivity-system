#!/bin/bash

# Auto-sync script for git repository
# Runs every 15 minutes to pull and push changes

REPO_DIR="/Users/simon/git/simon"
LOG_FILE="$REPO_DIR/.auto-sync.log"

# Function to log with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Change to repository directory
cd "$REPO_DIR" || exit 1

log "Starting auto-sync..."

# Check if there are any changes
if [[ -n $(git status -s) ]]; then
    log "Changes detected, committing..."

    # Add all changes
    git add -A

    # Commit with auto-generated message
    git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE" 2>&1

    log "Changes committed"
fi

# Pull latest changes (rebase to avoid merge commits)
log "Pulling latest changes..."
git pull --rebase origin main >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    log "Pull successful"
else
    log "Pull failed - check log for details"
fi

# Push changes
log "Pushing changes..."
git push origin main >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    log "Push successful"
else
    log "Push failed - check log for details"
fi

log "Auto-sync completed"
log "---"
