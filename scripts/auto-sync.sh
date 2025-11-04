#!/usr/bin/env bash
set -euo pipefail
LOG=".auto-sync.log"
git add -A
if ! git diff --cached --quiet; then
  MSG="Auto-sync: $(date +'%Y-%m-%d %H:%M:%S %Z')"
  git commit -m "$MSG" | tee -a "$LOG"
  git pull --rebase | tee -a "$LOG"
  git push | tee -a "$LOG"
else
  echo "No changes" | tee -a "$LOG"
fi
tail -n 1000 "$LOG" > "$LOG.tmp" 2>/dev/null || true
[[ -f "$LOG.tmp" ]] && mv "$LOG.tmp" "$LOG"
