# Bali Team Meeting - October 23, 2025

**Date**: 2025-10-23 (Wednesday, 2:00 PM)
**Duration**: ~90 minutes
**Attendees**: Simon, Kevin, Eko, Yosua, (Anjelito for FunDe.Fi)

---

## Agenda

### Misc / Infrastructure
- **GitHub Projects**: Setup and overview for Printora, FunDe.Fi, and other projects
  - How team will use boards for task tracking
  - Daily standup via GitHub Projects
  - Integration with spec-docs

---

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

---

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

---

### 3. Review FunDe.Fi Spec-Docs Repository
- **Repository**: https://github.com/zee-mon/fundefi-spec-docs
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

---

## Printora Project

### Printora AI-Design: Deploy to Staging Server (Kevin)
- **Objective**: Make AI-Design feature work on staging server online
- **Current Status**: Frontend MVP ~80% complete
- **Assigned to**: Kevin
- **Discussion Points**:
  - Current deployment status
  - Any blockers or technical issues
  - Testing plan for staging environment
  - Timeline for completion

### Stripe Sandbox Setup for Staging/Dev (Kevin)
- **Status**: Signed up for Stripe account, Kevin given access
- **Assigned to**: Kevin
- **Tasks**:
  - Work on sandbox Stripe for Printora staging
  - Testing sandbox integration
  - Prepare for live Stripe setup
- **Note**: Contact Stripe directly for setup assistance if needed

### Sign Up to Fulfillment Services (Kevin)
- **Assigned to**: Kevin (admin@printora.ai)
- **Options to evaluate**: Printful, Printify, or Gelato
- **Timeline**: POD decision needed by November 1
- **Tasks**:
  - Sign up to fulfillment service
  - Order sample products from all three (if multiple)
  - Compare quality, shipping time, pricing
  - Prepare recommendation

### Create Social Media Presence (Kevin)
- **Assigned to**: Kevin (admin@printora.ai)
- **Channels**: Twitter, Instagram, TikTok (at minimum)
- **Purpose**: Prepare for beta launch
- **Content**: Design examples, creator guidelines, early announcements

---

## AkunIndo Project

### Optimize Mobile Layout (Kevin)
- **Assigned to**: Kevin
- **Current Status**: Layout improvements needed for mobile users
- **Discussion Points**:
  - Current mobile UX issues
  - Priority fixes
  - Timeline for completion

### AkunIndo Hiring Discussion
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

---

## FunDe.Fi Project

### FunDe.Fi Mechanics Clarification
- **Critical Question**: Weekly emissions and launchpad adaptation
- **Key Discussion**:
  - **How to adapt DEX emission model to Launchpad model?**
  - Weekly emissions to campaigns/projects/token vaults (Anjelito's question)
  - What percentage distribution?
  - Integration with ve(3,3) tokenomics

- **Multi-Chain Consideration & Tokenised Assets**:
  - HIC invested $250K in joinn.io (5% at $10M valuation)
  - HIC bullish on Polkadot for tokenised assets
  - **DECISION**: Add Polkadot to blockchain evaluation (6th option)
  - Options: Ethereum/Arbitrum/Optimism/Base/Polygon/**Polkadot**

  - **Tokenised Assets Tech** (Josh):
    - Josh already developed the tech for tokenised assets
    - Waiting for Josh to come back with update
    - Could be critical differentiator for FunDe.Fi
    - How to integrate with ve(3,3) tokenomics?

- **Action Items**:
  - Discuss weekly emissions mechanics (DEX → Launchpad adaptation)
  - Create clear documentation of emission system
  - Schedule follow-up with Anjelito to explain system
  - Update spec-docs with detailed emission mechanics
  - **Add Polkadot to blockchain evaluation** (6th option)
  - Follow up with Josh re tokenised assets tech status
  - Explore tokenised assets integration with ve(3,3) model

---

## Infrastructure / Admin Tasks

### Favourse.com Migration & Setup (Kevin)
- **Assigned to**: Kevin
- **Current status**: Need to migrate from current host
- **Tasks**:
  - Migrate domain and services
  - Update DNS if needed
  - Verify everything works

### Netcup.de - Migrate and Cancel (Kevin)
- **Assigned to**: Kevin
- **Action**: Migrate services away, then cancel account
- **Related to**: Favourse.com setup

### Bluehost.com - Migrate and Cancel (Kevin)
- **Assigned to**: Kevin
- **Action**: Migrate services away, then cancel account
- **Related to**: Favourse.com setup

---

## Action Items Summary

### Immediate (This Week)
- [ ] **Kevin**: Printora AI-Design staging deployment (start, timeline)
- [ ] **Kevin**: Stripe sandbox setup for Printora
- [ ] **Kevin**: Sign up to POD fulfillment service (Printful/Printify/Gelato)
- [ ] **Kevin**: Create Printora social media accounts
- [ ] **Kevin**: Optimize AkunIndo mobile layout
- [ ] **Kevin**: Migrate favourse.com, netcup.de, bluehost.com

### FunDe.Fi (Critical)
- [ ] Discuss how to adapt DEX emissions model to Launchpad
- [ ] **URGENT**: Design weekly emissions system (campaigns/projects/vaults distribution)
- [ ] Create detailed documentation for FunDe.Fi emissions mechanics
- [ ] Schedule follow-up with Anjelito to explain system
- [ ] Update fundefi-spec-docs with emission distribution details
- [ ] **Add Polkadot to blockchain evaluation** (6th option alongside ETH/Arbitrum/Optimism/Base/Polygon)
- [ ] Follow up with Josh re tokenised assets tech (waiting for his response)
- [ ] Explore how tokenised assets integrate with ve(3,3) tokenomics

### AkunIndo
- [ ] Team to share AkunIndo job postings on social media (tag Simon)
- [ ] Discuss hiring strategy for 2-3 positions

### Admin
- [ ] Review GitHub Projects boards for Printora, FunDe.Fi, FavosApp
- [ ] Review spec-docs completeness

---

## Notes

### Strategic Opportunities
- **Josh's tokenised assets tech** + **HIC's Polkadot interest** = unique positioning for FunDe.Fi
- Could differentiate from competing launchpads
- Polkadot multi-chain reduces platform risk

### Dependencies
- **Anjelito**: Waiting on weekly emissions clarification
- **Josh**: Waiting on tokenised assets tech update
- **Kevin**: Heavy load - multiple projects (Printora, AkunIndo, infrastructure)

### Timeline Critical Dates
- **November 1**: Printora POD provider decision
- **Unknown**: Josh's tokenised assets tech response
- **Unknown**: HIC follow-up for investment/partnership

---

**Prepared by**: Claude Code
**Date Created**: 2025-10-22
**Last Updated**: 2025-10-23

