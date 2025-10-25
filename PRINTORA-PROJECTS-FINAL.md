# Printora Projects - Final Organization

## Current State (After Cleanup)

You now have **2 projects**:

1. **Project #2**: https://github.com/orgs/Printora/projects/2/views/1
   - Name: "Printora Development" (confirmed from screenshot)
   - Has 7 existing issues (from screenshot):
     - Deploy AI-Design Feature to Staging Server #2
     - Setup Stripe Sandbox for Dev/Staging Environment #3
     - Sign Up to Fulfillment Services and Evaluate POD Providers #4
     - Create Social Media Presence for Beta Launch #5
     - Nhung: Research Vietnamese Fulfillment Providers #6
     - Nhung: Gather Mockups and Integration Data from Providers #7
     - Nhung: AI Prompt Training Framework Research #8

2. **Project #5**: https://github.com/orgs/Printora/projects/5
   - Name: Unknown (need to check)
   - Purpose: To be determined

---

## Recommended Organization

### Project #2: "Printora Development"
**Purpose**: All development work (frontend, backend, AI/ML)

**Should contain**:
- All issues from `printora` repo (#9-#21 that we created)
- Technical docs from `printora-spec-docs`
- The existing 7 issues (#2-#8)

**Team**: Eko, Kevin, Yosua, Simon

**Current issues to review**:
1. **#2 - Deploy AI-Design Feature to Staging**
   - Status: Needs assessment - is this still relevant?
   - May be duplicate of our #10 (Build AI design studio)

2. **#3 - Setup Stripe Sandbox**
   - ✅ Good! Aligns with our #9 (Implement Stripe checkout)
   - Can be merged or kept as subtask

3. **#4 - Sign Up to Fulfillment Services**
   - ✅ Essential! Not in our 20 issues
   - Should be kept, maybe assigned to Simon/Nhung

4. **#5 - Create Social Media Presence**
   - ✅ Good! Not in our 20 issues
   - Should this be in Operations project instead?

5. **#6 - Nhung: Research Vietnamese Fulfillment**
   - ✅ Operations task! Should move to Project #5

6. **#7 - Nhung: Gather Mockups**
   - ✅ Operations task! Should move to Project #5

7. **#8 - Nhung: AI Prompt Training Framework**
   - Could be Dev (if technical) or Ops (if research)
   - Assign based on nature of work

### Project #5: "Printora Operations"
**Purpose**: Marketing, admin, research, support

**Should contain**:
- All issues from `printora-marketing` repo (#1-#3)
- Business docs from `printora-spec-docs`
- Nhung's tasks (#6, #7, and possibly #5)

**Team**: Nhung, Simon, Thuy

---

## Action Plan

### Step 1: Rename/Verify Projects

**Project #2**:
- ✅ Already named "Printora Development"
- Keep as is

**Project #5**:
- [ ] Check current name
- [ ] Rename to "Printora Operations" if not already

**How to rename** (via web UI):
1. Go to https://github.com/orgs/Printora/projects/5
2. Click "..." menu → Settings
3. Change name to "Printora Operations"
4. Save

---

### Step 2: Review and Organize Existing Issues

**Pre-existing issues (#2-#8) - Recommended assignments**:

| Issue | Current | Recommended Project | Assignee | Priority |
|-------|---------|-------------------|----------|----------|
| #2 Deploy AI-Design | Dev | Dev (review if duplicate) | Yosua | Medium |
| #3 Stripe Sandbox | Dev | Dev (merge with #9) | Kevin | Critical |
| #4 Fulfillment Services | Dev | Operations | Simon/Nhung | High |
| #5 Social Media | Dev | Operations | Nhung | High |
| #6 Vietnamese Fulfillment | Dev | Operations | Nhung | Medium |
| #7 Gather Mockups | Dev | Operations | Nhung | High |
| #8 AI Prompt Framework | Dev | Dev or Ops? | Yosua/Nhung | Medium |

**Actions needed**:
1. Move #4, #5, #6, #7 from Dev to Operations project
2. Review #2 - possibly duplicate of #10 (our AI design studio issue)
3. Review #3 - coordinate with #9 (our Stripe issue)
4. Decide on #8 - technical (Dev) or research (Ops)?

---

### Step 3: Add Our 20 New Issues to Projects

**All our issues (#9-#21 in printora, #1-#4 in spec-docs, #1-#3 in marketing) should automatically appear IF repos are linked.**

**Verify repo linking**:

**Printora Development** should link:
- [ ] Printora/printora
- [ ] Printora/printora-spec-docs

**Printora Operations** should link:
- [ ] Printora/printora-marketing
- [ ] Printora/printora-spec-docs

**How to link repos**:
1. Open project
2. Click "..." → Settings
3. Scroll to "Repositories"
4. Add repos
5. Issues from those repos will auto-appear

---

### Step 4: Set Up Project Columns

**Both projects should have**:
- Backlog
- To Do
- In Progress
- Review
- Done

**How to add columns** (if not already there):
1. Open project
2. Click "+" next to existing columns
3. Add missing columns
4. Set up automation (optional)

---

### Step 5: Move Issues Between Projects

**To move issues from Dev to Operations**:

Option A - Via Web UI:
1. Open "Printora Development" project
2. Find issues #4, #5, #6, #7
3. For each: Click "..." → Remove from project
4. Open "Printora Operations" project
5. Click "+ Add item" → Search for issue → Add

Option B - Issues can be in BOTH projects if needed!
- Example: #4 (Fulfillment) might need both dev and ops visibility

---

## Final Structure

### Printora Development (Project #2)
**Focus**: Building the product

**Issues**:
- #2 Deploy AI-Design Feature (review/merge with #10)
- #3 Setup Stripe Sandbox (coordinate with #9)
- #8 AI Prompt Framework (if technical)
- #9-#21 (our dev issues from printora repo)
- printora-spec-docs #1-3 (docs issues)

**Team View**:
- Eko sees: His 8 assigned tasks
- Kevin sees: His 5 assigned tasks
- Yosua sees: His 2 assigned tasks
- Simon sees: His dev-related tasks

### Printora Operations (Project #5)
**Focus**: Marketing, research, partnerships

**Issues**:
- #4 Sign Up to Fulfillment Services
- #5 Create Social Media Presence
- #6 Research Vietnamese Fulfillment
- #7 Gather Mockups from Providers
- #8 AI Prompt Framework (if research)
- printora-marketing #1-3 (marketing issues)
- printora-spec-docs #4 (API partnerships)

**Team View**:
- Nhung sees: Her tasks (#6, #7, marketing #1-3)
- Simon sees: His ops tasks (#4, spec-docs #4)
- Thuy sees: Everything (oversight)

---

## Issue Analysis - Pre-existing vs New

### Potential Duplicates/Overlaps

**#2 "Deploy AI-Design Feature" vs #10 "Build AI design studio"**:
- Check if same thing or different phases
- If same: Close #2 or merge into #10
- If different: #2 is deployment, #10 is building - keep both

**#3 "Setup Stripe Sandbox" vs #9 "Implement Stripe checkout"**:
- #3 = Environment setup
- #9 = Integration implementation
- These complement each other! Keep both
- #3 should be done BEFORE #9

**#4 "Sign Up to Fulfillment Services"**:
- ✅ Not covered in our 20 issues!
- Critical for MVP
- Should be high priority
- Assign to Simon + Nhung

**#5 "Create Social Media Presence"**:
- Partially covered by marketing #1 (Christmas designs)
- But this is more about setup (accounts, profiles)
- Keep as separate task
- Move to Operations

**#6, #7 Nhung's research tasks**:
- ✅ Great! Complementary to our tasks
- Move to Operations
- Keep priorities

---

## Recommended Immediate Actions

### Right Now (Web UI - 10 min)

1. **Check Project #5 name**:
   - Go to https://github.com/orgs/Printora/projects/5
   - If not "Printora Operations", rename it

2. **Link repositories** (both projects):
   - Dev: Link printora + printora-spec-docs
   - Ops: Link printora-marketing + printora-spec-docs

3. **Move Nhung's tasks** to Operations:
   - #4, #5, #6, #7 from Dev → Operations

4. **Verify our 20 issues appear**:
   - Dev project should show #9-21 automatically
   - Ops project should show marketing #1-3 automatically

### Review with Team (Monday)

1. **Existing issues status**:
   - Is #2 still relevant? Progress?
   - Is #3 done or in progress?
   - Who's working on what?

2. **Merge or coordinate**:
   - #2 + #10 (AI design)
   - #3 + #9 (Stripe)

3. **Prioritize**:
   - #4 (Fulfillment) is CRITICAL - not in our 20
   - #3 (Stripe Sandbox) blocks #9
   - Everything else follows ROADMAP

---

## Summary of Changes Needed

| Action | Where | Why |
|--------|-------|-----|
| Rename Project #5 | Web UI | Should be "Printora Operations" |
| Link repos to Dev | Project #2 settings | Auto-pull dev issues |
| Link repos to Ops | Project #5 settings | Auto-pull ops issues |
| Move #4, #5, #6, #7 | From Dev to Ops | They're ops tasks |
| Review #2 | Project #2 | Check for duplicate with #10 |
| Coordinate #3 + #9 | Project #2 | Sandbox before integration |
| Prioritize #4 | Project Ops | Critical, not in our 20 |

---

## Final Checklist

**Printora Development (Project #2)**:
- [ ] Repos linked: printora, printora-spec-docs
- [ ] Shows issues #9-21 (our dev issues)
- [ ] Shows issues #2, #3, #8 (existing dev tasks)
- [ ] Team members added: Eko, Kevin, Yosua, Simon
- [ ] Columns: Backlog, To Do, In Progress, Review, Done

**Printora Operations (Project #5)**:
- [ ] Named "Printora Operations"
- [ ] Repos linked: printora-marketing, printora-spec-docs
- [ ] Shows marketing #1-3 (our marketing issues)
- [ ] Shows #4, #5, #6, #7 (moved from Dev)
- [ ] Team members added: Nhung, Simon, Thuy
- [ ] Columns: Backlog, To Do, In Progress, Review, Done

**Issues organized**:
- [ ] Dev issues in Dev project
- [ ] Ops issues in Ops project
- [ ] No duplicates (or duplicates resolved)
- [ ] All 20 new issues visible in appropriate projects
- [ ] Existing 7 issues (#2-#8) properly categorized

---

## Questions to Answer

1. **Project #5 current name?** (check and rename if needed)
2. **Are repos linked?** (issues won't appear without this)
3. **Is #2 duplicate of #10?** (review and decide)
4. **Who owns #4?** (Fulfillment Services - critical task!)
5. **Should #8 be Dev or Ops?** (depends on nature of work)

---

## Next Steps

1. **Check Project #5 now**: What's it called?
2. **Link repos** (critical for issues to appear)
3. **Move Nhung's tasks** to Operations
4. **I'll help you** with any duplicates or questions

**Want me to help you check the current state and make these changes?**
