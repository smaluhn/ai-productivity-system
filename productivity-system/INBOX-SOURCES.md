# Inbox Sources & Processing

**Last Updated**: 2025-10-22

## Calendar Configuration

### Google Calendar Filters
**Show Only**:
- ✅ simon@favourse.com (Main calendar)
- ✅ simon@smaluhn.com (Personal calendar)

**Hide**:
- ❌ seminardesk
- ❌ Other calendars (specify as needed)

**Important**:
- **Include full-day tasks/events** (especially those marked as "Free" availability)
- These are often used as reminders and should appear in daily view
- Full-day "Free" tasks should be processed as inbox items

## Inbox Sources to Process

### 1. Digital Inboxes
- [ ] **Email Accounts** (Multiple - need to connect all)
  - Review: At least once a week
  - Action: Unsubscribe from unnecessary services
  - Process: Inbox zero weekly

- [ ] **Google Calendar Full-Day Tasks**
  - Marked as "Free" availability
  - Used as reminders
  - Should be processed and converted to actionable tasks

- [ ] **Phone Alarms**
  - Currently used as reminder inbox (acknowledged as bad habit)
  - Should be reviewed and converted to proper task system

### 2. File System Inboxes
- [ ] **Desktop Text Files**
  - Review regularly
  - Archive or process into proper notes

- [ ] **Desktop Other Files**
  - Keep desktop clean
  - Move to appropriate folders or delete

- [ ] **Downloads Folder**
  - Process weekly
  - Archive important files, delete temporary downloads
  - Target: Zero or near-zero files in Downloads

### 3. Digital Communication
- [ ] **WhatsApp/Telegram** (Future integration - HIGH PRIORITY)
  - **Integration Options**:
    - Option A: n8n workflow automation
    - Option B: ChatGPT Agent Kit
    - Option C: Claude API direct integration
    - Option D: Make.com (Integromat)
  - **Functionality Needed**:
    - Forward important messages to inbox system
    - Auto-extract action items from messages
    - Create tasks in GitHub Projects from messages
    - Daily digest of unread messages
  - **Priority**: High (reduces manual WhatsApp checking)
  - **Timeline**: Research and implement Q4 2025

- [ ] **Fireflies.ai Meeting Transcriptions**
  - Already integrated (Python script available)
  - Import action items from meetings

## Processing Frequency

| Source | Frequency | Target |
|--------|-----------|--------|
| Email accounts | Weekly (minimum) | Inbox zero |
| Calendar full-day tasks | Daily | Process as tasks |
| Phone alarms | Weekly review | Convert to tasks |
| Desktop files | Weekly | Clean/organize |
| Downloads folder | Weekly | Archive/delete |
| WhatsApp/Telegram | Daily (once integrated) | Process messages |
| Meeting transcriptions | After each meeting | Extract action items |

## Zero Inbox Goal

**Philosophy**: Keep all inbox sources at zero or near-zero regularly

**Benefits**:
- Reduces mental clutter
- Nothing falls through cracks
- Clear mind for focused work
- Easy to identify what needs attention

**Weekly Review Checklist**:
- [ ] Process all email accounts → Inbox zero
- [ ] Review phone alarms → Convert to tasks
- [ ] Clean desktop files → Organize or delete
- [ ] Empty downloads folder → Archive important files
- [ ] Review calendar full-day tasks → Process as needed
- [ ] Check WhatsApp/Telegram → Process important messages

## Email Management

### Accounts to Connect
*(List your email accounts here)*
- simon@favourse.com
- simon@smaluhn.com
- *(Add others)*

### Email Processing Workflow
1. **Quick Scan**: Identify important vs. spam
2. **Unsubscribe**: Aggressively unsubscribe from newsletters/promotions
3. **Archive**: Move processed emails to archive (don't delete)
4. **Action Items**: Extract tasks into TODO system
5. **Inbox Zero**: Goal is empty inbox weekly

### Unsubscribe Strategy
- Use unsubscribe links in emails
- Consider services like Unroll.me or Leave Me Alone
- Mark as spam if unsubscribe doesn't work
- Block sender if persistent

## Automation Ideas

### Current
- ✅ Fireflies.ai → Python import script
- ✅ Google Calendar → MCP integration (needs configuration)

### Future
- [ ] Email → Task extraction (AI-powered)
- [ ] WhatsApp/Telegram → Inbox integration (n8n or Claude API)
- [ ] Desktop file monitoring → Auto-organize script
- [ ] Downloads folder → Auto-archive old files
- [ ] Phone alarms → Sync to task system (if possible)

## Notes

- Full-day calendar tasks marked as "Free" are intentionally used as reminders
- These should be visible in daily view and processed like inbox items
- Phone alarms as inbox is a "bad habit" to phase out gradually
- Email checking is rare - need weekly discipline to review
- Multiple email accounts need consolidation or at least regular review
- Unsubscribe from services to reduce inbox noise

---

**Related Documents**:
- [WORKFLOW.md](WORKFLOW.md) - Daily/weekly workflows
- [CALENDAR-CONFIG.md](CALENDAR-CONFIG.md) - Google Calendar setup details
- [EMAIL-CONFIG.md](EMAIL-CONFIG.md) - Email account configurations
