# GitHub Projects Setup Guide

**Last Updated**: 2025-10-22

This guide covers the optimal setup for GitHub Projects boards across all organizations.

---

## Board Structure Overview

| Organization | Board | Team Members |
|-------------|-------|--------------|
| **Printora** | https://github.com/orgs/Printora/projects/1 | Simon, Kevin, Eko, Yosua |
| **FUNDEdotFI** | https://github.com/orgs/FUNDEdotFI/projects/1 | Simon, Kevin, Eko, Yosua, Anjelito |
| **FavosApp** | (to be created) | Simon, Kevin, Eko, Yosua, Anjelito |

---

## Standard Custom Fields (Apply to All Boards)

### Priority (Single Select)
- 🔴 **Urgent** - Blocking issues, critical bugs
- 🟠 **High** - Important features, significant bugs
- 🟡 **Normal** - Regular development tasks
- 🟢 **Low** - Nice-to-have, optimization, refactoring

### Type (Single Select)
- 🎯 **Feature** - New functionality
- 🐛 **Bug** - Something broken
- 🔧 **Refactor** - Code improvement
- 📚 **Docs** - Documentation
- 🧪 **Test** - Testing tasks
- 🚀 **Deploy** - Deployment tasks
- 🔍 **Research** - Investigation, spike

### Sprint/Week (Text)
- Format: `Week 43 2025` or `Sprint 12`
- Used for weekly planning and filtering

### Estimate (Number)
- Story points or hours
- Optional but helpful for planning

### Status (Built-in)
- Use GitHub's status field for workflow stages

---

## Standard Views for Each Board

### 1. Board View (Kanban)
**Columns:**
1. **📥 Backlog** - Not yet prioritized
2. **📋 To Do** - Prioritized, ready to start
3. **🏗️ In Progress** - Currently being worked on
4. **👀 In Review** - PR open, awaiting review
5. **✅ Done** - Completed this week
6. **🗄️ Archive** - Closed more than 1 week ago

**Configuration:**
- Group by: Status
- Filter: None (show all)
- Sort: Priority (Urgent → Low)

### 2. Table View (Spreadsheet)
**Visible Columns:**
- Title
- Assignee
- Status
- Priority
- Type
- Sprint/Week
- Estimate
- Repository
- Labels

**Configuration:**
- Sort by: Priority, then Status
- Filter: None
- Group by: None

### 3. This Week View
**Configuration:**
- Filter: `Sprint/Week = "Week [current]"`
- Group by: Assignee
- Sort by: Priority

**Purpose:** Monday planning and Friday review

### 4. Per-Person Views
Create a saved view for each team member:
- **Simon's Tasks** - Filter: Assignee = sudosimonglitch
- **Kevin's Tasks** - Filter: Assignee = Kevin
- **Eko's Tasks** - Filter: Assignee = Eko
- **Yosua's Tasks** - Filter: Assignee = Yosua
- **Anjelito's Tasks** - Filter: Assignee = Anjelito (FunDe.Fi/Favos only)

**Purpose:** Individual daily standup view

### 5. Roadmap View (Timeline)
**Configuration:**
- Group by: Sprint/Week
- Show dates on timeline
- Filter: Type ≠ Bug

**Purpose:** High-level planning, milestone tracking

### 6. Bugs Only View
**Configuration:**
- Filter: Type = Bug
- Sort by: Priority
- Group by: Status

**Purpose:** Bug triage meetings

---

## Weekly Workflow

### Monday Planning Meeting (2x per week in-person)

**Agenda:**
1. Review "Done" column from last week
2. Move completed tasks to Archive
3. Review "Backlog" - prioritize top items
4. Move tasks to "To Do" for this week
5. Assign tasks to team members
6. Set Sprint/Week field to current week
7. Discuss blockers or dependencies

**Time:** 30-45 minutes per project

### During the Week

**Developers:**
- Move card to "In Progress" when starting
- Link PRs to issues (use `Closes #123` in PR description)
- Update card if blocked or needs help
- Move to "In Review" when PR is open
- Card auto-moves to "Done" when PR merges

**Simon (Project Manager):**
- Check "This Week" view daily
- Review "In Review" column - approve/comment on PRs
- Unblock team members
- Add new urgent tasks as they arise

### Friday Review (Async or Quick Sync)

**Check:**
1. "This Week" view completion %
2. What got done vs. planned?
3. Any blockers for next week?
4. Move incomplete tasks to next week's sprint

**Time:** 15 minutes per project

---

## Setting Up Custom Fields (Step-by-Step)

### Via GitHub Web UI:
1. Open project board
2. Click "⚙️" (Settings) in top-right
3. Scroll to "Custom fields"
4. Click "+ New field"
5. Configure each field:

**Priority Field:**
```
Name: Priority
Type: Single select
Options:
  - Urgent (🔴)
  - High (🟠)
  - Normal (🟡)
  - Low (🟢)
```

**Type Field:**
```
Name: Type
Type: Single select
Options:
  - Feature (🎯)
  - Bug (🐛)
  - Refactor (🔧)
  - Docs (📚)
  - Test (🧪)
  - Deploy (🚀)
  - Research (🔍)
```

**Sprint/Week Field:**
```
Name: Sprint/Week
Type: Text
```

**Estimate Field:**
```
Name: Estimate
Type: Number
```

### Via GitHub CLI:
```bash
# Create custom field (Priority)
gh project field-create 1 --owner Printora --name "Priority" --data-type "SINGLE_SELECT" --single-select-options "🔴 Urgent,🟠 High,🟡 Normal,🟢 Low"

# Create custom field (Type)
gh project field-create 1 --owner Printora --name "Type" --data-type "SINGLE_SELECT" --single-select-options "🎯 Feature,🐛 Bug,🔧 Refactor,📚 Docs,🧪 Test,🚀 Deploy,🔍 Research"

# Create custom field (Sprint/Week)
gh project field-create 1 --owner Printora --name "Sprint/Week" --data-type "TEXT"

# Create custom field (Estimate)
gh project field-create 1 --owner Printora --name "Estimate" --data-type "NUMBER"
```

---

## Creating Issues from TODO.md

### Manual Creation (Web UI):
1. Go to repository (e.g., https://github.com/Printora/printora)
2. Click "Issues" → "New issue"
3. Title: From TODO.md task
4. Description: Add context, acceptance criteria
5. Assignee: Assign to team member
6. Labels: Add relevant labels
7. Project: Add to "Printora Board"
8. Submit

### Bulk Creation (CLI Script):
```bash
# Create issue and add to project
gh issue create \
  --repo Printora/printora \
  --title "Complete POD provider integration" \
  --body "Compare Printful, Printify, Gelato..." \
  --assignee sudosimonglitch \
  --label "urgent,feature" \
  --project "Printora Board"
```

I can create a script to migrate your TODO.md files automatically!

---

## Team Onboarding Checklist

### For Each Team Member:

**GitHub Account Setup:**
- [ ] Create personal GitHub account (if not already)
- [ ] Add profile photo and bio
- [ ] Enable 2FA (security)

**Organization Invites:**
- [ ] Invite to appropriate org(s)
- [ ] Set role: Member or Admin
- [ ] Accept invitation via email

**Project Board Access:**
- [ ] Add to project board
- [ ] Show how to filter by their name
- [ ] Explain card movement workflow

**Repository Access:**
- [ ] Clone repository locally
- [ ] Set up development environment
- [ ] Test commit/push access

**Training:**
- [ ] Review this guide (GITHUB-PROJECTS-SETUP.md)
- [ ] Practice creating an issue
- [ ] Practice linking PR to issue
- [ ] Practice moving cards on board

---

## Integration with TODO.md

### Personal TODO.md (Simon's Use)
- Keep for personal notes, brainstorming
- Offline access via Obsidian
- Quick capture on mobile

### GitHub Issues (Team Use)
- All assigned tasks
- Team collaboration
- Progress tracking
- Linked to PRs and commits

### Sync Strategy:
- Weekly: Review TODO.md → Create GitHub Issues
- Don't duplicate - either TODO.md OR GitHub Issue, not both

---

## Migration from ClickUp

### Steps:
1. **Export ClickUp tasks** (CSV or manually)
2. **Create GitHub Issues** for active tasks
3. **Assign to team members** on GitHub
4. **Cancel ClickUp subscription** (save $300-720/year)
5. **Train team** on new workflow (1-2 weeks transition)

### What to Migrate:
- ✅ Active tasks (In Progress, To Do)
- ✅ This week's sprint items
- ✅ High-priority backlog items
- ❌ Completed tasks (keep in ClickUp archive)
- ❌ Old ideas (review and decide)

---

## Troubleshooting

### Issue: Can't see project board
**Solution:** Check organization membership, request access from admin

### Issue: Can't move cards
**Solution:** Ensure you have "Write" access to repository

### Issue: PR doesn't auto-close issue
**Solution:** Use keywords in PR description: `Closes #123` or `Fixes #456`

### Issue: Too many notifications
**Solution:** Customize notification settings:
- Settings → Notifications → "Participating and @mentions" only

---

## Resources

- **GitHub Projects Docs**: https://docs.github.com/en/issues/planning-and-tracking-with-projects
- **GitHub CLI Docs**: https://cli.github.com/manual/gh_project
- **Workflow Automation**: https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project

---

**Questions?** Ask Simon or check GitHub Docs.

**Last Updated**: 2025-10-22
