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
