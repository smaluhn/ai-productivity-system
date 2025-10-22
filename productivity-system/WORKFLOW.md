# Daily & Weekly Workflow

**Last Updated**: 2025-10-22

This document outlines the daily and weekly routines for productivity and planning.

---

## Daily Workflow

### Morning Routine (Start of Day)
**Receive morning schedule message from Claude with:**
- Today's full schedule
- **MIT (Most Important Task)** - The ONE thing to finish by 11am (or latest lunch)
- Top 3-5 tasks for the day
- Meeting times and prep needed

**Then:**
- [ ] Review today's schedule (check `daily-schedule-YYYY-MM-DD.md`)
- [ ] **Tackle MIT FIRST** - Finish by 11am or lunch
- [ ] Check GitHub Projects boards for assigned tasks
- [ ] Process Obsidian inbox folder (move notes to proper locations)
- [ ] Check calendar for meetings and full-day tasks

**MIT Philosophy:**
- **ONE task** that would make the day a success
- **Finish by 11am or lunch** (morning energy is highest)
- **Tackle first** before checking email/messages
- Examples: Close a sale, finish feature, make key decision

### During the Day
- [ ] Move GitHub Project cards to "In Progress" when starting work
- [ ] Update issue status and add comments for blockers
- [ ] Link PRs to issues (use `Closes #123` in PR description)
- [ ] Commit and sync Obsidian notes throughout the day

### Evening Planning (5-6 PM)
⏰ **Reminder Time: 5:00-6:00 PM UTC+8**

**Daily Review & Tomorrow Planning (15-20 min):**
1. **Review Today (EOD - End of Day Goals)**
   - [ ] What did I accomplish today?
   - [ ] Which GitHub issues did I complete?
   - [ ] What's still in progress?
   - [ ] Any blockers or issues?

2. **Plan Tomorrow**
   - [ ] Check calendar for tomorrow's meetings
   - [ ] Identify Most Important Task (MIT)
   - [ ] Create `daily-schedule-YYYY-MM-DD.md` for tomorrow
   - [ ] Assign priorities to tasks
   - [ ] Set realistic goals (3-5 major tasks max)

3. **Inbox Processing**
   - [ ] Process email (aim for inbox zero weekly)
   - [ ] Check WhatsApp/Telegram for important messages
   - [ ] Review Obsidian inbox folder
   - [ ] Clear desktop files
   - [ ] Check downloads folder

**Template for Daily Planning:**
```markdown
# Daily Schedule - [Date]

**MIT (Most Important Task)**: [Single most important thing - finish by 11am or lunch]

## Morning (High Energy - Tackle MIT First!)
- [ ] **MIT**: [Most important task]
- [ ] Task 2
- [ ] Task 3

## Afternoon
- [ ] Meeting at [time]
- [ ] Task 4

## Evening
- [ ] Task 5
- [ ] 5pm: Daily review & tomorrow planning
- [ ] 9:30pm: Wind down
- [ ] 10:00pm: Bedtime
```

**Claude Code Morning Message Format:**
```
Good morning, Simon! ☀️

Here's your schedule for [Date]:

🎯 **MIT (Most Important Task)**: [Task] - Finish by 11am or lunch!

📋 Top Tasks:
1. [MIT - tackle first!]
2. [Task 2]
3. [Task 3]

📅 Meetings:
- [Time]: [Meeting]
- [Time]: [Meeting]

⚡ Focus: Tackle your MIT before anything else!

Full schedule: /Users/simon/git/simon/productivity-system/daily-schedule-[date].md
```

### Evening Wind-Down (9:30 PM)
⏰ **Reminder Time: 9:30 PM UTC+8**

**Wind-Down Routine:**
- [ ] Close all work apps
- [ ] Light stretching
- [ ] Walking meditation
- [ ] Prepare for bed

**Bedtime Goal**: Before 10:00 PM

---

## Weekly Workflow

### Monday Morning Planning (Start of Week)
**Week Planning (30-45 min):**

1. **Review Last Week (EOW - End of Week Goals)**
   - [ ] What did we accomplish last week?
   - [ ] Which sprint goals were completed?
   - [ ] What carried over?
   - [ ] Team velocity check

2. **Plan This Week**
   - [ ] Set Sprint/Week field in GitHub Projects (e.g., "Week 43 2025")
   - [ ] Identify weekly goals per project:
     - AkunIndo: [goals]
     - Printora: [goals]
     - FunDe.Fi: [goals]
     - Favos App: [goals]
   - [ ] Create issues for this week's tasks
   - [ ] Assign to team members
   - [ ] Set priorities

3. **Team Meeting Preparation**
   - [ ] Review TODO.md files for each project
   - [ ] Check spec-docs for open questions
   - [ ] Prepare agenda for weekly team meetings

### Friday Review (End of Week)
**Week Review (15-20 min):**

1. **Completion Review**
   - [ ] Check "This Week" view in GitHub Projects
   - [ ] Calculate completion % per project
   - [ ] Review individual team member progress

2. **Retrospective**
   - [ ] What went well?
   - [ ] What didn't go well?
   - [ ] What can we improve next week?
   - [ ] Any process changes needed?

3. **Carryover Planning**
   - [ ] Move incomplete tasks to next week
   - [ ] Update priorities
   - [ ] Document blockers

---

## Reminder Schedule

| Time | Reminder | Action |
|------|----------|--------|
| **Morning** | Daily schedule review | Check today's tasks and meetings |
| **5:00-6:00 PM** | Evening planning | Review EOD, plan tomorrow |
| **9:30 PM** | Wind down | Stop work, light stretching, meditation |
| **10:00 PM** | Bedtime | Lights out |
| **Monday AM** | Week planning | Set weekly goals, assign tasks |
| **Friday PM** | Week review | Review EOW goals, retrospective |

---

## Weekly Team Meetings

### Schedule
- **2x per week in-person** (when possible)
- Typically includes: Simon, Kevin, Eko, Yosua
- Anjelito joins for FunDe.Fi/Favos discussions

### Standard Agenda
1. **Quick standup** (10 min)
   - What did you work on?
   - What are you working on?
   - Any blockers?

2. **Project reviews** (15-20 min each)
   - Review spec-docs if needed
   - Discuss technical decisions
   - Review open questions
   - Assign tasks

3. **Planning** (10 min)
   - Set goals for next meeting
   - Discuss upcoming deadlines

**Total**: 60-90 minutes

---

## Inbox Processing Schedule

| Source | Frequency | Goal |
|--------|-----------|------|
| **Email** | Weekly (minimum) | Inbox zero |
| **Calendar full-day tasks** | Daily | Convert to tasks |
| **WhatsApp/Telegram** | Daily | Process messages |
| **Desktop files** | Weekly | Clean/organize |
| **Downloads folder** | Weekly | Archive/delete |
| **Obsidian inbox** | Daily | Move to proper folders |
| **Fireflies meetings** | After each meeting | Extract action items |

See [INBOX-SOURCES.md](INBOX-SOURCES.md) for detailed processing workflows.

---

## GitHub Projects Workflow

### Daily
- Move cards to "In Progress" when starting
- Update status throughout the day
- Link PRs to issues
- Move to "Done" when completed

### Weekly (Monday)
- Set Sprint/Week field for new tasks
- Review "Backlog" → move to "To Do"
- Assign tasks to team
- Archive old "Done" items

### Weekly (Friday)
- Check completion %
- Move incomplete tasks to next week
- Update priorities

See [GITHUB-PROJECTS-SETUP.md](GITHUB-PROJECTS-SETUP.md) for detailed GitHub Projects workflows.

---

## Tools Used

- **Planning**: GitHub Projects, daily-schedule markdown files
- **Notes**: Obsidian (synced via Git)
- **Calendar**: Google Calendar (MCP integration)
- **Meetings**: Fireflies.ai for transcriptions
- **Communication**: WhatsApp, Telegram, Email
- **Task Tracking**: GitHub Issues + TODO.md files

---

## Automation & Reminders

### Claude Code Can Help:
- Create daily schedule at 5-6 PM
- Remind about wind-down at 9:30 PM
- Generate meeting agendas
- Extract Fireflies action items
- Process inbox sources
- Create GitHub issues from TODO.md

### Manual Review:
- Email (until automated)
- WhatsApp/Telegram (until automated)
- Phone alarms (phasing out)

---

## Success Metrics

**Daily:**
- ✅ MIT completed
- ✅ Evening planning done before 6 PM
- ✅ Wind down by 9:30 PM
- ✅ In bed before 10:00 PM

**Weekly:**
- ✅ All inboxes processed (email, desktop, downloads)
- ✅ Sprint goals 70%+ completed
- ✅ Team meetings held
- ✅ Week planning and review completed

**Monthly:**
- ✅ Project milestones hit
- ✅ Spec-docs updated
- ✅ TODO.md files current
- ✅ No major blockers

---

**Related Documents**:
- [IMPORTANT-NOTES.md](IMPORTANT-NOTES.md) - Preferences and configuration
- [INBOX-SOURCES.md](INBOX-SOURCES.md) - Inbox processing details
- [GITHUB-PROJECTS-SETUP.md](GITHUB-PROJECTS-SETUP.md) - Project board setup
- [CALENDAR-CONFIG.md](CALENDAR-CONFIG.md) - Calendar setup

---

**Last Updated**: 2025-10-22
