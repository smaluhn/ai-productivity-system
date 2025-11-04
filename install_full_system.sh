#!/usr/bin/env bash
set -euo pipefail
echo "🚀 Installing Complete Productivity System v2..."

# The basic structure is already created, now add all the advanced features

# --- Validation & Structure Check ---
cat > scripts/verify-structure.sh <<'EOM'
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
  [[ "$base" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$ ]] || { echo "Bad daily name: $f" >&2; fail=1; }
done < <(find journal/daily -type f -name '*.md' -print0 2>/dev/null || true)
echo "Checking weekly filenames (W##.md)…"
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  [[ "$base" =~ ^W[0-9]{2}\.md$ ]] || { echo "Bad weekly name: $f" >&2; fail=1; }
done < <(find journal/weekly -type f -name '*.md' -print0 2>/dev/null || true)
echo "Checking monthly filenames (YYYY-MM.md)…"
while IFS= read -r -d '' f; do
  base=$(basename "$f")
  [[ "$base" =~ ^[0-9]{4}-[0-9]{2}\.md$ ]] || { echo "Bad monthly name: $f" >&2; fail=1; }
done < <(find journal/monthly -type f -name '*.md' -print0 2>/dev/null || true)
echo "Checking front-matter presence…"
while IFS= read -r -d '' f; do
  head -n 1 "$f" | grep -q '^---$' || { echo "Missing front-matter: $f" >&2; fail=1; }
done < <(find journal -type f -name '*.md' -print0 2>/dev/null || true)
[[ $fail -eq 0 ]] && echo "OK ✅" || { echo "Issues found ❌" >&2; exit 1; }
EOM
chmod +x scripts/verify-structure.sh

# --- Frontmatter Validator ---
cat > scripts/validate_frontmatter.py <<'EOM'
#!/usr/bin/env python3
import sys, re, argparse
from pathlib import Path

SCHEMAS = {
  "daily": {"required": ["type","date"], "optional": ["tags","score_focus","score_calm","score_energy","score_sleep"]},
  "weekly": {"required": ["type","week","year"], "optional": ["tags"]},
  "monthly": {"required": ["type","month","year"], "optional": ["tags"]},
  "project": {"required": ["type","title"], "optional": ["tags","status"]},
}
FM_RE = re.compile(r'^---\n([\s\S]*?)\n---\n', re.MULTILINE)

def parse_fm(txt):
  m = FM_RE.match(txt)
  if not m: return {}
  data = {}
  for line in m.group(1).splitlines():
    if ":" in line:
      k,v = line.split(":",1)
      data[k.strip()] = v.strip().strip('"').strip("'")
  return data

def validate(path):
  txt = path.read_text(encoding="utf-8", errors="ignore")
  fm = parse_fm(txt)
  if not fm: return False, f"Missing front-matter: {path}"
  t = fm.get("type","").lower()
  if t not in SCHEMAS: return False, f"Unknown type '{t}' in {path}"
  for req in SCHEMAS[t]["required"]:
    if req not in fm or not fm[req]: return False, f"Missing required '{req}' in {path}"
  return True, ""

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("paths", nargs="*", default=["journal","templates"])
  args = ap.parse_args()
  bad=[]
  for root in args.paths:
    if not Path(root).exists(): continue
    for p in Path(root).rglob("*.md"):
      ok,msg = validate(p)
      if not ok: bad.append(msg)
  if bad:
    print("\n".join(bad), file=sys.stderr); sys.exit(1)
  print("Front-matter OK ✅")

if __name__ == "__main__": main()
EOM
chmod +x scripts/validate_frontmatter.py

# --- Weekly Rollup (metrics aggregation) ---
cat > scripts/rollup_weekly.py <<'EOM'
#!/usr/bin/env python3
import re, datetime
from pathlib import Path
from collections import Counter, defaultdict

def iso_today(): return datetime.date.today()
def get_week_span(d):
    iso_year, iso_week, _ = d.isocalendar()
    start = d - datetime.timedelta(days=d.weekday())
    end = start + datetime.timedelta(days=6)
    return iso_year, iso_week, start, end

def parse_fm(txt):
    if not txt.startswith("---\n"): return {}
    end = txt.find("\n---", 4)
    if end == -1: return {}
    block = txt[4:end].strip().splitlines()
    data={}
    for line in block:
        if ":" in line:
            k,v=line.split(":",1); data[k.strip()] = v.strip().strip("[]")
    return data

def get_score(name, body):
    m = re.search(rf"{name}\s*:\s*(\d+)", body, re.IGNORECASE)
    return int(m.group(1)) if m else None

def main():
    today = iso_today()
    iso_year, iso_week, start, end = get_week_span(today)
    daily_dir = Path(f"journal/daily/{iso_year}")
    if not daily_dir.exists():
        print(f"No daily directory for {iso_year}")
        return
    files = sorted([f for f in daily_dir.glob("*.md") if start.strftime("%Y-%m-%d") <= f.stem <= end.strftime("%Y-%m-%d")])

    agg = defaultdict(list)
    tag_counter = Counter()
    for f in files:
        t = f.read_text(encoding="utf-8")
        fm = parse_fm(t); body = t
        for k in ["Focus","Calm","Energy","Sleep"]:
            v = get_score(k, body);
            if v is not None: agg[k].append(v)
        tags=[s.strip() for s in fm.get("tags","").split(",") if s.strip()]
        tag_counter.update(tags)

    def avg(xs): return round(sum(xs)/len(xs),2) if xs else None
    lines = [
        "## Metrics (auto)",
        f"- Week window: {start} → {end}",
        f"- Avg Focus: {avg(agg['Focus'])}",
        f"- Avg Calm: {avg(agg['Calm'])}",
        f"- Avg Energy: {avg(agg['Energy'])}",
        f"- Avg Sleep: {avg(agg['Sleep'])}",
        "- Top tags: " + (", ".join(f"{k}×{v}" for k,v in tag_counter.most_common(5)) if tag_counter else "(none)"),
        f"- Days counted: {len(files)}",
        ""
    ]
    weekly = Path(f"journal/weekly/{iso_year}/W{iso_week:02}.md")
    weekly.parent.mkdir(parents=True, exist_ok=True)
    content = weekly.read_text(encoding="utf-8") if weekly.exists() else ""
    if "## Metrics (auto)" in content:
        content = re.sub(r"## Metrics \(auto\)[\s\S]*?(?:\n## |\Z)", "\n".join(lines) + "\n## ", content, count=1)
        content = content.replace("\n## \n", "\n## ")
    else:
        content += ("\n" if content and not content.endswith("\n") else "") + "\n".join(lines)
    weekly.write_text(content, encoding="utf-8")
    print(f"Updated {weekly}")

if __name__ == "__main__": main()
EOM
chmod +x scripts/rollup_weekly.py

# --- Build Index Pages ---
cat > scripts/build_indexes.py <<'EOM'
#!/usr/bin/env python3
from pathlib import Path
def md_link(p): return f"- [{p.stem}]({p.as_posix()})"
def index_dir(root, title):
    root = Path(root)
    if not root.exists(): return
    items = sorted(root.glob("*.md"))
    if not items: return
    lines = [f"# {title}", ""] + [md_link(p) for p in items]
    (root / "INDEX.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print(f"Created index: {root}/INDEX.md")
def main():
    for year in sorted((Path("journal/daily")).glob("*")):
        if year.is_dir(): index_dir(year, f"Daily {year.name}")
    for year in sorted((Path("journal/weekly")).glob("*")):
        if year.is_dir(): index_dir(year, f"Weekly {year.name}")
    for year in sorted((Path("journal/monthly")).glob("*")):
        if year.is_dir(): index_dir(year, f"Monthly {year.name}")
if __name__ == "__main__": main()
EOM
chmod +x scripts/build_indexes.py

# --- Inbox Config ---
cat > config/inbox_rules.yaml <<'EOM'
projects:
  akunindo: ["akunindo", "akun indo", "accounting"]
  favos: ["favos", "favourse"]
  printora: ["printora", "pod", "print"]
  fundefi: ["fundefi", "fun defi", "defi"]
  mindfool: ["mindfool", "mind fool"]

areas:
  health: ["health", "sleep", "exercise", "meditation"]
  practice: ["practice", "meditation", "zhan zhuang"]

resources:
  research: ["paper", "study", "guide", "tutorial"]

routes:
  daily: "journal/daily/{YYYY}/{YYYY}-{MM}-{DD}.md"
  weekly: "journal/weekly/{YYYY}/W{WW}.md"
  monthly: "journal/monthly/{YYYY}/{YYYY}-{MM}.md"
  project: "projects/{PROJECT}/{BASENAME}.md"
  area: "docs/areas/{AREA}/{BASENAME}.md"
  resource: "docs/resources/{RESOURCE}/{BASENAME}.md"
  archive: "archives/inbox/{YYYY}/{BASENAME}"

misc:
  min_task_lines: 2
  embed_tasks_into_daily: true
EOM

# --- Inbox Suggest (AI routing) ---
cat > scripts/inbox_suggest.py <<'EOM'
#!/usr/bin/env python3
import re, yaml
from pathlib import Path
from datetime import datetime
INBOX=Path("inbox"); TRIAGE_DIR=Path("triage"); CONFIG=Path("config/inbox_rules.yaml")
DATE=datetime.now(); yyyy=DATE.strftime("%Y"); mm=DATE.strftime("%m"); dd=DATE.strftime("%d"); ww=DATE.strftime("%V")
TRIAGE_PATH=TRIAGE_DIR/f"inbox_triage_{yyyy}{mm}{dd}.yaml"

def load_cfg():
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8")) if CONFIG.exists() else {}
def read_text(p):
    try: return p.read_text(encoding="utf-8", errors="ignore")
    except: return ""

def classify(p,cfg):
    name=p.name.lower(); ext=p.suffix.lower(); is_md=(ext==".md"); text=read_text(p) if is_md else ""

    # Project keyword matching
    def match(mp):
        for bucket,kws in (mp or {}).items():
            for kw in kws or []:
                if kw.lower() in name or (is_md and re.search(rf"\b{re.escape(kw)}\b", text, re.IGNORECASE)):
                    return bucket
        return None

    proj=match(cfg.get("projects"))
    if proj:
        return {"action":"MOVE","target":cfg["routes"]["project"].format(PROJECT=proj,BASENAME=p.name),"reason":f"project: {proj}"}

    # Default to review
    return {"action":"REVIEW","target":f"archives/inbox/{yyyy}/{p.name}","reason":"no strong signal"}

def main():
    if not INBOX.exists():
        print("No inbox/ directory.")
        return
    cfg=load_cfg(); TRIAGE_DIR.mkdir(parents=True, exist_ok=True); items=[]
    for p in sorted(INBOX.iterdir()):
        if p.name.startswith(".") or p.is_dir(): continue
        sug=classify(p,cfg); text=read_text(p) if p.suffix.lower()==".md" else ""
        preview=" ".join(text.strip().split())[:80] if text else ""
        items.append({"path": p.as_posix(), "size": p.stat().st_size, "suggestion": sug, "preview": preview})
    payload={"generated": datetime.now().isoformat(), "mode":"suggest", "items":items}
    TRIAGE_PATH.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"✅ Suggestions: {TRIAGE_PATH}")
if __name__=="__main__": main()
EOM
chmod +x scripts/inbox_suggest.py

# --- Inbox Apply ---
cat > scripts/inbox_apply.py <<'EOM'
#!/usr/bin/env python3
import sys, yaml, shutil
from pathlib import Path
TRIAGE_DIR=Path("triage"); TRASH=Path(".trash")

def read_yaml(p): return yaml.safe_load(p.read_text(encoding="utf-8"))
def ensure_parent(path): Path(path).parent.mkdir(parents=True, exist_ok=True)

def main():
    matches=sorted(TRIAGE_DIR.glob("inbox_triage_*.yaml"))
    if not matches:
        print("No triage file. Run: make inbox-scan")
        return
    triage=read_yaml(matches[-1]); items=triage.get("items", []); dry=("--apply" not in sys.argv)
    if dry: print("DRY-RUN (add --apply to execute)\n")

    for it in items:
        p=Path(it["path"])
        if not p.exists():
            print(f"Missing: {p}")
            continue
        sg=it.get("suggestion",{}); decision=it.get("decision","ACCEPT").upper()
        if decision=="SKIP":
            print(f"SKIP {p}")
            continue
        act=sg.get("action","REVIEW"); target=sg.get("target"); reason=sg.get("reason","")

        if dry:
            print(f"{act} {p} → {target} ({reason})")
        else:
            ensure_parent(target)
            shutil.move(p.as_posix(), target)
            print(f"✔ moved {p} → {target}")

    print("\nDone." if not dry else "\nDry-run completed. Use --apply to execute.")

if __name__=="__main__": main()
EOM
chmod +x scripts/inbox_apply.py

# --- Docs ---
cat > docs/ARCHITECTURE.md <<'EOM'
# Architecture

- **PARA-inspired**: Projects, Areas, Resources, Archives + time-indexed journals
- **Journals**: Daily/Weekly/Monthly with ISO naming (YYYY-MM-DD, W##, YYYY-MM)
- **Inbox**: Smart routing based on keywords in config/inbox_rules.yaml
- **Validation**: Front-matter schemas, structure checks, pre-commit hooks
- **Automation**: Auto-sync, metrics rollup, index generation

## Daily Workflow
1. `make daily` - Create today's note
2. Work in today's note, track metrics
3. `make inbox-scan` - Route inbox items
4. `make sync` - Commit and push

## Weekly Review
1. `make weekly` - Create this week's note
2. `make rollup` - Auto-generate metrics
3. Review and plan
4. `make sync`
EOM

cat > docs/INBOX.md <<'EOM'
# Inbox Processing

## Quick Start
```bash
# 1. Generate routing suggestions
make inbox-scan

# 2. Review (optional - edit triage/inbox_triage_*.yaml)
# Change "action", "target", or add "decision: SKIP"

# 3. Preview changes
make inbox-apply

# 4. Execute
make inbox-apply-now
```

## How It Works
- Scans `inbox/` folder
- Matches files against keywords in `config/inbox_rules.yaml`
- Suggests MOVE/APPEND/REVIEW actions
- Creates reviewable YAML in `triage/`
- Executes moves with `--apply` flag
EOM

cat > CONTRIBUTING.md <<'EOM'
# Contributing

## Before Committing
```bash
make validate  # Check structure and front-matter
make index     # Update index files
```

## Pre-commit hooks
- Structure validation
- Front-matter schema check
- Trailing whitespace removal

Install: `pip install pre-commit && pre-commit install`
EOM

# --- Git & Editor Config ---
cat > .editorconfig <<'EOM'
root = true
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
trim_trailing_whitespace = true
EOM

cat >> .gitignore <<'EOM'

# Productivity System
.trash/
triage/
*.log
tmp/
EOM

# --- Pre-commit Config ---
cat > .pre-commit-config.yaml <<'EOM'
repos:
  - repo: local
    hooks:
      - id: verify-structure
        name: Verify structure & front-matter
        entry: scripts/verify-structure.sh
        language: system
        pass_filenames: false
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
EOM

# --- Makefile (Complete) ---
cat > Makefile <<'EOM'
.PHONY: daily weekly monthly sync rollup verify index validate inbox-scan inbox-apply inbox-apply-now

daily:
	@scripts/new_daily.sh

weekly:
	@scripts/new_weekly.sh

monthly:
	@scripts/new_monthly.sh

sync:
	@scripts/auto-sync.sh

rollup:
	@python3 scripts/rollup_weekly.py

index:
	@python3 scripts/build_indexes.py

verify:
	@scripts/verify-structure.sh

validate:
	@scripts/verify-structure.sh && python3 scripts/validate_frontmatter.py

inbox-scan:
	@python3 scripts/inbox_suggest.py

inbox-apply:
	@python3 scripts/inbox_apply.py

inbox-apply-now:
	@python3 scripts/inbox_apply.py --apply
EOM

echo ""
echo "✅ Complete Productivity System v2 Installed!"
echo ""
echo "📋 Quick Start:"
echo "  make daily              # Create today's note"
echo "  make inbox-scan         # Scan inbox for routing"
echo "  make inbox-apply-now    # Apply inbox routing"
echo "  make rollup             # Generate weekly metrics"
echo "  make index              # Build index pages"
echo "  make validate           # Check structure"
echo "  make sync               # Git commit + push"
echo ""
echo "🔧 Setup (one-time):"
echo "  pip install pre-commit pyyaml"
echo "  pre-commit install"
echo ""
