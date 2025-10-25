# Quick Web UI Guide - Move Issues to Operations

**Time needed**: 5 minutes
**Why manual**: GitHub CLI doesn't support project issue management

---

## Method 1: From Operations Project (Recommended - Fastest)

### Go to Operations Project
👉 https://github.com/orgs/Printora/projects/5

### Add Each Issue
1. Click **"+ Add item"** button at bottom of any column
2. Type issue number in search (e.g., `#4`)
3. Click the issue when it appears
4. Done! Issue is now in Operations project

### Repeat for:
- [ ] Issue #4 - Fulfillment Services
- [ ] Issue #5 - Social Media Presence
- [ ] Issue #6 - Vietnamese Fulfillment
- [ ] Issue #7 - Gather Mockups

**That's it!** Total time: ~2 minutes

---

## Method 2: From Development Project (Alternative)

### Go to Development Project
👉 https://github.com/orgs/Printora/projects/2/views/1

### For each issue (#4, #5, #6, #7):
1. Find the issue card
2. Click the **"..."** menu on the card
3. Hover over **"Copy to project"** or **"Move to project"**
4. Select **"Printora Operations"**

### Note:
- "Copy" = Issue appears in both projects
- "Move" = Issue only in Operations project

**Recommendation**: Use "Copy" if you want visibility in both, "Move" if Operations only.

---

## After Moving Issues

### Verify Everything (1 minute)

**Check Development Project** should show:
- Issues #2, #3, #8 (old dev issues)
- Issues #9-21 (new dev issues) ← Should auto-appear from repo link
- Total: ~15 issues

**Check Operations Project** should show:
- Issues #4, #5, #6, #7 (just moved)
- Marketing issues #1-3 ← Should auto-appear from repo link
- Spec-docs issue #4 (API partnerships)
- Total: ~8 issues

---

## Troubleshooting

### "New issues (#9-21) don't appear in Development project"

**Fix**:
1. Go to project settings
2. Check "Repositories" section
3. Verify `Printora/printora` is linked
4. Refresh page

### "Marketing issues don't appear in Operations project"

**Fix**:
1. Go to Operations project settings
2. Check "Repositories" section
3. Verify `Printora/printora-marketing` is linked
4. Refresh page

### "Can't find issue #4 when searching"

**Try**:
- Type just the number: `4`
- Type with hash: `#4`
- Type full title: `Fulfillment Services`
- Check you're searching in the right project

---

## Visual Reference

### What You'll See When Adding Issues

```
┌─────────────────────────────────────────┐
│  + Add item                             │
│  ┌───────────────────────────────────┐  │
│  │ #4                              ↓ │  │
│  └───────────────────────────────────┘  │
│                                          │
│  Search results:                         │
│  ┌────────────────────────────────────┐ │
│  │ #4 Fulfillment Services            │ │ ← Click this
│  │ Printora/printora                  │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

## Done? ✅

After moving all 4 issues:
- [x] #4 in Operations project
- [x] #5 in Operations project
- [x] #6 in Operations project
- [x] #7 in Operations project

**You're ready for Monday!** 🎉

See `MONDAY-ACTION-ITEMS.md` for complete Monday checklist.
