# Fireflies Meeting Processing Workflow

## Overview
This document describes the standardized workflow for processing Fireflies meeting transcripts and converting them into actionable tasks.

## File Naming Convention

### Meeting Notes
- **Format:** `YYYY-MM-DD-HHam/pm-meeting-title-fireflies.md`
- **Example:** `2025-10-25-11am-bali-team-meeting-fireflies.md`
- **Location:** `{project-name}-spec-docs/meetings/transcripts/`

### Meeting Agendas
- **Format:** `YYYY-MM-DD-HHam/pm-meeting-title-agenda.md`
- **Example:** `2025-10-25-11am-bali-team-meeting-agenda.md`
- **Location:** `{project-name}-spec-docs/meetings/agendas/`

## Step-by-Step Process

### 1. Retrieve Meeting from Fireflies
```bash
# Get list of recent transcripts
mcp__fireflies__fireflies_get_transcripts --limit 10

# Get specific meeting summary
mcp__fireflies__fireflies_generate_summary --transcript_id {id} --format bullet_points
```

### 2. Store Full Transcript
- Save complete transcript in project's `meetings/transcripts/` folder
- Use standardized naming convention
- Include metadata at top:
  - Meeting Title
  - Date & Time
  - Duration
  - Participants
  - Fireflies URL

### 3. Extract Action Items
From the summary, identify:
- **Who:** Assignee (must be specific person)
- **What:** Task description (brief, high-level)
- **When:** Deadline or milestone
- **Context:** Link to meeting transcript (for reference)

### 4. Create GitHub Issues
For each action item:
- Create issue in appropriate repo
- Add labels: `type:task`, `type:feature`, or `type:bug`
- Add to project board
- Link to meeting notes in issue description
- Assign to team member
- Add to milestone if applicable

### 5. Update Project Documentation
After processing meeting:
- Update `CHANGELOG.md` with decisions made
- Update `ROADMAP.md` if strategic changes discussed
- Update next meeting agenda with follow-ups
- Add review items for Simon/Thuy if needed

### 6. Commit Changes
```bash
git add .
git commit -m "Meeting notes: [Meeting Title] - YYYY-MM-DD

- Processed Fireflies transcript
- Created [X] GitHub issues: #issue1, #issue2, #issue3
- Updated CHANGELOG.md and ROADMAP.md
- Added items to next meeting agenda

Related issues: #issue1, #issue2, #issue3"
```

## Folder Structure in spec-docs Repo

```
{project-name}-spec-docs/
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── meetings/
│   ├── transcripts/
│   │   └── 2025-10-25-11am-bali-team-meeting-fireflies.md
│   ├── agendas/
│   │   ├── 2025-10-25-11am-bali-team-meeting-agenda.md
│   │   └── NEXT-MEETING-AGENDA.md
│   └── summaries/
│       └── 2025-10-weekly-summary.md
├── specifications/
│   ├── technical-spec.md
│   ├── feature-specs/
│   └── api-specs/
└── workflows/
    ├── development-workflow.md
    ├── deployment-workflow.md
    └── meeting-workflow.md
```

## Review Process

### Weekly Review (Simon & Thuy)
1. Review `meetings/summaries/{week}-summary.md`
2. Check progress on tasks from previous week
3. Approve/adjust priorities
4. Review upcoming deadlines

### Daily Standup (Optional)
- Check GitHub Project board
- Review tasks in "In Progress"
- Identify blockers
- Update status

## Integration with GitHub Projects

### Project Board Columns
1. **Backlog** - Future tasks, not yet prioritized
2. **To Do** - Prioritized for current sprint/iteration
3. **In Progress** - Actively being worked on
4. **Review** - Pending review (Simon/Thuy for features)
5. **Done** - Completed tasks

### Labels
- `type:feature` - New functionality
- `type:bug` - Bug fixes
- `type:task` - General tasks
- `type:documentation` - Documentation updates
- `priority:high` - Critical/urgent
- `priority:medium` - Important but not urgent
- `priority:low` - Nice to have
- `area:frontend` - Frontend work
- `area:backend` - Backend work
- `area:ai-ml` - AI/ML work
- `area:marketing` - Marketing work
- `area:admin` - Admin/operations work

### Milestones
- `MVP Launch` - First iteration, end of next week
- `Phase 2` - Post-MVP enhancements
- `Future` - Long-term vision

## Best Practices

1. **Single Source of Truth:** All tasks in GitHub, meeting notes in spec-docs repo
2. **Link Everything:** Tasks link to meetings, commits link to issues
3. **Keep It Simple:** Brief titles, descriptions only when needed
4. **Assign Immediately:** Every task has an owner
5. **Review Regularly:** Weekly reviews to keep on track
6. **Update Status:** Team members update their own task status
7. **Clear Deadlines:** Every task has a target date or milestone

## Tools & Automation

- **Fireflies MCP:** Automated transcript retrieval
- **GitHub Actions:** (Future) Auto-create issues from meeting notes
- **MCP Automation:** (Future) Cross-repo task synchronization
- **Daily Digest:** (Future) Daily summary of tasks and progress
