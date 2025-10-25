# Printora Changelog

All notable changes, decisions, and updates to the Printora project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned for MVP (2025-11-01)
- Stripe payment integration
- AI design studio with image generation
- Image upload (file + webcam)
- Text editing with custom styles
- Product mockup preview (4 core products)
- Dual image storage system
- Version control workflow

---

## [0.1.0] - 2025-10-25

### Added - Project Structure & Planning

#### Meeting & Documentation
- Bali Team Meeting held (2025-10-25, 11:23 AM, 72 minutes)
- Established project documentation repository structure
- Created comprehensive ROADMAP.md
- Initialized CHANGELOG.md

#### Technical Decisions
- **Multi-element design flow** combining:
  - AI-generated images
  - User-uploaded photos
  - Custom text prompts
- **UI/UX Design** inspired by Sora and Fiddle Art
  - Left sidebar with prompt input
  - Step-by-step design process
  - Three core input elements
  - Font customization and multi-text support

#### Architecture Decisions
- **Version Control Strategy**
  - Three-branch workflow: dev, staging, main/production
  - Semantic versioning: major.minor.patch
  - Branch protection rules
  - Code review process

- **Image Storage System**
  - Dual storage approach:
    - Preview version with watermarks
    - Print-ready high-resolution version
  - Metadata storage for:
    - Layers (text, images, AI prompts)
    - Positioning (opacity, rotation)
    - Printer instructions
  - Security: Only print-ready files sent to printers

- **Payment Processing**
  - Provider: Stripe
  - Checkout session flow
  - Webhook confirmation
  - Target error rate: < 0.5%

#### Product Strategy
- **Initial Launch**: 4 core popular products
- **Expansion Plan**: Gradual addition based on demand
- **Mockup Strategy**: Prioritize popular templates with search capability
- **Design Reusability**: Enable easy adaptation across product types

#### Marketing Decisions
- **Launch Timeline**: End of next week (2025-11-01)
- **Initial Campaign**: Christmas-themed designs
- **Marketing Start**: First week of November 2025
- **Target Audiences**:
  1. Customers (primary focus for MVP)
  2. Content Creators (future)
  3. Artists (marketplace - Phase 3)
  4. Partners (API integrations - Phase 3)

#### Competitive Differentiation
- Multi-element design combining AI + user content + custom text
- User-friendly step-by-step interface
- Community features (sharing, favorites, competitions)
- Strategic API partnerships with AI platforms

### Technical Specifications

#### MVP Scope (Phase 1)
1. Stripe payment integration
2. Basic AI design studio
3. Image upload (file + webcam)
4. Text editing with style options
5. Preview + print-ready image storage
6. Test product orders
7. Core 4 products
8. Version control workflow

#### Post-MVP (Phase 2)
- Additional products (expand from 4 to 10-15)
- Social features (sharing, favorites)
- Community features (competitions, royalty system)
- Admin dashboard
- Subscription features
- User testing integration

#### Future Phases
- Artist marketplace
- API partnerships (Fiddle Art, Sogni AI)
- International expansion
- Advanced AI features
- Mobile app

### Team Organization

#### GitHub Structure
- **Repositories**:
  - `printora` - Main application (dev team)
  - `printora-marketing` - Marketing automation (dev + marketing)
  - `printora-spec-docs` - Documentation (all team + executives)

- **Projects** (Organization-level):
  - Printora Development - Dev work tracking
  - Printora Operations - Marketing/admin tracking

- **Milestones**:
  - MVP Launch (2025-11-01)
  - Phase 2 (Post-MVP enhancements)

#### Team Roles
- **Eko** (Senior Frontend Dev): UI/UX, image upload, text editing, mockups
- **Kevin** (Backend Dev): Stripe integration, image storage, APIs
- **Yosua** (AI/ML Dev): AI design studio, image generation
- **Nhung** (Operations): Marketing, admin, user testing, fulfillment
- **Thuy** (Executive): Vision, feature feedback, testing, approval
- **Simon** (Executive): Technical direction, review, partnerships, documentation

### Security Considerations
- Abuse prevention strategies discussed
- User sign-up strategy: Tolerate early misuse to gain traction
- Watermarks on preview images to prevent misuse
- Print-ready files secured separately

### Partnership Opportunities
- **Fiddle Art**: AI image generation platform
- **Sogni AI**: Alternative AI platform
- **Strategy**: Commission-based POD integration, shared user base

### User Testing
- **Timeline**: Next 2 weeks
- **Participants**: 10+ users
- **Focus**: UI/UX workflow intuitiveness
- **Goal**: Validate design studio interaction clarity

---

## Process & Workflow Changes

### Meeting Notes Process
- All meetings recorded via Fireflies.ai
- Meeting notes stored in `printora-spec-docs/meetings/transcripts/`
- Action items extracted and converted to GitHub issues
- Standardized meeting note format adopted

### Task Management
- GitHub Issues for all actionable tasks
- Organization-level Projects for coordination
- Labels for type, priority, area
- Milestones for phase tracking
- Clear assignees for every task

### Commit Standards
- Link commits to issues
- Update issue status in commit messages
- Update CHANGELOG.md for significant changes
- Semantic commit messages

---

## Notes

### Key Dates
- Project kickoff: 2025-10-22
- Bali Team Meeting: 2025-10-25
- MVP Launch target: 2025-11-01 (end of next week)
- Marketing start: 2025-11-04 (first week of November)

### Reference Documents
- [Bali Team Meeting Notes](meetings/transcripts/2025-10-25-11am-bali-team-meeting-fireflies.md)
- [ROADMAP.md](ROADMAP.md)
- [GitHub Issues](https://github.com/Printora/printora/issues)

### Next Review
- After MVP launch
- Weekly sprint reviews
- Monthly strategic planning

---

## Version History

- **0.1.0** (2025-10-25) - Project structure, planning, and MVP definition
- **1.0.0** (Planned 2025-11-01) - MVP Launch

---

**Maintained by**: Simon Smaluhn
**Last Updated**: 2025-10-25
