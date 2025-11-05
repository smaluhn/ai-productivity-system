# ClickUp Workflow Integration

**Created:** 2025-11-04
**Team:** Simon, Thuy, Kevin, Yosua, Eko (Yulieko)

---

## 🗓️ Weekly Sprint Schedule

### Team Meetings
- **Monday:** Team meeting (all projects)
- **Thursday:** Team meeting (all projects)

### Sprint Cycles
**Sprint Length:** Monday → Thursday (3 days) + Thursday → Monday (4 days)

**Deadlines:**
- **Monday meeting:** Review weekend work, plan until Thursday
- **Thursday meeting:** Mid-week check-in, plan until Monday

---

## 📅 Simon's Work Schedule

| Day | Primary Focus | Secondary |
|-----|---------------|-----------|
| **Monday** | Printora | Team meeting |
| **Tuesday** | AkunIndo | |
| **Wednesday** | FunDeFi | |
| **Thursday** | Printora | Team meeting |
| **Friday** | FunDeFi | |
| **Saturday** | Printora | |
| **Sunday** | OFF | No work |

**Result:** Each project gets ~2 days/week of Simon's focus time

---

## 👥 Team Assignment by Project

### Printora
- **Simon** (Product/Strategy) - Mon, Thu, Sat
- **Kevin** (Development)
- **Yosua** (Marketing/Content)
- **Eko/Yulieko** (Development)
- **Nhung** (Content/Research)

### AkunIndo
- **Simon** (Product/Strategy) - Tue
- **Kevin** (Development)
- **Yosua** (Marketing/Social Media)
- **Gilles** (Advisor - Tue meetings)
- **Jan** (Advisor - Tue afternoon)

### FunDeFi
- **Simon** (Product/Strategy) - Wed, Fri
- **Thuy** (Strategy/Operations)
- **Anjelito** (Smart Contracts)
- **Eko** (Development)
- **Werner** (CMC/Advisor)

### FavOS
- **Kevin** (Development)
- **Eko** (Development)
- **Yosua** (Marketing)

---

## 📋 ClickUp List Structure & Usage

### Project Lists (for team collaboration)
- **Printora** → Dev tasks (Kevin, Eko)
- **Printora Ops** → Business/marketing tasks (Yosua, Nhung)
- **FunDeFi** → Dev/tech tasks (Anjelito, Eko)
- **FunDeFi Ops** → Business/fundraising tasks (Thuy, Simon)
- **AkunIndo** → All tasks (Kevin, Yosua)
- **FavOS** → All tasks (Kevin, Eko, Yosua)

### Simon's Personal List
- **Simon** → Tasks assigned specifically to Simon across ALL projects
- This is Simon's daily view - "What do I need to work on today?"

**Rule:**
- If task is for Simon → Assign to Simon list + tag with project
- If task is for team member → Keep in project list only

---

## 🎯 Daily Workflow Integration

### Morning Routine (8:00 AM)
```bash
make daily                  # Create today's note
make clickup-today         # Fetch Simon's tasks for today
```

**Output in daily note:**
```markdown
## ClickUp Tasks - Monday (Printora Day)

### 🔴 Due Today
- [ ] [Printora] Review Nhung's mockup research [CU-abc123]
- [ ] [Printora] Setup Stripe sandbox [CU-def456]

### 🟡 This Week (Due Thu)
- [ ] [AkunIndo] Finalize logo with Gede [CU-ghi789]
- [ ] [FunDeFi] Send pitch deck to Brent [CU-jkl012]

### Meetings Today
- 10:00 AM: Monday Team Meeting
```

### During Day
- Work from daily note OR ClickUp (whichever is easier)
- Check off tasks in either place
- Add notes in daily journal
- ClickUp comments for team collaboration

### Evening Review (6:00 PM)
```bash
make clickup-sync-back     # Sync completed tasks back to ClickUp
make validate              # Verify system integrity
```

---

## 📊 Weekly Sprint Planning

### Monday Morning Meeting
**Duration:** 60-90 minutes
**Attendees:** Simon, Thuy, Kevin, Yosua, Eko

**Agenda:**
1. **Weekend Review** (10 min)
   - What got done Fri-Sun?
   - Any blockers?

2. **This Week Sprint Planning** (40 min)
   - Monday → Thursday sprint goals
   - Assign tasks with Thu deadline
   - Check ClickUp "This Week" view

3. **Project Updates** (30 min)
   - Printora: Simon + team
   - AkunIndo: Simon + Yosua
   - FunDeFi: Simon + Thuy
   - FavOS: Kevin + Eko

4. **Action Items**
   - Clear assignments in ClickUp
   - Everyone knows their focus for Mon-Thu

### Thursday Team Meeting
**Duration:** 45-60 minutes

**Agenda:**
1. **Mid-Week Check** (15 min)
   - Progress on Monday goals
   - Blockers?

2. **Weekend Sprint Planning** (20 min)
   - Thursday → Monday sprint goals
   - Assign tasks with Mon deadline

3. **Project Updates** (15 min)
   - Quick roundup per project

4. **Next Week Preview** (10 min)
   - What's coming next week?
   - Any prep needed?

---

## 🔄 ClickUp ↔ Productivity System Sync

### Daily Sync (Automatic)

**Morning - Pull from ClickUp:**
```python
# scripts/clickup_daily_fetch.py
# Fetch tasks assigned to Simon
# Filter by:
#   - Assigned to: Simon
#   - Due: Today, Overdue, This Week
#   - Status: Not "Closed"
#   - Priority: Critical, High, Medium
# Group by: Project
# Insert into daily note
```

**Evening - Push to ClickUp:**
```python
# scripts/clickup_daily_push.py
# For each checked task in daily note:
#   - Find matching ClickUp task by [CU-xxxxx] ID
#   - Mark as complete
#   - Add comment with daily note link
#   - Update "Completed Date" custom field
```

### Weekly Rollup (Sunday Evening)
```bash
make clickup-weekly-report
```

**Generates:**
```markdown
# Week 45 Report (Oct 28 - Nov 3)

## Printora (Simon's focus: Mon, Thu, Sat)
- ✅ Completed: 8 tasks
- 🚧 In Progress: 3 tasks
- ⏰ Overdue: 1 task

## AkunIndo (Simon's focus: Tue)
- ✅ Completed: 4 tasks
- 🚧 In Progress: 2 tasks

## FunDeFi (Simon's focus: Wed, Fri)
- ✅ Completed: 6 tasks
- 🚧 In Progress: 4 tasks

## Team Velocity
- Kevin: 12 tasks completed
- Yosua: 8 tasks completed
- Eko: 10 tasks completed
```

---

## 🎨 ClickUp Views to Create

### 1. **Simon's Daily Focus** (List View)
**Filters:**
- Assigned to: Simon
- Status: Not "Closed"
- Due: Today, Overdue

**Sort:** Priority DESC → Due Date ASC

**Groups:** By Project

**Use:** Simon's morning view - "What do I work on today?"

---

### 2. **This Week Sprint** (Board View)
**Columns:** To Do | In Progress | Review | Done

**Filters:**
- Due: This Week (Mon-Thu or Thu-Mon)
- Team: All

**Groups:** By Assignee

**Use:** Monday/Thursday sprint planning

---

### 3. **Project: Printora Focus** (List View)
**Filters:**
- List: Printora OR Printora Ops
- Status: Not "Closed"

**Sort:** Priority → Due Date

**Groups:**
- Dev (Printora list)
- Ops (Printora Ops list)

**Use:** Monday/Thursday/Saturday Printora days

---

### 4. **Project: AkunIndo Focus** (List View)
**Filters:**
- List: AkunIndo
- Status: Not "Closed"

**Sort:** Priority → Due Date

**Use:** Tuesday AkunIndo days

---

### 5. **Project: FunDeFi Focus** (List View)
**Filters:**
- List: FunDeFi OR FunDeFi Ops
- Status: Not "Closed"

**Sort:** Priority → Due Date

**Groups:**
- Dev (FunDeFi list)
- Ops (FunDeFi Ops list)

**Use:** Wednesday/Friday FunDeFi days

---

### 6. **Team Workload** (Workload View)
**Shows:** Tasks per person this week

**Filters:** Due: This Week

**Use:** Monday sprint planning - balance workload

---

### 7. **Waiting For** (List View)
**Filters:**
- Status: Blocked
- OR Tag: "waiting-for"

**Groups:** By "Waiting On" (custom field)

**Use:** Daily check - follow up on dependencies

---

### 8. **Upcoming Deadlines** (Calendar View)
**Shows:** All tasks with due dates

**Filters:** Due: Next 2 weeks

**Colors:** By Project

**Use:** Weekly planning visibility

---

## 🏷️ ClickUp Custom Fields

### Required for All Tasks
1. **Project** (Dropdown)
   - Printora
   - AkunIndo
   - FunDeFi
   - FavOS
   - Other

2. **Priority** (Dropdown)
   - 🔴 Critical
   - 🟠 High
   - 🟡 Medium
   - 🟢 Low

3. **Due Date** (Date)
   - Use for real deadlines only
   - Sprint deadlines: Monday or Thursday

### Optional Fields
4. **GitHub Issue** (URL)
   - Link to original GitHub issue (if synced)

5. **Blocked By** (Relationship)
   - Link to blocking task

6. **Waiting On** (Text)
   - Person name if waiting for external dependency

7. **Sprint** (Dropdown)
   - Current Sprint
   - Next Sprint
   - Backlog

8. **Estimated Hours** (Number)
   - Optional time estimate

---

## 📝 Task Naming Convention

```
[Project] Action Verb + Object - Context (if needed)
```

**Examples:**
- ✅ `[Printora] Setup Stripe sandbox for testing`
- ✅ `[AkunIndo] Review hiring post from Yosua`
- ✅ `[FunDeFi] Send pitch deck v2 to Brent - URGENT`
- ✅ `[Simon] Prepare for Tuesday Gilles meeting`
- ❌ `Stripe` (too vague)
- ❌ `Work on website` (no clear outcome)

---

## 🚀 Implementation Plan

### Phase 1: Setup (Today - Nov 4)
- [x] Create ClickUp workspace structure
- [x] Sync all GitHub issues to ClickUp
- [x] Close GitHub issues (now in ClickUp)
- [ ] Create ClickUp custom fields
- [ ] Set up 8 core views
- [ ] Assign all current tasks to correct people

### Phase 2: Daily Integration (Nov 5-10)
- [ ] Build `clickup_daily_fetch.py`
- [ ] Build `clickup_daily_push.py`
- [ ] Test daily workflow for 1 week
- [ ] Refine based on usage

### Phase 3: Sprint Integration (Nov 11+)
- [ ] Build `clickup_weekly_report.py`
- [ ] Create sprint planning templates
- [ ] Train team on Monday/Thursday flow
- [ ] Establish sprint rhythm

### Phase 4: Optimization (Nov 18+)
- [ ] ClickUp automations (auto-assign, status changes)
- [ ] Slack/Telegram notifications
- [ ] Mobile workflow optimization
- [ ] Team feedback and iteration

---

## 💡 Team Usage Guidelines

### For Simon
1. **Morning:** Check "Simon's Daily Focus" view + daily note
2. **Work from:** Either ClickUp or daily note (sync happens evening)
3. **Project focus day:** Use project-specific view (Printora Focus, etc.)
4. **Add new tasks:** To "Simon" list if personal, project list if for team

### For Kevin, Yosua, Eko
1. **Morning:** Check your assigned tasks in team view
2. **Update status:** Move cards in Board view (To Do → In Progress → Done)
3. **Blockers:** Change status to "Blocked", add comment with issue
4. **Questions:** Comment on task, @ mention Simon or Thuy

### For Thuy
1. **Strategic view:** Use "Team Workload" to see big picture
2. **Sprint planning:** Help Simon plan Mon/Thu sprints
3. **Unblock team:** Check "Waiting For" view daily

### For All Team
- **Due dates = real deadlines:** Don't move them without discussion
- **Status updates:** Update at least daily
- **Comments > DMs:** Keep context in ClickUp comments
- **@mentions:** Tag people for quick questions
- **Attachments:** Add files/links directly to tasks

---

## 🔧 Makefile Commands

```makefile
# Daily Workflow
clickup-today: ; @python3 scripts/clickup_daily_fetch.py
clickup-done: ; @python3 scripts/clickup_daily_push.py

# Weekly Workflow
clickup-weekly: ; @python3 scripts/clickup_weekly_report.py

# Sync & Maintenance
clickup-sync: ; @python3 scripts/github_clickup_sync.py
clickup-explore: ; @python3 scripts/clickup_explore_workspace.py
clickup-test: ; @python3 scripts/clickup_test_connection.py

# Combined
morning: ; @make daily && make clickup-today
evening: ; @make clickup-done && make validate
```

---

## 📖 Daily Workflow Example

**Monday Morning (Printora Day):**

```bash
make morning
```

**Terminal output:**
```
📅 Created: journal/daily/2025/2025-11-04.md
🔄 Fetching ClickUp tasks for Simon...

📋 Today's Focus (Printora Day):
   🔴 [Printora] Setup Stripe sandbox - Due Today
   🟠 [Printora] Review Nhung's research - Due Today
   🟡 [Simon] Prep for Tue Gilles meeting

📊 This Week Sprint (Due Thursday):
   [Printora] 3 tasks
   [AkunIndo] 2 tasks
   [FunDeFi] 1 task

✅ Tasks added to daily note
```

**Work during day:**
- Open daily note OR ClickUp (whatever's easier)
- Check off completed tasks
- Add notes/context in daily journal
- Collaborate via ClickUp comments

**Monday Evening:**
```bash
make evening
```

**Terminal output:**
```
🔄 Syncing completed tasks to ClickUp...
   ✅ Marked complete: [Printora] Setup Stripe sandbox
   ✅ Marked complete: [Printora] Review Nhung's research
   💬 Added daily note link to task comments

✅ Validation passed
📊 Today: 2 tasks completed, 1 in progress
```

---

## 🎯 Success Metrics

### Team Adoption (First 2 weeks)
- [ ] All team members checking ClickUp daily
- [ ] 80%+ tasks have status updates
- [ ] Monday/Thursday meetings using ClickUp sprint views
- [ ] Zero tasks with stale status (>3 days)

### Simon's Workflow (First week)
- [ ] Daily sync working smoothly
- [ ] Morning routine takes <5 minutes
- [ ] Clear view of today's priorities
- [ ] Project focus aligned with schedule

### Team Velocity (After 1 month)
- Track: Tasks completed per week per person
- Goal: Steady increase in velocity
- Measure: Sprint goals consistently hit

---

**Next Review:** Nov 11 (after 1 week of usage)
**Owner:** Simon (workflow), Thuy (team adoption)
