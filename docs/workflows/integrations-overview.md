# AI Productivity System - Integrations Overview

## Core Integrations (Active)

### 1. Fireflies.ai (Meeting Transcription)
**Status**: ✅ Active
**Purpose**: Automatic meeting transcription and note-taking
**MCP**: `fireflies-mcp-server`

**Features:**
- Auto-transcribe all meetings
- Generate summaries
- Extract action items
- Search past meetings

**Workflow:**
1. Meeting happens → Fireflies records
2. Retrieve transcript via MCP
3. Process into meeting notes
4. Extract action items
5. Create GitHub issues

**Configuration:**
```json
{
  "fireflies": {
    "command": "npx",
    "args": ["-y", "fireflies-mcp-server"],
    "env": {
      "FIREFLIES_API_KEY": "${FIREFLIES_API_KEY}"
    }
  }
}
```

### 2. GitHub (Task & Project Management)
**Status**: ✅ Active
**Purpose**: Issue tracking, project management, code repository
**MCP**: `@modelcontextprotocol/server-github`

**Features:**
- Create/manage issues
- Project boards (kanban)
- Pull requests and code review
- Milestones and labels
- Organization-level coordination

**Workflow:**
1. Action items from meetings → GitHub issues
2. Issues added to project boards
3. Team tracks progress
4. PRs linked to issues
5. Automated status updates

**Configuration:**
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
    }
  }
}
```

### 3. Google Calendar (Schedule & Time Management)
**Status**: ✅ Active
**Purpose**: Calendar management, meeting scheduling, availability
**MCP**: `@cocal/google-calendar-mcp`

**Features:**
- View/create calendar events
- Check availability
- Block time for tasks
- Sync with meetings
- Multiple calendar support

**Workflow:**
1. Meetings scheduled → Calendar events
2. Task deadlines → Calendar blocks
3. Daily schedule review
4. Automatic reminders
5. Integration with Reclaim.ai

**Configuration:**
```json
{
  "google-calendar": {
    "command": "npx",
    "args": ["@cocal/google-calendar-mcp"],
    "env": {
      "GOOGLE_OAUTH_CREDENTIALS": "${GOOGLE_OAUTH_CREDENTIALS}"
    }
  }
}
```

### 4. Obsidian (Note-Taking & Knowledge Base)
**Status**: ✅ Active (Local)
**Purpose**: Personal knowledge management, note-taking, linking ideas

**Features:**
- Daily notes
- Meeting notes backup
- Knowledge graph
- Linking notes
- Markdown-based
- Git sync for backup

**Workflow:**
1. Meeting notes also saved to Obsidian
2. Daily notes with task references
3. Knowledge base for project docs
4. Backlinks to related notes
5. Git sync to backup

**Integration:**
- Save meeting notes to Obsidian vault
- Link to GitHub issues
- Cross-reference project notes
- Daily review in daily notes

**Location**: `/Users/simon/Obsidian/` or configured vault

---

## Calendar & Scheduling Integrations

### 5. Reclaim.ai (AI Calendar Management)
**Status**: ✅ Active
**Purpose**: Intelligent time blocking, habit scheduling, task time allocation
**MCP**: `reclaim-mcp-server`

**Features:**
- Auto-schedule tasks from GitHub
- Defend focus time
- Smart meeting scheduling
- Habit scheduling
- Buffer time management
- Sync with Google Calendar

**Workflow:**
1. GitHub issues → Reclaim tasks
2. Reclaim auto-schedules work time
3. Defends focus blocks
4. Reschedules when meetings added
5. Updates Google Calendar

**Configuration:**
```json
{
  "reclaim": {
    "command": "npx",
    "args": ["-y", "reclaim-mcp-server"],
    "env": {
      "RECLAIM_API_KEY": "${RECLAIM_API_KEY}"
    }
  }
}
```

**Future Automation:**
- Auto-create Reclaim tasks from GitHub issues
- Sync task completion status
- Adjust time blocks based on actual time spent
- Weekly capacity planning

### 6. Calendly (External Meeting Scheduling)
**Status**: 🔄 Manual (No MCP yet)
**Purpose**: Let others schedule meetings with you

**Features:**
- Share booking link
- Auto-sync with Google Calendar
- Buffer time before/after
- Meeting type templates
- Integration with Reclaim.ai

**Workflow:**
1. Share Calendly link with clients/partners
2. They book available slot
3. Auto-adds to Google Calendar
4. Reclaim.ai adjusts schedule
5. Pre-meeting prep time blocked

**Integration Points:**
- Connected to Google Calendar
- Respects Reclaim.ai focus time
- Sets up Fireflies for recording
- Auto-creates meeting prep tasks

---

## Social Media & Content Platform

### 7. X/Twitter (Social Media)
**Status**: 🔄 Structure Ready, MCP Not Yet Connected
**Purpose**: Share updates, build-in-public, engage community

**Features** (When MCP Connected):
- Auto-post from content folder
- Schedule tweets
- Thread posting
- Analytics tracking
- Cross-post to other platforms

**Content Structure:**
```
content/social-media/twitter/
├── posts/
│   └── 2025-10-26-productivity-system-launch.md
└── threads/
    └── 2025-10-26-why-i-built-this.md
```

**Workflow:**
1. Write post in markdown
2. Set status: draft → scheduled
3. MCP auto-posts at scheduled time
4. Track engagement
5. Save to archive

**Future MCP**: Twitter/X MCP integration (when available)

### 8. LinkedIn (Professional Network)
**Status**: 🔄 Structure Ready, MCP Not Yet Connected
**Purpose**: Professional updates, thought leadership, networking

**Features** (When MCP Connected):
- Auto-post articles
- Share project updates
- Professional tone
- Cross-post from blog
- Analytics

**Content Structure:**
```
content/social-media/linkedin/
├── posts/
│   └── 2025-10-26-ai-productivity-system.md
└── articles/
    └── 2025-10-26-how-we-manage-remote-team.md
```

**Workflow:**
1. Write post/article
2. Convert from blog if needed
3. Schedule posting
4. MCP auto-publishes
5. Track engagement

**Future MCP**: LinkedIn MCP integration

### 9. Facebook (Social Network)
**Status**: 🔄 To Add
**Purpose**: Share updates, community building, business page

**Use Cases:**
- Personal updates
- Project announcements
- Community engagement
- Business page for projects (Printora, AkunIndo)

**Content Types:**
- Status updates
- Photo/video posts
- Links to blog posts
- Event announcements

**Structure** (To Create):
```
content/social-media/facebook/
├── personal/
└── business/
    ├── printora/
    └── akunindo/
```

**Note**: Facebook Graph API is free for basic posting

### 10. Threads (Text-Based Social)
**Status**: 🔄 Structure Ready, MCP Not Yet Connected
**Purpose**: Quick updates, casual engagement

**Content Structure:**
```
content/social-media/threads/
└── posts/
    └── 2025-10-26-quick-update.md
```

### 11. Substack (Newsletter/Blog Platform)
**Status**: 🔄 To Add
**Purpose**: Long-form content, newsletter, subscriber base building

**Features:**
- Free publishing platform
- Built-in newsletter
- Subscriber management
- Comments and community
- Monetization option (later)

**Use Cases:**
- Weekly project updates
- Build-in-public series
- Technical tutorials
- Lessons learned

**Content Strategy:**
- Blog posts from simon.smaluhn.com → Substack
- Or vice versa
- Cross-link between platforms
- Weekly/monthly newsletter

**Integration:**
- RSS feed from blog
- Email notification to subscribers
- Cross-post to social media
- Archive on personal website

**Structure** (To Create):
```
content/substack/
├── newsletters/
│   └── 2025-10-week-43-update.md
├── articles/
│   └── 2025-10-26-ai-productivity-system.md
└── drafts/
```

### 12. Personal Blog (simon.smaluhn.com)
**Status**: 🔄 Need Tech Stack Info
**Purpose**: Central content hub, portfolio, personal brand

**Integration Points:**
- Auto-post from markdown
- Cross-post to Substack
- Share on social media
- Link from all platforms
- SEO optimization

**Content Flow:**
```
Write Post (Markdown)
    ↓
Blog (simon.smaluhn.com)
    ↓
├→ Substack (newsletter)
├→ LinkedIn (snippet + link)
├→ Twitter (announcement)
└→ Facebook (share)
```

**Needs:**
- Tech stack info (Static site? CMS? Custom?)
- API or file-based posting?
- Build/deploy process?

---

## Database & Storage

### 13. PostgreSQL (Database)
**Status**: ✅ MCP Available
**Purpose**: Data storage, analytics, task history
**MCP**: `@modelcontextprotocol/server-postgres`

**Use Cases:**
- Store task completion history
- Analytics on team velocity
- Time tracking data
- Custom reports
- Metrics dashboard

**Configuration:**
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": {
      "POSTGRES_CONNECTION_STRING": "${POSTGRES_CONNECTION_STRING}"
    }
  }
}
```

### 14. Filesystem (Local Storage)
**Status**: ✅ MCP Available
**Purpose**: Read/write local files, manage content
**MCP**: `@modelcontextprotocol/server-filesystem`

**Use Cases:**
- Manage meeting notes locally
- Process markdown files
- Sync with git
- Organize project files

---

## Communication

### 15. Telegram (Messaging)
**Status**: ✅ MCP Available
**Purpose**: Team communication, notifications, quick updates
**MCP**: `telegram-mcp`

**Features:**
- Send notifications
- Bot for team updates
- Quick task capture
- File sharing
- Group chats

**Configuration:**
```json
{
  "telegram": {
    "command": "npx",
    "args": ["-y", "telegram-mcp"],
    "env": {
      "TELEGRAM_API_ID": "${TELEGRAM_API_ID}",
      "TELEGRAM_API_HASH": "${TELEGRAM_API_HASH}",
      "TELEGRAM_SESSION": "${TELEGRAM_SESSION}"
    }
  }
}
```

**Use Cases:**
- Daily task reminders
- Deadline notifications
- Team status updates
- Quick captures via bot
- Meeting reminders

---

## Integration Roadmap

### Phase 1: Active Now ✅
- [x] Fireflies (meetings)
- [x] GitHub (tasks)
- [x] Google Calendar (scheduling)
- [x] Obsidian (notes)
- [x] Reclaim.ai (time management)

### Phase 2: Structure Ready 🔄
- [x] X/Twitter (content structure)
- [x] LinkedIn (content structure)
- [x] Threads (content structure)
- [ ] MCP connections for social media

### Phase 3: To Add 📋
- [ ] Facebook integration
- [ ] Substack integration
- [ ] simon.smaluhn.com blog automation
- [ ] Calendly automation (if MCP available)

### Phase 4: Advanced 🚀
- [ ] PostgreSQL analytics
- [ ] Telegram bot for task capture
- [ ] Cross-platform content sync
- [ ] Automated posting schedule
- [ ] Analytics dashboard

---

## Integration Map

```
INPUTS (Information In)
├── Fireflies → Meeting transcripts
├── Google Calendar → Schedule data
├── GitHub → Issues, PRs, commits
└── Telegram → Quick captures

PROCESSING (AI + Automation)
├── Claude Code → Process transcripts
├── Extract action items
├── Create tasks
└── Schedule content

STORAGE (Single Source of Truth)
├── GitHub → All tasks
├── Obsidian → Knowledge base
├── Filesystem → Meeting notes
└── PostgreSQL → Analytics

OUTPUTS (Information Out)
├── Reclaim.ai → Scheduled work time
├── Google Calendar → Updated schedule
├── X/Twitter → Social posts
├── LinkedIn → Professional content
├── Blog → Long-form articles
├── Substack → Newsletters
└── Telegram → Notifications

COORDINATION
└── GitHub Projects → Team dashboard
```

---

## Next Steps

### Immediate
1. ✅ Fireflies, GitHub, Google Calendar, Reclaim - Already working
2. 🔄 Set up social media MCPs (Twitter, LinkedIn) when available
3. 📋 Add Facebook and Substack structure
4. 📋 Blog integration (need tech stack info)

### Soon
1. Automate content posting workflow
2. Set up Telegram notifications
3. Create analytics dashboard
4. Cross-platform content sync

### Future
1. Mobile app integration
2. Voice capture for tasks
3. AI-powered content generation
4. Advanced analytics and insights
