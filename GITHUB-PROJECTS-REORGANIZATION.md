# GitHub Projects Reorganization Plan for Printora

## Current Situation (From Screenshots)

You have multiple projects:
1. **Printora Development** (Private) - Updated 1 min ago
2. **printora-development** (Private) - Updated 7 hours ago
3. **@zee-mon's untitled project** (Private)
4. **printora** (Private) - Updated 7 hours ago

**Issues**: Duplication, unclear naming, mixed scope

## Your Question: Should Issues Be Separated Dev vs Non-Dev?

**YES! Absolutely correct.** Here's why:

### Problem with Current Setup
- All 20 issues created are in **repository issues** (printora, printora-marketing, printora-spec-docs)
- Repository issues are tied to repo access
- If Thuy/Nhung don't have access to `printora` repo, they can't see dev issues
- **BUT** they don't need to see dev issues - creates noise

### Solution: Organization-Level Projects

**Recommended Structure**:

```
Organization: Printora
│
├── Projects (Organization-level - everyone can access based on membership)
│   ├── Printora Development (Dev team: Eko, Kevin, Yosua, Simon)
│   └── Printora Operations (Ops team: Nhung, Simon, Thuy)
│
└── Repositories (Code storage)
    ├── printora (Issues stay here, pulled into Dev project)
    ├── printora-marketing (Issues stay here, pulled into Ops project)
    └── printora-spec-docs (Issues pulled into BOTH projects)
```

## How It Works

### Issues Stay in Repositories
✅ **Keep issues where they are** (in repos)
- Dev issues → `printora` repo
- Marketing issues → `printora-marketing` repo
- Doc issues → `printora-spec-docs` repo

### Projects Pull Issues In
✅ **Projects aggregate issues** from multiple repos
- **Printora Development** project shows:
  - All issues from `printora` repo
  - Technical docs from `printora-spec-docs` repo

- **Printora Operations** project shows:
  - All issues from `printora-marketing` repo
  - Business docs from `printora-spec-docs` repo

### Team Sees Only What They Need
✅ **Filtered visibility**
- Eko/Kevin/Yosua → Only see "Printora Development" project
- Nhung → Only sees "Printora Operations" project
- Simon/Thuy → Can see BOTH projects (admin)

## Recommended Actions

### 1. Clean Up Duplicate Projects

**Keep**:
- ✅ **Printora Development** (capitalize, professional)

**Delete**:
- ❌ **printora-development** (lowercase duplicate)
- ❌ **printora** (too generic, confusing with repo name)
- ❌ **@zee-mon's untitled project** (personal project, move issues first)

### 2. Create Second Project

**Create**:
- ✅ **Printora Operations** (for Nhung, marketing, admin tasks)

### 3. Configure Access

**Printora Development**:
- Members: Eko, Kevin, Yosua, Simon
- Thuy: View-only (optional, for oversight)

**Printora Operations**:
- Members: Nhung, Simon, Thuy
- Dev team: View-only (optional, for context)

### 4. Add Issues to Projects

This is automatic once you link repos to projects!

**Printora Development** → Link these repos:
- printora
- printora-spec-docs (for technical docs)

**Printora Operations** → Link these repos:
- printora-marketing
- printora-spec-docs (for business docs)

## Step-by-Step Migration Plan

### Phase 1: Audit Existing Issues (Do First)

1. Check what's in existing projects:
   - "Printora Development" (the capital one)
   - "printora-development" (lowercase)
   - "printora"
   - "@zee-mon's untitled project"

2. Identify which issues are:
   - Already created from our session (good)
   - Pre-existing (need to evaluate)
   - Duplicates (need to merge/delete)

### Phase 2: Clean Up Projects

1. **Rename if needed**:
   ```bash
   # Projects can be renamed in web UI
   # "Printora Development" is already good
   ```

2. **Create "Printora Operations"**:
   - Go to https://github.com/orgs/Printora/projects
   - Click "New project"
   - Name: "Printora Operations"
   - Template: Table or Board
   - Add columns: Backlog, To Do, In Progress, Review, Done

3. **Delete duplicates**:
   - Move any unique issues from duplicates first
   - Then delete: printora-development, printora, @zee-mon's project

### Phase 3: Link Repos to Projects

**For "Printora Development"**:
1. Open project settings
2. Link repositories:
   - Printora/printora
   - Printora/printora-spec-docs
3. Issues from these repos auto-appear in project

**For "Printora Operations"**:
1. Open project settings
2. Link repositories:
   - Printora/printora-marketing
   - Printora/printora-spec-docs
3. Issues from these repos auto-appear in project

### Phase 4: Configure Automation

**Both Projects**:
- When issue opened → Add to "Backlog"
- When issue assigned → Move to "To Do"
- When PR opened → Move to "In Progress"
- When PR merged → Move to "Done"
- When issue closed → Move to "Done"

## Benefits of This Structure

### 1. Clean Separation
- Dev team sees dev work only
- Ops team sees ops work only
- No noise, clear focus

### 2. Repository Access Control Still Works
- Thuy/Nhung don't need access to `printora` repo code
- But they CAN be members of "Printora Operations" project
- They see their issues without seeing dev code

### 3. Simon/Thuy Oversight
- Can view both projects
- Dashboard view of all work
- Easy to track progress across teams

### 4. Scalability
- Add more repos later → auto-pull into projects
- Add team members → just add to project
- Clear boundaries between work types

## Common Confusion Clarified

### "Should issues be in Projects or Repos?"

**Both!** Here's how:
1. **Issues LIVE in repositories** (created there, stored there)
2. **Projects DISPLAY issues** (pull them in for visualization)
3. Issues are NOT moved - they're linked/displayed in projects

Think of it like:
- **Repository** = Filing cabinet (where documents live)
- **Project** = Dashboard (shows filtered view of documents)

### "Can one issue be in multiple projects?"

**YES!** For example:
- Issue in `printora-spec-docs` about API documentation
- Shows in "Printora Development" (dev team needs to know)
- ALSO shows in "Printora Operations" (for release planning)

### "What about repo-level projects?"

**Don't use them for Printora.** Reasons:
- You have 3 repos → would need 3 repo-level projects
- Can't coordinate across repos
- Team members can't see full picture
- Organization-level projects are better for your use case

## Answer to Your Specific Questions

### Q1: "Shouldn't we separate issues: dev vs non-dev?"
**A**: YES! But do it via **Projects**, not by moving issues. Issues stay in repos, projects filter them.

### Q2: "Issues are in repo: printora now (only devs have access)"
**A**: This is CORRECT for dev issues. Keep them there. Non-dev issues should be in `printora-marketing` repo.

### Q3: "Don't we utilize the gh project:issues?"
**A**: You DO utilize them! But through Organization-level Projects, not repo-level projects.

### Q4: "Should we move issues to org: printora: project?"
**A**: Issues DON'T move. They stay in repos. Projects DISPLAY them. Think "link" not "move".

## Implementation Checklist

- [ ] Audit existing project issues (check for duplicates)
- [ ] Keep: "Printora Development"
- [ ] Create: "Printora Operations"
- [ ] Delete: printora-development, printora, @zee-mon's project (after moving unique issues)
- [ ] Link repos to "Printora Development": printora, printora-spec-docs
- [ ] Link repos to "Printora Operations": printora-marketing, printora-spec-docs
- [ ] Configure columns: Backlog, To Do, In Progress, Review, Done
- [ ] Set up automation rules
- [ ] Add team members to projects
- [ ] Test: Create issue in repo, verify it appears in project

## Final Structure (Visual)

```
┌─────────────────────────────────────────────────┐
│  Organization: Printora                         │
├─────────────────────────────────────────────────┤
│                                                  │
│  📊 PROJECTS (Organization-level)               │
│                                                  │
│  ┌──────────────────────────────────────────┐  │
│  │ Printora Development                     │  │
│  │ Members: Eko, Kevin, Yosua, Simon        │  │
│  │ Pulls from:                              │  │
│  │   • printora repo (all issues)           │  │
│  │   • printora-spec-docs (tech docs)       │  │
│  └──────────────────────────────────────────┘  │
│                                                  │
│  ┌──────────────────────────────────────────┐  │
│  │ Printora Operations                      │  │
│  │ Members: Nhung, Simon, Thuy              │  │
│  │ Pulls from:                              │  │
│  │   • printora-marketing (all issues)      │  │
│  │   • printora-spec-docs (business docs)   │  │
│  └──────────────────────────────────────────┘  │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  📁 REPOSITORIES (Code & Issues)                │
│                                                  │
│  printora/                                      │
│  └─ Issues: #9-#21 (dev tasks)                 │
│                                                  │
│  printora-marketing/                            │
│  └─ Issues: #1-#3 (marketing tasks)            │
│                                                  │
│  printora-spec-docs/                            │
│  └─ Issues: #1-#4 (documentation)              │
│                                                  │
└─────────────────────────────────────────────────┘

FLOW:
1. Create issue in repository (e.g., printora#9)
2. Issue auto-appears in linked project (Printora Development)
3. Team member sees it in project board
4. Moves through columns: To Do → In Progress → Done
5. Issue stays in repo, status synced to project
```

## Next Steps

1. **I'll help you audit the existing projects** - what issues are already there?
2. **Clean up duplicates** - delete the redundant projects
3. **Link repos to projects** - so issues auto-appear
4. **You're done!** - Team can start working with clear separation

Want me to start by checking what's currently in those existing projects?
