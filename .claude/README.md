# Claude Code Configuration

This directory contains Claude Code configuration for the productivity-system repository.

## Files

- **settings.local.json** - Auto-approval permissions and MCP server configuration
- **AUTO_APPROVAL_GUIDE.md** - Comprehensive guide on safe command auto-approvals

## Auto-Sync

This repository has automatic git sync enabled:

- **Frequency:** Every 15 minutes
- **Script:** `/.auto-sync.sh`
- **Service:** `com.smaluhn.git-autosync` (launchd)
- **Log:** `/.auto-sync.log`

The auto-sync will automatically:
1. Pull latest changes from remote
2. Commit any local changes with timestamp
3. Push to remote

## Auto-Approved Commands

We've configured extensive auto-approvals for safe, reversible operations:

### Categories
- Git operations (all safe - version controlled)
- GitHub CLI operations (issues, PRs, projects)
- File system read operations
- Package managers (npm, pip, brew)
- Development tools (python, node, pytest)
- macOS service management (launchctl for user services)
- Google Calendar MCP (all operations)

See **AUTO_APPROVAL_GUIDE.md** for complete details.

## MCP Servers

Currently enabled:
- **google-calendar** - Full calendar management

Wildcard approval enabled for all google-calendar operations via `mcp__google-calendar__*`.

## Safety

Commands that are **NEVER** auto-approved:
- Destructive file operations (rm -rf, etc.)
- Dangerous git operations (git clean -fd, force push to main)
- System-level changes (sudo, system services)
- Database drops or truncates

## Quick Reference

```bash
# View auto-sync status
launchctl list | grep smaluhn

# View sync log
tail -f /.auto-sync.log

# Stop auto-sync temporarily
launchctl unload ~/Library/LaunchAgents/com.smaluhn.git-autosync.plist

# Restart auto-sync
launchctl load ~/Library/LaunchAgents/com.smaluhn.git-autosync.plist
```

## Adding New Auto-Approvals

1. Evaluate if command is safe (see AUTO_APPROVAL_GUIDE.md)
2. Add to `settings.local.json` permissions.allow array
3. Document in AUTO_APPROVAL_GUIDE.md
4. Commit changes

---

**Last Updated:** 2025-10-24
