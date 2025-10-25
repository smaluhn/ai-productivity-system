# Complete Setup Guide - AI Productivity System

## Core Setup (Required)

### 1. VSCode + Claude Code CLI

**What it is**: Claude Code is an AI-powered CLI that runs in your IDE. It's the brain of the entire system.

**Installation**:

1. **Install VSCode** (if you don't have it)
   ```bash
   # Download from https://code.visualstudio.com/
   # Or via brew:
   brew install --cask visual-studio-code
   ```

2. **Install Claude Code CLI**
   ```bash
   # Install via npm
   npm install -g @anthropic-ai/claude-code

   # Or follow official docs
   # https://docs.claude.com/en/docs/claude-code
   ```

3. **Launch Claude Code in VSCode**
   ```bash
   # Open VSCode
   code .

   # Open Claude Code (usually Cmd/Ctrl + Shift + P → "Claude Code")
   ```

4. **Authenticate**
   - Sign in with your Anthropic account
   - Grant necessary permissions

**Alternative LLMs**: While this guide uses Claude Code, the system works with:
- Cursor IDE (has built-in AI)
- GitHub Copilot Chat
- Any IDE with MCP support

---

### 2. MCP Configuration (.mcp.json)

**What is MCP?**: Model Context Protocol - allows Claude Code to interact with external tools.

**Location**: `/Users/yourusername/.mcp.json` (or in your project root)

**Create the file**:

```json
{
  "mcpServers": {
    "fireflies": {
      "command": "npx",
      "args": ["-y", "fireflies-mcp-server"],
      "env": {
        "FIREFLIES_API_KEY": "${FIREFLIES_API_KEY}"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    },
    "google-calendar": {
      "command": "npx",
      "args": ["@cocal/google-calendar-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS": "${GOOGLE_OAUTH_CREDENTIALS}"
      }
    },
    "reclaim": {
      "command": "npx",
      "args": ["-y", "reclaim-mcp-server"],
      "env": {
        "RECLAIM_API_KEY": "${RECLAIM_API_KEY}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"]
    }
  }
}
```

**Get API Keys**:

1. **Fireflies**: https://fireflies.ai/integrations/custom/fireflies-api
2. **GitHub**: https://github.com/settings/tokens (need `repo`, `read:org` scopes)
3. **Google Calendar**: Follow Google OAuth setup
4. **Reclaim.ai**: https://app.reclaim.ai/settings/api

**Set Environment Variables**:

```bash
# Add to ~/.zshrc or ~/.bashrc
export FIREFLIES_API_KEY="your-key-here"
export GITHUB_PERSONAL_ACCESS_TOKEN="your-token-here"
export GOOGLE_OAUTH_CREDENTIALS="your-credentials-here"
export RECLAIM_API_KEY="your-key-here"

# Reload shell
source ~/.zshrc
```

**Restart Claude Code** after adding MCP config!

---

### 3. Obsidian Setup

#### Desktop Obsidian

**Installation**:
```bash
# Download from https://obsidian.md/
# Or via brew:
brew install --cask obsidian
```

**Create Vault**:
1. Open Obsidian
2. "Create new vault"
3. Location: `/Users/yourusername/Obsidian/` (recommended)
4. Name: "Knowledge Base" or "Personal"

**Folder Structure** (recommended):
```
Obsidian/
├── Daily/
│   └── 2025-10-25.md
├── Projects/
│   ├── Printora/
│   └── AkunIndo/
├── Meetings/
│   └── 2025-10-25-bali-team-meeting.md
├── Templates/
│   ├── daily-note.md
│   └── meeting-note.md
└── Archive/
```

**Install Core Plugins**:
- Daily notes (built-in)
- Templates (built-in)
- Git (for backup) - Community plugin

#### Obsidian Mobile Sync

**Option 1: Obsidian Sync (Official - $8/month)**
1. Subscribe at https://obsidian.md/sync
2. Enable in desktop: Settings → Sync
3. Install Obsidian on mobile (iOS/Android)
4. Sign in → Sync vault

**Option 2: Git Sync (Free)**
1. Install **Obsidian Git** plugin (desktop)
2. Create git repo:
   ```bash
   cd ~/Obsidian
   git init
   git add .
   git commit -m "Initial vault"
   gh repo create yourusername/obsidian-vault --private --source=. --push
   ```
3. Mobile: Use **Working Copy** (iOS) or **Termux** (Android)
4. Configure auto-sync (pull on open, push on close)

**Option 3: iCloud/Dropbox (Free but slower)**
1. Move vault to iCloud Drive or Dropbox
2. Install Obsidian on mobile
3. Open vault from cloud location

**Recommended: Obsidian Sync** (most reliable for mobile)

---

### 4. GitHub Configuration

**Already done if you have GitHub CLI**:
```bash
gh auth status
```

**If not authenticated**:
```bash
gh auth login
# Follow prompts
# Choose: GitHub.com → HTTPS → Login with browser
```

**Create Personal Access Token** (for MCP):
```bash
# Go to: https://github.com/settings/tokens/new
# Scopes needed:
# - repo (full control)
# - read:org
# - read:project
# - write:org (if creating org projects)

# Add to environment:
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxxxxxxxxx"
```

---

### 5. Google Calendar MCP

**Get OAuth Credentials**:

1. Go to https://console.cloud.google.com/
2. Create new project (or use existing)
3. Enable Google Calendar API
4. Create OAuth 2.0 credentials
5. Download JSON credentials
6. Set environment variable:
   ```bash
   export GOOGLE_OAUTH_CREDENTIALS="$(cat path/to/credentials.json)"
   ```

**First Run**:
```bash
# In Claude Code, try:
# "Show me my calendar for today"
# It will prompt for OAuth authorization
# Follow the link, authorize, paste code back
```

---

## Optional Integrations

### 6. Reclaim.ai (AI Time Blocking)

**Setup**:
1. Sign up at https://reclaim.ai/
2. Connect Google Calendar
3. Get API key from https://app.reclaim.ai/settings/api
4. Add to `.mcp.json` (already in template above)

**What it does**:
- Auto-schedules tasks from GitHub
- Defends focus time
- Smart meeting scheduling

### 7. Telegram (Notifications)

**Setup**:
1. Get API credentials from https://my.telegram.org/apps
2. Add to `.mcp.json`:
   ```json
   "telegram": {
     "command": "npx",
     "args": ["-y", "telegram-mcp"],
     "env": {
       "TELEGRAM_API_ID": "${TELEGRAM_API_ID}",
       "TELEGRAM_API_HASH": "${TELEGRAM_API_HASH}",
       "TELEGRAM_SESSION": "${TELEGRAM_SESSION}"
     }
   }
   ```

**Use for**:
- Daily task reminders
- Deadline notifications
- Quick task capture via bot

---

## Verification Checklist

After setup, verify everything works:

### Claude Code CLI
- [ ] Claude Code opens in VSCode
- [ ] Can chat with Claude
- [ ] Can execute commands

### MCP Integrations
- [ ] Fireflies: `fireflies_get_transcripts --limit 5`
- [ ] GitHub: `gh issue list --repo yourrepo`
- [ ] Google Calendar: Ask "Show my calendar"
- [ ] Filesystem: Can read/write local files

### Obsidian
- [ ] Desktop vault created
- [ ] Mobile sync working (test by editing on phone)
- [ ] Daily notes working
- [ ] Templates configured

### GitHub
- [ ] `gh auth status` shows authenticated
- [ ] Can create issues via CLI
- [ ] MCP GitHub integration working

---

## The Workflow

Once everything is set up:

### Daily Routine

**Morning** (5 min):
1. Open Claude Code in VSCode
2. Ask: "Show my calendar for today"
3. Ask: "What GitHub issues are assigned to me?"
4. Open Obsidian daily note
5. Review tasks

**After Meeting** (15 min):
1. In Claude Code: "Get my last Fireflies meeting"
2. "Process this meeting and create GitHub issues"
3. Claude extracts action items
4. Creates issues with assignments
5. Saves meeting notes to Obsidian

**End of Day** (5 min):
1. Update issue status in GitHub
2. Update daily note in Obsidian
3. Sync Obsidian (mobile sync)

### Weekly Routine

**Monday** (30 min):
- Review last week's completed tasks
- Plan this week's priorities
- Update project boards
- Team standup

**Friday** (15 min):
- Review completed work
- Update CHANGELOG
- Plan next week
- Create next week's agenda

---

## Advanced Configuration

### Custom Commands

Create shortcuts in Claude Code:

```json
// In your IDE settings
{
  "claude-code.commands": {
    "process-meeting": "Get my last Fireflies meeting, extract action items, create GitHub issues",
    "daily-standup": "Show my calendar, GitHub issues assigned to me, and today's priorities",
    "weekly-review": "Show completed issues this week and progress on milestones"
  }
}
```

### Git Hooks

Auto-commit Obsidian changes:

```bash
# In ~/Obsidian/.git/hooks/post-commit
#!/bin/bash
git push origin main
```

### Automation Scripts

Create cron jobs for:
- Daily digest email
- Weekly summary
- Deadline reminders

---

## Troubleshooting

### Claude Code Not Finding MCP Servers

**Solution**:
1. Check `.mcp.json` location (should be in home directory or project root)
2. Restart Claude Code
3. Check environment variables are set
4. Try: `npx fireflies-mcp-server` manually to test

### Obsidian Sync Issues

**Solution**:
1. Check sync status in Obsidian settings
2. Force sync: Settings → Sync → Sync now
3. Check network connection
4. Clear sync cache if needed

### GitHub MCP Not Working

**Solution**:
1. Verify token has correct scopes
2. Test with: `gh api user` (should show your username)
3. Refresh auth: `gh auth refresh -s repo,read:org`
4. Restart Claude Code

### Google Calendar OAuth

**Solution**:
1. Check credentials.json is valid
2. Delete cached tokens: `rm ~/.cache/google-calendar-mcp/*`
3. Re-authorize when prompted

---

## What You Need To Do Now

Based on your current setup, here's what's left:

### ✅ Already Done
- VSCode (you're using it)
- Claude Code CLI (you're using it)
- GitHub CLI (you have it)
- Fireflies MCP (configured)
- Google Calendar MCP (configured)
- Reclaim.ai MCP (configured)

### 📋 To Do

1. **Verify MCP Configuration** (5 min)
   - Check `.mcp.json` has all integrations
   - Restart Claude Code
   - Test each integration

2. **Set Up Obsidian Mobile Sync** (15 min)
   - Choose sync method (Obsidian Sync recommended)
   - Install on mobile
   - Test sync by editing on phone

3. **Test Full Workflow** (15 min)
   - Process a Fireflies meeting
   - Create GitHub issues
   - Save to Obsidian
   - Check mobile sync

4. **Document Your Setup** (10 min)
   - Save your `.mcp.json` config
   - Note your folder structure
   - Keep API keys secure

### 🚀 Optional Enhancements

- Set up Telegram notifications
- Configure Reclaim.ai auto-scheduling
- Create custom Claude Code commands
- Set up git auto-commit for Obsidian

---

## Getting Help

- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code
- **MCP Documentation**: https://docs.anthropic.com/en/docs/mcp
- **Obsidian Forum**: https://forum.obsidian.md/
- **This Project**: https://github.com/smaluhn/ai-productivity-system/issues

---

## Summary

**Core Stack**:
- VSCode + Claude Code CLI (command center)
- MCP integrations (connect all tools)
- Obsidian + mobile sync (knowledge base)
- GitHub (task management)

**What makes it work**:
- Everything runs through Claude Code CLI
- MCP connects to all your tools
- Obsidian syncs everywhere (desktop + mobile)
- GitHub is single source of truth
- Automation removes manual work

**Result**:
- Meeting → Tasks in 15 min
- Mobile access to everything
- No context switching
- AI-powered workflows
- 20+ hours saved per week

---

**You're ready!** Test the workflow and report back any issues. 🚀
