# Root Folder Cleanup Plan

**Current State**: 23 markdown files in root
**Goal**: Keep only `index.md` in root, organize everything else

---

## 📁 Proposed Structure

```
/Users/simon/git/simon/
├── index.md                          ← KEEP (main entry point)
├── daily/
│   └── TODAY.md                      ← Symlink to current day
├── archive/
│   └── 2025-10-25-printora-setup/   ← Move all Printora setup docs here
├── docs/
│   ├── setup/                        ← System setup guides
│   └── workflows/                    ← Already exists
└── projects/
    └── printora/                     ← Project-specific docs
```

---

## 🗂️ File Organization

### Move to `archive/2025-10-25-printora-setup/`:
All Printora project setup documents (completed work):
- ADD-ISSUES-MANUAL-COMMANDS.md
- COMPLETE-STATUS.md
- FINAL-PROJECT-STRUCTURE.md
- FINAL-SUMMARY.md
- GITHUB-PROJECTS-REORGANIZATION.md
- MONDAY-ACTION-ITEMS.md
- NEXT-ACTIONS.md
- PRINTORA-PROJECTS-FINAL.md
- PROJECT-7-TROUBLESHOOTING.md
- PROJECTS-FINAL-STATUS.md
- QUICK-START-PROJECTS.md
- QUICK-WEB-UI-GUIDE.md
- READ-ME-FIRST.md
- START-HERE-FINAL.md
- WHY-PROJECT-5-IS-EMPTY.md

### Move to `docs/setup/`:
System setup documentation:
- FIREFLIES-CONTEXT.md
- FIREFLIES-QUICK-START.md
- SETUP-SUMMARY.md
- WHATS-NEXT.md

### Keep in Root (for now):
- index.md ← Main entry
- README.md ← Git repository readme
- DELEGATIONS.md ← Active reference
- WIP.md ← Work in progress

---

## 📥 Inbox Processing Strategy

**27 items to process**

### Categories:

**Quick Actions** (empty files - just titles):
- Delete Imron 1Password
- Add X to subscriptions
- Budget Starlink
- Cloudflare email approved
- Update Gilles Jour fixe to 10am
- Gmail n8n
- Skills.google
- Liquidity Provider
- AkunIndo colors/logo
- Printora fiddle.art task

**Move to Projects**:
- Build micro saas → projects/micro-saas/
- FunDeFi idea → projects/funde-fi/
- Sadhana files → personal/practice/

**Move to Daily/Weekly**:
- Make clear deadlines → planning/
- Practice folder items → personal/practice/

**Archive/Delete**:
- Test files (Nddjdj.md, New Android 222.md, etc.)
- Duplicate content

---

## 🎯 Execution Order

1. Create archive folder structure
2. Move completed Printora docs to archive
3. Move setup docs to docs/setup/
4. Process inbox by category
5. Update index.md with new structure
6. Update TODAY.md

**Time estimate**: 20-30 minutes
