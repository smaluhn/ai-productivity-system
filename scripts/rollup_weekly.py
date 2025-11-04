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
