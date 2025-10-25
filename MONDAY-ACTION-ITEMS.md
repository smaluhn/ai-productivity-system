# Monday Action Items - 2025-10-28

## 🔴 CRITICAL: Get GitHub Usernames

**Need from team members**:
1. **Nhung**: GitHub username → Add to repos
2. **Thuy**: GitHub username → Add to repos

**Once you have them, run**:
```bash
# For Thuy (Admin to marketing/docs, Read to printora)
gh api repos/Printora/printora/collaborators/[thuy-username] -X PUT -f permission=pull
gh api repos/Printora/printora-marketing/collaborators/[thuy-username] -X PUT -f permission=admin
gh api repos/Printora/printora-spec-docs/collaborators/[thuy-username] -X PUT -f permission=admin

# For Nhung (Write to marketing/docs, Read to printora)
gh api repos/Printora/printora/collaborators/[nhung-username] -X PUT -f permission=pull
gh api repos/Printora/printora-marketing/collaborators/[nhung-username] -X PUT -f permission=push
gh api repos/Printora/printora-spec-docs/collaborators/[nhung-username] -X PUT -f permission=push
```

## 📋 GitHub Projects Cleanup

### Current Projects (From Screenshots)
1. ✅ **Printora Development** - Keep this one (already has issues)
2. ❌ **printora-development** - Delete (duplicate, lowercase)
3. ❌ **printora** - Delete (too generic)
4. ❓ **@zee-mon's untitled project** - Check first, then delete

### Actions Needed

#### 1. Audit Existing Issues
Check what's in each project:
- Go to each project
- Note which issues are there
- Check for duplicates
- Export/save anything unique

#### 2. Clean Up
- Move unique issues from duplicates to "Printora Development"
- Delete: printora-development, printora
- Ask Kevin about @zee-mon's project (move his issues first)

#### 3. Create "Printora Operations"
- Go to https://github.com/orgs/Printora/projects
- Click "New project"
- Name: "Printora Operations"
- Template: Table or Board
- Columns: Backlog, To Do, In Progress, Review, Done

#### 4. Link Repositories

**Printora Development**:
- Link: Printora/printora
- Link: Printora/printora-spec-docs (technical docs only)

**Printora Operations**:
- Link: Printora/printora-marketing
- Link: Printora/printora-spec-docs (business docs)

#### 5. Configure Team Access

**Printora Development**:
- Add members: mrfavi, zee-mon, yosuatriantara, smaluhn
- Role: Can edit

**Printora Operations**:
- Add members: [nhung-username], smaluhn, [thuy-username]
- Role: Can edit

## 📁 Upload to printora-spec-docs

Files ready in `/Users/simon/git/simon/temp/`:

1. **Meeting Notes**
   - Source: `2025-10-25-11am-bali-team-meeting-fireflies.md`
   - Destination: `meetings/transcripts/`

2. **ROADMAP.md**
   - Source: `printora-ROADMAP.md`
   - Destination: Root of repo

3. **CHANGELOG.md**
   - Source: `printora-CHANGELOG.md`
   - Destination: Root of repo

**How to upload**:
Option A - Via GitHub Web:
1. Go to https://github.com/Printora/printora-spec-docs
2. Create folders if needed
3. Upload files

Option B - Via Git (if you clone locally):
```bash
cd /path/to/printora-spec-docs
mkdir -p meetings/transcripts
cp /Users/simon/git/simon/temp/2025-10-25-11am-bali-team-meeting-fireflies.md meetings/transcripts/
cp /Users/simon/git/simon/temp/printora-ROADMAP.md ./ROADMAP.md
cp /Users/simon/git/simon/temp/printora-CHANGELOG.md ./CHANGELOG.md
git add .
git commit -m "Add meeting notes, ROADMAP, and CHANGELOG

- Bali team meeting Oct 25 (72 min)
- Complete roadmap with 4 phases
- Initial changelog with all decisions

From AI Productivity System workflow"
git push
```

## 🎯 Team Standup Agenda

**Topics to cover**:

1. **New Workflow Introduction** (10 min)
   - Explain GitHub Projects vs Issues
   - Show project boards
   - Demonstrate workflow

2. **Issue Assignments Review** (10 min)
   - Each person reviews their assigned issues
   - Questions about tasks
   - Clarify deadlines

3. **MVP Timeline** (5 min)
   - Confirm end of next week deadline
   - Identify any blockers
   - Adjust if needed

4. **Project Access** (5 min)
   - Ensure everyone can access their project
   - Test creating/updating issues
   - Show how to move cards

## 📢 Social Media

**Ready to post** (optional):
- Twitter: `/Users/simon/git/simon/content/social-media/twitter/posts/2025-10-26-ai-productivity-system-launch.md`
- LinkedIn: `/Users/simon/git/simon/content/social-media/linkedin/posts/2025-10-26-ai-productivity-system.md`
- Blog: `/Users/simon/git/simon/content/blog/drafts/2025-10-26-how-i-built-ai-productivity-system.md`

**Note**: MCP integration for auto-posting coming later

## ✅ Completed This Weekend

- [x] AI Productivity System pushed to GitHub (https://github.com/smaluhn/ai-productivity-system)
- [x] 20 Printora issues created with assignments
- [x] Labels and milestones configured
- [x] ROADMAP and CHANGELOG created
- [x] Workflow documentation complete
- [x] Social media content drafted

## 📊 Quick Reference

**Printora Repos**:
- https://github.com/Printora/printora
- https://github.com/Printora/printora-marketing
- https://github.com/Printora/printora-spec-docs

**Issues Summary**:
- 13 issues in printora (dev work)
- 3 issues in printora-marketing
- 4 issues in printora-spec-docs
- Total: 20 issues across MVP and Phase 2

**Team Assignments**:
- Eko: 8 tasks (frontend, version control lead)
- Kevin: 5 tasks (backend, payment, storage)
- Yosua: 2 tasks (AI/ML)
- Nhung: 2 tasks (marketing, user testing)
- Simon: 5 tasks (docs, setup, partnerships)

**Milestones**:
- MVP Launch: Nov 1, 2025
- Phase 2: TBD post-MVP

## 🚀 Success Metrics

By end of Monday, you should have:
- [  ] Nhung and Thuy added to repos
- [  ] Clean project structure (2 projects total)
- [  ] All 20 issues visible in appropriate projects
- [  ] Team understands new workflow
- [  ] Documentation uploaded to spec-docs
- [  ] Everyone knows their tasks for the week

**Time estimate**: 1-2 hours to complete all Monday actions

---

**Review this file Monday morning before team standup!** 📅
