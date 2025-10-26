# Add Issues to Projects - Manual Commands

**Problem**: The GitHub CLI needs additional permissions that require interactive authentication.

---

## Option 1: Run the Automated Script (Recommended)

I've created a script that will add all 27 issues automatically.

### Step 1: Refresh GitHub Auth
```bash
gh auth refresh -s read:project,write:org -h github.com
```

This will:
- Open your browser
- Ask you to authorize additional scopes
- Takes 30 seconds

### Step 2: Run the Script
```bash
/Users/simon/git/simon/scripts/add-issues-to-projects.sh
```

This will:
- Add 8 issues to Project #5 (Operations)
- Add 19 issues to Project #2 (Development)
- Takes 2-3 minutes

**Total time**: 3-4 minutes

---

## Option 2: Manual Commands (If Script Fails)

If the script doesn't work, copy/paste these commands one by one:

### First, Refresh Auth:
```bash
gh auth refresh -s read:project,write:org -h github.com
```

### Add to Project #5 (Operations):

```bash
# From printora repo
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/4
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/5
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/6
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora/issues/7

# From printora-marketing repo
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/1
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/2
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-marketing/issues/3

# From printora-spec-docs repo
gh project item-add 5 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/4
```

### Add to Project #2 (Development):

```bash
# From printora repo - dev issues
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/2
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/3
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/8
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/9
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/10
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/11
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/12
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/13
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/14
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/15
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/16
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/17
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/18
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/19
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/20
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora/issues/21

# From printora-spec-docs repo - doc issues
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/1
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/2
gh project item-add 2 --owner Printora --url https://github.com/Printora/printora-spec-docs/issues/3
```

---

## Option 3: Web UI (Slowest but Always Works)

See `QUICK-WEB-UI-GUIDE.md` for visual guide.

**For each project**:
1. Go to project URL
2. Click "+ Add item"
3. Type issue number
4. Click issue to add

**Time**: 10-15 minutes

---

## Verification

After running commands or using web UI:

**Check Project #5**:
```bash
open https://github.com/orgs/Printora/projects/5
```
Should show 8 issues.

**Check Project #2**:
```bash
open https://github.com/orgs/Printora/projects/2
```
Should show 19 issues.

---

## Recommended Approach

1. **Try the script first** (fastest if auth works)
2. **If script fails**, use manual commands
3. **If commands fail**, use web UI

**My recommendation**: Use the script! It's much faster once you refresh auth.

---

## Why This Needs Interactive Auth

The GitHub token Claude Code uses doesn't have the `read:project` and `write:org` scopes needed to manage GitHub Projects. You need to:

1. Authorize in browser (one time)
2. Then the script/commands work automatically

This is a one-time setup. Future project operations will work without re-auth.
