# Reclaim.ai Habits Integration

**Date:** 2025-10-23
**Status:** Habits configured in Reclaim.ai, ready for integration

---

## Current Habits in Reclaim.ai

### Active Habits (Enabled)

1. **🍽️ Lunch**
   - **Schedule:** Every Monday - Sunday
   - **Duration:** 25 mins - 50 mins
   - **Ideal Time:** 13:00 (1:00 PM)
   - **Next:** Fri, 24 Oct at 12:00
   - **Purpose:** Protected lunch break

2. **☕ Morning Catch Up**
   - **Schedule:** Every Monday - Friday
   - **Duration:** 15 mins - 30 mins
   - **Ideal Time:** 9:00 AM
   - **Next:** Fri, 24 Oct at 9:00
   - **Purpose:** Morning planning and catch-up time

3. **☕ Afternoon Catch Up**
   - **Schedule:** Every Monday - Friday
   - **Duration:** 25 mins
   - **Ideal Time:** 16:30 (4:30 PM)
   - **Next:** Fri, 24 Oct at 16:15
   - **Purpose:** Afternoon break and processing

4. **📝 Review Today, Plan Tomorrow**
   - **Schedule:** Every Monday - Saturday
   - **Duration:** 5 mins - 15 mins
   - **Ideal Time:** 17:00 (5:00 PM)
   - **Next:** Fri, 24 Oct at 16:45
   - **Purpose:** Daily review and tomorrow planning (MIT selection)

5. **🧠 Process Notes & Ideas**
   - **Schedule:** Every day
   - **Duration:** 15 mins - 30 mins
   - **Ideal Time:** 17:30 (5:30 PM)
   - **Next:** Fri, 24 Oct at 17:15
   - **Purpose:** Inbox processing, note organization

6. **🏊 Swim/Pool**
   - **Schedule:** Every Tuesday, Thursday, Sunday
   - **Duration:** 15 mins - 30 mins
   - **Ideal Time:** 18:00 (6:00 PM)
   - **Next:** Fri, 24 Oct at 18:00
   - **Purpose:** Exercise and health

7. **🌙 Evening Ritual**
   - **Schedule:** Every Monday - Sunday
   - **Duration:** 30 mins - 1 hr
   - **Ideal Time:** 22:00 (10:00 PM)
   - **Next:** Thu, 23 Oct at 21:30
   - **Purpose:** Wind down, prepare for sleep

### Disabled Habits

8. **🗣️ Communication**
   - **Schedule:** Every Thursday
   - **Duration:** 30 mins
   - **Ideal Time:** 9:00 AM
   - **Status:** Currently disabled
   - **Purpose:** Team communication time

9. **🏃 Run, Pool, Relax**
   - **Schedule:** Every Monday - Sunday
   - **Duration:** 1 hr - 2 hrs
   - **Ideal Time:** 18:00 (6:00 PM)
   - **Status:** Currently disabled
   - **Note:** Replaced by Swim/Pool habit

10. **👥 Team Meeting**
    - **Schedule:** Every Monday - Saturday
    - **Duration:** 15 mins - 30 mins
    - **Ideal Time:** 12:00 PM
    - **Status:** Currently disabled
    - **Note:** Handled by actual calendar events now

11. **☕ Morning Catch Up** (duplicate)
    - **Status:** Disabled (duplicate of active habit)

---

## Integration with Productivity System

### Phase 1: Habit Sync to Daily Notes
**Priority:** HIGH

Automatically sync habit completions to daily notes:

```markdown
## Habits Completed Today
- ✅ Morning Catch Up (9:15 AM - 9:30 AM)
- ✅ Lunch (12:30 PM - 1:00 PM)
- ✅ Review Today, Plan Tomorrow (5:00 PM - 5:15 PM)
- ⏸️ Swim/Pool (Skipped)
```

### Phase 2: Habit Reminders
**Priority:** MEDIUM

- Create Claude Code reminders before each habit
- Suggest tasks to do during each habit block
- Track habit completion streaks

### Phase 3: Habit Analytics
**Priority:** LOW

- Track which habits are consistently completed
- Identify habit conflicts with meetings
- Suggest habit timing optimizations

---

## Recommended Habit Optimizations

### 1. Morning Catch Up (9:00 AM)
**Current:** 15-30 mins
**Suggestion:** Use this time for:
- Quick email check
- Review GitHub notifications
- Check team progress on projects
- Respond to urgent messages

**Integration:** Auto-fetch overnight updates and present summary

### 2. Review Today, Plan Tomorrow (5:00 PM)
**Current:** 5-15 mins
**Suggestion:** Automate this with Claude Code!
- Review completed tasks
- Archive completed GitHub issues
- Select tomorrow's MIT
- Create tomorrow's daily note
- Update WIP.md file

**Integration:** Run automated daily review script

### 3. Process Notes & Ideas (5:30 PM)
**Current:** 15-30 mins
**Suggestion:** Use for:
- Inbox zero processing
- Move notes from inbox to proper locations
- Update project documentation
- Process meeting notes

**Integration:** Auto-organize inbox files

### 4. Evening Ritual (10:00 PM)
**Current:** 30 mins - 1 hr
**Suggestion:** Wind down routine:
- Close all work apps
- Review tomorrow's calendar
- Light stretching
- Walking meditation
- Prepare for bed

**Integration:** Auto-close work applications, show tomorrow's schedule

---

## Habit-Based Task Suggestions

### Morning Catch Up (9:00 AM)
```bash
# Quick morning script
- Check email inbox
- Review GitHub notifications
- Check Slack/WhatsApp for urgent messages
- Review today's calendar
- Confirm MIT is still valid
```

### Review Today, Plan Tomorrow (5:00 PM)
```bash
# Automated daily review
- What did I accomplish today?
- MIT completed? (Yes/No)
- Blockers encountered?
- Team progress checked?
- Tomorrow's MIT selected?
- Tomorrow's top 3 tasks listed?
```

### Process Notes & Ideas (5:30 PM)
```bash
# Inbox processing checklist
- Desktop cleanup
- Downloads folder review
- Email inbox to zero
- WhatsApp/Telegram processing
- Meeting notes filed
- Ideas captured in system
```

---

## API Integration Plan

### Habit Endpoints (to discover)
- `GET /habits` - List all habits
- `GET /habits/:id` - Get specific habit details
- `GET /habits/:id/events` - Get habit time blocks
- `POST /habits/:id/complete` - Mark habit complete
- `PUT /habits/:id` - Update habit settings

### Data to Sync
1. **Habit Schedule:** When each habit is scheduled
2. **Habit Completion:** Which habits were completed
3. **Habit Duration:** Actual time spent on each habit
4. **Habit Streaks:** Consecutive days completed

### Integration Points
1. **Daily Note Generation:** Include habit schedule
2. **Habit Reminders:** 5 mins before each habit
3. **Completion Tracking:** Auto-mark in daily notes
4. **Streak Tracking:** Motivational dashboard

---

## Reclaim.ai Habits Documentation

**Learn More:**
- Reclaim.ai Habits Overview: https://reclaim.ai/features/habits
- How Habits Work: https://help.reclaim.ai/en/articles/habits
- Habit Best Practices: https://reclaim.ai/blog/how-to-build-better-habits

**Key Features:**
- ✅ Smart scheduling around meetings
- ✅ Flexible time windows (min-max duration)
- ✅ Ideal time preferences
- ✅ Automatic rescheduling when conflicts arise
- ✅ Habit streaks and completion tracking
- ✅ Integration with calendar

---

## Next Steps

### Immediate (This Week)
- [ ] Test Reclaim.ai API with habit endpoints
- [ ] Fetch today's habit schedule
- [ ] Display habit schedule in daily notes

### Short-term (Next 2 Weeks)
- [ ] Build habit reminder system
- [ ] Auto-sync habit completions to notes
- [ ] Create habit-specific task suggestions

### Medium-term (Next Month)
- [ ] Build habit analytics dashboard
- [ ] Streak tracking and motivation system
- [ ] Habit optimization suggestions based on data

### Long-term (Future)
- [ ] AI-powered habit coaching
- [ ] Automatic habit timing optimization
- [ ] Habit interference detection with deep work

---

**Last Updated:** 2025-10-23
**Next Review:** After Reclaim.ai API integration complete
