# Project #7 Shows Empty - Troubleshooting

**Confirmed**: Project #7 **HAS 19 issues** (verified via CLI)
**Problem**: Web UI shows empty

---

## Quick Fixes

### 1. Hard Refresh Browser (Try This First)
```
Cmd + Shift + R (Mac)
Ctrl + Shift + R (Windows/Linux)
```

Or clear cache and reload.

---

### 2. Check View Filters

**Go to**: https://github.com/orgs/Printora/projects/7

**Look for filter bar** at top of board:
- If you see any filters active (assignee, label, status, etc.)
- Click "Clear filters" or the X next to each filter
- Issues should appear

---

### 3. Check View Type

The iterative template might have created multiple views:
- Look for tabs/dropdowns near top (Board, Table, Roadmap, etc.)
- Switch to **"Table"** view first
- You should see all 19 issues listed
- Then switch back to Board view

**To switch views**:
1. Look for view selector (usually near project title)
2. Click dropdown
3. Select "Table" or "Board"

---

### 4. Check Status Field

Iterative template uses "Status" field. Issues might not have status set:

**In Table view**:
1. Look for "Status" column
2. Issues might show "(No status)" or blank
3. Set status for each issue:
   - Backlog
   - Todo
   - In Progress
   - Done

**Bulk update**:
1. Select multiple issues (checkboxes)
2. Set status to "Backlog" for all
3. They'll appear in Board view

---

### 5. Create a Simple Board View

If the default view is problematic:

1. Click "+ New view" (top right)
2. Choose "Board" layout
3. Group by: "Status"
4. Name it: "Simple Board"
5. All 19 issues should appear

---

## Verify Issues Are There

### Via CLI (confirms they're there):
```bash
gh project item-list 7 --owner Printora --limit 50
```

You should see all 19 issues listed.

### Via Web (should match):
1. Go to Project #7
2. Switch to **Table view**
3. You should see 19 rows
4. If not, clear all filters

---

## Most Likely Cause

**The iterative template board is grouped by "Status"** and your issues don't have Status set yet.

**Solution**:
1. Go to Table view
2. Select all issues
3. Set Status to "Backlog"
4. Switch to Board view
5. All issues appear in Backlog column

---

## Don't Delete Project #2 Yet!

Since you can see issues in Project #2 but not #7, **keep Project #2** until you can see issues in Project #7.

**Steps**:
1. Fix Project #7 view (use solutions above)
2. Verify you can see all 19 issues
3. **Then** delete Project #2

---

## Alternative: Copy Project #2 Layout

If you prefer Project #2's simpler layout:

**Option A**: Don't use Project #7, just keep using Project #2
- Project #2 works fine
- Iterative template might be overkill

**Option B**: Recreate Project #7 with simpler template
- Delete Project #7
- Create new project with "Board" template (simpler)
- Re-run the add-items script

**Option C**: Customize Project #7 to be simpler
- Remove complex views
- Create simple board view
- Keep the 19 issues that are already there

---

## My Recommendation

1. **Try hard refresh first** (Cmd+Shift+R)
2. **Switch to Table view** to see all issues
3. **Set Status = "Backlog"** for all issues
4. **Switch to Board view** - should now see them

**Time**: 2 minutes

If that doesn't work, **just use Project #2** - it's working fine! The iterative template might be more complex than needed.

---

## Summary

✅ **Project #7 HAS your 19 issues** (confirmed)
❓ **Web UI not showing them** (likely view/filter issue)
✅ **Project #2 is safe to keep** until #7 is working

**Don't panic!** Your issues are there, just need to fix the view.
