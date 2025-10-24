# Reclaim.ai Integration Setup

**Date:** 2025-10-23
**Status:** API Key Created, Integration Pending

---

## API Key Details

**Created:** 2025-10-23
**Purpose:** Integrate Reclaim.ai with Claude Code productivity system

**Storage:** Store API key securely in environment or config file

---

## Integration Resources

### Official Documentation
- **Status:** Not yet released (coming soon)
- **Notification:** Added to waitlist for REST API docs release

### Example Projects (Unofficial)
1. **Unofficial Python SDK by labiso-gmbh**
   - Repository: https://github.com/labiso-gmbh/reclaim-sdk
   - Use case: Python integration examples
   - Language: Python
   - Features: Task management, calendar sync, scheduling

2. **Raycast Integration (Official Community Extension)**
   - Repository: https://github.com/raycast/extensions/tree/7aa65f290a37d8a8dca40f612da9a6cc5ef47754/extensions/reclaim-ai/
   - Use case: Desktop app integration examples
   - Language: TypeScript/JavaScript
   - Features: Full Reclaim.ai integration in Raycast

3. **XHR Requests**
   - Method: Inspect Reclaim web app network requests
   - Tool: Browser DevTools → Network tab
   - Purpose: Understand API endpoints and request formats

---

## Where to Store API Key

### Option 1: Environment Variable (Recommended)
```bash
# Add to ~/.zshrc or ~/.bash_profile
export RECLAIM_API_KEY="your-api-key-here"

# Reload shell
source ~/.zshrc
```

### Option 2: Config File in Productivity System
```bash
# Create config file
mkdir -p ~/.config/productivity-system
echo "RECLAIM_API_KEY=your-api-key-here" > ~/.config/productivity-system/.env

# Add to .gitignore
echo ".env" >> ~/git/simon/.gitignore
```

### Option 3: 1Password (Backup/Reference)
- Store in 1Password for backup
- Title: "Reclaim.ai API Key"
- Category: API Credentials
- Note: Used for Claude Code productivity integration

---

## Planned Integration Features

### Phase 1: Calendar Sync
- [ ] Fetch daily calendar events
- [ ] Sync to daily notes automatically
- [ ] Display upcoming meetings in Claude Code

### Phase 2: Task Time Blocking
- [ ] Create Reclaim tasks from GitHub issues
- [ ] Auto-block time for MITs
- [ ] Sync task completion status

### Phase 3: Scheduling Links
- [ ] Store Reclaim scheduling links in notes
- [ ] Quick access to meeting scheduler
- [ ] Auto-include in relevant documents

### Phase 4: Analytics
- [ ] Track time spent on projects
- [ ] Meeting load analysis
- [ ] Focus time optimization suggestions

---

## Next Steps

1. **Immediate:**
   - [ ] Decide where to store API key
   - [ ] Add API key to chosen storage method
   - [ ] Test basic API connectivity

2. **Short-term:**
   - [ ] Review unofficial Python SDK examples
   - [ ] Study Raycast integration code
   - [ ] Map out key API endpoints needed

3. **Medium-term:**
   - [ ] Build basic Reclaim.ai MCP server
   - [ ] Integrate with Claude Code
   - [ ] Test calendar sync functionality

4. **Long-term:**
   - [ ] Wait for official API documentation release
   - [ ] Migrate to official SDK when available
   - [ ] Expand integration features

---

## API Endpoints to Explore

### Calendar
- Get today's events
- Get week's events
- Get specific date events

### Tasks
- Create task
- Update task
- Mark task complete
- Get task list

### Scheduling
- Get scheduling links
- Create new scheduling link
- Update availability

### Habits & Routines
- Get habits list
- Update habit completion
- Get smart 1:1 meetings

---

## Reference

**Your Reclaim.ai Profile:**
- Website: https://reclaim.ai
- Scheduling Link: https://app.reclaim.ai/m/simonfavourse

**Web App for XHR Inspection:**
- URL: https://app.reclaim.ai
- Method: Open DevTools → Network → Filter: XHR
- Look for: API calls to learn endpoints

---

## Questions for Reclaim.ai Team

- [ ] When will REST API documentation be officially released?
- [ ] What are rate limits for API calls?
- [ ] Are webhooks available for real-time updates?
- [ ] Best practices for authentication and security?

---

**Last Updated:** 2025-10-23
