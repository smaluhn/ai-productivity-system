# ClickUp Personal Projects - Labels/Tags System

**List:** Simon (in Team space)
**Strategy:** Use tags/labels to organize different personal projects within one list

---

## 📌 Recommended Labels for Simon List

### Business Projects
- `#printora` - Printora-specific personal tasks
- `#akunindo` - AkunIndo-specific personal tasks
- `#fundefi` - FunDeFi-specific personal tasks
- `#favos` - FavOS-related tasks

### Personal Development Projects
- `#mindfulness-app` - Your mindfulness/meditation app project
- `#productivity-system` - This productivity system development
- `#personal-dev` - General personal development tasks

### Life Admin
- `#life-admin` - Bills, errands, calls (like calling sister)
- `#health` - Health, fitness, meditation practice
- `#learning` - Courses, reading, skill development

### Investment/Fundraising
- `#fundraising` - Investor outreach, pitch decks
- `#networking` - Advisor/angel connections

---

## 🎯 How to Use Labels

### 1. **Create Tags in ClickUp**
In the Simon list:
1. Click any task
2. Click "Add Tag" button
3. Create these tags with suggested colors:
   - `#printora` - 🟣 Purple
   - `#akunindo` - 🟢 Green
   - `#fundefi` - 🔵 Blue
   - `#mindfulness-app` - 🟡 Yellow
   - `#productivity-system` - 🟠 Orange
   - `#life-admin` - ⚫ Gray
   - `#health` - 🔴 Red
   - `#fundraising` - 💚 Teal

### 2. **Filter by Tag**
Create custom views in Simon list:
- **Mindfulness App Focus** - Filter: tag = `#mindfulness-app`
- **Productivity System** - Filter: tag = `#productivity-system`
- **Life Admin** - Filter: tag = `#life-admin`

### 3. **Daily Note Integration**
The `clickup_daily_fetch.py` script can show tags in task names:
```markdown
## ClickUp Tasks - Tuesday (AkunIndo Day)

### 📋 Simon's Tasks
- [ ] [#mindfulness-app] Design meditation timer UI [CU-abc123]
- [ ] [#life-admin] Call sister ⭐ [CU-abc124]
- [ ] [#productivity-system] Fix ClickUp sync [CU-abc125]
```

---

## 🔄 Migration Strategy

### Step 1: Assign Yourself to All Your Tasks
**Problem:** Most tasks in Simon list aren't assigned to you
**Solution:** Bulk assign yourself in ClickUp:
1. Go to Simon list
2. Select all tasks (checkbox at top)
3. Click "Assign" → Select "Simon"
4. Click "Apply"

### Step 2: Add Tags to Existing Tasks
Go through 18 existing tasks and add appropriate tags:

**FunDeFi Related (add `#fundefi`):**
- fix testnet
- Bonding Curve Simulation
- Solana Devnet
- KOL-Deck
- Source Links
- Whitepaper
- Projections
- Update FAQs
- USPs and Blurb
- Outreach to 5 Advisors & Angels
- Pitch Deck

**Fundraising (add `#fundraising`):**
- Organize Fundraising-Notion
- Outreach to 5 Advisors & Angels
- Pitch Deck

**Personal Dev (add `#personal-dev`):**
- favxbot on MBA
- Irem Artiffine Material
- Kindle Mac JLA book
- Naval Ravikant brain Reddit link

**Life Admin (add `#life-admin`):**
- Buy small mic for Mac and Galaxy

**Productivity System (add `#productivity-system`):**
- Create 8 ClickUp Views for Team Workflow

### Step 3: Add New Project Tasks
For your new projects:

**Mindfulness App (#mindfulness-app):**
- [ ] Define app MVP features
- [ ] Design meditation timer
- [ ] Research mindfulness app market
- [ ] Choose tech stack (React Native? Flutter?)
- [ ] Create wireframes

**Productivity System (#productivity-system):**
- [ ] Create 8 ClickUp Views
- [ ] Test ClickUp daily workflow
- [ ] Add tag support to daily fetch script
- [ ] Document system for team

---

## 🔧 Script Updates Needed

### Update `scripts/clickup_daily_fetch.py`

Add tag display in task formatting:

```python
def format_task_line(task):
    """Format task as markdown checkbox with tags and ClickUp ID"""
    task_id = task["id"]
    task_name = task["name"]

    # Get tags
    tags = task.get("tags", [])
    tag_str = ""
    if tags:
        tag_names = [f"#{tag['name']}" for tag in tags]
        tag_str = f"[{', '.join(tag_names)}] "

    # Get priority emoji
    priority = task.get("priority", {})
    priority_emoji = ""
    if priority:
        priority_name = priority.get("priority", "").lower()
        if "urgent" in priority_name or priority.get("id") == "1":
            priority_emoji = "🔴 "
        elif "high" in priority_name or priority.get("id") == "2":
            priority_emoji = "🟠 "

    return f"- [ ] {priority_emoji}{tag_str}{task_name} [CU-{task_id}]"
```

### Create Project-Specific Views

In `docs/clickup-views-setup-guide.md`, add:

**9. Mindfulness App (List View)**
- Filter: Tag contains `#mindfulness-app`
- Sort: Priority → Due Date
- Purpose: Focus on mindfulness app development

**10. Productivity System (List View)**
- Filter: Tag contains `#productivity-system`
- Sort: Priority → Due Date
- Purpose: System improvements and maintenance

---

## 📊 Example Daily Note Output

```markdown
## ClickUp Tasks - Tuesday (AkunIndo Day)

### ⏰ OVERDUE
- [ ] 🔴 [#fundefi] Send pitch deck to Brent [CU-abc123]

### 🔴 Due Today
- [ ] 🟠 [#life-admin] Call sister ⭐ [CU-abc124]
- [ ] [#productivity-system] Create 8 ClickUp Views [CU-abc125]

### 🟡 This Week
- [ ] [#mindfulness-app] Design meditation timer UI [CU-abc126]
- [ ] [#fundraising] Outreach to 5 advisors [CU-abc127]

### 📋 Simon's Backlog
- [ ] [#personal-dev] Read Naval Ravikant brain mapping [CU-abc128]
- [ ] [#health] Morning meditation routine [CU-abc129]
```

---

## ✅ Action Items

**Today:**
1. In ClickUp, go to Simon list
2. Select all tasks → Assign to Simon
3. Create the 8-10 recommended tags (with colors)
4. Add tags to existing 18 tasks (5-10 min)

**Tomorrow:**
1. Create 2 new views for personal projects:
   - "Mindfulness App Focus"
   - "Productivity System Focus"
2. Test `make morning` and see tags in daily note

**This Week:**
1. Update `clickup_daily_fetch.py` to display tags
2. Add mindfulness app tasks to Simon list with `#mindfulness-app` tag
3. Document any other personal projects you want to track

---

**Created:** 2025-11-05
**Owner:** Simon
**Status:** Ready to implement
