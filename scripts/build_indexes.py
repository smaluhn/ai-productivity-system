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
