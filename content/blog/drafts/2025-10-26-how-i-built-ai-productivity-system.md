---
title: "How I Built an AI Productivity System That Saves 20+ Hours Per Week"
date: 2025-10-26
author: Simon Smaluhn
tags: [productivity, ai, automation, opensource]
status: draft
description: "From 72-minute meetings to 20 GitHub issues in minutes: How I automated my team's workflow"
---

# How I Built an AI Productivity System That Saves 20+ Hours Per Week

## The Problem: Meeting Overload

Last week, I had a 72-minute team meeting for Printora, our AI-powered print-on-demand platform. Five team members, three different specializations (frontend, backend, AI/ML), plus operations and executive oversight.

By the end, we had:
- Defined our MVP scope
- Made critical technical decisions
- Assigned 20+ action items across the team
- Set deadlines for end of next week

**The old way?** I'd spend 2-3 hours:
1. Re-listening to the recording
2. Writing meeting notes
3. Extracting action items
4. Creating tasks in various tools
5. Emailing assignments to team
6. Following up because someone missed an email

**The new way?** 30 minutes, fully automated.

## The Solution: AI + Automation

I built a system that:

1. **Records automatically** (Fireflies.ai)
2. **Transcribes with AI** (built-in)
3. **Processes via Claude** (extract action items)
4. **Creates GitHub issues** (with assignments & labels)
5. **Links everything** (meeting notes ↔ tasks ↔ code)

## How It Works

### Step 1: Meeting Happens

Fireflies.ai joins the call automatically. Records everything. Generates transcript.

No manual work.

### Step 2: Process Transcript

```bash
# Get recent meetings
fireflies_get_transcripts --limit 5

# Get specific meeting summary
fireflies_generate_summary --transcript_id {id} --format bullet_points
```

I get:
- Overview
- Discussion points with timestamps
- Decisions made
- Action items with assignees
- Keywords

### Step 3: Create Structured Notes

I use a standardized template:

```markdown
# Meeting Title - YYYY-MM-DD

**Participants**: Name1, Name2
**Duration**: 72 minutes

## Key Decisions
1. Decision 1
2. Decision 2

## Action Items
| Task | Assignee | Deadline | Priority |
|------|----------|----------|----------|
| Implement Stripe | Kevin | Nov 1 | Critical |
```

### Step 4: Generate GitHub Issues

For each action item, create an issue:

```bash
gh issue create \
  --repo project/repo \
  --title "Implement Stripe checkout" \
  --body "..." \
  --assignee kevin \
  --label "type:feature,priority:critical" \
  --milestone "MVP Launch"
```

### Step 5: Track in Projects

Issues automatically appear in GitHub Projects (kanban board).

Team sees:
- What they need to do
- When it's due
- Who else is working on what

## Real Results: Printora Example

**Meeting**: Oct 25, 11:23 AM, 72 minutes

**Processed**:
- 20 action items created
- 3 repositories organized
- 2 project boards set up
- Complete ROADMAP.md
- Full CHANGELOG.md

**Time spent**: ~30 minutes

**Time saved**: ~20 hours (compared to old manual process)

## The Tech Stack

### Core Tools
- **Fireflies.ai**: Meeting transcription ($0-20/month)
- **GitHub**: Task management (free for small teams)
- **Claude Code**: AI automation
- **Google Calendar**: Scheduling (free)
- **Reclaim.ai**: AI time blocking (free tier available)

### Optional Additions
- **Obsidian**: Knowledge base (free)
- **Telegram**: Notifications (free)
- **Substack**: Newsletter (free)

Total cost: **$0-50/month** depending on team size

## Key Features

### 1. Single Source of Truth

Everything lives in GitHub:
- Tasks as Issues
- Progress on Project boards
- Code in repositories
- Documentation in spec-docs repos

One place to check. No context switching.

### 2. Clear Assignments

Every task has:
- Assignee (person responsible)
- Labels (type, priority, area)
- Milestone (when it's due)
- Description (context from meeting)

No ambiguity. No "I thought you were doing that."

### 3. Executive Visibility

Non-technical leaders (like my executive team) can:
- View project boards
- See progress
- Review completed work
- No need to understand code

### 4. Scalable

Started with Printora. Now using for:
- AkunIndo (expense tracking app)
- FunDe.Fi (DeFi project)
- Personal tasks

Same system. Same process.

## The Workflow in Practice

### Monday: Team Meeting
1. Fireflies records
2. I process transcript (15 min)
3. Create issues (15 min)
4. Team sees tasks in project board

### Tuesday-Friday: Work
1. Team picks tasks from "To Do"
2. Moves to "In Progress"
3. Completes work
4. Creates PR
5. Moves to "Review"

### Friday: Weekly Review
1. Check "Done" column
2. Review progress
3. Plan next week
4. Update roadmap if needed

### Repeat

## Common Questions

**Q: Does this work for solo founders?**
Yes! I use it for my personal tasks too. Even a one-person "team" benefits from organization.

**Q: What if I don't use Fireflies?**
You can manually create meeting notes. The system works with any structured notes.

**Q: Do I need to know how to code?**
No. The basic setup requires copy-pasting commands. I provide templates for everything.

**Q: How much time to set up?**
10 minutes if you follow the quick start guide.

**Q: What about privacy?**
Everything is in your GitHub. You control the data. Fireflies has enterprise-grade security.

## Open Source

I'm releasing this as open source (MIT license) because:

1. **Accessibility**: Everyone should have access to good productivity tools
2. **Community**: Others can contribute improvements
3. **Transparency**: You can see exactly how it works
4. **Customization**: Adapt it to your needs

**Future plans**:
- Mobile app (track tasks on the go)
- Advanced AI features (smart prioritization)
- Pro tier (for teams that want support)

But the core will always be free.

## Get Started

### Quick Start (10 minutes)

1. **Set up Fireflies**
   - Sign up at fireflies.ai
   - Connect calendar
   - Get API key

2. **Clone the repo**
   ```bash
   git clone https://github.com/smaluhn/ai-productivity-system
   ```

3. **Configure MCP**
   - Add Fireflies API key
   - Connect GitHub
   - Done!

4. **Process your first meeting**
   - Get transcript
   - Use meeting template
   - Create issues

Full guide: https://github.com/smaluhn/ai-productivity-system

## The Impact

### Before
- Meetings felt like black holes
- Action items forgotten
- No clear ownership
- Constant "What were we supposed to do?" messages

### After
- Every meeting → clear outcomes
- 100% task capture
- Zero ambiguity
- Team autonomy

**ROI**: 20+ hours saved per week. Team productivity up. Stress down.

## What's Next

I'm building this in public. Follow along:
- **X/Twitter**: @SimonFavourse
- **LinkedIn**: Simon Smaluhn
- **Blog**: simon.smaluhn.com

Next features:
- Automated social media posting
- AI-powered task prioritization
- Mobile app for on-the-go updates
- Analytics dashboard

## Try It

Star the repo: https://github.com/smaluhn/ai-productivity-system

Questions? Open an issue or DM me.

Let's make productivity accessible to everyone.

---

*Simon Smaluhn is building AI-powered productivity tools and print-on-demand platforms in Bali. He helps remote teams stay organized without the overhead.*

**Want updates?** Subscribe to my newsletter (link) for weekly insights on building with AI, remote team management, and productivity hacks.
