# MCP Server Setup Guide

**Last Updated:** 2025-10-24
**Repository:** /Users/simon/git/simon

---

## Overview

This repository is configured with **7 MCP servers** to extend Claude Code's capabilities:

1. **Google Calendar** - Calendar management ✅ Already configured
2. **GitHub** - Repository and issue management 🆕 New
3. **Telegram** - Messaging and group management 🆕 New
4. **Reclaim.ai** - AI calendar and task management 🆕 New
5. **Fireflies.ai** - Meeting transcription analysis 🆕 New
6. **PostgreSQL** - Database operations 🆕 New
7. **File System** - Extended file operations 🆕 New

---

## Configuration Status

### ✅ Fully Configured
- **Google Calendar** - OAuth credentials set up

### ⚙️ Needs API Keys/Setup
- **GitHub** - Needs Personal Access Token
- **Telegram** - Needs API credentials + session
- **Reclaim.ai** - Needs API token
- **Fireflies.ai** - Needs API key
- **PostgreSQL** - Needs connection string (if using)
- **File System** - No credentials needed ✅

---

## Setup Instructions

### 1. GitHub MCP

**Purpose:** Manage repositories, issues, PRs across your organizations (DiverseProjects, FavosApp, favourse, Printora, FUNDEdotFI, Favorsid)

**Setup Steps:**

1. Create GitHub Personal Access Token:
   - Go to: https://github.com/settings/tokens/new
   - Login as: **smaluhn**
   - Token name: "Claude Code MCP - Full Access"
   - Expiration: 1 year (or no expiration)
   - Scopes needed:
     - ✓ `repo` (Full control of private repositories)
     - ✓ `workflow` (Update GitHub Action workflows)
     - ✓ `admin:org` (Full control of orgs and teams)
     - ✓ `project` (Full control of projects)
   - Click "Generate token"
   - **COPY THE TOKEN IMMEDIATELY**

2. Save token in 1Password:
   - Title: "GitHub PAT - smaluhn - Claude Code MCP"
   - Category: API Credential
   - Store the token securely

3. Add to environment:
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_your_token_here"

   # Reload shell
   source ~/.zshrc
   ```

4. Verify:
   ```bash
   echo $GITHUB_PERSONAL_ACCESS_TOKEN
   ```

**Capabilities:**
- Create/update/close issues across all your orgs
- Manage PRs, projects
- Search repositories
- View organization members
- Automate GitHub project management (perfect for AkunIndo!)

---

### 2. Telegram MCP

**Purpose:** Connect to Telegram groups like Printora.ai, send messages, analyze conversations

**Setup Steps:**

1. **Get Telegram API Credentials:**
   - Go to: https://my.telegram.org/apps
   - Login with your phone number
   - Click "API Development Tools"
   - Create a new application:
     - App title: "Claude Code MCP"
     - Short name: "claude-mcp"
     - Platform: Desktop
   - **Copy:**
     - `api_id` (numeric)
     - `api_hash` (alphanumeric string)

2. **Save in 1Password:**
   - Title: "Telegram API Credentials - Claude Code MCP"
   - Store both `api_id` and `api_hash`

3. **Add to environment:**
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export TELEGRAM_API_ID="your_api_id"
   export TELEGRAM_API_HASH="your_api_hash"
   export TELEGRAM_SESSION="session_name"  # Can be any name like "claude-mcp"

   # Reload shell
   source ~/.zshrc
   ```

4. **First Time Setup:**
   - When you first use the Telegram MCP, it will ask for your phone number
   - You'll receive a code via Telegram
   - Enter the code to authenticate
   - Session will be saved and reused

**Capabilities:**
- List all your chats/groups
- Send messages to Printora.ai group
- Read message history
- Search conversations
- Analyze group discussions
- Automate responses

**Example Use Cases:**
- "Send a status update to the Printora.ai Telegram group"
- "What were the main topics discussed in Printora group this week?"
- "Search for mentions of 'invoice' in Printora chat"

---

### 3. Reclaim.ai MCP

**Purpose:** Manage your AI-powered calendar and tasks

**Setup Steps:**

1. **Get Reclaim API Token:**
   - Go to: https://app.reclaim.ai/settings/developer
   - Login to your Reclaim.ai account
   - Click "Create new token"
   - Name: "Claude Code MCP"
   - Copy the token

2. **Save in 1Password:**
   - Title: "Reclaim.ai API Token - Claude Code MCP"

3. **Add to environment:**
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export RECLAIM_API_TOKEN="your_token_here"

   # Reload shell
   source ~/.zshrc
   ```

**Capabilities:**
- Create and manage tasks
- Schedule focus time
- View calendar events
- Optimize your schedule
- Integrate with Google Calendar data

**Why useful?**
- You already use Reclaim.ai
- Automate task creation from conversations
- "Schedule 2 hours of focus time for Printora development this week"

---

### 4. Fireflies.ai MCP

**Purpose:** Access and analyze meeting transcriptions

**Setup Steps:**

1. **Get Fireflies API Key:**
   - Go to: https://app.fireflies.ai/integrations/custom/api
   - Login to your Fireflies.ai account
   - Click "Generate API Key"
   - Copy the key

2. **Save in 1Password:**
   - Title: "Fireflies.ai API Key - Claude Code MCP"

3. **Add to environment:**
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export FIREFLIES_API_KEY="your_api_key_here"

   # Reload shell
   source ~/.zshrc
   ```

**Capabilities:**
- Search meeting transcripts
- Generate meeting summaries
- Find action items across meetings
- Analyze discussions
- Extract insights from calls

**Why useful?**
- You already use Fireflies.ai
- "Summarize all meetings from last week about Printora"
- "What action items came out of yesterday's standup?"
- "Search all meetings for discussions about pricing"

---

### 5. PostgreSQL MCP

**Purpose:** Direct database access for your projects

**Setup Steps:**

1. **Get Database Connection String:**
   - Format: `postgresql://username:password@host:port/database`
   - Example: `postgresql://simon:mypass@localhost:5432/printora_db`

2. **Save in 1Password:**
   - Title: "PostgreSQL Connection - Claude Code MCP"
   - Store full connection string

3. **Add to environment:**
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export POSTGRES_CONNECTION_STRING="postgresql://user:pass@host:port/db"

   # Reload shell
   source ~/.zshrc
   ```

**Capabilities:**
- Query databases directly
- Analyze data
- Generate reports
- Debug database issues
- Create/modify schemas

**Security Note:**
- Only use for development/staging databases
- Never for production without read-only credentials

---

### 6. File System MCP

**Purpose:** Extended file operations beyond basic read/write

**Setup:**
- ✅ No configuration needed!
- Already enabled and ready to use

**Capabilities:**
- Advanced file searching
- Batch operations
- File metadata access
- Directory watching

---

## Quick Setup Checklist

After adding all API keys to your environment, verify:

```bash
# Check all environment variables are set
echo "GitHub: ${GITHUB_PERSONAL_ACCESS_TOKEN:0:10}..."
echo "Telegram ID: $TELEGRAM_API_ID"
echo "Telegram Hash: ${TELEGRAM_API_HASH:0:10}..."
echo "Reclaim: ${RECLAIM_API_TOKEN:0:10}..."
echo "Fireflies: ${FIREFLIES_API_KEY:0:10}..."
echo "Postgres: ${POSTGRES_CONNECTION_STRING:0:20}..."
```

All should show partial values (not empty).

---

## Auto-Approval Configuration

All MCP servers have been added to auto-approval in `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "mcp__google-calendar__*",
      "mcp__github__*",
      "mcp__telegram__*",
      "mcp__reclaim__*",
      "mcp__fireflies__*",
      "mcp__postgres__*",
      "mcp__filesystem__*"
    ]
  }
}
```

You can use these tools without approval prompts!

---

## Testing MCP Servers

Once configured, test each server:

### Test GitHub:
```
"List all repositories in the DiverseProjects organization"
```

### Test Telegram:
```
"List my Telegram groups"
"Show recent messages from Printora.ai group"
```

### Test Reclaim:
```
"Show my tasks for this week"
"Schedule 2 hours of focus time tomorrow"
```

### Test Fireflies:
```
"List my recent meeting transcripts"
"Summarize yesterday's standup meeting"
```

### Test PostgreSQL:
```
"Show all tables in the database"
"Count users in the users table"
```

---

## Troubleshooting

### MCP Server Not Working

1. **Check environment variables:**
   ```bash
   env | grep -E "GITHUB|TELEGRAM|RECLAIM|FIREFLIES|POSTGRES"
   ```

2. **Restart Claude Code:**
   - Exit current session
   - Start new session to reload environment

3. **Check MCP status:**
   ```bash
   claude mcp list
   ```

4. **View MCP logs:**
   - Check `~/.config/Claude/debug/` for error logs

### Session/Authentication Issues

- **Telegram:** Delete session file and re-authenticate
- **GitHub:** Regenerate token if expired
- **Reclaim/Fireflies:** Check if API key is still valid

---

## Environment Variables Reference

Add these to `~/.zshrc` or `~/.bashrc`:

```bash
# Google Calendar (already set up)
export GOOGLE_OAUTH_CREDENTIALS="your_oauth_credentials"

# GitHub
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_your_token_here"

# Telegram
export TELEGRAM_API_ID="your_api_id"
export TELEGRAM_API_HASH="your_api_hash"
export TELEGRAM_SESSION="claude-mcp"

# Reclaim.ai
export RECLAIM_API_TOKEN="your_reclaim_token"

# Fireflies.ai
export FIREFLIES_API_KEY="your_fireflies_key"

# PostgreSQL (optional, only if using)
export POSTGRES_CONNECTION_STRING="postgresql://user:pass@host:port/db"
```

Don't forget to reload after editing:
```bash
source ~/.zshrc
```

---

## Security Best Practices

1. **Store all tokens in 1Password** - Never commit to git
2. **Use environment variables** - Keep credentials out of code
3. **Rotate tokens quarterly** - Update every 3 months
4. **Read-only database access** - For production databases
5. **Monitor API usage** - Check for unusual activity

---

## Next Steps

1. ✅ Set up GitHub PAT (highest priority for project management)
2. ✅ Set up Telegram API (connect to Printora.ai group)
3. ✅ Set up Reclaim.ai token (you already use this)
4. ✅ Set up Fireflies API (you already use this)
5. ⏸️ PostgreSQL (only if needed for specific projects)

Once these are configured, you'll have a powerful automation system!

---

**Questions?** Check the official documentation:
- GitHub MCP: https://github.com/modelcontextprotocol/servers/tree/main/src/github
- Telegram MCP: https://github.com/chigwell/telegram-mcp
- Reclaim MCP: https://github.com/jj3ny/reclaim-mcp-server
- Fireflies MCP: https://docs.fireflies.ai/getting-started/mcp-configuration
