# 🔥 Fireflies MCP - Quick Start Guide

## ✅ What's Been Done

1. **Fixed MCP Configuration** (`/Users/simon/git/simon/.mcp.json`)
   - Corrected package name: `fireflies-mcp-server`
   - Previous incorrect name: `@props-labs/fireflies-mcp` ❌

2. **API Key Configured**
   - Location: `~/.zshrc`
   - Value: `361247e5-1ad5-4072-b1c8-32f64f20ad39`
   - Already loaded in environment ✓

3. **Documentation Created**
   - Full setup guide: `docs/fireflies-mcp-setup.md`
   - This quick start: `FIREFLIES-QUICK-START.md`

4. **Automation Script Created**
   - Webhook processor: `scripts/process-fireflies-webhook.js`
   - Package config: `scripts/package.json`
   - Status: Template ready, needs implementation

---

## 🚀 Next Steps After Restart

### 1. Test Fireflies MCP (FIRST THING!)
After restarting Claude Code, immediately test:
```
"Get my last Fireflies meeting summary"
```

### 2. Verify MCP Connection
```bash
claude mcp list
```
Should show: `fireflies: ✓ Connected`

### 3. Set Up Webhook (When Ready)
- Get webhook URL from Fireflies.ai dashboard
- Deploy endpoint (options in `docs/fireflies-mcp-setup.md`)
- Configure automation script

---

## 📋 Available Commands (After Restart)

Once MCP is active, you can ask Claude:
- "Get my last Fireflies meeting"
- "Show recent Fireflies meetings"
- "Get transcript from [meeting name]"
- "Summarize today's Fireflies meetings"

---

## 🔧 Troubleshooting

**If MCP still fails:**
1. Check package: `npm info fireflies-mcp-server`
2. Test manually: `npx -y fireflies-mcp-server`
3. Verify API key: `echo $FIREFLIES_API_KEY`
4. Check logs in `~/.claude/debug/`

**If webhook needed:**
- See full guide: `docs/fireflies-mcp-setup.md` (section: Webhook Integration)
- Script location: `scripts/process-fireflies-webhook.js`

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `.mcp.json` | MCP server configuration |
| `~/.zshrc` | API key environment variable |
| `docs/fireflies-mcp-setup.md` | Complete setup documentation |
| `scripts/process-fireflies-webhook.js` | Webhook automation (template) |
| `daily/TODAY.md` | Updated with next steps |

---

## 🎯 Webhook Automation Goals

When implemented, the webhook will:
1. ✅ Automatically receive new meeting notifications
2. ✅ Extract action items and decisions
3. ✅ Create GitHub issues in relevant projects
4. ✅ Update daily notes with meeting references
5. ✅ Track delegated tasks
6. ✅ Save meeting notes to `meetings/` directory

Implementation status: **Template created, needs API integration**

---

## 💡 Remember

- **MUST RESTART CLAUDE CODE** for MCP changes to take effect
- MCP config is project-scoped (lives in this repo)
- API key is user-scoped (lives in `~/.zshrc`)
- Webhook is optional - MCP works without it

---

**Last Updated:** 2025-10-25
**Status:** Ready for testing after Claude Code restart

---

## Quick Test After Restart

1. Restart Claude Code
2. Open this file again
3. Ask: "Get my last Fireflies meeting summary"
4. If it works ✅ → Proceed to webhook setup
5. If it fails ❌ → Check troubleshooting section above
