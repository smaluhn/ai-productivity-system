# Fireflies MCP Setup - Context for Future Claude Sessions

## Session Summary: 2025-10-25

### What Was Done

**Problem:** Fireflies MCP was failing to connect in Claude Code

**Root Cause:** Incorrect npm package name in `.mcp.json`
- ❌ Was: `@props-labs/fireflies-mcp` (doesn't exist)
- ✅ Now: `fireflies-mcp-server` (correct package)

**Solution Applied:**
1. Debugged MCP configuration
2. Found API key already configured in `~/.zshrc`
3. Corrected package name in `.mcp.json`
4. Created comprehensive documentation
5. Built webhook automation template

### Changes Made

**Files Modified:**
- `.mcp.json` - Fixed fireflies package name

**Files Created:**
- `docs/fireflies-mcp-setup.md` - Complete setup guide
- `FIREFLIES-QUICK-START.md` - Quick reference
- `FIREFLIES-CONTEXT.md` - This file (session context)
- `scripts/process-fireflies-webhook.js` - Webhook automation template
- `scripts/package.json` - Dependencies for webhook script

**Files Updated:**
- `daily/TODAY.md` - Added restart reminder and next steps

---

## For Future Claude Sessions

### When User Says: "Get Fireflies meeting summary"

**Expected Behavior:**
If MCP is working, you should have access to `mcp__fireflies__*` tools.

**If Tools Not Available:**
1. Check `.mcp.json` has `fireflies-mcp-server` (not `@props-labs/fireflies-mcp`)
2. Verify API key: `echo $FIREFLIES_API_KEY` should output key
3. Confirm Claude Code was restarted after config changes
4. Check `claude mcp list` shows fireflies as connected

**Reference Files:**
- Quick troubleshooting: `FIREFLIES-QUICK-START.md`
- Detailed setup: `docs/fireflies-mcp-setup.md`

### When User Says: "Set up Fireflies webhook"

**Current Status:** Template created but not deployed

**Next Steps:**
1. Get webhook URL from user's Fireflies.ai account
2. Choose deployment method (ngrok/Vercel/Lambda)
3. Complete TODO sections in `scripts/process-fireflies-webhook.js`:
   - Fireflies GraphQL API integration
   - Action item parsing
   - GitHub issue creation
   - Daily notes updates
4. Install dependencies: `cd scripts && npm install`
5. Test: `npm test`
6. Deploy endpoint

**Key Features to Implement:**
- Automatic meeting processing on webhook receive
- Extract action items → create GitHub issues
- Map meetings to projects (config in script)
- Update daily notes
- Save meeting summaries to `meetings/` dir
- Track delegated tasks

### Configuration Details

**MCP Configuration:**
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

**Environment Variable:**
- `FIREFLIES_API_KEY=361247e5-1ad5-4072-b1c8-32f64f20ad39`
- Location: `~/.zshrc`

**Enabled MCP Servers:**
- google-calendar ✓
- github ✓
- telegram ✗ (not connected)
- reclaim ✗ (not connected)
- fireflies ✓ (should work after restart)
- postgres ✗ (not connected)
- filesystem ✓

---

## User's Goals

### Immediate
- [x] Fix Fireflies MCP connection
- [ ] Restart Claude Code
- [ ] Test: "Get my last meeting summary"

### Short-term
- [ ] Get webhook URL from Fireflies.ai
- [ ] Set up webhook endpoint
- [ ] Test webhook automation

### Long-term Vision
Fully automated meeting workflow:
1. Meeting happens (Fireflies records)
2. Webhook fires when transcript ready
3. Script processes meeting:
   - Extracts action items
   - Creates GitHub issues in relevant projects
   - Updates daily notes
   - Tracks delegated tasks
   - Saves formatted meeting notes
4. User reviews and refines (not starts from scratch)

---

## Important Notes for Future Sessions

1. **API Key Security:** The API key is visible in this documentation. If this repo becomes public, rotate the key and use environment variables only.

2. **Package Name:** The correct package is `fireflies-mcp-server`, NOT `@props-labs/fireflies-mcp`

3. **Restart Required:** Any changes to `.mcp.json` require Claude Code restart

4. **Project Mapping:** The webhook script has a project mapping config - update with user's actual GitHub repos

5. **Dependencies:** Webhook script needs `npm install` before running

---

## Testing Checklist

After Claude Code restart:
- [ ] `claude mcp list` shows fireflies connected
- [ ] Can retrieve meeting summaries via MCP
- [ ] Webhook script can run: `node scripts/process-fireflies-webhook.js`
- [ ] Can test webhook locally: `npm test` in scripts directory

---

## Links & Resources

- Fireflies API Docs: https://docs.fireflies.ai/
- Package on npm: https://npm.im/fireflies-mcp-server
- Alternative package: https://npm.im/@gongrzhe/server-fireflies-mcp

---

**Created:** 2025-10-25
**Status:** Configuration complete, awaiting restart and testing
**Next Session:** Test MCP connection, then implement webhook
