#!/usr/bin/env bash
set -euo pipefail
echo "🚀 Bootstrapping Productivity System v2 (full featured)..."

# --- prepare dirs ---
mkdir -p docs/SOPs templates scripts journal/daily/$(date +%Y) journal/weekly/$(date +%Y) journal/monthly/$(date +%Y)
mkdir -p .github/workflows archives/inbox triage _reports assets/inbox config docs/projects docs/areas docs/resources .trash inbox

# --- README ---
cat > README.md <<'EOM'
# Productivity System v2

A unified PARA + journal + inbox-processing system.

### Daily use
```bash
make daily
make inbox-scan && make inbox-tui && make inbox-apply-now && make inbox-learn
make rollup index validate sync
```

## Folder map
- journal/ — daily, weekly, monthly logs
- templates/ — note templates
- scripts/ — all automations
- inbox/ — drop new notes, screenshots, drafts
- triage/ — AI suggestions for inbox routing
- config/ — routing rules
EOM

# --- Templates ---
cat > templates/daily.md <<'EOM'
---
type: daily
date: {{DATE}}
tags: [routine, deep-work, outreach]
---

# 📅 {{DATE}} — Daily Note

## Morning
- Wake 06:30–07:00 • Walk • Sit • ZZ • Stretch
- Water + coconut water
- Intent for the day (1 line):

## Mission Blocks (2–3)
- [ ] Block 1 (90–120m)
- [ ] Block 2 (90–120m)
- [ ] Block 3 (optional)

## Investor/Revenue Metrics
- [ ] 30 outreach points
- [ ] CRM updates pushed

## Practice
- [ ] Walking meditation (10–20m)
- [ ] Samādhi sukha / whole-body awareness (20–60m)
- [ ] Evening wind-down before 21:00

## Notes
- Wins:
- Obstacles:
- Adjustments for tomorrow:

## Scores
- Focus: /10  Calm: /10  Energy: /10  Sleep: /10
EOM

cat > templates/weekly.md <<'EOM'
---
type: weekly
week: {{WEEK}}
year: {{YEAR}}
tags: [review, planning]
---

# Weekly Review — {{YEAR}} W{{WEEK}}

## Snapshot
- Theme:
- Biggest win:
- Blocker:

## Metrics
- Outreach points:
- Deep-work blocks:
- Practice sessions:

## Notes
- What worked:
- What didn't:
- Adjust for next week:

## Plan (Top 3)
- [ ]
- [ ]
- [ ]
EOM

cat > templates/monthly.md <<'EOM'
---
type: monthly
month: {{MONTH}}
year: {{YEAR}}
tags: [review, planning]
---

# Monthly Review — {{YEAR}}-{{MONTH}}

## Highlights
-

## Systems
- Health:
- Focus:
- Finance:

## Next month — Top 3
- [ ]
- [ ]
- [ ]
EOM

# --- Core scripts ---
cat > scripts/new_daily.sh <<'EOM'
#!/usr/bin/env bash
set -euo pipefail
TZ="${TZ:-Asia/Jakarta}"
DATE="$(TZ=$TZ date +%F)"
YEAR="$(TZ=$TZ date +%Y)"
DIR="journal/daily/$YEAR"
TPL="templates/daily.md"
OUT="$DIR/$DATE.md"
mkdir -p "$DIR"
if [[ ! -f "$OUT" ]]; then
  sed "s/{{DATE}}/$DATE/g" "$TPL" > "$OUT"
  echo "Created $OUT"
else
  echo "Already exists: $OUT"
fi
EOM
chmod +x scripts/new_daily.sh

cat > scripts/new_weekly.sh <<'EOM'
#!/usr/bin/env bash
set -euo pipefail
TZ="${TZ:-Asia/Jakarta}"
YEAR="$(TZ=$TZ date +%Y)"
WEEK="$(TZ=$TZ date +%V)"
DIR="journal/weekly/$YEAR"
TPL="templates/weekly.md"
OUT="$DIR/W$WEEK.md"
mkdir -p "$DIR"
if [[ ! -f "$OUT" ]]; then
  sed -e "s/{{WEEK}}/$WEEK/g" -e "s/{{YEAR}}/$YEAR/g" "$TPL" > "$OUT"
  echo "Created $OUT"
else
  echo "Already exists: $OUT"
fi
EOM
chmod +x scripts/new_weekly.sh

cat > scripts/new_monthly.sh <<'EOM'
#!/usr/bin/env bash
set -euo pipefail
TZ="${TZ:-Asia/Jakarta}"
YEAR="$(TZ=$TZ date +%Y)"
MONTH="$(TZ=$TZ date +%m)"
DIR="journal/monthly/$YEAR"
TPL="templates/monthly.md"
OUT="$DIR/$YEAR-$MONTH.md"
mkdir -p "$DIR"
if [[ ! -f "$OUT" ]]; then
  sed -e "s/{{MONTH}}/$MONTH/g" -e "s/{{YEAR}}/$YEAR/g" "$TPL" > "$OUT"
  echo "Created $OUT"
else
  echo "Already exists: $OUT"
fi
EOM
chmod +x scripts/new_monthly.sh

cat > scripts/auto-sync.sh <<'EOM'
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
EOM
chmod +x scripts/auto-sync.sh

echo "✅ v2 system scaffold complete."
echo "Next steps:"
echo "1) Run: bash bootstrap_productivity_system.sh"
echo "2) Install hooks: pip install pre-commit && pre-commit install"
echo "3) Try: make daily"
