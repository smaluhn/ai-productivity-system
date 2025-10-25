# Quick Start - Set Up Both Projects

**Goal**: Add all 27 issues to your 2 projects in 5 minutes

---

## 🚀 One Command Each

### 1. Authorize GitHub (One Time - 30 seconds)

```bash
gh auth refresh -s read:project,write:org -h github.com
```

This opens your browser to authorize. Click "Authorize" and you're done.

---

### 2. Add Issues to Project #7 - Development (2 minutes)

```bash
/Users/simon/git/simon/scripts/move-to-project-7.sh
```

Adds 19 development issues.

---

### 3. Add Issues to Project #5 - Operations (1 minute)

Copy/paste this entire block:

```bash
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/4
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/5
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/6
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/7
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/1
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/2
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/3
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/4
```

Adds 8 operations issues.

---

### 4. Verify (30 seconds)

**Check Development**:
```bash
open https://github.com/orgs/Printora/projects/7
```
Should see 19 issues.

**Check Operations**:
```bash
open https://github.com/orgs/Printora/projects/5
```
Should see 8 issues.

---

### 5. Delete Old Project #2 (30 seconds)

```bash
open https://github.com/orgs/Printora/projects/2
```

Click Settings → Delete project

---

## ✅ Done!

**Total time**: 5 minutes
**Result**:
- ✅ Project #7 (Development) with 19 issues
- ✅ Project #5 (Operations) with 8 issues
- ✅ Project #2 deleted
- ✅ Ready for Monday!

---

## If Commands Fail

See `FINAL-PROJECT-STRUCTURE.md` for detailed explanations and web UI alternatives.
