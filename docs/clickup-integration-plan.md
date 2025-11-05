# ClickUp Integration Plan

**Decision Date:** 2025-11-04
**Decided By:** Simon + Thuy
**Reason:** Team already familiar with ClickUp, better for non-technical users, visual task management

---

## 🎯 Goals

1. **Single source of truth** - ClickUp as the task management hub for all projects
2. **Team adoption** - Everyone (Thuy, Kevin, Yosua, Eko, Anjelito, Nhung) uses it daily
3. **Integration** - Sync with productivity system (journal notes, project files)
4. **Fresh start** - Clean workspace structure, no legacy clutter

---

## 📋 Workspace Structure (Recommended)

### Option A: Multi-Space Setup (Recommended)
```
Workspace: Favourse Ecosystem
├── Space: AkunIndo
│   ├── List: Product Development
│   ├── List: Marketing & Sales
│   ├── List: Legal & Compliance
│   └── List: Hiring Campaign
│
├── Space: Printora
│   ├── List: Product Development
│   ├── List: Content Creation (Nhung)
│   ├── List: Business Development
│   └── List: Partnerships (Merchize, etc.)
│
├── Space: FunDeFi
│   ├── List: Pitch Deck & Fundraising
│   ├── List: Smart Contracts (Anjelito)
│   ├── List: Marketing & Community
│   └── List: Fair Launch Prep
│
├── Space: FavOS
│   ├── List: Development
│   ├── List: Content & Marketing
│   └── List: Partnerships
│
└── Space: Personal (Simon)
    ├── List: Daily Tasks
    ├── List: Weekly Goals
    └── List: Waiting For
```

### Option B: Single-Space Setup (Simpler)
```
Workspace: Favourse Projects
├── Folder: AkunIndo
│   └── Lists (as above)
├── Folder: Printora
│   └── Lists (as above)
├── Folder: FunDeFi
│   └── Lists (as above)
└── Folder: FavOS
    └── Lists (as above)
```

**Recommendation:** Option A - Better permissions, cleaner separation, easier to scale

---

## 🏷️ Universal Custom Fields (All Projects)

1. **Priority** - Dropdown: 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low
2. **Project** - Dropdown: AkunIndo, Printora, FunDeFi, FavOS, Other
3. **GitHub Issue** - URL field (link to GitHub issue if exists)
4. **Deadline Type** - Dropdown: Hard Deadline, Soft Target, No Rush
5. **Blocked By** - Relationship field (link to blocking task)
6. **Payment Status** - Dropdown: Unpaid, Partial, Paid, N/A (for contractor work)
7. **Notes Link** - URL field (link to journal note or meeting note)

---

## 👥 Team Members & Permissions

### Workspace Admin
- Simon (owner)
- Thuy (admin)

### Project Members
| Person | AkunIndo | Printora | FunDeFi | FavOS |
|--------|----------|----------|---------|-------|
| Kevin | Member | Member | Member | Member |
| Yosua | Member | Member | Member | Member |
| Eko | - | - | Member | Member |
| Anjelito | - | - | Member | Member |
| Nhung | - | Member | - | - |
| Gilles | Guest | - | - | - |
| Jan | Guest | - | - | - |
| Werner | - | - | Guest | - |

**Permission Levels:**
- **Admin:** Full access, can manage workspace
- **Member:** Can create/edit tasks, comment, assign
- **Guest:** View + comment on specific lists only (free!)

---

## 🔗 Integration with Productivity System

### 1. Daily Journal Integration

**Script:** `scripts/clickup_daily_sync.py`

**Flow:**
```
Morning (make daily):
1. Fetch today's ClickUp tasks assigned to Simon
2. Insert into daily note under "## ClickUp Tasks for Today"
3. Format as checklist with [CU-TASKID] references

Evening (make daily-review):
1. Prompt: Which tasks completed today?
2. Update ClickUp task status via API
3. Add completion note with link to daily journal entry
```

**Daily Note Template Update:**
```markdown
## ClickUp Tasks for Today
<!-- Auto-generated from ClickUp API -->
- [ ] [AkunIndo] Setup Meta Ads account [CU-abc123]
- [ ] [FunDeFi] Finalize pitch deck v2 [CU-def456]
- [ ] [Printora] Review Nhung's content [CU-ghi789]

## Manual Tasks (Not in ClickUp)
- [ ] Personal task 1
- [ ] Personal task 2
```

### 2. Weekly Rollup Integration

**Script:** `scripts/clickup_weekly_rollup.py`

**Flow:**
```
Weekly (make weekly):
1. Fetch all tasks completed this week (per project)
2. Fetch all tasks created this week
3. Calculate completion rate
4. Insert into weekly note:
   - Tasks completed by project
   - Tasks created vs completed
   - Top blockers (tasks marked "Blocked By")
   - Team velocity (tasks/person)
```

### 3. Project File Sync

**Script:** `scripts/clickup_project_sync.py`

**Flow:**
```
On demand (make clickup-sync):
1. Fetch all tasks for specific project (e.g., AkunIndo)
2. Group by status: Blocked, Critical, In Progress, Todo, Done
3. Update projects/akunindo.md with current task list
4. Preserve manual notes and context
```

**Project File Format:**
```markdown
# AkunIndo

## Tasks from ClickUp
<!-- Last synced: 2025-11-04 10:30 -->

### 🔴 Blocked
- Setup payment integration - Blocked by Kevin research [CU-123]

### 🔥 Critical
- Launch hiring campaign - Due Nov 5 [CU-456]

### 🚀 In Progress
- Logo review with Designer Gede [CU-789]

<!-- Manual notes below preserved -->
## Meeting Notes
...
```

### 4. Inbox Processing Integration

**Script:** Update `scripts/inbox_suggest.py`

**Enhancement:**
```python
# After suggesting routing destination
# Offer to create ClickUp task directly:

def create_clickup_task(title, project, description, inbox_file):
    """Create task in ClickUp and move inbox item"""
    # Use ClickUp API to create task
    # Link to inbox file in task description
    # Move inbox file to appropriate project folder
    # Return task URL
```

---

## 🔧 ClickUp API Setup

### 1. Get API Key
1. Go to ClickUp Settings → Apps
2. Generate API Token
3. Store in `.env`:
   ```bash
   CLICKUP_API_TOKEN=pk_your_token_here
   CLICKUP_WORKSPACE_ID=your_workspace_id
   ```

### 2. Install Python SDK
```bash
pip3 install pyclickup
```

### 3. Test Connection
```bash
python3 scripts/clickup_test_connection.py
```

---

## 📊 ClickUp Setup Checklist

### Initial Setup (Do with Thuy Today)
- [ ] Create fresh ClickUp workspace OR clean existing one
- [ ] Set up Space structure (Option A recommended)
- [ ] Create custom fields (Priority, Project, etc.)
- [ ] Invite team members with appropriate permissions
- [ ] Create initial Lists for each project
- [ ] Set up default task templates

### AkunIndo Setup
- [ ] Create lists: Product Dev, Marketing, Legal, Hiring
- [ ] Import current tasks from projects/akunindo.md
- [ ] Create tasks for Tuesday meeting action items
- [ ] Assign: Kevin (tech), Yosua (marketing), Simon (strategy)
- [ ] Add Gilles & Jan as Guests to specific lists

### Printora Setup
- [ ] Create lists: Product Dev, Content (Nhung), BizDev, Partnerships
- [ ] Import tasks from projects/printora.md
- [ ] Create Nhung onboarding checklist
- [ ] Create tasks for Nov 15 deadline
- [ ] Link Merchize meeting tasks

### FunDeFi Setup
- [ ] Create lists: Fundraising, Smart Contracts, Marketing, Launch
- [ ] Import tasks from projects/fundefi-view.md
- [ ] Mark Anjelito tasks with "Blocked By" relationships
- [ ] Create pitch deck v2 checklist
- [ ] Add Werner as Guest to relevant lists

### Integration Setup
- [ ] Get ClickUp API token
- [ ] Add to `.env` and `.gitignore`
- [ ] Create `scripts/clickup_daily_sync.py`
- [ ] Create `scripts/clickup_weekly_rollup.py`
- [ ] Create `scripts/clickup_project_sync.py`
- [ ] Update `Makefile` with clickup commands
- [ ] Test sync with one project first

### Team Onboarding
- [ ] Create ClickUp onboarding doc for team
- [ ] Record Loom video: "How we use ClickUp"
- [ ] Set up notification preferences (avoid spam!)
- [ ] Create task templates for common workflows
- [ ] Schedule: ClickUp training session with team

---

## 🎯 Makefile Commands (To Add)

```makefile
# ClickUp Integration
clickup-sync: ; @python3 scripts/clickup_project_sync.py
clickup-today: ; @python3 scripts/clickup_daily_sync.py
clickup-create: ; @python3 scripts/clickup_create_task.py
clickup-done: ; @python3 scripts/clickup_mark_done.py
clickup-weekly: ; @python3 scripts/clickup_weekly_rollup.py
```

---

## 📱 Mobile Workflow

**ClickUp Mobile App:**
- Great for quick updates on the go
- Push notifications for mentions/assignments
- Can check off tasks anywhere
- Comment and add attachments easily

**Recommended Settings:**
- Enable push notifications for: Assigned, Mentions, Due dates
- Disable: Comments on watched tasks (too noisy)
- Enable: Daily digest (morning summary)

---

## 🔄 Daily Workflow Example

**Morning (8:00 AM):**
```bash
make daily                    # Creates today's note
make clickup-today           # Fetches today's ClickUp tasks
                             # Auto-inserted into daily note
```

**During Day:**
- Work from daily note checklist
- Check off tasks in daily note OR ClickUp (either works)
- Add notes/context to daily journal

**Evening (6:00 PM):**
```bash
make clickup-done            # Syncs completed tasks back to ClickUp
                             # Adds link to daily note in task comments
make validate                # Verify system integrity
```

**Weekly (Sunday):**
```bash
make weekly                  # Create weekly note
make clickup-weekly          # Generate weekly metrics from ClickUp
make rollup                  # Aggregate daily scores
```

---

## 🎨 ClickUp Views to Create

### 1. **My Daily Focus** (List View)
- Filter: Assigned to Me + Due Today/Overdue
- Sort: Priority → Due Date
- Group: By Project

### 2. **Team Workload** (Board View)
- Columns: Backlog, Todo, In Progress, Review, Done
- Group: By Assignee
- Useful for: Seeing who's overloaded

### 3. **Project Timeline** (Gantt View)
- Filter: By Space (e.g., FunDeFi only)
- Show: Dependencies and blockers
- Useful for: Seeing critical path to launch

### 4. **Nov 15 Deadline** (Calendar View)
- Filter: Due before 2025-11-15
- Group: By Project
- Useful for: Thuy's return deadline tracking

### 5. **Waiting For** (List View)
- Filter: Status = Blocked
- Group: By "Blocked By" person
- Useful for: Following up on dependencies

---

## 💡 Best Practices

### Task Naming Convention
```
[Project] Action Verb + Object - Context
Examples:
✅ [AkunIndo] Review hiring post from Yosua
✅ [FunDeFi] Finalize pitch deck v2 - send to Brent
✅ [Printora] Set up Stripe account - German entity
❌ Hiring post (too vague)
❌ Work on pitch deck (no clear outcome)
```

### Using Subtasks
- Break complex tasks into subtasks (max 5-7 per task)
- Each subtask should be completable in < 2 hours
- Assign subtasks to different people if collaborative

### Comments vs Descriptions
- **Description:** What needs to be done (permanent)
- **Comments:** Updates, questions, blockers (threaded)
- Tag people with @ for notifications

### Due Dates
- Use sparingly - only for TRUE deadlines
- Soft targets → use "Target Date" custom field instead
- Avoid "due date creep" (constantly pushing dates)

---

## 🚀 Quick Start (Today's Session)

**With Thuy (30 minutes):**
1. [ ] Open existing ClickUp account
2. [ ] Create new Workspace: "Favourse Ecosystem" (or clean existing)
3. [ ] Create 4 Spaces: AkunIndo, Printora, FunDeFi, FavOS
4. [ ] Set up custom fields (copy from above)
5. [ ] Invite team members
6. [ ] Create 5-10 tasks for each project (most critical)
7. [ ] Assign owners and due dates
8. [ ] Show Thuy the mobile app

**Simon Solo (1 hour):**
1. [ ] Get API token from ClickUp
2. [ ] Create `.env` with ClickUp credentials
3. [ ] Install pyclickup: `pip3 install pyclickup`
4. [ ] Create basic sync script (fetch tasks only)
5. [ ] Test integration with one project
6. [ ] Document setup in this file

**Next Steps:**
- Build out full integration scripts
- Train team on ClickUp usage
- Create templates for recurring workflows
- Set up automations (e.g., auto-assign based on labels)

---

## 📚 Resources

- **ClickUp API Docs:** https://clickup.com/api
- **Python SDK:** https://github.com/Hawk777/pyclickup
- **Integration Examples:** See `scripts/clickup_*.py` (to be created)
- **Team Guide:** `docs/team-clickup-guide.md` (to be created)

---

**Next Review:** After 1 week of usage (Nov 11) - assess adoption and iterate
**Owner:** Simon (integration), Thuy (team adoption)
