# Productivity System v2

A unified productivity system integrating **ClickUp** (task management), PARA, journaling, and inbox processing.

## ✨ Single Source of Truth: ClickUp

**All tasks live in ClickUp** and sync automatically to your daily notes via `make morning`.

### Daily Workflow
```bash
# Morning: Sync tasks from ClickUp to today's note
make morning

# During the day: Work on tasks, update in ClickUp
# - Open: https://app.clickup.com/25699608
# - Update task status, add comments, check off completed

# Evening: Validate and prepare for tomorrow
make evening
```

### Old Inbox Processing (Still Available)
```bash
make inbox-scan && make inbox-tui && make inbox-apply-now && make inbox-learn
make rollup index validate sync
```

## 📋 ClickUp Integration

**Workspace:** https://app.clickup.com/25699608

### Lists & Structure
- **Printora** - Mon/Thu/Sat focus days
- **AkunIndo** - Tuesday focus day
- **FunDeFi** - Wed/Fri focus days
- **Simon** - Personal tasks with tags (#mindfulness-app, #life-admin, etc.)
- **FavOS** - FavOS related tasks

### Tags for Personal Projects
- `#fundefi`, `#printora`, `#akunindo` - Project-specific
- `#mindfulness-app` - Meditation app project
- `#productivity-system` - This system's development
- `#life-admin` - Personal errands
- `#fundraising` - Investor outreach
- `#learning` - Courses, books

### Key Scripts
- `scripts/clickup_daily_fetch.py` - Fetch tasks into daily note
- `scripts/clickup_setup_personal_tasks.py` - Bulk assign/tag personal tasks
- `scripts/process_all_to_clickup.py` - Process inbox → ClickUp

## Folder map
- journal/ — daily, weekly, monthly logs
- templates/ — note templates
- scripts/ — all automations (including ClickUp integration)
- inbox/ — drop new notes, screenshots, drafts (auto-processes to ClickUp)
- triage/ — AI suggestions for inbox routing
- config/ — routing rules, ClickUp configuration
