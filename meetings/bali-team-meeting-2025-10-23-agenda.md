# Bali Team Meeting - October 23, 2025

**Date**: 2025-10-23
**Type**: Team Meeting

---

## Agenda

### 1. Spec-Docs Template & System Introduction
- **Templates Location**: `/Users/simon/git/simon/templates/`
  - `spec-docs-megaprompt.md` - Comprehensive prompt for generating spec-docs
  - `spec-docs-template.md` - Standard structure and sections
- **Example**: AkunIndo spec-docs (production-grade reference)
  - Repository: https://github.com/sudosimonglitch/akunindo-spec-docs
  - 11 technical documents + roadmap + CLAUDE.md
- **Discussion Points**:
  - Explain spec-docs system and benefits
  - Show template structure
  - How to use megaprompt with Claude
  - When to create spec-docs for new projects

### 2. Review Printora Spec-Docs Repository
- **Repository**: https://github.com/zee-mon/printora-spec-docs
- **Status**: Complete documentation created (17 files, 7,321 lines)
- **Contents**:
  - Complete technical architecture decisions
  - Data models and API contracts
  - User journeys and UI guidelines
  - Testing strategy
  - Security and compliance requirements
  - Deployment infrastructure
- **Discussion Points**:
  - Review documentation completeness
  - Identify any missing sections or updates needed
  - Ensure team alignment on technical decisions

### 3. Review FunDe.Fi Spec-Docs Repository
- **Repository**: https://github.com/favosapp/fundefi-spec-docs
- **Status**: Foundational documentation created (8 files)
- **Contents**:
  - Project context and market analysis
  - Roadmap with tokenomics details (100M FAV distribution, emission schedule)
  - Open questions requiring decisions
  - Initial technical documentation (project context)
- **Discussion Points**:
  - Review ve(3,3) tokenomics implementation
  - Address open questions (blockchain selection, audit partner, milestone verification)
  - Plan remaining technical documentation (10 docs pending)

### 4. Printora AI-Design: Deploy to Staging Server
- **Objective**: Make AI-Design feature work on staging server online
- **Current Status**: Frontend MVP ~80% complete
- **Task**: Deploy and test AI design generation on staging environment
- **Discussion Points**:
  - Current deployment status
  - Any blockers or technical issues
  - Testing plan for staging environment
  - Timeline for completion

### 5. AkunIndo Hiring - Sales & Marketing Staff
- **Positions Needed** (2-3 people total):
  - Sales person (Door-to-door)
  - Sales person (Cold calls)
  - Marketing person (Instagram/Facebook)
- **Discussion Points**:
  - Does anyone on the team know candidates?
  - **ACTION**: Team to share on social media looking for 2-3 people
  - Tag Simon in social media posts
  - Job description and requirements
- **Related**: See AkunIndo TODO.md for hiring requirements

### 6. FunDe.Fi Mechanics & Weekly Emissions System
- **Critical Question from Anjelito**: Weekly emissions to campaigns/projects/token vaults
  - How do weekly FAV token emissions get distributed?
  - What percentage goes to campaigns vs projects vs token vaults?
  - Emission schedule mechanics
  - Integration with ve(3,3) tokenomics

- **Multi-Chain Consideration & Tokenised Assets**:
  - HIC invested $250K in joinn.io (5% at $10M valuation)
  - HIC bullish on Polkadot for tokenised assets
  - **DECISION**: Add Polkadot to blockchain evaluation
  - New options: Ethereum/Arbitrum/Optimism/Base/Polygon/**Polkadot**

  - **Tokenised Assets Tech**:
    - Josh already developed the tech for tokenised assets
    - Waiting for Josh to come back to us about this
    - Could be critical differentiator for FunDe.Fi
    - Integration with ve(3,3) tokenomics?

- **Action Items**:
  - Discuss mechanics internally with team
  - Create clear documentation
  - Schedule follow-up with Anjelito to explain system
  - Update spec-docs with detailed emission mechanics
  - **Add Polkadot to blockchain evaluation** (6th option)
  - Follow up with Josh re tokenised assets tech status
  - Explore tokenised assets integration with ve(3,3) model

- **Update**: Simon's discussion with Thuy (if completed)
- **Related**: See fundefi-spec-docs OPEN-QUESTIONS.md and ROADMAP.md (tokenomics section)

---

## Action Items
- [ ] Review and provide feedback on printora-spec-docs
- [ ] Review and provide feedback on fundefi-spec-docs
- [ ] Assign owner for Printora AI-Design staging deployment
- [ ] Set timeline for staging deployment completion
- [ ] Team to share AkunIndo job postings on social media (tag Simon)
- [ ] **URGENT**: Design FunDe.Fi weekly emissions system (distribute to campaigns/projects/vaults)
- [ ] Create detailed documentation for FunDe.Fi emissions mechanics
- [ ] Schedule follow-up with Anjelito to explain emissions system
- [ ] Update fundefi-spec-docs with emission distribution details
- [ ] **Add Polkadot to blockchain evaluation** for FunDe.Fi (6th option alongside ETH/Arbitrum/Optimism/Base/Polygon)
- [ ] Follow up with Josh re tokenised assets tech (waiting for his response)
- [ ] Explore how tokenised assets integrate with ve(3,3) tokenomics
- [ ] Kevin: Continue Stripe sandbox setup for Printora
- [ ] Simon: Follow up with HIC re investment/partnership (Polkadot, tokenised assets)

---

**Prepared by**: Claude Code
**Date Created**: 2025-10-22
