# Multi-Project Workspace Integration Setup

This document describes the standardized workspace integration setup used across all projects to enable seamless access and auto-syncing via the productivity system.

## Overview

Each project follows the same pattern:
1. **Master Location**: `/git/productivity-system/projects/PROJECT-NAME-project/`
2. **Symlink Location**: `/git/PROJECT-NAME/PROJECT-NAME-project/` 
3. **Auto-sync**: Via productivity-system's GitHub integration

## Projects Setup

### ✅ Completed Projects

| Project | Master Location | Symlink Location |
|---------|----------------|------------------|
| **FunDeFi** | `/productivity-system/projects/fundefi-project/` | `/fundefi/fundefi-project/` |
| **Akunindo** | `/productivity-system/projects/akunindo-project/` | `/akunindo/akunindo-project/` |
| **Affiliate** | `/productivity-system/projects/affiliate-project/` | `/affiliate/affiliate-project/` |
| **Mindfool** | `/productivity-system/projects/mindfool-project/` | `/mindfool/mindfool-project/` |
| **Printora** | `/productivity-system/projects/printora-project/` | `/printora/printora-project/` |
| **Favors** | `/productivity-system/projects/favors-project/` | `/favors/favors-project/` |
| **Favos** | `/productivity-system/projects/favos-project/` | `/favos/favos-project/` |

### Folder Structure Overview

```
/Users/simon/git/
├── productivity-system/
│   └── projects/                    # MASTER LOCATIONS (auto-synced)
│       ├── fundefi-project/        # ✅ Complete
│       ├── akunindo-project/       # ✅ Ready
│       ├── affiliate-project/      # ✅ Ready  
│       ├── mindfool-project/       # ✅ Ready
│       ├── printora-project/       # ✅ Ready
│       ├── favors-project/         # ✅ Ready
│       └── favos-project/          # ✅ Ready
├── fundefi/
│   └── fundefi-project/            # → symlink to productivity-system
├── akunindo/
│   └── akunindo-project/           # → symlink to productivity-system
├── affiliate/
│   └── affiliate-project/          # → symlink to productivity-system
├── mindfool/
│   └── mindfool-project/           # → symlink to productivity-system
├── printora/
│   └── printora-project/           # → symlink to productivity-system
├── favors/
│   └── favors-project/             # → symlink to productivity-system
└── favos/
    └── favos-project/              # → symlink to productivity-system
```

## Setup Commands

### Manual Symlink Creation

If you need to create or recreate symlinks manually:

```bash
# Akunindo
cd /Users/simon/git/akunindo
ln -sf "/Users/simon/git/productivity-system/projects/akunindo-project" akunindo-project

# Affiliate  
cd /Users/simon/git/affiliate
ln -sf "/Users/simon/git/productivity-system/projects/affiliate-project" affiliate-project

# Mindfool
cd /Users/simon/git/mindfool
ln -sf "/Users/simon/git/productivity-system/projects/mindfool-project" mindfool-project

# Printora
cd /Users/simon/git/printora
ln -sf "/Users/simon/git/productivity-system/projects/printora-project" printora-project

# Favors
cd /Users/simon/git/favors
ln -sf "/Users/simon/git/productivity-system/projects/favors-project" favors-project

# Favos
cd /Users/simon/git/favos
ln -sf "/Users/simon/git/productivity-system/projects/favos-project" favos-project
```

### Verification Commands

```bash
# Check symlink status
ls -la /Users/simon/git/*/PROJECT-NAME-project

# Verify access from both locations
ls /Users/simon/git/productivity-system/projects/PROJECT-NAME-project/
ls /Users/simon/git/PROJECT-NAME/PROJECT-NAME-project/
```

## Benefits

### ✅ Centralized Management
- All project materials in one location (`productivity-system/projects/`)
- Single Git repository tracks all project files
- Consistent backup and version control

### ✅ Seamless Access
- Work on projects from their natural context
- No need to switch between repositories
- Files instantly available in both locations

### ✅ Auto-Sync
- All changes automatically committed to productivity-system
- GitHub integration provides cloud backup
- Version history for all project materials

### ✅ Privacy Control
- Project-specific `.gitignore` excludes symlinked folders
- Private materials never committed to public repositories
- Controlled access via productivity-system permissions

## Usage Patterns

### For Daily Work
```bash
# Work on FunDeFi materials
cd /Users/simon/git/fundefi/fundefi-project
# OR
cd /Users/simon/git/productivity-system/projects/fundefi-project
```

### For Cross-Project Planning
```bash
# View all project materials
cd /Users/simon/git/productivity-system/projects
ls -la  # See all projects at once
```

### For Backup Verification
```bash
# Check git status across all projects
cd /Users/simon/git/productivity-system
git status  # Should show changes from all projects
```

## Project-Specific Folders

Each project folder should contain:

### Standard Files
- `README.md` - Project overview and current status
- `TASKS-AND-DECISIONS.md` - Task tracking and decision log
- `BUDGET.md` - Financial planning and budget tracking
- `WORKSPACE-SETUP.md` - Technical setup documentation

### Team Folders
- `meetings/` - Meeting agendas, notes, and follow-ups
- `planning/` - Strategic planning documents
- `partnerships/` - Collaboration and partnership materials

### Example: FunDeFi Structure
```
fundefi-project/
├── README.md
├── TASKS-AND-DECISIONS.md
├── BUDGET.md
├── PRIVATE-FUNDRAISING-STRATEGY.md
├── METADAO-MECHANICS.md
├── POST-TGE-OTC-STRATEGY.md
├── WEBSITE-HOW-IT-WORKS.md
├── WORKSPACE-SETUP.md
└── werner/
    ├── WERNER-VERMAAK-CMC-RESEARCH.md
    └── MEETING-AGENDA-2025-10-29.md
```

## Troubleshooting

### Broken Symlinks
```bash
# Remove broken symlink
rm /Users/simon/git/PROJECT-NAME/PROJECT-NAME-project

# Recreate symlink
cd /Users/simon/git/PROJECT-NAME
ln -sf "/Users/simon/git/productivity-system/projects/PROJECT-NAME-project" PROJECT-NAME-project
```

### Permission Issues
```bash
# Fix permissions
chmod -R 755 /Users/simon/git/productivity-system/projects/PROJECT-NAME-project
```

### Git Issues
```bash
# If files not being tracked
cd /Users/simon/git/productivity-system
git add projects/PROJECT-NAME-project/
git status
```

## Adding New Projects

### Step 1: Create Master Folder
```bash
mkdir /Users/simon/git/productivity-system/projects/NEW-PROJECT-project
```

### Step 2: Create Symlink
```bash
cd /Users/simon/git/NEW-PROJECT
ln -sf "/Users/simon/git/productivity-system/projects/NEW-PROJECT-project" NEW-PROJECT-project
```

### Step 3: Initialize Documentation
```bash
cd /Users/simon/git/productivity-system/projects/NEW-PROJECT-project
cp ../fundefi-project/WORKSPACE-SETUP.md .
# Edit WORKSPACE-SETUP.md for new project
```

### Step 4: Update Project .gitignore
```bash
# Add to /Users/simon/git/NEW-PROJECT/.gitignore
NEW-PROJECT-project/
```

---

**Setup Date**: October 29, 2025  
**Status**: Complete for 5 projects  
**Maintenance**: Check symlinks monthly  
**Owner**: Simon (Productivity System)