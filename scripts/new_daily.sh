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
