# GitHub Projects Deep Dive - Issues, Projects, Organization

## Understanding the Hierarchy

```
Organization (Printora)
├── Repositories
│   ├── printora (has issues)
│   ├── printora-marketing (has issues)
│   └── printora-spec-docs (has issues)
│
└── Projects (Organization-level)
    ├── Printora Development
    └── Printora Operations
```

## Issues vs Projects: The Core Distinction

### Issues (Live in Repositories)
- **Location**: Inside specific repositories
- **Purpose**: Track specific, actionable work items
- **Scope**: Repository-specific
- **Examples**:
  - `printora` repo, issue #23: "Implement Stripe checkout"
  - `printora-marketing` repo, issue #5: "Create Christmas campaign"

### Projects (Live at Organization or User Level)
- **Location**: Organization-level or User-level
- **Purpose**: Coordinate and visualize work across multiple repos
- **Scope**: Can pull issues from ANY repo in the organization
- **Examples**:
  - "Printora Development" project: Shows all dev issues from all repos
  - "Printora Operations" project: Shows all marketing/admin issues

## Best Practice for Printora

### Strategy: Repository Issues + Organization Projects

**Why This Works:**
1. **Issues stay with code** - Dev issues in `printora`, marketing in `printora-marketing`
2. **Projects provide overview** - See all work across repos in one place
3. **Team separation** - Dev team vs Ops team have different project views
4. **Executive visibility** - Simon/Thuy can see everything in project boards

### Recommended Structure

#### Repositories & Their Issues

**printora (Main App Repo)**
- Issues for: Features, bugs, technical tasks
- Team: Eko, Kevin, Yosua (Write access)
- Reviewers: Simon (Admin), Thuy (Admin)
- Examples:
  - #1: Implement Stripe checkout
  - #2: Build AI design studio
  - #3: Create image upload component

**printora-marketing (Marketing Repo)**
- Issues for: Marketing tasks, content, campaigns
- Team: Nhung (Write), Eko/Kevin/Yosua (Write for automation)
- Reviewers: Simon, Thuy
- Examples:
  - #1: Create Christmas campaign content
  - #2: Write blog post for MVP launch
  - #3: Set up social media schedule

**printora-spec-docs (Documentation Repo)**
- Issues for: Documentation updates, spec changes, meeting follow-ups
- Team: All team members (Write access)
- Owners: Simon (maintains structure)
- Examples:
  - #1: Update ROADMAP with Phase 2 features
  - #2: Document API specifications
  - #3: Create user journey documentation

#### Organization Projects (2 Main Projects)

**Project 1: Printora Development**
- **Purpose**: Track all development work
- **Pulls issues from**: `printora`, `printora-spec-docs` (technical docs)
- **Team**: Eko, Kevin, Yosua, Simon
- **Views**:
  - Board view: Backlog → To Do → In Progress → Review → Done
  - Table view: Filtered by assignee, priority, area
  - Roadmap view: Timeline for MVP Launch milestone
- **Columns**:
  - Backlog (future work)
  - To Do (prioritized for current sprint)
  - In Progress (actively working)
  - Review (pending code review or Simon/Thuy review)
  - Done (completed)

**Project 2: Printora Operations**
- **Purpose**: Track marketing, admin, research, support
- **Pulls issues from**: `printora-marketing`, `printora-spec-docs` (business docs)
- **Team**: Nhung, Simon, Thuy (+ dev team for visibility)
- **Views**:
  - Board view: Backlog → To Do → In Progress → Review → Done
  - Table view: Filtered by campaign, deadline
  - Calendar view: Marketing calendar with campaign dates
- **Columns**: Same as Development project

### Access Control

| Person | Role | printora | printora-marketing | printora-spec-docs | Dev Project | Ops Project |
|--------|------|----------|-------------------|-------------------|-------------|-------------|
| Eko | Senior Dev | Write | Write | Write | Member | View |
| Kevin | Backend Dev | Write | Write | Write | Member | View |
| Yosua | AI/ML Dev | Write | Write | Write | Member | View |
| Nhung | Operations | Read | Write | Write | View | Member |
| Thuy | Executive | Admin | Admin | Admin | Admin | Admin |
| Simon | Executive | Admin | Admin | Admin | Admin | Admin |

**Access Levels:**
- **Admin**: Full access, settings, manage projects
- **Write**: Create issues, PRs, push code
- **Read**: View code, comment on issues
- **Member** (Project): Can edit project, move items between columns
- **View** (Project): Can see project, cannot edit

### Why This Structure?

**1. Clear Separation of Concerns**
- Dev work in dev repo
- Marketing work in marketing repo
- Documentation centralized in spec-docs

**2. Team Autonomy**
- Dev team works in Development project
- Nhung works in Operations project
- No overlap or confusion

**3. Executive Visibility**
- Simon/Thuy can see both projects
- Easy to review dev progress vs marketing progress
- Single dashboard view of all work

**4. Scalability**
- Add more repos later (e.g., `printora-backend`, `printora-frontend`)
- Issues stay with their repos
- Projects automatically pull in new issues

**5. Milestone Coordination**
- "MVP Launch" milestone exists in ALL repos
- Both projects show MVP progress
- Easy to see if on track across all workstreams

## How Issues Flow to Projects

### Automatic Addition (Recommended)
1. Create issue in repository (e.g., `printora` repo)
2. Add label like `area:frontend`
3. Project automation adds it to "To Do" column
4. Team member assigns to themselves
5. Moves through columns as work progresses

### Manual Addition
1. Create issue in repository
2. Open organization project
3. Click "Add items" → Search for issue
4. Add to project
5. Assign and move to appropriate column

### Best Practice: Use Automation
Set up project workflows:
- When issue created with `priority:critical` → Auto-add to "To Do"
- When issue assigned → Auto-move to "In Progress"
- When PR merged → Auto-move to "Done"
- When issue closed → Auto-move to "Done"

## Example Workflow

### 1. Meeting Happens (Oct 25 Bali Team Meeting)
- Fireflies records transcript
- Simon processes meeting notes
- Extracts 20 action items

### 2. Create Issues in Appropriate Repos
```bash
# Dev issue
gh issue create \
  --repo Printora/printora \
  --title "Implement Stripe checkout API integration" \
  --body "..." \
  --assignee zee-mon \
  --label "type:feature,priority:critical,area:backend" \
  --milestone "MVP Launch"

# Marketing issue
gh issue create \
  --repo Printora/printora-marketing \
  --title "Create Christmas-themed design concepts" \
  --body "..." \
  --assignee nhung-username \
  --label "type:task,priority:high,area:marketing" \
  --milestone "MVP Launch"
```

### 3. Issues Auto-Appear in Projects
- Dev issue appears in "Printora Development" project
- Marketing issue appears in "Printora Operations" project

### 4. Team Works
- Eko checks "Printora Development" project
- Sees issue assigned to Kevin
- Picks own tasks from "To Do"
- Moves to "In Progress"

### 5. Review Process
- Kevin completes Stripe integration
- Creates PR
- Moves issue to "Review"
- Simon reviews code
- Approves → merged → auto-moves to "Done"

## When to Use What

### Use Repository Issues When:
- Task is specific to that codebase
- Work happens in that repo
- Team needs to track it with code

### Use Organization Projects When:
- Coordinating across multiple repos
- Need team-wide view of work
- Planning sprints or milestones
- Executives need dashboard view

### Use Repository Projects When (Rare):
- Single repo with complex work
- Repo-specific kanban needed
- Small team, single repo focus

**For Printora: Use Organization Projects** ✅
- Multiple repos
- Multiple teams (dev vs ops)
- Need coordination
- Executive oversight

## Milestones

Milestones can exist in each repository:
- `printora` repo: "MVP Launch" milestone
- `printora-marketing` repo: "MVP Launch" milestone
- Projects can filter by milestone across all repos

**Best Practice**: Use same milestone name across repos
- Makes project filtering easy
- Clear alignment on timeline
- Easy to track progress

## Alternative: Single Project vs Multiple Projects

### Single "Printora" Project (Not Recommended for You)
❌ Pros: Everything in one place
❌ Cons:
- Dev team sees marketing tasks (noise)
- Marketing sees dev tasks (irrelevant)
- Hard to focus on your work area

### Multiple Projects (Recommended for You)
✅ Pros:
- Dev team focuses on dev work
- Ops team focuses on ops work
- Clear separation
- Each team has autonomy

✅ Cons:
- Simon/Thuy need to check 2 projects
- (Mitigated by having admin access to both)

## Summary for Printora

**Repositories (Where Issues Live):**
1. `printora` - Dev issues
2. `printora-marketing` - Marketing issues
3. `printora-spec-docs` - Documentation issues

**Projects (How You Coordinate):**
1. "Printora Development" - Tracks dev issues across repos
2. "Printora Operations" - Tracks marketing/admin issues across repos

**Team Access:**
- Devs: Write to all repos, member of Dev project
- Nhung: Write to marketing/docs, member of Ops project
- Thuy: Read to app repo, write to docs, admin of all
- Simon: Admin of everything

**Issue Flow:**
1. Create issue in appropriate repo
2. Add labels and assignee
3. Issue auto-appears in appropriate project
4. Team moves through columns
5. Review and complete

This gives you:
- ✅ Clear organization
- ✅ Team autonomy
- ✅ Executive visibility
- ✅ Scalable structure
- ✅ Single source of truth per work type
