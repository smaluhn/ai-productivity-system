# Claude Code Auto-Approval Guide

**Last Updated:** 2025-10-24
**Repository:** /Users/simon/git/simon

---

## Overview

This guide documents safe commands that can be auto-approved for Claude Code to run without user confirmation. These commands are carefully selected to be safe, non-destructive, and useful for productivity.

---

## Safety Principles

1. **Read-only operations are safe** - Viewing, listing, checking status
2. **Version controlled changes are safe** - Git operations (can always revert)
3. **Standard package managers are safe** - npm, pip, brew (with specific commands)
4. **Service management for user-owned services** - launchctl for personal services
5. **NEVER auto-approve destructive operations** - rm -rf, force push to main, database drops

---

## Categories of Auto-Approved Commands

### 1. Git Operations (Safe - Version Controlled)

All git operations are safe because they're version controlled and reversible:

```
Bash(git status:*)
Bash(git log:*)
Bash(git diff:*)
Bash(git branch:*)
Bash(git checkout:*)
Bash(git add:*)
Bash(git commit:*)
Bash(git push:*)
Bash(git pull:*)
Bash(git fetch:*)
Bash(git remote:*)
Bash(git remote add:*)
Bash(git config:*)
Bash(git check-ignore:*)
Bash(git init:*)
Bash(git stash:*)
Bash(git merge:*)
Bash(git rebase:*)
Bash(git tag:*)
```

**Why safe:** Git operations are reversible. Even force pushes can be recovered via reflog.

**Exceptions to avoid:**
- `git push --force` to main/master on shared repos (should ask first)
- `git clean -fd` (deletes untracked files permanently)

---

### 2. GitHub CLI (Safe - Read & Project Management)

```
Bash(gh auth:*)
Bash(gh repo list:*)
Bash(gh repo view:*)
Bash(gh repo create:*)
Bash(gh issue list:*)
Bash(gh issue create:*)
Bash(gh issue edit:*)
Bash(gh issue close:*)
Bash(gh pr list:*)
Bash(gh pr create:*)
Bash(gh pr view:*)
Bash(gh pr merge:*)
Bash(gh project list:*)
Bash(gh project create:*)
Bash(gh project item-add:*)
Bash(gh project item-create:*)
Bash(gh api:*)
```

**Why safe:** GitHub operations are tracked and reversible. Issues/PRs can be reopened.

---

### 3. File System Operations (Safe - Read Only)

```
Bash(ls:*)
Bash(cat:*)
Bash(head:*)
Bash(tail:*)
Bash(find:*)
Bash(grep:*)
Bash(tree:*)
Bash(pwd:*)
Bash(which:*)
Bash(file:*)
Bash(stat:*)
Bash(du:*)
Bash(df:*)
```

**Why safe:** These only read files, never modify.

**Write operations (also safe with git tracking):**
```
Bash(mkdir:*)
Bash(touch:*)
Bash(chmod:*)
Bash(chown:*)
```

**Why safe:** Changes are tracked by git and can be reverted.

---

### 4. Package Managers (Safe - Specific Commands)

```
Bash(npm install:*)
Bash(npm update:*)
Bash(npm run:*)
Bash(npm test:*)
Bash(npm run build:*)
Bash(pip3 install:*)
Bash(pip3 list:*)
Bash(brew install:*)
Bash(brew update:*)
Bash(brew upgrade:*)
Bash(brew list:*)
```

**Why safe:**
- Package installations are reversible
- Build/test operations don't modify source
- Can always reinstall dependencies

---

### 5. Python & Development Tools

```
Bash(python3:*)
Bash(python:*)
Bash(node:*)
Bash(npm:*)
Bash(pytest:*)
Bash(poetry:*)
Bash(pipenv:*)
```

**Why safe:** Running scripts in development environment. If destructive, would be caught in testing.

---

### 6. macOS Service Management (User Services Only)

```
Bash(launchctl load:*)
Bash(launchctl unload:*)
Bash(launchctl start:*)
Bash(launchctl stop:*)
Bash(launchctl list:*)
Bash(launchctl list | grep:*)
```

**Why safe:** Only affects user-level services (~/Library/LaunchAgents), not system services.

**Safety note:** Requires services are in ~/Library/LaunchAgents, not /Library/LaunchDaemons.

---

### 7. Project-Specific Scripts

```
Bash(/Users/simon/git/simon/.auto-sync.sh)
```

**Why safe:** Custom scripts we control and trust.

**Guidelines for adding scripts:**
1. Script must be in version control
2. Script must be reviewed and understood
3. Script should be idempotent (safe to run multiple times)
4. Script should not delete files permanently

---

### 8. Claude Code Operations

```
Bash(claude --version:*)
Bash(claude update:*)
Bash(claude migrate-installer:*)
Bash(claude mcp list:*)
Bash(claude mcp install:*)
```

**Why safe:** Managing Claude Code itself.

---

### 9. MCP Server Operations

```
mcp__google-calendar__list-events
mcp__google-calendar__list-calendars
mcp__google-calendar__get-event
mcp__google-calendar__create-event
mcp__google-calendar__update-event
mcp__google-calendar__delete-event
mcp__google-calendar__get-freebusy
mcp__google-calendar__search-events
mcp__google-calendar__get-current-time
mcp__google-calendar__list-colors
```

**Why safe:** Calendar operations are non-destructive and reversible.

---

### 10. Shell Utilities

```
Bash(echo:*)
Bash(printf:*)
Bash(test:*)
Bash(date:*)
Bash(sleep:*)
Bash(whoami:*)
Bash(hostname:*)
Bash(source ~/.zshrc)
Bash(source ~/.bashrc)
```

**Why safe:** Standard shell utilities that are read-only or benign.

---

### 11. Loop Constructs (Safe Patterns)

```
Bash(for org in favourse DiverseProjects Favorsid FUNDEdotFI Printora FavosApp)
Bash(do echo "=== $org ===")
Bash(done)
Bash(for file in *)
Bash(while read line)
```

**Why safe:** These are control flow patterns, harmless by themselves.

---

## Commands to NEVER Auto-Approve

### Destructive File Operations
```
❌ rm -rf
❌ rm *
❌ dd
❌ mkfs
❌ fdisk
```

### Dangerous Git Operations
```
❌ git reset --hard (can lose uncommitted work)
❌ git clean -fd (permanently deletes untracked files)
❌ git push --force origin main (on shared repos)
```

### System-Level Changes
```
❌ sudo anything
❌ System service modifications (/Library/LaunchDaemons)
❌ System file modifications (/etc, /usr, /bin)
```

### Database Operations
```
❌ DROP DATABASE
❌ DELETE FROM without WHERE
❌ TRUNCATE TABLE
```

---

## Project-Specific Auto-Approvals

### Productivity System (`/Users/simon/git/simon`)

**Safe operations:**
- All git operations (everything is version controlled)
- Running `.auto-sync.sh` (safe, idempotent sync script)
- Creating/updating markdown files (tracked by git)
- Installing npm/python dependencies
- Running tests and builds

**Repository remote:** `https://github.com/smaluhn/productivity-system.git`

---

### AkunIndo Project

**Safe operations:**
- GitHub issue creation/updates via `gh` CLI
- GitHub project management
- Documentation updates
- Test runs

---

## How to Add New Auto-Approvals

1. **Evaluate Safety:**
   - Is it read-only?
   - Is it reversible (version controlled)?
   - Does it modify only user-owned resources?
   - Is it idempotent (safe to run multiple times)?

2. **Add to settings.local.json:**
   ```json
   {
     "permissions": {
       "allow": [
         "Bash(new-safe-command:*)"
       ]
     }
   }
   ```

3. **Document here:**
   - Add to appropriate category
   - Explain why it's safe
   - Note any caveats

4. **Test:**
   - Verify command works as expected
   - Confirm it doesn't require additional approval

---

## Current Auto-Approval List

See `/Users/simon/git/simon/.claude/settings.local.json` for the complete, active list.

---

## Recommendations for Additional Safe Commands

### Consider Adding:

```json
"Bash(git status:*)",
"Bash(git log:*)",
"Bash(git diff:*)",
"Bash(git branch:*)",
"Bash(git fetch:*)",
"Bash(git stash:*)",
"Bash(npm test:*)",
"Bash(npm run build:*)",
"Bash(npm run dev:*)",
"Bash(pytest:*)",
"Bash(launchctl unload:*)",
"Bash(launchctl start:*)",
"Bash(launchctl stop:*)",
"Bash(date:*)",
"Bash(whoami:*)",
"Bash(hostname:*)",
"Bash(gh pr list:*)",
"Bash(gh pr view:*)",
"Bash(gh issue close:*)",
"WebFetch(domain:*.github.com)",
"mcp__google-calendar__*"
```

### Wildcards for MCP Servers:

Consider using wildcards for trusted MCP servers:
```json
"mcp__google-calendar__*"
```

This approves all Google Calendar operations since they're all safe and reversible.

---

## Review Schedule

**Quarterly Review:** Review this list every 3 months to:
1. Remove unused permissions
2. Add commonly-requested safe commands
3. Update based on new projects
4. Verify safety assumptions still hold

**Next Review:** 2025-01-24

---

## Emergency: Disable All Auto-Approvals

If you need to temporarily disable all auto-approvals:

```bash
# Backup current settings
cp ~/.claude/settings.local.json ~/.claude/settings.local.json.backup

# Clear auto-approvals
echo '{"permissions": {"allow": [], "deny": [], "ask": []}}' > ~/.claude/settings.local.json

# Restore later
cp ~/.claude/settings.local.json.backup ~/.claude/settings.local.json
```

---

**Remember:** When in doubt, ask for approval. Safety first!
