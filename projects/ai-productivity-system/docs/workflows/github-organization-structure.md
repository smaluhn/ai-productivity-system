# GitHub Organization Structure & Best Practices

## Repository Strategy

### Printora Organization

```
Printora/
├── printora                  # Main application repo (dev team)
├── printora-marketing        # Marketing automation (dev + marketing team)
└── printora-spec-docs        # Specifications & documentation (all team + executives)
```

### Repository Access Levels

| Repo | Eko | Kevin | Yosua | Nhung | Thuy | Simon |
|------|-----|-------|-------|-------|------|-------|
| printora | Write | Write | Write | Read | Admin | Admin |
| printora-marketing | Write | Write | Write | Write | Admin | Admin |
| printora-spec-docs | Write | Write | Write | Write | Admin | Admin |

**Roles:**
- **Admin:** Full access, settings, team management (Simon, Thuy)
- **Write:** Push, create branches, create issues (Dev team, Nhung on marketing/docs)
- **Read:** View code, comment on issues (Nhung on main app - if needed for context)

## Issues vs Projects: When to Use What

### Repository Issues
**Use for:** Specific, actionable tasks tied to a single repository
- Code bugs in `printora` repo
- Feature development in `printora` repo
- Marketing tasks in `printora-marketing` repo
- Documentation updates in `printora-spec-docs` repo

**Example:**
- Issue #23 in `printora`: "Implement Stripe checkout API integration"
- Issue #5 in `printora-marketing`: "Create Christmas campaign content"

### Organization-Level Projects
**Use for:** Cross-repo coordination, milestone tracking, team planning

**Current Setup:**
1. **Printora Development** (Project)
   - Tracks all dev-related issues across repos
   - Includes: Features, bugs, technical tasks from `printora` repo
   - Team: Eko, Kevin, Yosua
   - Template: Iterative Project

2. **Printora Operations** (Project) - NEW SUGGESTION
   - Tracks marketing, admin, research, support
   - Includes: Issues from `printora-marketing` and operational tasks
   - Team: Nhung, + dev team for marketing automation
   - Template: Iterative Project

### Best Practice Structure

```
┌─────────────────────────────────────────────────────────┐
│  Organization: Printora                                  │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Projects (Organization Level)                           │
│  ├─ Printora Development                                │
│  │   ├─ Pulls from: printora, printora-spec-docs        │
│  │   ├─ Team: Dev team                                  │
│  │   └─ Milestones: MVP Launch, Phase 2                 │
│  │                                                        │
│  └─ Printora Operations                                  │
│      ├─ Pulls from: printora-marketing, spec-docs       │
│      ├─ Team: Nhung, + dev support                      │
│      └─ Milestones: MVP Launch, Marketing Campaigns     │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Repositories                                            │
│  ├─ printora                                             │
│  │   ├─ Issues: Dev tasks, bugs, features               │
│  │   └─ Milestones: MVP Launch, Phase 2                 │
│  │                                                        │
│  ├─ printora-marketing                                   │
│  │   ├─ Issues: Marketing tasks, content, campaigns     │
│  │   └─ Milestones: MVP Launch, Christmas Campaign      │
│  │                                                        │
│  └─ printora-spec-docs                                   │
│      ├─ Issues: Documentation updates, spec changes     │
│      ├─ Folders: meetings/, specifications/             │
│      └─ Files: ROADMAP.md, CHANGELOG.md                 │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## Workflow: From Meeting to Task

1. **Meeting happens** → Fireflies records transcript
2. **Process meeting** → Extract action items with assignees
3. **Create issues** → In appropriate repository
   - Dev tasks → `printora` repo
   - Marketing tasks → `printora-marketing` repo
   - Documentation → `printora-spec-docs` repo
4. **Add to project** → Issues auto-add to project boards
5. **Assign & label** → Set assignee, labels, milestone
6. **Track progress** → Team updates status in project board
7. **Review** → Simon/Thuy review completed tasks

## Labels Standard (Apply to All Repos)

### Type Labels
- `type:feature` - New functionality
- `type:bug` - Bug fixes
- `type:task` - General task
- `type:documentation` - Documentation

### Priority Labels
- `priority:critical` - Blocks MVP/production
- `priority:high` - Important for current iteration
- `priority:medium` - Important but can wait
- `priority:low` - Nice to have

### Area Labels
- `area:frontend` - Frontend work (Eko)
- `area:backend` - Backend work (Kevin)
- `area:ai-ml` - AI/ML work (Yosua)
- `area:marketing` - Marketing work (Nhung + dev)
- `area:admin` - Admin/ops work (Nhung)
- `area:design` - Design/UX work

### Status Labels (if not using project board automation)
- `status:blocked` - Blocked by external dependency
- `status:review-needed` - Needs review from Simon/Thuy
- `status:in-progress` - Currently being worked on

## Milestones

### MVP Launch (Target: End of next week)
**Scope:**
- Stripe payment integration
- Basic AI design studio
- Image upload + AI generation + text editing
- Preview + print-ready image storage
- Test product orders
- Core 4 products

**Repos:**
- `printora`: All core features
- `printora-marketing`: MVP announcement content
- `printora-spec-docs`: MVP specifications finalized

### Phase 2 (Post-MVP)
**Scope:**
- Additional products (expand from 4 to more)
- Social features (sharing, favorites)
- Community features
- Admin dashboard
- Subscription features

### Backlog
**Scope:**
- Artist marketplace
- API partnerships
- Advanced AI features
- International expansion

## Team Task Visibility

### For Simon
**Daily View:**
- GitHub Project board for "Review" column
- Issues assigned to Simon
- Critical/high priority issues

**Weekly View:**
- Milestone progress (MVP Launch)
- Team velocity (issues closed per week)
- Upcoming deadlines
- Meeting summaries in spec-docs

### For Each Team Member
**Daily View:**
- GitHub Project board, filtered by assignee
- Issues assigned to them
- Issues in "In Progress" or "To Do"

**Weekly View:**
- Sprint/iteration planning
- Completed tasks
- Next week's priorities

## Commit Message Standard

```
[Brief description of change]

- Detailed change 1
- Detailed change 2
- Detailed change 3

Related issues: #issue1, #issue2
Status: #issue1 completed, #issue2 in progress
```

**Example:**
```
Implement Stripe checkout API integration

- Added Stripe SDK dependency
- Created payment service with checkout session
- Added webhook handler for payment confirmation
- Updated product model with payment status

Related issues: #23, #45
Status: #23 completed, #issue2 in progress
```

## Review & Approval Process

### Code Reviews (Dev tasks)
1. Developer creates PR
2. Eko reviews (as senior dev)
3. Merge to dev branch
4. Deploy to staging
5. Simon/Thuy review on staging
6. Merge to main/production

### Feature Reviews (New features)
1. Developer implements
2. Creates PR with demo/screenshots
3. Eko reviews code
4. Simon/Thuy review functionality and UX
5. Approve → merge
6. Update CHANGELOG.md

### Content Reviews (Marketing)
1. Nhung creates content
2. Posts as draft
3. Simon/Thuy review
4. Approve → publish
5. Update marketing tracker

## Automation Opportunities (Future)

1. **Auto-create issues from meeting notes** - GitHub Action
2. **Daily digest email** - Summary of tasks due today
3. **Weekly summary** - Progress report for Simon/Thuy
4. **Auto-assign based on area label** - GitHub Action
5. **Deadline reminders** - Notifications for upcoming deadlines
6. **Cross-repo task linking** - MCP automation
