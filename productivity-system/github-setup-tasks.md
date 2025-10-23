# GitHub Setup Tasks - Team Member Access

**Date**: 2025-10-23
**Action**: Add sudosimonglitch to all orgs and team members to project boards

---

## Team Member GitHub Accounts

| Name | GitHub Username | Role | Projects |
|------|----------------|------|----------|
| **Simon** | sudosimonglitch | Owner/Admin | All projects |
| **Kevin** | zee-mon | Developer | Printora, AkunIndo, Infrastructure |
| **Eko** | mrfavi | Developer | All projects |
| **Yosua** | YosuaTriantara | Developer | All projects |
| **Anjelito** | OneBigStar3 | Developer | FunDe.Fi, Favos App |

---

## 1. Add sudosimonglitch to All Organizations

You need to add your personal account (sudosimonglitch) to all orgs as Owner/Admin.

### Via GitHub Web UI:

**For each organization:**
1. Go to organization settings
2. Click "People" in sidebar
3. Click "Invite member"
4. Enter: `sudosimonglitch`
5. Select role: **Owner**
6. Send invitation
7. Accept invitation from sudosimonglitch account

**Organizations to update:**
- [ ] https://github.com/Printora → Add sudosimonglitch as Owner
- [ ] https://github.com/FUNDEdotFI → Add sudosimonglitch as Owner
- [ ] https://github.com/FavosApp → Add sudosimonglitch as Owner
- [ ] https://github.com/DiverseProjects → Add sudosimonglitch as Owner
- [ ] https://github.com/Favourse → Add sudosimonglitch as Owner
- [ ] https://github.com/Favorsid → Add sudosimonglitch as Owner

### Via GitHub CLI (if you have admin access):

```bash
# Switch to an account with admin access
gh auth switch

# For each org, invite sudosimonglitch
gh api -X PUT /orgs/Printora/memberships/sudosimonglitch -f role=admin
gh api -X PUT /orgs/FUNDEdotFI/memberships/sudosimonglitch -f role=admin
gh api -X PUT /orgs/FavosApp/memberships/sudosimonglitch -f role=admin
gh api -X PUT /orgs/DiverseProjects/memberships/sudosimonglitch -f role=admin
gh api -X PUT /orgs/Favourse/memberships/sudosimonglitch -f role=admin
gh api -X PUT /orgs/Favorsid/memberships/sudosimonglitch -f role=admin
```

---

## 2. Add Team Members to GitHub Project Boards

### Printora Project Board
**URL**: https://github.com/orgs/Printora/projects/1

**Team Members to Add:**
- [ ] sudosimonglitch (Simon) - Admin
- [ ] zee-mon (Kevin) - Write
- [ ] mrfavi (Eko) - Write
- [ ] YosuaTriantara (Yosua) - Write

**How to add:**
1. Open project board
2. Click "⋯" (three dots) → "Settings"
3. Go to "Manage access"
4. Click "Add people"
5. Search for username
6. Select permission level (Admin or Write)
7. Click "Add to project"

### FunDe.Fi Project Board
**URL**: https://github.com/orgs/FUNDEdotFI/projects/1

**Team Members to Add:**
- [ ] sudosimonglitch (Simon) - Admin
- [ ] zee-mon (Kevin) - Write
- [ ] mrfavi (Eko) - Write
- [ ] YosuaTriantara (Yosua) - Write
- [ ] OneBigStar3 (Anjelito) - Write

### FavosApp Project Board
**URL**: https://github.com/orgs/FavosApp/projects/2

**Team Members to Add:**
- [ ] sudosimonglitch (Simon) - Admin
- [ ] zee-mon (Kevin) - Write
- [ ] mrfavi (Eko) - Write
- [ ] YosuaTriantara (Yosua) - Write
- [ ] OneBigStar3 (Anjelito) - Write

---

## 3. GitHub Issues to Create

### Printora Project Issues
**Create in**: Printora organization repos (or directly in project board)

#### Issue 1: Deploy AI-Design to Staging Server
```markdown
**Title**: 🚀 Deploy AI-Design Feature to Staging Server

**Assignee**: @zee-mon (Kevin)
**Labels**: deployment, urgent, printora
**Project**: Printora Board
**Priority**: 🔴 Urgent

## Description
Deploy the AI-Design feature to staging server so it works online.

## Current Status
- Frontend MVP ~80% complete
- Need to deploy to staging environment

## Tasks
- [ ] Deploy AI-Design endpoint to staging
- [ ] Test with actual AI providers (OpenAI/Midjourney/Stability)
- [ ] Verify image generation workflow
- [ ] Test design variations (3 per prompt)
- [ ] Ensure error handling works
- [ ] Performance test (< 30s generation time)

## Acceptance Criteria
- AI-Design works on staging server
- Can generate designs via web UI
- Images save to database and cloud storage correctly
- Error handling functional

## Timeline
Discuss in team meeting 2025-10-23
```

#### Issue 2: Stripe Sandbox Setup
```markdown
**Title**: 💳 Set Up Stripe Sandbox for Printora Staging/Dev

**Assignee**: @zee-mon (Kevin)
**Labels**: infrastructure, printora, stripe
**Project**: Printora Board
**Priority**: 🟠 High

## Description
Configure Stripe sandbox environment for Printora testing.

## Tasks
- [ ] Access Stripe account (already given access)
- [ ] Set up sandbox/test mode
- [ ] Configure webhooks for staging
- [ ] Test payment flow
- [ ] Document setup for team
- [ ] Prepare for live Stripe setup

## Notes
- Account already created, Kevin has access
- Can contact Stripe support if needed
```

#### Issue 3: Sign Up to POD Fulfillment Service
```markdown
**Title**: 📦 Evaluate and Sign Up to POD Fulfillment Service

**Assignee**: @zee-mon (Kevin)
**Labels**: fulfillment, printora, research
**Project**: Printora Board
**Priority**: 🔴 Urgent
**Deadline**: November 1, 2025

## Description
Sign up to print-on-demand fulfillment service(s) using admin@printora.ai

## Options to Evaluate
- Printful
- Printify
- Gelato

## Tasks
- [ ] Sign up to all three services (admin@printora.ai)
- [ ] Order sample products from each
- [ ] Compare:
  - Quality
  - Shipping time
  - Pricing
  - Product catalog
  - API integration
- [ ] Prepare recommendation for team
- [ ] Make final decision by Nov 1

## Decision Criteria
- Product quality
- Shipping speed
- Pricing competitiveness
- API ease of integration
- Product variety
```

#### Issue 4: Create Printora Social Media Presence
```markdown
**Title**: 📱 Create Printora Social Media Accounts

**Assignee**: @zee-mon (Kevin)
**Labels**: marketing, printora, setup
**Project**: Printora Board
**Priority**: 🟡 Normal

## Description
Create social media presence for Printora beta launch.

## Tasks
- [ ] Create Twitter account (admin@printora.ai)
- [ ] Create Instagram account (admin@printora.ai)
- [ ] Create TikTok account (admin@printora.ai)
- [ ] Set up profiles (bio, links, branding)
- [ ] Create initial content plan
- [ ] Post design examples
- [ ] Prepare creator guidelines

## Purpose
Prepare for beta launch, build audience

## Content Ideas
- AI-generated design showcase
- Creator success stories
- Platform features
- Beta launch announcements
```

---

### AkunIndo Project Issues

#### Issue 5: Optimize AkunIndo Mobile Layout
```markdown
**Title**: 📱 Optimize AkunIndo Mobile Layout

**Assignee**: @zee-mon (Kevin)
**Labels**: mobile, ux, akunindo
**Project**: (AkunIndo doesn't have project board yet - create in repo)
**Priority**: 🟠 High

## Description
Improve mobile UX and layout for AkunIndo website.

## Discussion Points
- Current mobile UX issues?
- Priority fixes needed?
- Timeline for completion?

## Tasks
- [ ] Audit current mobile experience
- [ ] Identify UX issues
- [ ] Prioritize fixes
- [ ] Implement improvements
- [ ] Test on multiple devices
- [ ] Get team feedback

## Related
- AkunIndo beta launch prep
- User testing feedback
```

#### Issue 6: AkunIndo Hiring - Find 2-3 Team Members
```markdown
**Title**: 👥 Hire Sales & Marketing Staff for AkunIndo (2-3 positions)

**Assignee**: @sudosimonglitch (Simon)
**Labels**: hiring, akunindo, urgent
**Project**: (AkunIndo project board)
**Priority**: 🔴 Urgent

## Description
Find and hire 2-3 people for AkunIndo team.

## Positions Needed
1. **Sales (Door-to-door)**
2. **Sales (Cold calls)**
3. **Marketing (Instagram/Facebook)**

## Action Items
- [ ] Team: Does anyone know candidates?
- [ ] Create job descriptions
- [ ] **Team to share on social media** (tag @sudosimonglitch)
- [ ] Review applications
- [ ] Interview candidates
- [ ] Make hiring decisions

## Requirements
- See AkunIndo TODO.md for detailed requirements
- Need people ASAP for beta launch

## Team Action
All team members: Please share job postings on your social media!
```

---

### FunDe.Fi Project Issues

#### Issue 7: Design Weekly Emissions System (URGENT)
```markdown
**Title**: 🔥 URGENT: Design FunDe.Fi Weekly Emissions System

**Assignee**: @sudosimonglitch (Simon), @OneBigStar3 (Anjelito)
**Labels**: tokenomics, fundefi, critical, ve33
**Project**: FunDe.Fi Board
**Priority**: 🔴 URGENT

## Description
Design how weekly FAV token emissions distribute to campaigns/projects/token vaults.

## Critical Question (from Anjelito)
**How do weekly FAV token emissions get distributed?**
- What % to campaigns?
- What % to projects?
- What % to token vaults?

## Key Challenge
**Adapt DEX emission model to Launchpad model**
- Traditional ve(3,3): DEX liquidity pools
- FunDe.Fi: Launchpad campaigns/projects

## Tasks
- [ ] Research ve(3,3) emission mechanics (Curve, Velodrome, etc.)
- [ ] Design emission distribution formula
- [ ] Define % split (campaigns/projects/vaults)
- [ ] Integration with voting power (lock duration)
- [ ] Create clear documentation
- [ ] Update fundefi-spec-docs
- [ ] Schedule meeting with Anjelito to explain
- [ ] Get Anjelito's feedback and approval

## Resources
- fundefi-spec-docs ROADMAP.md (tokenomics section)
- fundefi-spec-docs OPEN-QUESTIONS.md

## Timeline
Discuss in team meeting 2025-10-23, then document ASAP
```

#### Issue 8: Add Polkadot to Blockchain Evaluation
```markdown
**Title**: ⛓️ Evaluate Polkadot as Blockchain Option for FunDe.Fi

**Assignee**: @sudosimonglitch (Simon), @mrfavi (Eko)
**Labels**: research, blockchain, fundefi, polkadot
**Project**: FunDe.Fi Board
**Priority**: 🟠 High

## Description
Add Polkadot as 6th blockchain option for FunDe.Fi evaluation.

## Current Options
1. Ethereum
2. Arbitrum
3. Optimism
4. Base
5. Polygon
6. **Polkadot** (NEW)

## Rationale
- HIC invested $250K in joinn.io (Polkadot focus)
- HIC bullish on Polkadot for tokenised assets
- Multi-chain reduces platform risk
- Josh has tokenised assets tech

## Evaluation Criteria
- [ ] Gas costs comparison
- [ ] Tokenised assets capabilities
- [ ] Developer ecosystem
- [ ] User adoption
- [ ] Smart contract maturity
- [ ] Cross-chain capabilities
- [ ] Integration with ve(3,3) model

## Tasks
- [ ] Research Polkadot parachain options
- [ ] Compare gas costs vs other chains
- [ ] Evaluate tokenised assets support
- [ ] Technical feasibility assessment
- [ ] Add to blockchain comparison matrix
- [ ] Update fundefi-spec-docs OPEN-QUESTIONS.md

## Related
- Josh's tokenised assets tech
- HIC partnership opportunity
```

#### Issue 9: Follow Up with Josh - Tokenised Assets Tech
```markdown
**Title**: 💎 Follow Up with Josh on Tokenised Assets Technology

**Assignee**: @sudosimonglitch (Simon)
**Labels**: research, tokenised-assets, fundefi, partnership
**Project**: FunDe.Fi Board
**Priority**: 🔴 Urgent

## Description
Josh already developed tokenised assets technology. Waiting for him to come back with details.

## Background
- Josh has working tokenised assets tech
- Could be critical differentiator for FunDe.Fi
- Aligns with HIC's Polkadot interest
- Waiting for Josh to respond

## Critical Questions
1. What is the current status of the tech?
2. How does it work technically?
3. **How can it integrate with ve(3,3) tokenomics?**
4. What blockchain(s) does it support?
5. What would partnership/licensing look like?

## Potential Impact
- Unique positioning: Only ve(3,3) launchpad with tokenised assets
- Differentiates from competitors
- Aligns with HIC investment thesis

## Tasks
- [ ] Reach out to Josh
- [ ] Schedule call/meeting
- [ ] Get technical overview
- [ ] Discuss integration possibilities
- [ ] Explore partnership options
- [ ] Document findings
- [ ] Share with team and Anjelito

## Strategic Alignment
Josh's tech + HIC's Polkadot interest + ve(3,3) = unique competitive moat
```

---

### Infrastructure Issues

#### Issue 10: Migrate Favourse.com, Cancel Old Hosts
```markdown
**Title**: 🔧 Migrate favourse.com and Cancel Old Hosting (netcup.de, bluehost.com)

**Assignee**: @zee-mon (Kevin)
**Labels**: infrastructure, migration, admin
**Project**: (Infrastructure/Admin)
**Priority**: 🟡 Normal

## Description
Migrate favourse.com away from current hosts and cancel old accounts.

## Tasks

### Favourse.com Migration
- [ ] Identify current hosting provider
- [ ] Choose new hosting provider
- [ ] Migrate website/services
- [ ] Update DNS if needed
- [ ] Verify everything works
- [ ] Test thoroughly

### Netcup.de
- [ ] Migrate any services away from netcup.de
- [ ] Verify nothing is left behind
- [ ] Cancel account
- [ ] Confirm cancellation

### Bluehost.com
- [ ] Migrate any services away from bluehost.com
- [ ] Verify nothing is left behind
- [ ] Cancel account
- [ ] Confirm cancellation

## Notes
- Ensure no downtime during migration
- Backup everything before migrating
- Document new setup for team
```

---

## 4. How to Create Issues in GitHub Projects

### Method 1: Via GitHub Web UI (Recommended)
1. Go to project board (e.g., https://github.com/orgs/Printora/projects/1)
2. Click "+ Add item" at bottom of "To Do" column
3. Type "/" to create new issue
4. Select "Create new issue"
5. Choose repository or create in project
6. Copy-paste title and description from above
7. Set assignee, labels, priority
8. Click "Create"

### Method 2: Create in Repository First
1. Go to repository Issues tab
2. Click "New issue"
3. Fill in details
4. Create issue
5. Add to project board via sidebar

### Method 3: Via GitHub CLI (Bulk Creation)
```bash
# Example for creating issue
gh issue create \
  --repo Printora/printora \
  --title "🚀 Deploy AI-Design Feature to Staging Server" \
  --body "$(cat issue-template.md)" \
  --assignee zee-mon \
  --label "deployment,urgent,printora" \
  --project "Printora Board"
```

---

## 5. Priority Order for Creating Issues

**Create these FIRST (Urgent):**
1. ✅ FunDe.Fi Weekly Emissions System (Anjelito waiting)
2. ✅ Printora POD Fulfillment (Nov 1 deadline)
3. ✅ Follow up with Josh (Tokenised assets)
4. ✅ AkunIndo Hiring (need people ASAP)

**Then create:**
5. Printora AI-Design Staging
6. Add Polkadot to evaluation
7. Stripe sandbox setup
8. AkunIndo mobile optimization

**Lower priority:**
9. Printora social media
10. Infrastructure migrations

---

## Summary

**Manual Steps Required:**
1. Add sudosimonglitch to all 6 orgs as Owner
2. Add all team members to the 3 project boards
3. Create 10 GitHub issues from templates above

**Why Manual:**
- GitHub CLI needs `project` scope (requires interactive auth refresh)
- Better to do via web UI for first-time setup
- Can automate future issues once access is set up

**Time Estimate:** 30-45 minutes to complete all steps

---

**Created**: 2025-10-23
**Last Updated**: 2025-10-23

