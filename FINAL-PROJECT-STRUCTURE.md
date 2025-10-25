# Printora Projects - Final Structure (Updated)

**Date**: 2025-10-25
**Status**: Ready to execute

---

## 🎯 New Structure

You've created **Project #7** with the iterative template (better kanban workflow).

### Final Projects:

1. **Project #7**: Printora Development (NEW - iterative template) ✅
   - URL: https://github.com/orgs/Printora/projects/7
   - Purpose: All development work
   - Team: Eko, Kevin, Yosua, Simon

2. **Project #5**: Printora Operations (existing)
   - URL: https://github.com/orgs/Printora/projects/5
   - Purpose: Marketing, admin, research
   - Team: Nhung, Thuy, Simon

### To Delete:

- ❌ **Project #2**: Old development project (will be replaced by #7)

---

## 🚀 How to Execute

### Step 1: Add Issues to Project #7 (Development)

Run the script I created:

```bash
# 1. Authorize (if you haven't already)
gh auth refresh -s read:project,write:org -h github.com

# 2. Run the script
/Users/simon/git/simon/scripts/move-to-project-7.sh
```

This adds **19 development issues** to Project #7:
- printora #2, #3, #8, #9-21 (16 issues)
- printora-spec-docs #1, #2, #3 (3 issues)

**Time**: 2-3 minutes

---

### Step 2: Add Issues to Project #5 (Operations)

You still need to add operations issues. Run:

```bash
# Use the original script (works for Project #5 too)
# Or manually add via web UI
```

**Issues to add to Project #5**:

From printora repo:
- #4 - Fulfillment Services
- #5 - Social Media Presence
- #6 - Vietnamese Fulfillment
- #7 - Gather Mockups

From printora-marketing repo:
- #1 - Christmas designs
- #2 - Marketing definitions
- #3 - User testing

From printora-spec-docs repo:
- #4 - API partnerships

**Commands**:
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

**Time**: 1 minute

---

### Step 3: Delete Project #2

After verifying Project #7 has all issues:

1. Go to: https://github.com/orgs/Printora/projects/2
2. Click "..." menu → Settings
3. Scroll to bottom
4. Click "Delete project"
5. Confirm deletion

**Time**: 30 seconds

---

## 📊 Final Structure Summary

### Project #7: Printora Development
**Template**: Iterative (better workflow) ✅
**Issues**: 19 total

| Issue | Title | Assignee | Priority |
|-------|-------|----------|----------|
| printora #2 | Deploy AI-Design to Staging | Kevin | High |
| printora #3 | Setup Stripe Sandbox | Kevin | Critical |
| printora #8 | AI Prompt Framework | Nhung | Medium |
| printora #9 | Stripe checkout | Kevin | Critical |
| printora #10 | AI design studio | Yosua | Critical |
| printora #11 | Image upload | Eko | Critical |
| printora #12 | Dual image storage | Kevin | Critical |
| printora #13 | Text editing | Eko | Critical |
| printora #14 | Product mockup | Eko | Critical |
| printora #15 | Version control | Eko | Critical |
| printora #16 | Design counter | Eko | Medium |
| printora #17 | Product filters | Eko | Medium |
| printora #18 | AI categorization | Yosua | Low |
| printora #19 | Social features | Eko | Low |
| printora #20 | Admin dashboard | Kevin | Low |
| printora #21 | Subscription system | Kevin | Low |
| spec-docs #1 | Docs structure | Simon | High |
| spec-docs #2 | Technical specs | Simon | High |
| spec-docs #3 | Projects setup | Simon | High |

**Team**: Eko (8), Kevin (7), Yosua (2), Simon (3), Nhung (1)

---

### Project #5: Printora Operations
**Template**: (current template)
**Issues**: 8 total

| Issue | Title | Assignee | Priority |
|-------|-------|----------|----------|
| printora #4 | Fulfillment Services | Kevin | High |
| printora #5 | Social Media | Kevin | Medium |
| printora #6 | Vietnamese Fulfillment | Nhung | High |
| printora #7 | Gather Mockups | Nhung | High |
| marketing #1 | Christmas designs | Nhung | High |
| marketing #2 | Marketing definitions | Simon | High |
| marketing #3 | User testing | Nhung | Medium |
| spec-docs #4 | API partnerships | Simon | Medium |

**Team**: Nhung (4), Simon (2), Kevin (2)

---

## 🔗 Dependencies & Critical Path

### Must Complete First (Blockers):
1. **#3 Setup Stripe Sandbox** → Blocks #9 (Stripe checkout)
2. **#10 Build AI design studio** → Blocks #2 (Deploy to staging)

### Critical Path (MVP - End of Next Week):
1. ✅ #3 - Stripe Sandbox
2. ✅ #9 - Stripe Checkout
3. ✅ #10 - AI Design Studio
4. ✅ #11 - Image Upload
5. ✅ #12 - Dual Storage
6. ✅ #13 - Text Editing
7. ✅ #14 - Product Mockup
8. ✅ #15 - Version Control

---

## ✅ Quick Execution Checklist

**Total time**: 5-10 minutes

- [ ] Step 1: Run auth refresh (30 sec)
  ```bash
  gh auth refresh -s read:project,write:org -h github.com
  ```

- [ ] Step 2: Add issues to Project #7 (2-3 min)
  ```bash
  /Users/simon/git/simon/scripts/move-to-project-7.sh
  ```

- [ ] Step 3: Verify Project #7 has 19 issues (30 sec)
  Visit: https://github.com/orgs/Printora/projects/7

- [ ] Step 4: Add 8 issues to Project #5 (1 min)
  Copy/paste the 8 commands above

- [ ] Step 5: Verify Project #5 has 8 issues (30 sec)
  Visit: https://github.com/orgs/Printora/projects/5

- [ ] Step 6: Delete Project #2 (30 sec)
  Settings → Delete project

- [ ] ✅ Done! Two clean projects ready for team

---

## 📝 What's Better About Project #7?

**Iterative Template** includes:
- ✅ Sprint planning views
- ✅ Better kanban columns
- ✅ Iteration tracking
- ✅ Velocity charts
- ✅ Burndown visualization
- ✅ Custom fields pre-configured

This is much better than the basic Project #2 template!

---

## 🎯 After Setup

Once both projects are populated:

### For Daily Standups:
- **Developers** check: https://github.com/orgs/Printora/projects/7
- **Operations** check: https://github.com/orgs/Printora/projects/5

### For Weekly Reviews:
- Review closed issues in each project
- Update sprint/iteration progress
- Adjust priorities as needed

### For Team Members:
- Eko: Check Project #7 for his 8 tasks
- Kevin: Check both projects (7 dev + 2 ops)
- Yosua: Check Project #7 for his 2 tasks
- Nhung: Check Project #5 for her 4 tasks
- Simon: Check both projects (3 dev + 2 ops)

---

## 🚀 You're Ready!

After executing these steps:
- ✅ 2 clean projects with proper templates
- ✅ All 27 issues organized
- ✅ Clear team assignments
- ✅ Dependencies documented
- ✅ Ready for Monday launch

**Next**: Run the scripts and you're done! 🎉
