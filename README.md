# Simon's Productivity System

> A fast, markdown-based productivity system built with Claude Code and designed for Obsidian sync.

## 🎯 Philosophy

- **Speed over features** - Plain text markdown beats slow web apps
- **Git-based** - Version control + easy mobile sync
- **CLI-first** - Claude Code integration for AI-assisted workflows
- **Project-linked** - Connected to actual code projects in `/git/PROJECTS/`

## 📁 Structure

```
simon/
├── daily/              # Daily notes with MIT (Most Important Task)
├── weekly/             # Weekly goals and reviews
├── monthly/            # Monthly objectives
├── meetings/           # Meeting notes
├── projects/           # Project tracking
├── inbox/              # Quick capture area
├── templates/          # Reusable templates
├── index.md            # Main dashboard
└── .mcp.json           # MCP server configuration
```

## 🚀 Quick Start

### 1. View Your Dashboard
```bash
cd /Users/simon/git/simon
cat index.md
```

### 2. Start Your Day
- Open `daily/2025-10-20.md` (or today's date)
- Set your MIT (Most Important Task) - complete before 11am
- Review calendar events (once Google Calendar is set up)
- Check weekly goals in `weekly/2025-W42.md`

### 3. Capture Quick Notes
Drop text files in `inbox/` - process them weekly

### 4. Track Projects
Each project in `projects/` links to code in `/git/PROJECTS/`

## 📱 Mobile Access with Obsidian

### Setup
1. Install Obsidian on Android
2. Install "Obsidian Git" plugin
3. Point vault to `/Users/simon/git/simon`
4. Configure auto-sync

### Benefits
- Access all notes on mobile
- Edit on the go
- Auto-sync via Git
- Great markdown editor

## 🗓️ Google Calendar Integration

### Status
Configuration ready in `.mcp.json` - follow setup guide

### Setup Steps
1. Read `SETUP_GOOGLE_CALENDAR.md` for detailed instructions
2. Create Google Cloud project
3. Enable Calendar API
4. Download OAuth credentials
5. Set environment variable
6. Restart Claude Code

Once configured, you can:
- See calendar events in daily notes
- Ask Claude to create/check events
- Sync schedule automatically

## 📝 Daily Workflow

### Morning Routine
1. Open today's daily note
2. Set your MIT (Most Important Task)
3. Review calendar events
4. Check weekly goals
5. Complete MIT before 11am

### Throughout Day
- Update tasks as you work
- Add notes to relevant sections
- Capture quick thoughts in inbox

### End of Day
- Mark completed tasks
- Review progress
- Plan tomorrow's MIT

## 📅 Weekly Workflow

### Monday
- Review weekly goals (`weekly/2025-W42.md`)
- Set daily MITs for the week
- Check project statuses

### Friday (EOW - End of Week)
- Complete weekly review
- Update project statuses
- Plan next week's goals

## 📆 Monthly Workflow

### Start of Month
- Set 3-5 key monthly goals
- Review active projects
- Update priorities

### End of Month
- Complete monthly review
- Evaluate goal completion
- Plan next month

## 🔗 Project Links

Projects in `/Users/simon/git/PROJECTS/` can have their own `todos.md`:
- Link from `projects/*.md` to project-specific todos
- Keep project context in both places
- Bidirectional references

Example in `projects/printora.md`:
```markdown
## Links
- [Todos in repo](../PROJECTS/printora/todos.md)
```

## 🛠️ Technology Stack

- **Editor**: Claude Code CLI + Obsidian
- **Format**: Markdown
- **Sync**: Git
- **Calendar**: Google Calendar (via MCP)
- **Mobile**: Obsidian Android app

## 📋 Templates

Located in `templates/`:
- `daily-template.md` - MIT, tasks, calendar, notes
- `weekly-template.md` - Goals, EOW targets, daily links
- `monthly-template.md` - Monthly goals, weekly breakdown
- `meeting-template.md` - Agenda, notes, action items
- `project-template.md` - Status, tasks, repo links

## 🎨 Customization

### Add a New Project
```bash
# Create from template
cp templates/project-template.md projects/your-project.md
# Edit and customize
```

### Add a Meeting Note
```bash
# Create from template
cp templates/meeting-template.md meetings/meeting-name-2025-10-20.md
# Fill in details
```

### Process Inbox
1. Review files in `inbox/`
2. Move to appropriate folder (meetings, projects, etc.)
3. Or integrate into existing notes
4. Delete from inbox

## 💡 Tips

1. **One MIT per day** - Focus on what matters most
2. **11am deadline** - Build momentum early
3. **Weekly reviews** - Don't skip Friday EOW review
4. **Inbox zero** - Process weekly, don't let it pile up
5. **Link everything** - Use `[[links]]` liberally in Obsidian
6. **Desktop files** - Move to `inbox/` instead of cluttering desktop

## 🔮 Future Enhancements

- [ ] Automated daily note creation
- [ ] Calendar event sync in daily notes
- [ ] Weekly email digest
- [ ] Project status dashboard
- [ ] Mobile app with Claude integration (optional)

## 📚 Key Files

- `index.md` - Your main dashboard, start here
- `SETUP_GOOGLE_CALENDAR.md` - Calendar integration guide
- `.mcp.json` - MCP server configuration
- `.gitignore` - Keeps credentials safe

## 🔒 Security

- Credentials never committed to Git
- `.gitignore` protects sensitive files
- Environment variables for API keys
- Token storage encrypted locally

---

**Created:** 2025-10-20
**Last Updated:** 2025-10-20
**Built with:** Claude Code + Obsidian + Google Calendar MCP
