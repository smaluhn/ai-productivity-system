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
