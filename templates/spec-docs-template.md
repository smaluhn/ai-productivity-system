# Project Spec-Docs Template

This template is based on the akunindo-spec-docs structure, designed to create comprehensive, maintainable technical documentation for any project.

## Repository Structure

```
project-spec-docs/
├── README.md                        # Overview and documentation map
├── CLAUDE.md                        # AI assistant rules for consistency
├── .gitignore                       # Standard ignores
├── roadmap/
│   ├── ROADMAP.md                  # Product roadmap (source of truth)
│   ├── CHANGELOG.md                # Roadmap version history
│   └── OPEN-QUESTIONS.md           # Unresolved decisions
├── technical/
│   ├── 01-project-context.md       # Business context and goals
│   ├── 02-architecture-decisions.md # Key technical decisions (ADRs)
│   ├── 03-data-models.md           # Data structures and API contracts
│   ├── 04-project-structure.md     # Code organization
│   ├── 05-user-journeys.md         # User flows and experiences
│   ├── 06-ui-guidelines.md         # Design system and components
│   ├── 07-testing-strategy.md      # Testing approach
│   ├── 08-security-compliance.md   # Security and logging
│   ├── 09-implementation-guide.md  # Developer setup guide
│   ├── 10-deployment-infrastructure.md  # Deployment and hosting
│   └── 11-versioning.md            # Versioning strategy
└── scripts/
    └── check-consistency.js         # Validation script (optional)
```

## Document Templates

### README.md
```markdown
# [Project Name] Documentation

This repository contains all technical documentation for [Project Name], [brief description].

## 📚 Documentation Structure

### Roadmap
- [`ROADMAP.md`](roadmap/ROADMAP.md) - Product roadmap and feature planning
- [`CHANGELOG.md`](roadmap/CHANGELOG.md) - Roadmap version history
- [`OPEN-QUESTIONS.md`](roadmap/OPEN-QUESTIONS.md) - Unresolved decisions

### Technical Documentation
1. [`01-project-context.md`](technical/01-project-context.md) - Business context and goals
2. [`02-architecture-decisions.md`](technical/02-architecture-decisions.md) - Key technical decisions
3. [`03-data-models.md`](technical/03-data-models.md) - Data structures and API contracts
4. [`04-project-structure.md`](technical/04-project-structure.md) - Code organization
5. [`05-user-journeys.md`](technical/05-user-journeys.md) - User flows and experiences
6. [`06-ui-guidelines.md`](technical/06-ui-guidelines.md) - Design system and components
7. [`07-testing-strategy.md`](technical/07-testing-strategy.md) - Testing approach
8. [`08-security-compliance.md`](technical/08-security-compliance.md) - Security and logging
9. [`09-implementation-guide.md`](technical/09-implementation-guide.md) - Developer setup guide
10. [`10-deployment-infrastructure.md`](technical/10-deployment-infrastructure.md) - Deployment and hosting
11. [`11-versioning.md`](technical/11-versioning.md) - Versioning strategy

## 🔄 Workflow

### Making Changes
1. Open in Claude Code: `claude .`
2. Edit documents directly
3. Use Claude Code to ensure consistency
4. Commit changes with clear messages

### Common Commands
\`\`\`bash
# Check consistency (if script exists)
node scripts/check-consistency.js

# View recent changes
git log --oneline -10

# See what changed
git diff
\`\`\`
```

### CLAUDE.md
```markdown
# Claude Code Rules for [Project Name] Documentation

## Project Context
This repository contains all documentation for [Project Name], [brief description and key differentiators].

## When Making Changes

### 1. Roadmap Updates
When the ROADMAP.md is modified:
- Identify ALL documents that need updates
- List specific sections requiring changes
- Ensure consistency across all documents
- Update CHANGELOG.md with the changes

### 2. Cross-Reference Validation
Always check:
- Data models match API documentation
- User journeys align with UI guidelines
- Technical decisions (ADRs) are reflected in implementation guide
- Security requirements are consistent across documents

### 3. Project-Specific Context
Maintain awareness of:
- [Key business requirement 1]
- [Key technical constraint 1]
- [Key user need 1]
- [Key integration point 1]

### 4. Document Standards
Each document should have:
- Version header with roadmap reference
- Clear section structure
- Practical examples where relevant
- No implementation details (only interfaces/contracts)

### 5. Versioning Strategy
**Current Phase**: Documentation Development (v0.9-draft)
- Use `v0.9-draft` for work-in-progress documentation
- Reserve `v1.0` for development-ready, question-resolved state
- CHANGELOG.md uses single consolidated entry per phase
- Version increments only for major milestones, not intermediate work

### 6. Change Protocol
For any modification:
1. Update the document
2. Check related documents
3. Update version/date in header if needed
4. Update CHANGELOG.md for significant architectural changes
5. Keep git commit messages clean and professional

## Common Tasks

### "Update all documents for feature X"
1. Search across all documents for related content
2. List all locations needing updates
3. Make consistent changes
4. Verify no conflicts introduced

### "Check consistency"
1. Verify all documents reference same roadmap version
2. Check that technical terms are used consistently
3. Ensure no contradictions between documents

### "Impact analysis for new feature"
1. Analyze which documents would be affected
2. Specify what sections need updates
3. Identify any new documents needed

## Important Relationships
- Roadmap → All documents (source of truth)
- Data Models ↔ API docs ↔ Testing Strategy
- User Journeys → UI Guidelines
- ADRs → Implementation Guide
- Security → All documents (cross-cutting concern)

## Roadmap Change Management Workflow

### Change Communication Methods
Users can provide roadmap changes in these formats:
- **Direct edit**: Share specific ROADMAP.md changes
- **Change description**: Describe what features/priorities are changing
- **New roadmap section**: Provide new content to add/replace

### Impact Analysis Process
When roadmap changes are provided:
1. **Analyze the changes** - Identify what's new, modified, or removed
2. **Map document impacts** - Use cross-reference matrix to find affected docs
3. **Create update plan** - List all documents needing changes and what sections
4. **Present for approval** - Show full scope before making changes

### Document Update Sequence
1. Update ROADMAP.md with changes
2. Update all technical documents that reference changed features
3. Update version headers in all affected docs (only if major milestone)
4. Update CHANGELOG.md with summary of changes
5. Update README.md if structure/workflow changes
6. Run consistency check to verify everything aligns
7. Commit and push changes

### Cross-Reference Impact Matrix
- **Data model changes** → affect API docs, testing strategy, implementation guide
- **Architecture changes** → affect ADRs, project structure, security docs
- **Feature changes** → affect user journeys, UI guidelines, implementation guide
- **Security changes** → affect all documents (cross-cutting)

### Recommended Change Format
\`\`\`
ROADMAP CHANGES - v0.1.X

Changed:
- [Feature X]: Description of change
- [Priority Y]: New priority/timeline

Added:
- [New Feature Z]: Description

Removed:
- [Feature W]: Reason for removal

Context: Brief explanation of why these changes
\`\`\`
```

### ROADMAP.md Template
```markdown
# [Project Name] Roadmap

**Version:** v0.9-draft
**Last Updated:** [Date]
**Status:** Documentation Development Phase

## Project Vision

[1-2 paragraph description of what this project aims to achieve]

## Target Users

1. **Primary User**: [Description]
2. **Secondary User**: [Description]

## Core Value Propositions

1. [Key value prop 1]
2. [Key value prop 2]
3. [Key value prop 3]

## Development Phases

### Phase 0: Documentation (Current)
**Goal:** Complete technical specifications before development

**Deliverables:**
- [ ] Complete all technical documentation
- [ ] Resolve all open questions
- [ ] Get stakeholder sign-off

### Phase 1: MVP Development
**Timeline:** [Estimate]

**Features:**
1. [Core feature 1]
2. [Core feature 2]
3. [Core feature 3]

**Success Metrics:**
- [Metric 1]
- [Metric 2]

### Phase 2: Beta Release
**Timeline:** [Estimate]

**Features:**
1. [Enhanced feature 1]
2. [Enhanced feature 2]

**Success Metrics:**
- [Metric 1]
- [Metric 2]

### Phase 3: Production Launch
**Timeline:** [Estimate]

**Features:**
1. [Production-ready feature 1]
2. [Production-ready feature 2]

**Success Metrics:**
- [Metric 1]
- [Metric 2]

## Feature Priority Matrix

### Must Have (P0) - MVP Blockers
- [Feature X]: [Brief description]
- [Feature Y]: [Brief description]

### Should Have (P1) - Enhanced Experience
- [Feature A]: [Brief description]
- [Feature B]: [Brief description]

### Nice to Have (P2) - Future Iterations
- [Feature M]: [Brief description]
- [Feature N]: [Brief description]

## Technical Constraints

1. [Constraint 1]
2. [Constraint 2]

## Open Questions

See [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) for unresolved items.

## Dependencies

1. [External dependency 1]
2. [External dependency 2]
```

### Technical Document Template
```markdown
# [Number]-[Document Title]

**Version:** v0.9-draft
**Roadmap Version:** v0.9-draft
**Last Updated:** [Date]

## Overview

[Brief description of what this document covers]

## [Section 1]

[Content]

### Subsection

[Details]

## [Section 2]

[Content]

## Related Documents

- [Link to related doc 1]
- [Link to related doc 2]

## References

- [External reference if applicable]
```

## Key Principles

1. **Roadmap is Source of Truth** - All documents reference and align with ROADMAP.md
2. **Cross-Reference Everything** - Maintain consistency across related docs
3. **Version Carefully** - Don't increment for every change, only major milestones
4. **Context-Aware** - Include project-specific constraints and requirements
5. **Implementation-Agnostic** - Focus on "what" and "why", not "how"
6. **AI-Assisted** - CLAUDE.md ensures consistency when using Claude Code

## Usage

1. Copy this template structure to new repo
2. Customize CLAUDE.md with project-specific context
3. Fill in ROADMAP.md first (source of truth)
4. Create technical documents referencing roadmap
5. Use Claude Code with CLAUDE.md rules for consistency
