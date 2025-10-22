# Important Notes & Preferences

**Last Updated**: 2025-10-22

## GitHub Configuration

### Repository Privacy
⚠️ **ALWAYS CREATE NEW REPOS AS PRIVATE BY DEFAULT**

**Reasoning**:
- Protects sensitive project information
- Allows private development before public release
- Can always make public later if needed

**Exception**: Only make public if explicitly requested

**How to ensure**:
```bash
# When creating new repos with gh CLI
gh repo create <name> --private --source=. --remote=origin --push

# NOT public (unless explicitly requested)
gh repo create <name> --public --source=. --remote=origin --push
```

## GitHub Organizations & Accounts

### Organizations
| Organization | Projects | URL |
|-------------|----------|-----|
| **Printora** | Printora AI POD platform | https://github.com/Printora |
| **FUNDEdotFI** | FunDe.Fi DeFi launchpad | https://github.com/FUNDEdotFI |
| **FavosApp** | Favos App social loyalty | https://github.com/FavosApp |
| **DiverseProjects** | RealPrice, other projects | https://github.com/DiverseProjects |
| **Favourse** | (Favos-related) | https://github.com/Favourse |
| **Favorsid** | favors.id related repos | https://github.com/Favorsid |
| **sudosimonglitch** | AkunIndo, personal projects | https://github.com/sudosimonglitch |

### Personal Accounts
- **sudosimonglitch** (Simon's personal) - simonsmaluhn@gmail.com
- **zee-mon** (formerly favosapp, shared with Kevin) - Used primarily for Vercel deployments

### GitHub Projects Boards
| Project | Board URL |
|---------|-----------|
| **Printora** | https://github.com/orgs/Printora/projects/1 |
| **FunDe.Fi** | https://github.com/orgs/FUNDEdotFI/projects/1 |
| **FavosApp** | (to be created) |
| **AkunIndo** | (using TODO.md for now) |

**Current Active Account**: zee-mon (switched via `gh auth switch -u zee-mon`)

## Calendar Configuration

### Calendars to Show
✅ **simon@favourse.com** (Main/Work)
✅ **simon@smaluhn.com** (Personal)

### Calendars to Hide
❌ seminardesk
❌ Other shared/subscribed calendars (unless specifically needed)

### Full-Day Events
✅ **Always show** full-day events, especially those marked as "Free" availability
- These are used as reminders
- Should be visible in daily calendar view
- Process as inbox items (convert to tasks if needed)

## Email Accounts

### To Be Connected
- simon@favourse.com
- simon@smaluhn.com
- *(Add other email accounts)*

### Review Frequency
- **Minimum**: Once per week
- **Goal**: Inbox zero weekly
- **Action**: Unsubscribe aggressively from newsletters/promotions

## Inbox Philosophy

**Goal**: Zero or near-zero for all inbox sources

**Why**:
- Reduces mental clutter
- Nothing falls through cracks
- Clear overview of what needs attention
- Easier to focus on important work

**Sources**:
- Email (multiple accounts)
- Calendar full-day tasks (marked "Free")
- Phone alarms (bad habit to phase out)
- Desktop files
- Downloads folder
- WhatsApp/Telegram (future)
- Meeting transcriptions (Fireflies.ai)

See [INBOX-SOURCES.md](INBOX-SOURCES.md) for detailed breakdown.

## Work Preferences

### Communication
- **Meetings**: Import via Fireflies.ai, extract action items
- **Async**: Prefer written communication (email, Telegram) over calls when possible
- **Inbox**: Multiple sources, need regular processing

### File Organization
- **Keep desktop clean**: No loose files
- **Downloads folder**: Process weekly, archive or delete
- **Text files**: Move to proper notes system

### Task Management
- **GitHub Projects**: Primary team task management (Kanban boards per org)
  - Printora: https://github.com/orgs/Printora/projects/1
  - FunDe.Fi: https://github.com/orgs/FUNDEdotFI/projects/1
  - Weekly planning, sprint tracking, team collaboration
- **TODO.md**: Personal task tracking in each project folder (committed to Git)
  - High-level project notes, offline access
  - Synced via Git, accessible on mobile via Obsidian
- **ClickUp**: Being phased out in favor of GitHub Projects

## Technical Preferences

### Development
- **Node.js**: v18+ preferred
- **TypeScript**: Strict mode
- **Git**: Commit messages follow Conventional Commits
- **Documentation**: Markdown, co-located with code

### Tools
- **Editor**: VS Code
- **Terminal**: zsh
- **Notes**: Obsidian (synced via Git)
- **Calendar**: Google Calendar
- **Meetings**: Fireflies.ai for transcriptions

## Project Statuses

| Project | Status | Next Milestone |
|---------|--------|---------------|
| **AkunIndo** | Beta prep | Launch to 100 users |
| **Printora** | 80% MVP complete | POD integration, beta launch |
| **FunDe.Fi** | Frontend MVP done | Smart contract development |
| **Favos App** | ? | (check status) |

## Pending Decisions

See individual project TODO.md files and project spec-docs OPEN-QUESTIONS.md for detailed pending decisions.

---

**Related Documents**:
- [INBOX-SOURCES.md](INBOX-SOURCES.md) - All inbox sources and processing
- [WORKFLOW.md](WORKFLOW.md) - Daily/weekly workflows
- [CALENDAR-CONFIG.md](CALENDAR-CONFIG.md) - Calendar setup
