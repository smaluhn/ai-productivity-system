# GitHub Issues to Create

**Created**: 2025-10-22

Copy these issues into your GitHub Projects boards manually.

---

## FunDe.Fi Project Board Issues
**Board**: https://github.com/orgs/FUNDEdotFI/projects/1

### Issue 1: 📋 Bali Team Meeting 2025-10-23: Review FunDe.Fi Spec-Docs

**Title**: `📋 Bali Team Meeting 2025-10-23: Review FunDe.Fi Spec-Docs`

**Description**:
```markdown
## Meeting Agenda Item

**Date**: 2025-10-23 (Tomorrow - Bali Team Meeting)
**Project**: FunDe.Fi

### Discussion Points

1. **Review spec-docs repository**: https://github.com/zee-mon/fundefi-spec-docs
   - Roadmap with tokenomics details
   - Project context and market analysis
   - Status: 8 foundational files created

2. **Review ve(3,3) tokenomics implementation**
   - 100M FAV token distribution
   - 4-year emission schedule
   - 4 staking tiers with 1x-10x multipliers
   - Vote-escrowed model

3. **Address open questions** (see OPEN-QUESTIONS.md):
   - **Blockchain selection**: Ethereum, Arbitrum, Optimism, Base, or Polygon?
   - **Audit partner selection**: Certik, Trail of Bits, or OpenZeppelin?
   - **Milestone verification mechanism**: Multi-sig vs. oracle options?

4. **Plan remaining technical documentation** (10 docs pending):
   - Smart contract architecture
   - API documentation
   - Frontend integration
   - Testing strategy
   - Security & compliance

### Action Items
- [ ] Team reviews fundefi-spec-docs repository
- [ ] Discuss and make decisions on 3 open questions
- [ ] Assign owners for remaining 10 technical documents
- [ ] Set timeline for smart contract development start

### Resources
- Spec-docs repo: https://github.com/zee-mon/fundefi-spec-docs
- Meeting agenda: /Users/simon/git/simon/meetings/bali-team-meeting-2025-10-23-agenda.md
```

**Assignees**: Simon, Kevin, Eko, Yosua, Anjelito
**Labels**: `meeting`, `discussion`, `urgent`
**Status**: To Do
**Priority**: 🔴 Urgent

---

### Issue 2: 📋 Bali Team Meeting 2025-10-23: Review Printora Spec-Docs

**Title**: `📋 Bali Team Meeting 2025-10-23: Review Printora Spec-Docs`

**Description**:
```markdown
## Meeting Agenda Item

**Date**: 2025-10-23 (Tomorrow - Bali Team Meeting)
**Project**: Printora

### Discussion Points

1. **Review spec-docs repository**: https://github.com/zee-mon/printora-spec-docs
   - Complete documentation: 17 files, 7,321 lines
   - Technical architecture decisions
   - Data models and API contracts
   - User journeys and UI guidelines
   - Testing strategy
   - Security and compliance requirements
   - Deployment infrastructure

2. **Review documentation completeness**
   - Are all sections up to date?
   - Any missing information?
   - Any technical decisions that need revision?

3. **Ensure team alignment on technical decisions**
   - Architecture decisions (11 ADRs)
   - Tech stack choices
   - Database schema
   - API contracts

### Action Items
- [ ] Team reviews printora-spec-docs repository
- [ ] Provide feedback on documentation
- [ ] Identify any missing sections or updates needed
- [ ] Update TODO.md based on spec-docs review

### Resources
- Spec-docs repo: https://github.com/zee-mon/printora-spec-docs
- Meeting agenda: /Users/simon/git/simon/meetings/bali-team-meeting-2025-10-23-agenda.md
```

**Assignees**: Simon, Kevin, Eko, Yosua
**Labels**: `meeting`, `discussion`, `documentation`
**Status**: To Do
**Priority**: 🟠 High

---

### Issue 3: 🚀 Printora AI-Design: Deploy to Staging Server

**Title**: `🚀 Printora AI-Design: Deploy to Staging Server`

**Description**:
```markdown
## Task: Deploy AI-Design Feature to Staging

**Objective**: Make AI-Design feature work on staging server online

**Current Status**: Frontend MVP ~80% complete

### Requirements
- Deploy AI design generation endpoint to staging
- Test with actual AI providers (OpenAI, Midjourney, Stability, etc.)
- Verify image generation workflow
- Test design variations (3 variations per prompt)
- Ensure proper error handling

### Discussion Points (Tomorrow's Meeting)
- Current deployment status
- Any blockers or technical issues
- Testing plan for staging environment
- Timeline for completion

### Acceptance Criteria
- [ ] AI-Design endpoint deployed to staging server
- [ ] Can generate designs via web UI
- [ ] Designs save to database correctly
- [ ] Images stored in cloud storage (Cloudinary/S3)
- [ ] Error handling works properly
- [ ] Performance acceptable (< 30s generation time)

### Technical Details
- **Environment**: Staging server (verify URL)
- **AI Provider**: TBD (OpenAI, Midjourney, Stability AI)
- **Stack**: Next.js, tRPC, Prisma
- **Deployment**: Vercel

### Resources
- Spec-docs: https://github.com/zee-mon/printora-spec-docs
- TODO.md: /Users/simon/git/printora/TODO.md
```

**Assignees**: TBD (assign during meeting)
**Labels**: `feature`, `deployment`, `ai`, `urgent`
**Status**: To Do
**Priority**: 🔴 Urgent

---

## FavosApp Project Board Issues
**Board**: https://github.com/orgs/FavosApp/projects/2

### Issue 4: 📋 Define Favos App Current Status and Next Steps

**Title**: `📋 Define Favos App Current Status and Next Steps`

**Description**:
```markdown
## Task: Document Current Project Status

**Objective**: Define current status and next milestone for Favos App

### Questions to Answer
1. What is the current development status?
2. What features are completed?
3. What features are in progress?
4. What is the next major milestone?
5. Who is working on what?

### Action Items
- [ ] Review current codebase
- [ ] Document completed features
- [ ] Identify in-progress work
- [ ] Define next milestone
- [ ] Update TODO.md with priorities
- [ ] Create spec-docs if needed (like Printora/FunDe.Fi)

### Resources
- TODO.md: /Users/simon/git/favos-app/TODO.md (currently empty template)
- GitHub org: https://github.com/FavosApp
```

**Assignees**: Simon, Kevin
**Labels**: `documentation`, `planning`
**Status**: To Do
**Priority**: 🟠 High

---

## How to Add These Issues

### Via GitHub Web UI:
1. Go to the project board URL
2. Click "+ Add item" at bottom of any column
3. Type "/" to create a new issue
4. Select "Create new issue"
5. Paste the title and description
6. Set assignees, labels, priority
7. Click "Create"

### Bulk Creation Tips:
- Create all 3 meeting-related issues for tomorrow first
- Assign to all team members attending the meeting
- Set priority to Urgent for meeting items
- Add `meeting` label for easy filtering

---

**Next Steps:**
1. Add these issues to respective project boards
2. Review with team tomorrow at Bali meeting
3. Update statuses as work progresses
4. Close issues when completed

