# Spec-Docs Megaprompt

Use this prompt to generate complete technical documentation for any project using Claude Code.

## Usage

1. Copy the prompt below
2. Replace `[PLACEHOLDERS]` with project-specific information
3. Run in Claude Code in a new repository directory
4. Review and refine the generated documentation

---

## THE MEGAPROMPT

```
I need you to create comprehensive technical documentation for my project following the spec-docs template structure.

# Project Information

**Project Name:** [e.g., FundeFi, Printora]
**Type:** [e.g., Web3 DeFi Platform, Print-on-Demand Platform, Mobile App]
**Target Platform:** [e.g., Web App, Mobile (iOS/Android), Desktop]

**Brief Description:**
[2-3 sentences describing what the project does and its core value proposition]

**Target Users:**
1. [Primary user type and their needs]
2. [Secondary user type and their needs]

**Core Features (MVP):**
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]
4. [Feature 4]
5. [Feature 5]

**Technical Stack:**
- Frontend: [e.g., React Native, Next.js, Flutter]
- Backend: [e.g., Node.js, Python/Django, Go]
- Database: [e.g., PostgreSQL, MongoDB, Firebase]
- Infrastructure: [e.g., AWS, Vercel, Self-hosted]
- Key Integrations: [e.g., Stripe, Web3 wallets, APIs]

**Key Constraints:**
- [Business constraint 1, e.g., Must comply with local regulations]
- [Technical constraint 1, e.g., Must work offline]
- [Budget constraint 1, e.g., Keep infra costs under $X/month]

**Unique Context:**
[Any special considerations: regulatory requirements, local market needs, specific user behaviors, competitive advantages]

# Task

Create a complete spec-docs repository with the following structure:

\`\`\`
project-spec-docs/
├── README.md
├── CLAUDE.md
├── .gitignore
├── roadmap/
│   ├── ROADMAP.md
│   ├── CHANGELOG.md
│   └── OPEN-QUESTIONS.md
└── technical/
    ├── 01-project-context.md
    ├── 02-architecture-decisions.md
    ├── 03-data-models.md
    ├── 04-project-structure.md
    ├── 05-user-journeys.md
    ├── 06-ui-guidelines.md
    ├── 07-testing-strategy.md
    ├── 08-security-compliance.md
    ├── 09-implementation-guide.md
    ├── 10-deployment-infrastructure.md
    └── 11-versioning.md
\`\`\`

# Requirements

1. **ROADMAP.md** should be comprehensive with:
   - Clear vision statement
   - Phased development plan (Phase 0: Docs → Phase 1: MVP → Phase 2: Beta → Phase 3: Production)
   - Feature priority matrix (P0/P1/P2)
   - Success metrics for each phase
   - Technical constraints
   - Dependencies

2. **CLAUDE.md** should include:
   - Project-specific context and constraints
   - Cross-reference validation rules
   - Change management workflow
   - Document update protocols

3. **Technical Documents** should cover:
   - **01-project-context.md**: Market analysis, user research, business goals
   - **02-architecture-decisions.md**: Key technical choices with rationale (ADR format)
   - **03-data-models.md**: Database schemas, API contracts, data flow
   - **04-project-structure.md**: Code organization, module structure, file naming
   - **05-user-journeys.md**: User flows from entry to goal completion
   - **06-ui-guidelines.md**: Design system, component library, UX patterns
   - **07-testing-strategy.md**: Unit, integration, E2E testing approach
   - **08-security-compliance.md**: Auth, data protection, logging, compliance
   - **09-implementation-guide.md**: Dev environment setup, commands, workflows
   - **10-deployment-infrastructure.md**: Hosting, CI/CD, monitoring, scaling
   - **11-versioning.md**: Semantic versioning for app, API, database migrations

4. **OPEN-QUESTIONS.md** should list:
   - Unresolved technical decisions
   - Business questions needing stakeholder input
   - UX research questions
   - Integration unknowns

5. **.gitignore** should include:
   - Common development files
   - OS-specific files
   - IDE files

# Output Format

For each file:
1. Start with clear file path
2. Use proper markdown formatting
3. Include version headers (v0.9-draft)
4. Reference related documents
5. Use concrete examples where helpful
6. Keep it practical and actionable

# Style Guidelines

- **Be specific**: Don't say "authentication system", say "JWT-based authentication with refresh tokens, 7-day expiry"
- **Be practical**: Include real examples, not just theory
- **Be consistent**: Use same terminology across all docs
- **Be complete**: Cover all aspects, but keep each section focused
- **Think ahead**: Consider Phase 2 and 3 while documenting Phase 1

# Questions to Consider

As you generate the documentation, think through:
- What problems does this solve?
- Who are the users and what do they need?
- What are the technical trade-offs?
- How will this scale?
- What could go wrong?
- How do we measure success?
- What are the dependencies?
- What's the migration path?

# Start Here

Please begin by:
1. Analyzing the project information provided
2. Creating README.md first (overview of the structure)
3. Creating ROADMAP.md (source of truth)
4. Creating all technical documents in order
5. Creating CLAUDE.md (AI assistant rules)
6. Creating OPEN-QUESTIONS.md (listing unknowns)
7. Creating .gitignore

After creating all files, provide a summary of:
- Key architectural decisions made
- Main open questions that need stakeholder input
- Recommended next steps

Let's create world-class documentation!
\`\`\`

---

## Example: Quick Project Brief for FundeFi

```
**Project Name:** FundeFi
**Type:** Web3 DeFi Crowdfunding Platform
**Target Platform:** Web App (Desktop + Mobile Responsive)

**Brief Description:**
FundeFi is a decentralized crowdfunding platform built on Ethereum that allows creators to launch funding campaigns with tokenized rewards. Backers receive ERC-20 tokens representing their contribution, which can be traded or used for governance. Smart contracts ensure trustless fund management and automated reward distribution.

**Target Users:**
1. Creators: Entrepreneurs, artists, and developers looking for decentralized funding without intermediaries
2. Backers: Crypto-native users who want to support projects and receive tradeable tokens

**Core Features (MVP):**
1. Wallet Connection (MetaMask, WalletConnect)
2. Campaign Creation with Smart Contract Deployment
3. Token-based Backing (ETH contributions → ERC-20 tokens)
4. Campaign Discovery and Search
5. Basic Dashboard for Campaign Creators

**Technical Stack:**
- Frontend: Next.js 14, TypeScript, TailwindCSS, Wagmi/Viem
- Smart Contracts: Solidity 0.8.x, Hardhat, OpenZeppelin
- Backend: Next.js API Routes, tRPC
- Database: PostgreSQL (Supabase)
- Infrastructure: Vercel (Frontend), Alchemy (RPC), IPFS (metadata)
- Key Integrations: Ethereum mainnet, ENS, The Graph

**Key Constraints:**
- Must support mainnet and test networks (Sepolia)
- Gas optimization critical (users pay fees)
- IPFS for decentralized campaign metadata storage
- Must handle wallet disconnections gracefully

**Unique Context:**
FundeFi targets Web3-native users familiar with DeFi concepts. No fiat payment support in MVP - only crypto. Smart contract security is paramount. Campaign tokens should be compatible with DEXes for liquidity.
```

This information would generate a complete, production-ready spec-docs repository for FundeFi.

---

## Tips for Success

1. **Be detailed in project info** - More context = better documentation
2. **List real features** - Specific features generate better technical docs
3. **Include constraints** - These shape architectural decisions
4. **Mention integrations** - Critical for data model and API docs
5. **Define success metrics** - Helps with roadmap and testing strategy

## Customization After Generation

After Claude generates the docs, you may want to:
1. Add specific user research findings
2. Include competitive analysis
3. Add wireframes/mockups to UI guidelines
4. Expand testing strategy with specific test cases
5. Add deployment runbooks
6. Include cost estimates for infrastructure

## Maintenance

Once generated, maintain docs by:
1. Opening in Claude Code: `claude .`
2. Using CLAUDE.md rules for consistency
3. Updating ROADMAP.md when priorities change
4. Letting Claude propagate changes across related docs
5. Keeping CHANGELOG.md updated

---

**Template Version:** 1.0
**Based on:** akunindo-spec-docs structure
**Last Updated:** 2025-10-22
