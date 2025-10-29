# FunDeFi Project - Workspace Integration Setup

This document describes the workspace integration setup that allows FunDeFi project materials to be accessible from both the project workspace and the productivity system, with automatic syncing via Git.

## Overview

The FunDeFi project has been set up with a dual-workspace system:
1. **Main Development**: `/git/fundefi/` - Contains all code repositories
2. **Productivity System**: `/git/productivity-system/` - Personal productivity and project management
3. **Integration Point**: This folder serves as the bridge between both systems

## Folder Structure

```
/Users/simon/git/
├── fundefi/                          # Main FunDeFi workspace
│   ├── fundefi/                      # Main Next.js application
│   ├── fundefi-blockchain/           # Smart contracts
│   ├── fundefi-spec-docs/           # Public documentation (no private folder)
│   └── fundefi-project/             # → SYMLINK to productivity-system
└── productivity-system/             # Personal productivity system
    └── projects/
        └── fundefi-project/         # MASTER LOCATION - All files here
```

## Current Setup (Phase 1 - Complete)

### What Was Done:
1. **Created** `/git/productivity-system/projects/fundefi-project/` folder (master location)
2. **Moved** all private strategy documents from `fundefi-spec-docs/private/` to productivity-system
3. **Created single symlink**: `/git/fundefi/fundefi-project` → `/git/productivity-system/projects/fundefi-project`
4. **Removed** private folder from fundefi-spec-docs completely
5. **Organized** Werner Vermaak materials in `werner/` subfolder

### Files in This Folder:
- `BUDGET.md` - Project budget and financial planning
- `DECISION-MARKETS-FUTARCHY.md` - Decision market mechanics
- `METADAO-MECHANICS.md` - DAO governance structure  
- `POST-TGE-OTC-STRATEGY.md` - Post-token generation strategies
- `PRIVATE-FUNDRAISING-STRATEGY.md` - Fundraising approach and targets
- `TASKS-AND-DECISIONS.md` - Project task tracking and decision log
- `WEBSITE-HOW-IT-WORKS.md` - Website functionality documentation
- `werner/` - Werner Vermaak (CMC) collaboration materials
  - `WERNER-VERMAAK-CMC-RESEARCH.md` - Background research
  - `MEETING-AGENDA-2025-10-29.md` - Strategic partnership meeting agenda

### Symlink Details:
```bash
# Single symlink (main folder sync):
/Users/simon/git/fundefi/fundefi-project
# Points to:
/Users/simon/git/productivity-system/projects/fundefi-project

# Command used:
cd /Users/simon/git/fundefi
ln -s "/Users/simon/git/productivity-system/projects/fundefi-project" fundefi-project
```

## Future Setup (Phase 2 - Complete! ✅)

### ✅ Productivity System Integration Complete:
1. **✅ Moved** this folder to `/git/productivity-system/projects/fundefi-project/`
2. **✅ Created symlink** from `/git/fundefi/fundefi-project` to productivity-system location
3. **✅ Enabled auto-sync** via productivity-system's GitHub integration

### Benefits Now Active:
- ✅ All FunDeFi materials accessible from both workspaces
- ✅ Auto-synced to GitHub via productivity-system
- ✅ Version controlled and backed up
- ✅ Private materials stay out of public repositories
- ✅ Seamless switching between contexts

## Git Integration

### Current Status:
- **fundefi-spec-docs**: `.gitignore` excludes `private/` folder ✅
- **fundefi-project**: Currently not tracked in any Git repository
- **productivity-system**: Ready to track fundefi-project when moved there

### Access Patterns:
```bash
# From FunDeFi project context:
cd /Users/simon/git/fundefi/fundefi-project

# From productivity system (MASTER LOCATION):
cd /Users/simon/git/productivity-system/projects/fundefi-project

# Both paths access the same files via symlink
```

## Technical Notes

### Symlink Verification:
```bash
# Check symlink status:
ls -la /Users/simon/git/fundefi/fundefi-spec-docs/private

# Should show:
# private -> ../fundefi-project
```

### File Accessibility:
All files are accessible via both paths due to the symlink:
- `/productivity-system/projects/fundefi-project/BUDGET.md` (master)
- `/fundefi/fundefi-project/BUDGET.md` (symlink)

Both paths reference the same physical file.

## Development Server Setup

### Node.js Installation Issues Resolved:
During setup, encountered Node.js linking issues that were resolved:

```bash
# Issue: Node.js installed but not linked
brew link --overwrite node

# Permission fixes required:
sudo chown -R $(whoami) /usr/local/include/node
sudo chown -R $(whoami) /usr/local/lib/node_modules

# Final verification:
node --version  # v24.10.0
npm --version   # 11.6.0
```

### Development Server:
```bash
cd /Users/simon/git/fundefi/fundefi
npm run dev
# Runs on: http://localhost:3001 (port 3000 was in use)
```

## Next Steps

1. **Complete Phase 2**: Move to productivity-system for auto-sync
2. **Test Integration**: Ensure seamless access from both contexts  
3. **Backup Strategy**: Verify Git tracking in productivity-system
4. **Document Workflows**: Create usage guides for team members

## Troubleshooting

### Symlink Issues:
```bash
# If symlink breaks, recreate:
cd /Users/simon/git/fundefi/fundefi-spec-docs
rm private  # Remove broken symlink
ln -s "../fundefi-project" private  # Recreate
```

### Access Issues:
```bash
# Check file permissions:
ls -la /Users/simon/git/fundefi/fundefi-project/

# Fix if needed:
chmod -R 755 /Users/simon/git/fundefi/fundefi-project/
```

---
*Setup completed: October 29, 2025*  
*Document version: 1.0*  
*Status: Phase 1 Complete*