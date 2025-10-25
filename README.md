# AI Productivity System

> An AI-powered productivity and task management system integrating Fireflies meeting transcripts, GitHub Projects, and automated workflows.

## Overview

This system provides a comprehensive workflow for managing team tasks, meeting notes, and project documentation using AI tools and GitHub automation.

## Key Features

- **Automated Meeting Processing**: Convert Fireflies transcripts into actionable GitHub issues
- **Standardized Workflows**: Consistent processes across all projects
- **Single Source of Truth**: All tasks in GitHub, all documentation in spec-docs repos
- **Team Visibility**: Clear task assignments and progress tracking
- **Review Processes**: Built-in approval workflows for executives and senior team members

## System Components

### 1. Meeting Management
- Fireflies integration for automatic transcription
- Standardized meeting note format
- Action item extraction and task creation
- Automated GitHub issue creation

### 2. Task Tracking
- GitHub Projects for kanban-style tracking
- Repository-based issues for specific work
- Organization-level projects for cross-repo coordination
- Milestone-based planning

### 3. Documentation
- Spec-docs repository per project
- ROADMAP.md for strategic planning
- CHANGELOG.md for tracking decisions
- Meeting transcripts and agendas

### 4. Automation (Future)
- Social media posting (X/Twitter, LinkedIn)
- Daily/weekly digest emails
- Auto-assignment based on task type
- Deadline notifications

## Repository Structure

```
your-org/
├── {project}-repo/              # Main application
├── {project}-marketing/         # Marketing automation
├── {project}-spec-docs/         # Documentation
│   ├── meetings/
│   │   ├── transcripts/
│   │   ├── agendas/
│   │   └── summaries/
│   ├── specifications/
│   ├── ROADMAP.md
│   └── CHANGELOG.md
└── workflows/                   # Shared workflows
```

## Quick Start

### 1. Set Up Fireflies MCP
```json
{
  "mcpServers": {
    "fireflies": {
      "command": "npx",
      "args": ["-y", "fireflies-mcp-server"],
      "env": {
        "FIREFLIES_API_KEY": "${FIREFLIES_API_KEY}"
      }
    }
  }
}
```

### 2. Create Spec-Docs Repository
```bash
gh repo create your-org/your-project-spec-docs --private
cd your-project-spec-docs
mkdir -p meetings/{transcripts,agendas,summaries}
mkdir -p specifications
touch ROADMAP.md CHANGELOG.md README.md
```

### 3. Set Up GitHub Projects
1. Create organization-level project
2. Use "Iterative Project" template
3. Configure columns: Backlog, To Do, In Progress, Review, Done
4. Add labels to repositories (see workflow docs)

### 4. Process Your First Meeting
```bash
# Get recent transcripts
fireflies_get_transcripts --limit 5

# Generate summary
fireflies_generate_summary --transcript_id {id} --format bullet_points

# Create meeting note file
# Extract action items
# Create GitHub issues
# Update CHANGELOG.md
```

## Workflows

See detailed documentation:
- [Fireflies Meeting Processing](../docs/workflows/fireflies-meeting-processing.md)
- [GitHub Organization Structure](../docs/workflows/github-organization-structure.md)
- [Team Task Management](../docs/workflows/team-task-management.md)

## Team Roles

### Developers
- Create branches for features/bugs
- Update task status in project board
- Link commits to issues
- Request code reviews

### Operations (Marketing, Admin)
- Create content and marketing tasks
- Update task progress
- Communicate with external parties
- Track customer feedback

### Executives/Reviewers
- Review completed features
- Approve strategic decisions
- Monitor milestone progress
- Guide priorities

## Labels & Organization

### Standard Labels (All Repos)
- **Type**: `type:feature`, `type:bug`, `type:task`, `type:documentation`
- **Priority**: `priority:critical`, `priority:high`, `priority:medium`, `priority:low`
- **Area**: `area:frontend`, `area:backend`, `area:ai-ml`, `area:marketing`, `area:admin`
- **Status**: `status:blocked`, `status:review-needed`, `status:in-progress`

### Milestones
- **MVP Launch**: First iteration, critical features
- **Phase 2**: Post-MVP enhancements
- **Backlog**: Future features

## Best Practices

1. **Single Source of Truth**: GitHub for tasks, spec-docs for documentation
2. **Link Everything**: Issues ↔ commits ↔ meetings ↔ PRs
3. **Brief & Clear**: Short titles, descriptions only when needed
4. **Immediate Assignment**: Every task has an owner from creation
5. **Regular Updates**: Team members update their own task status
6. **Weekly Reviews**: Executive review of progress and priorities

## Commit Message Format

```
[Brief description]

- Detailed change 1
- Detailed change 2

Related issues: #1, #2
Status: #1 completed, #2 in progress
```

## Future Enhancements

- [ ] Mobile app for task tracking
- [ ] Automated social media posting
- [ ] AI-powered task summarization
- [ ] Integration with calendar systems
- [ ] Cross-project dependency tracking
- [ ] Automated daily digest emails
- [ ] Build-in-public blog automation

## License

MIT License - Feel free to fork and adapt for your own use

## Contributing

This system is designed to be generalizable. If you have improvements or adaptations, please share them!

## Contact

Created by Simon Smaluhn - [simon.smaluhn.com](https://simon.smaluhn.com)
