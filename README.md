# Simon's Productivity System

Personal productivity and project management system synced via Git and accessible on mobile via Obsidian.

**Last Updated**: 2025-10-23
**Timezone**: UTC+8 (Bali)

---

## 📁 Folder Structure

```
/Users/simon/git/simon/
├── daily/              # Daily schedules and task lists
│   ├── 2025-10-23.md  # Today's schedule with MIT
│   └── 2025-10/       # Archived daily notes by month
├── weekly/             # Weekly planning and reviews
│   └── 2025-W43.md    # Current week
├── monthly/            # Monthly goals and reviews
│   └── 2025-10.md     # Current month
├── meetings/           # Meeting agendas and notes
│   ├── akunindo-team-meeting-2025-10-21.md
│   └── bali-team-meeting-2025-10-23-agenda.md
├── projects/           # Project notes and context
│   ├── akunindo.md
│   ├── printora.md
│   ├── launchpad.md   # (FunDe.Fi)
│   ├── favos.md
│   └── home-tasks.md
├── productivity-system/  # System documentation
│   ├── WORKFLOW.md       # Daily/weekly workflows, EOD/EOW reviews
│   ├── IMPORTANT-NOTES.md  # Preferences, GitHub accounts, calendar
│   ├── INBOX-SOURCES.md    # Inbox processing guide
│   ├── GITHUB-PROJECTS-SETUP.md  # GitHub Projects guide
│   ├── SETUP_GOOGLE_CALENDAR.md  # Calendar integration
│   └── github-issues-to-create.md  # Issue templates
├── templates/          # Templates for notes
│   ├── daily-template.md
│   ├── weekly-template.md
│   ├── monthly-template.md
│   ├── meeting-template.md
│   ├── project-template.md
│   ├── spec-docs-template.md
│   └── spec-docs-megaprompt.md
├── scripts/            # Automation scripts
│   └── fireflies-import.py  # Import Fireflies meetings
├── archive/            # Processed/old files
│   ├── 2025-10-20.md
│   └── 2025-10-21-akunindo-gilles-feedback.md
├── inbox/              # Quick capture (process daily)
└── .trash/             # Deleted files (auto-cleaned by Obsidian)
```

---

## 🎯 Daily Workflow

### Morning (Start of Day)
1. **Receive morning message** with MIT and schedule
2. **Tackle MIT FIRST** (finish by 11am or lunch)
3. Review full schedule in `/daily/YYYY-MM-DD.md`
4. Check GitHub Projects for assigned tasks
5. Process inbox folder

### Evening (5-6 PM)
1. **Daily Review (EOD)**:
   - What did I accomplish?
   - MIT completed?
   - Blockers?
2. **Plan Tomorrow**:
   - Identify tomorrow's MIT
   - List top 3-5 tasks
   - Create tomorrow's schedule
3. **Inbox Processing**:
   - Email, WhatsApp/Telegram
   - Desktop cleanup, downloads folder

### Wind Down (9:30 PM)
- Close work apps
- Light stretching
- Walking meditation
- Bedtime by 10:00 PM

---

## 📊 Weekly Workflow

### Monday (Week Planning)
- Review last week (EOW)
- Set this week's goals
- Create GitHub Issues for sprint
- Prepare team meeting agenda

### Friday (Week Review)
- Check completion %
- Retrospective
- Carryover planning
- Archive completed tasks

---

## 🔗 Quick Links

### Core Documentation
- [WORKFLOW.md](productivity-system/WORKFLOW.md) - Daily/weekly routines
- [IMPORTANT-NOTES.md](productivity-system/IMPORTANT-NOTES.md) - Preferences & config
- [INBOX-SOURCES.md](productivity-system/INBOX-SOURCES.md) - Inbox processing

### GitHub Projects
- [Printora Board](https://github.com/orgs/Printora/projects/1)
- [FunDe.Fi Board](https://github.com/orgs/FUNDEdotFI/projects/1)
- [FavosApp Board](https://github.com/orgs/FavosApp/projects/2)

### Project Repositories
- [AkunIndo](https://github.com/sudosimonglitch/akunindo-website) - Beta prep
- [Printora](https://github.com/Printora/printora) - 80% MVP
- [FunDe.Fi](https://github.com/FUNDEdotFI/fundefi) - Frontend MVP
- [Favos App](https://github.com/FavosApp/favos-app)

### Spec-Docs
- [AkunIndo Spec-Docs](https://github.com/sudosimonglitch/akunindo-spec-docs)
- [Printora Spec-Docs](https://github.com/zee-mon/printora-spec-docs)
- [FunDe.Fi Spec-Docs](https://github.com/zee-mon/fundefi-spec-docs)

---

## 🛠️ Tools & Integrations

- **Task Management**: GitHub Projects + TODO.md in project repos
- **Notes**: Obsidian (synced via Git)
- **Calendar**: Google Calendar (MCP integration)
- **Meetings**: Fireflies.ai for transcriptions
- **Communication**: WhatsApp, Telegram, Email
- **Code**: VS Code with GitHub extensions
- **Automation**: Python scripts, Git hooks

---

## 📝 Key Concepts

### MIT (Most Important Task)
- **ONE task** per day that makes the day a success
- **Finish by 11am or lunch** (highest energy)
- **Tackle FIRST** before anything else

### EOD (End of Day) / EOW (End of Week)
- Daily review at 5-6 PM
- Weekly review on Fridays
- Track progress, identify blockers

### Inbox Zero Philosophy
- Email, calendar tasks, WhatsApp, desktop files, downloads
- Process regularly (daily or weekly)
- Nothing falls through the cracks

---

## 🚀 Current Projects

| Project | Status | Next Milestone | GitHub Org |
|---------|--------|----------------|------------|
| **AkunIndo** | Beta prep | Launch to 100 users | sudosimonglitch |
| **Printora** | 80% MVP | POD integration, beta | Printora |
| **FunDe.Fi** | Frontend MVP | Smart contracts | FUNDEdotFI |
| **Favos App** | TBD | Define status | FavosApp |

---

## ⚙️ Setup & Configuration

### Fireflies.ai Integration
```bash
# Import latest meeting
source ~/.zshrc && python3 /Users/simon/git/simon/scripts/fireflies-import.py import-latest

# List recent meetings
python3 /Users/simon/git/simon/scripts/fireflies-import.py list
```

### Google Calendar
- Configured via MCP (see `productivity-system/SETUP_GOOGLE_CALENDAR.md`)
- Shows: simon@favourse.com, simon@smaluhn.com
- Hides: seminardesk, other shared calendars

### Obsidian Git Sync
- **Mobile**: Use "Commit-and-sync" command
- **Desktop**: Auto-commit/push (every 30 min)
- **Inbox folder**: Default location for new files on mobile

---

## 📞 Support

For questions or issues with:
- **GitHub Projects**: See `productivity-system/GITHUB-PROJECTS-SETUP.md`
- **Daily Workflow**: See `productivity-system/WORKFLOW.md`
- **Automation**: Check `scripts/` folder

---

**Maintained by**: Simon
**Built with**: Claude Code + Obsidian + GitHub Projects
**Last System Audit**: 2025-10-23

