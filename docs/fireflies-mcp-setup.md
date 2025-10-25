# Fireflies.ai MCP Integration Setup

## Overview
This document describes the complete setup for integrating Fireflies.ai with Claude Code via MCP (Model Context Protocol), including webhook automation for processing new meetings.

## Current Status
- **MCP Package**: `fireflies-mcp-server` (v1.0.0)
- **Configuration File**: `/Users/simon/git/simon/.mcp.json`
- **API Key Location**: `~/.zshrc`
- **Status**: Configured, requires Claude Code restart to activate

---

## MCP Configuration

### 1. Package Information
The correct npm package for Fireflies MCP integration is:
- **Package Name**: `fireflies-mcp-server`
- **npm URL**: https://npm.im/fireflies-mcp-server
- **Version**: 1.0.0
- **Published**: 2025-06-24
- **Maintainer**: mikewille

**Note**: The package `@props-labs/fireflies-mcp` does NOT exist and will cause connection failures.

### 2. MCP Configuration File
Located at: `/Users/simon/git/simon/.mcp.json`

```json
{
  "mcpServers": {
    "fireflies": {
      "command": "npx",
      "args": [
        "-y",
        "fireflies-mcp-server"
      ],
      "env": {
        "FIREFLIES_API_KEY": "${FIREFLIES_API_KEY}"
      }
    }
  }
}
```

### 3. API Key Setup
Location: `~/.zshrc`

```bash
# Productivity System - Fireflies.ai API
export FIREFLIES_API_KEY="361247e5-1ad5-4072-b1c8-32f64f20ad39"
```

### 4. Claude Code Settings
Enable Fireflies MCP in Claude Code settings:
- File: `/Users/simon/git/simon/.claude/settings.local.json`
- Enabled in `enabledMcpjsonServers`: `["fireflies", ...]`
- Permission granted: `"mcp__fireflies__*"`

---

## Usage

### Getting Meeting Summaries
Once Claude Code is restarted, you can request:
- "Get my last Fireflies meeting summary"
- "Show me recent meetings from Fireflies"
- "Get transcript from [meeting name/date]"

### Available MCP Tools
The `fireflies-mcp-server` package provides tools for:
- Listing transcripts
- Getting transcript details
- Searching meetings
- Retrieving summaries

---

## Webhook Integration (To Be Implemented)

### Goal
Automatically process new Fireflies meetings and:
1. Extract action items
2. Create GitHub issues in relevant projects
3. Add tasks to delegated lists
4. Update project documentation

### Webhook Setup Steps

1. **Get Fireflies Webhook URL**
   - Navigate to Fireflies.ai Settings > Integrations > Webhooks
   - Create new webhook endpoint
   - Note the webhook URL provided

2. **Create Webhook Receiver**
   - Set up a local or cloud endpoint to receive webhook POST requests
   - Options:
     - Local: Use `ngrok` for development/testing
     - Cloud: Deploy to Vercel, Netlify Functions, or AWS Lambda

3. **Webhook Payload Structure**
   Expected payload from Fireflies when a new meeting completes:
   ```json
   {
     "event": "transcript.completed",
     "transcript_id": "...",
     "meeting_title": "...",
     "meeting_date": "...",
     "participants": [...],
     "summary": "...",
     "action_items": [...]
   }
   ```

4. **Processing Automation Script**
   Create script at: `/Users/simon/git/simon/scripts/process-fireflies-webhook.js`

   Features:
   - Parse webhook payload
   - Extract action items and key decisions
   - Identify relevant projects based on meeting content
   - Create GitHub issues using `gh` CLI or GitHub API
   - Update daily notes in `/Users/simon/git/simon/daily/`
   - Add delegated items to tracking system

5. **Integration with Claude Code**
   - Store webhook processing logic in project
   - Create slash command: `/process-meeting [transcript_id]`
   - Allow manual trigger for existing meetings

---

## Troubleshooting

### MCP Connection Failed
If `claude mcp list` shows Fireflies as "Failed to connect":

1. **Check package name**: Must be `fireflies-mcp-server`, not `@props-labs/fireflies-mcp`
2. **Verify API key**: `echo $FIREFLIES_API_KEY` should output your key
3. **Reload environment**: `source ~/.zshrc`
4. **Restart Claude Code**: Required after any `.mcp.json` changes
5. **Check npm**: `npx -y fireflies-mcp-server --help` should work

### API Key Not Found
```bash
# Ensure it's in ~/.zshrc
cat ~/.zshrc | grep FIREFLIES_API_KEY

# Source the file
source ~/.zshrc

# Verify it's set
echo $FIREFLIES_API_KEY
```

### Package Not Found
```bash
# Search for available packages
npm search fireflies-mcp

# Verify the correct package
npm info fireflies-mcp-server
```

---

## Next Steps

1. **Immediate**: Restart Claude Code to activate Fireflies MCP
2. **Test**: Request "Get my last Fireflies meeting summary"
3. **Webhook**: Set up webhook endpoint and processing automation
4. **Document**: Record webhook URL and automation workflow once implemented

---

## Related Files
- MCP Config: `/Users/simon/git/simon/.mcp.json`
- Environment: `~/.zshrc`
- Claude Settings: `/Users/simon/git/simon/.claude/settings.local.json`
- This Doc: `/Users/simon/git/simon/docs/fireflies-mcp-setup.md`

---

## Last Updated
2025-10-25 - Initial setup and documentation created
