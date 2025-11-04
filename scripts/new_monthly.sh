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
