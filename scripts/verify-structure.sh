#!/usr/bin/env bash
set -euo pipefail
fail=0
echo "Checking required folders…"
for d in journal/daily journal/weekly journal/monthly templates docs; do
  [[ -d "$d" ]] || { echo "Missing dir: $d" >&2; fail=1; }
done
echo "Checking daily filenames (YYYY-MM-DD.md)…"
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  [[ "$base" == "INDEX.md" ]] && continue  # Skip index files (auto-generated)
  [[ "$base" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$ ]] || { echo "Bad daily name: $f" >&2; fail=1; }
done < <(find journal/daily -type f -name '*.md' -print0 2>/dev/null || true)
echo "Checking weekly filenames (W##.md)…"
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  [[ "$base" == "INDEX.md" ]] && continue  # Skip index files
  [[ "$base" =~ ^W[0-9]{2}\.md$ ]] || { echo "Bad weekly name: $f" >&2; fail=1; }
done < <(find journal/weekly -type f -name '*.md' -print0 2>/dev/null || true)
echo "Checking monthly filenames (YYYY-MM.md)…"
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  [[ "$base" == "INDEX.md" ]] && continue  # Skip index files
  [[ "$base" =~ ^[0-9]{4}-[0-9]{2}\.md$ ]] || { echo "Bad monthly name: $f" >&2; fail=1; }
done < <(find journal/monthly -type f -name '*.md' -print0 2>/dev/null || true)
echo "Checking front-matter presence…"
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  [[ "$base" == "INDEX.md" ]] && continue  # Skip index files (auto-generated)
  head -n 1 "$f" | grep -q '^---$' || { echo "Missing front-matter: $f" >&2; fail=1; }
done < <(find journal -type f -name '*.md' -print0 2>/dev/null || true)
[[ $fail -eq 0 ]] && echo "OK ✅" || { echo "Issues found ❌" >&2; exit 1; }
