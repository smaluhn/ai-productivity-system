# Quick Start Guide

Get up and running with AI Productivity System in 10 minutes.

## Prerequisites

- GitHub account
- Fireflies.ai account (for meeting transcripts)
- Basic knowledge of Git and Markdown

## Step 1: Set Up Fireflies Integration

1. Get your Fireflies API key from https://fireflies.ai/integrations/custom/fireflies-api
2. Add to your MCP configuration (`.mcp.json`):

```json
{
  "mcpServers": {
    "fireflies": {
      "command": "npx",
      "args": ["-y", "fireflies-mcp-server"],
      "env": {
        "FIREFLIES_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

3. Test the integration:
```bash
# Get recent meetings
fireflies_get_transcripts --limit 5
```

## Step 2: Create Your Project Repository Structure

```bash
# Create your organization or use your personal account
gh repo create your-org/your-project-spec-docs --private

# Clone and set up structure
cd your-project-spec-docs
mkdir -p meetings/{transcripts,agendas,summaries}
mkdir -p specifications
touch ROADMAP.md CHANGELOG.md README.md

# Commit structure
git add .
git commit -m "Initial repository structure"
git push
```

## Step 3: Process Your First Meeting

1. **Get the meeting summary**:
```bash
# List recent meetings
fireflies_get_transcripts --limit 10

# Get summary for specific meeting
fireflies_generate_summary --transcript_id YOUR_ID --format bullet_points
```

2. **Create meeting note file**:
- Use template: `meeting-note-template.md`
- Save as: `meetings/transcripts/2025-10-25-11am-team-meeting-fireflies.md`

3. **Extract action items**:
- Identify tasks with assignees
- Set deadlines and priorities
- Link to meeting notes

## Step 4: Create GitHub Issues from Action Items

For each action item:

```bash
# Create issue in appropriate repo
gh issue create \
  --repo your-org/your-project \
  --title "Implement feature X" \
  --body "Description from meeting notes. Link to meeting: [Meeting Notes](url)" \
  --assignee username \
  --label "type:feature,priority:high" \
  --milestone "MVP Launch"
```

## Step 5: Set Up GitHub Project Board

1. Create organization-level project
2. Choose "Iterative Project" template
3. Configure columns:
   - Backlog
   - To Do
   - In Progress
   - Review
   - Done

4. Add your issues to the project

## Step 6: Configure Labels

Create standard labels in your repository:

```bash
# Type labels
gh label create "type:feature" --color "0e8a16"
gh label create "type:bug" --color "d73a4a"
gh label create "type:task" --color "fbca04"
gh label create "type:documentation" --color "0075ca"

# Priority labels
gh label create "priority:critical" --color "b60205"
gh label create "priority:high" --color "d93f0b"
gh label create "priority:medium" --color "fbca04"
gh label create "priority:low" --color "0e8a16"

# Area labels (customize for your project)
gh label create "area:frontend" --color "c5def5"
gh label create "area:backend" --color "bfdadc"
```

## Example Workflow

### Monday: Team Meeting
1. Meeting happens, Fireflies records
2. After meeting, process transcript
3. Create meeting notes file
4. Extract 10 action items
5. Create 10 GitHub issues
6. Add to project board

### Tuesday-Friday: Development
1. Team members check project board
2. Pick tasks from "To Do"
3. Move to "In Progress"
4. Work on tasks
5. Create PRs
6. Request reviews
7. Move to "Review" when ready

### Friday: Weekly Review
1. Check "Done" column
2. Review completed work
3. Plan next week
4. Update ROADMAP.md if needed
5. Create next meeting agenda

## Tips for Success

1. **Be Consistent**: Use the same format for all meetings and tasks
2. **Link Everything**: Issues → Meetings → PRs → Commits
3. **Keep It Simple**: Brief titles, descriptions only when needed
4. **Update Regularly**: Daily status updates on project board
5. **Review Weekly**: Check progress, adjust priorities

## Common Issues

**Q: Too many issues to create manually?**
A: Start with just critical/high priority items. Add others to backlog later.

**Q: Team not updating task status?**
A: Make it part of daily routine. Review in standups.

**Q: Meeting notes taking too long?**
A: Use the templates. Don't aim for perfect, aim for useful.

**Q: Overwhelmed by the system?**
A: Start small. Just meeting notes + action items. Add more as you go.

## Next Steps

- Read the full [Fireflies Meeting Processing Workflow](../docs/workflows/fireflies-meeting-processing.md)
- Check out [GitHub Organization Structure](../docs/workflows/github-organization-structure.md)
- Join our community discussions
- Share your experience and improvements

## Get Help

- Create an issue with questions
- Check the documentation
- Reach out on X: [@SimonFavourse](https://x.com/SimonFavourse)

---

Ready to supercharge your team's productivity? Let's go! 🚀
