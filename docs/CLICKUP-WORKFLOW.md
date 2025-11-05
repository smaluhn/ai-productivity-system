# ClickUp Workflow - Single Source of Truth

**Updated:** 2025-11-05
**Status:** ACTIVE - Production system
**Workspace:** https://app.clickup.com/25699608

---

## 🎯 Philosophy: Single Source of Truth

### Before ClickUp Integration
- ❌ Tasks scattered: Obsidian, GitHub issues, Notion, email, Slack
- ❌ No team collaboration on tasks
- ❌ Hard to see what's urgent vs important
- ❌ Manual sync between systems

### After ClickUp Integration
- ✅ All tasks in ClickUp (60+ tasks and growing)
- ✅ Daily notes auto-sync with `make morning`
- ✅ Team can collaborate in ClickUp
- ✅ Tasks organized by project, priority, due date, tags
- ✅ Single command to see what's important today

---

## 📊 Current State (as of Nov 5, 2025)

### Total Tasks: 59
- **Simon (Personal):** 27 tasks with tags
- **FunDeFi:** 14 tasks (Wed/Fri focus)
- **AkunIndo:** 11 tasks (Tue focus)
- **Printora:** 6 tasks (Mon/Thu/Sat focus)
- **FavOS:** 1 task

### Task Breakdown by Urgency
- 🔴 **Due Today:** 3 tasks
- 🟡 **This Week:** 11 tasks
- 🟢 **By Nov 15:** 18 tasks
- 📋 **Backlog:** 27 tasks

---

## 🔄 Daily Workflow

### Every Morning (8:00 AM)
```bash
make morning
```

**What it does:**
1. Creates today's daily note (if doesn't exist)
2. Fetches ALL your tasks from ClickUp
3. Classifies by urgency:
   - ⏰ OVERDUE (if any)
   - 🔴 Due Today
   - 🟡 This Week
   - 📋 Project Backlog (based on day focus)
   - 📋 Personal Tasks (from Simon list)
4. Inserts into today's note with tags and priorities

**Example Output:**
```markdown
## ClickUp Tasks - Wednesday (FunDeFi Day)

### 🔴 Due Today
- [ ] 🔴 [FunDeFi] Send pitch deck v2 to Brent [CU-86d0vnhmr]
- [ ] 🔴 [#life-admin] Call sister [CU-86d0vnhk0]

### 🟡 This Week
- [ ] 🟠 [Printora] Prepare Merchize partnership [CU-86d0vnhmh]

### 📋 FunDeFi Backlog
- [ ] 🟡 [FunDeFi] Complete fair launch plan [CU-86d0vnhqb]

### 📋 Personal Tasks
- [ ] [#mindfulness-app] Design meditation timer [CU-xxx]
- [ ] [#fundefi, #fundraising] KOL-Deck [CU-xxx]
```

---

### During the Day

**Work on Tasks:**
1. Open today's note: `code journal/daily/2025/2025-11-05.md`
2. See your tasks organized by urgency
3. Work on tasks based on day focus:
   - **Monday:** Printora
   - **Tuesday:** AkunIndo
   - **Wednesday:** FunDeFi
   - **Thursday:** Printora (+ team meeting)
   - **Friday:** FunDeFi
   - **Saturday:** Printora
   - **Sunday:** OFF

**Update Progress:**
- Option 1: Update in ClickUp web (https://app.clickup.com/25699608)
- Option 2: Check off in your note (manual for now, will sync later)
- Option 3: Add comments in ClickUp for team collaboration

---

### Every Evening (Before Bed)
```bash
make evening
```

**What it does:**
1. Validates your note structure
2. Checks for any errors
3. Prepares for tomorrow

---

## 📋 ClickUp Structure

### Team Space
```
Team (Space)
├── Projects (Folder)
│   ├── Printora (List)
│   ├── Printora Ops (List)
│   ├── FunDeFi (List)
│   ├── FunDeFi Ops (List)
│   ├── AkunIndo (List)
│   ├── FavOS (List)
│   ├── Simon (List) ← Your personal tasks
│   └── ... (other lists)
```

### List Purposes

**Printora** - Client work, business tasks
- Mon/Thu/Sat focus days
- Aimee Bui (Merchize) partnership
- Nhung onboarding
- Stripe, email, website

**AkunIndo** - Tax filing app
- Tuesday focus day
- Gilles (investor) related
- Logo, hiring, Meta Ads, social media
- Kevin (dev), Yosua (ops) tasks

**FunDeFi** - DeFi gaming project
- Wed/Fri focus days
- Pitch deck, fundraising
- Emissions design, fair launch
- Werner, Anjelito collaboration

**Simon (Personal)** - Your personal projects
- Always visible in daily notes
- Uses tags for organization:
  - `#fundefi`, `#printora`, `#akunindo` - Project personal tasks
  - `#mindfulness-app` - Meditation app project
  - `#productivity-system` - This system's development
  - `#life-admin` - Errands, calls, personal
  - `#fundraising` - Investor outreach
  - `#learning` - Books, courses, videos
  - `#health` - Fitness, meditation practice
  - `#personal-dev` - Personal development

**FavOS** - Previous project (legacy)
- Limited active work
- Nate follow-ups
- AllinX pitch deck with FunDeFi pivot

---

## 🏷️ Tag System (Simon List)

### Why Tags?
Personal projects don't fit cleanly into one list. Tags let you organize without creating separate lists.

### How Tags Appear in Daily Notes
```markdown
- [ ] [#mindfulness-app] Design meditation timer [CU-123]
- [ ] [#fundefi, #fundraising] KOL-Deck [CU-124]
- [ ] [#life-admin] Call sister [CU-125]
```

### Creating More Tags
1. Go to Simon list in ClickUp
2. Click any task
3. Click "Add Tag"
4. Create new tag (e.g., `#new-project`)
5. Assign to tasks
6. Run `make morning` tomorrow - tags appear automatically!

---

## 👥 Team Collaboration

### Assigning Tasks to Team Members

**Kevin (Developer):**
```
1. Go to task in ClickUp
2. Click "Assignee" dropdown
3. Change from "Simon" to "Kevin"
4. Add comment: "Kevin - please prioritize this week"
5. Kevin gets notification
```

**Example Tasks for Kevin:**
- Stripe sandbox setup (Printora)
- Payment integration (AkunIndo - Xendit/Doku)
- Mobile optimization (AkunIndo)

**Yosua (Operations/Social):**
- Setup tally.so for hiring (AkunIndo)
- Manage social media accounts (Instagram, Facebook, YouTube, TikTok)
- Post hiring campaign content

**Thuy (PM/Strategic):**
- Participates in key meetings (Merchize, BNB Chain)
- Reviews ClickUp workflow with team
- Strategic decisions across all projects

**Eko/Yulieko (Developer Support):**
- Supports Kevin on technical blockers
- Code review and quality

---

## 🚀 Advanced Features

### Creating Tasks Directly in ClickUp
```
1. Go to appropriate list (Printora, FunDeFi, etc.)
2. Click "+ New Task"
3. Fill in:
   - Name (required)
   - Description
   - Assignee (yourself or team)
   - Due Date
   - Priority (🔴 Urgent, 🟠 High, 🟡 Normal)
   - Tags (if in Simon list)
4. Save
5. Run `make morning` tomorrow - it appears in your note!
```

### Bulk Processing Inbox → ClickUp
```bash
# Dry run to preview
python3 scripts/process_all_to_clickup.py --dry-run

# Actually create tasks
python3 scripts/process_all_to_clickup.py
```

This script:
- Reads from `inbox/` folder
- Reads from outstanding tasks docs
- Creates tasks in appropriate lists
- Sets due dates, priorities, tags
- Assigns to you (Simon)

### Custom Scripts Available

**clickup_daily_fetch.py** - The core sync script
```bash
# Fetch tasks for today
python3 scripts/clickup_daily_fetch.py

# Fetch for specific date
python3 scripts/clickup_daily_fetch.py 2025-11-06
```

**clickup_setup_personal_tasks.py** - Bulk operations
```bash
# Assign all tasks in Simon list to yourself
# Add tags to existing tasks
python3 scripts/clickup_setup_personal_tasks.py
```

**process_all_to_clickup.py** - Inbox processing
```bash
# Process all pending items
python3 scripts/process_all_to_clickup.py
```

**create_tomorrow_mits.py** - MITs (Most Important Tasks)
```bash
# Create tomorrow's MITs based on manual input
python3 scripts/create_tomorrow_mits.py
```

---

## 📅 Weekly Sprint System

### Sprint Schedule
**Mon → Thu (3 days)**
- Monday: Team meeting, sprint planning
- Tuesday-Thursday: Execution
- Thursday: Team meeting, sprint review

**Thu → Mon (4 days)**
- Thursday: Sprint planning for long weekend
- Friday-Monday: Execution
- Monday: Sprint review, new planning

### Thursday Team Meetings (15:00-15:30)
**Agenda:**
1. Review "This Week Sprint" board in ClickUp
2. Each person reports progress (use ClickUp tasks as reference)
3. Move completed tasks to "Done"
4. Identify blockers
5. Plan next sprint (Thu → Mon or Mon → Thu)
6. Assign new tasks

**ClickUp View for Meetings:**
- Create "This Week Sprint" board view
- Filter: Due Date = This Week
- Columns: To Do | In Progress | Review | Done
- Group by: Assignee or Status

---

## 🎯 Focus Days & Project Time

### Weekly Schedule
| Day | Primary Focus | Secondary |
|-----|---------------|-----------|
| Monday | Printora | Team meeting (sprint planning) |
| Tuesday | AkunIndo | Gilles meetings |
| Wednesday | FunDeFi | Investor outreach |
| Thursday | Printora | Team meeting (sprint review) |
| Friday | FunDeFi | Execution |
| Saturday | Printora | Catch-up |
| Sunday | OFF | No work |

### How Daily Notes Reflect This
**Wednesday (FunDeFi Day):**
```markdown
## ClickUp Tasks - Wednesday (FunDeFi Day)

### 📋 FunDeFi Backlog
- Shows FunDeFi tasks without due dates
- Helps you focus on FunDeFi work today

### 📋 Personal Tasks
- Always shown (personal projects don't follow day schedule)
```

**Tuesday (AkunIndo Day):**
```markdown
## ClickUp Tasks - Tuesday (AkunIndo Day)

### 📋 AkunIndo Backlog
- Shows AkunIndo tasks
- Includes Gilles meeting prep items
```

---

## 📈 Success Metrics

### Week 1 (Nov 5-12, 2025)
**Goals:**
- [ ] Team adopts ClickUp (4/4 team members active)
- [ ] All new tasks created in ClickUp (not Slack/email)
- [ ] `make morning` used daily by Simon
- [ ] 8 ClickUp views created
- [ ] Thursday team meeting uses ClickUp views

### Month 1 (Nov 2025)
**Goals:**
- [ ] 100+ tasks in ClickUp
- [ ] Zero tasks in old systems (GitHub issues closed)
- [ ] Team fully collaborative in ClickUp
- [ ] All 3 projects on track (Printora, AkunIndo, FunDeFi)

### Long-term
**Goals:**
- [ ] ClickUp becomes natural part of workflow
- [ ] Tasks created immediately when identified
- [ ] No more "I forgot to do X"
- [ ] Clear visibility: What's urgent, important, backlog
- [ ] Team autonomy: Everyone knows their tasks

---

## 🆘 Troubleshooting

### "make morning shows no tasks"
**Issue:** Task fetching failed or no tasks assigned to you

**Solutions:**
1. Check ClickUp: Are tasks assigned to simon@favourse.com?
2. Run manually: `python3 scripts/clickup_daily_fetch.py`
3. Check .env file: CLICKUP_API_TOKEN set?
4. Clear Python cache: `find . -name "*.pyc" -delete`

### "Tags not showing in daily notes"
**Issue:** Tags field not being fetched

**Solutions:**
1. Tasks in Simon list have tags assigned in ClickUp?
2. Re-run: `python3 scripts/clickup_daily_fetch.py 2025-11-05`
3. Check task in ClickUp web - tags visible there?

### "Too many tasks showing"
**Issue:** All 60+ tasks flood the daily note

**Solutions:**
1. Add due dates to tasks (limits what shows)
2. Close completed tasks in ClickUp
3. Archive old tasks
4. Adjust `scripts/clickup_daily_fetch.py` limit (currently 10 personal tasks)

### "Team can't see my tasks"
**Issue:** Tasks are private or permissions wrong

**Solutions:**
1. Check list permissions in ClickUp
2. Ensure task is in team list (not private)
3. Share specific task link: Copy from ClickUp

---

## 💡 Pro Tips

### 1. Use Task IDs for Quick Access
Every task has a CU-XXX ID in your daily note:
```markdown
- [ ] 🔴 [FunDeFi] Send pitch deck [CU-86d0vnhmr]
```

**To open in browser:**
1. Copy the ID (e.g., `86d0vnhmr`)
2. Go to: `https://app.clickup.com/t/86d0vnhmr`

### 2. Create Custom Views
**Personal Views to Create:**
- "My Urgent Tasks" - Filter: Assignee=Simon, Priority=Urgent
- "This Week" - Filter: Due Date=This Week
- "FunDeFi Focus" - Filter: List=FunDeFi, Assignee=Simon
- "Waiting For" - Filter: Status=Blocked, Assignee=Simon

### 3. Use Comments for Updates
Instead of Slack messages:
1. Go to task in ClickUp
2. Add comment: "Update: Made progress on X, blocked on Y"
3. Mention team members: @Kevin @Yosua
4. They get notified in ClickUp + email

### 4. Mobile App for On-the-Go
**Download:** ClickUp app (iOS/Android)
**Use cases:**
- Check tasks during commute
- Add tasks when ideas strike
- Update status after meetings
- Quick inbox capture

### 5. Keyboard Shortcuts (Web)
- `N` - New task
- `T` - Go to task
- `?` - Show all shortcuts

---

## 🔄 Future Enhancements

### Planned Features
- [ ] Two-way sync (check off in note → updates ClickUp)
- [ ] Voice-to-task (Whisper API → ClickUp)
- [ ] AI task prioritization
- [ ] Auto-assignment based on keywords
- [ ] Slack integration (commands in Slack → ClickUp)
- [ ] Weekly goal generation from tasks
- [ ] Progress tracking dashboard

### Under Consideration
- [ ] Time tracking integration
- [ ] Pomodoro timer linked to tasks
- [ ] Energy level tracking (work on high-energy tasks when fresh)
- [ ] Context switching cost visualization

---

## 📚 Related Documentation

- `docs/clickup-views-setup-guide.md` - How to create 8 essential views
- `docs/clickup-personal-projects-labels.md` - Tag system for personal projects
- `docs/clickup-workflow-integration.md` - Original integration plan (893 lines!)
- `docs/2025-11-05-week-goals.md` - This week's goals and planning
- `config/clickup_structure.py` - Auto-generated workspace structure

---

**Last Updated:** 2025-11-05 20:30
**Maintained By:** Simon
**Status:** Active Production System
**Support:** See troubleshooting section above or update this doc!
