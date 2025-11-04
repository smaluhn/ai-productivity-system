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
