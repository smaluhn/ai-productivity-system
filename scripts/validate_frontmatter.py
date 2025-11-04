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
