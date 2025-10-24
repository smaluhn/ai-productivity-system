# Obsidian Mobile GitHub Sync Setup

**Status:** Needs Configuration
**Created:** 2025-10-24
**Priority:** Medium

---

## Issue

Obsidian mobile app GitHub connection not working smoothly yet.

## Tasks

- [ ] Update GitHub username in Obsidian mobile settings (from `sudosimonglitch` to `smaluhn`)
- [ ] Verify GitHub personal access token is valid for mobile
- [ ] Test sync from mobile to `smaluhn/productivity-system` repository
- [ ] Verify pull/push operations work on mobile
- [ ] Document final working configuration

---

## Repository Details

**Repository:** https://github.com/smaluhn/productivity-system
**Branch:** main
**Access:** smaluhn has admin access

---

## GitHub Username Change

**Old username:** sudosimonglitch
**New username:** smaluhn

All organization invitations accepted for smaluhn:
- ✅ DiverseProjects (admin)
- ✅ FavosApp (admin)
- ✅ favourse (admin)
- ✅ Printora (admin)
- ✅ FUNDEdotFI (admin)
- ✅ Favorsid (admin)

---

## Configuration Steps (To Complete)

### Step 1: Create GitHub Personal Access Token (smaluhn)
1. ✅ Browser opened to: https://github.com/settings/tokens/new
2. Login as: **smaluhn**
3. Token settings:
   - **Name:** "Obsidian Git Plugin - Mobile & Desktop"
   - **Expiration:** No expiration (or 1 year)
   - **Scopes:**
     - ✓ `repo` (Full control of private repositories)
     - ✓ `workflow` (Update GitHub Action workflows)
4. Click **"Generate token"**
5. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
6. Save in 1Password: "GitHub PAT - smaluhn - Obsidian"

### Step 2: Configure Obsidian Desktop
1. Open Obsidian → Settings → Community Plugins → Git
2. **Authentication:**
   - Username: `smaluhn`
   - Personal Access Token: [paste token from Step 1]
3. **Repository:**
   - Remote: `https://github.com/smaluhn/productivity-system.git`
   - Branch: `main`
4. Test pull operation
5. Test push operation

### Step 3: Configure Obsidian Mobile
1. Open Obsidian mobile app
2. Go to Settings → Community Plugins → Git
3. **Authentication:**
   - Username: `smaluhn` (change from `sudosimonglitch`)
   - Personal Access Token: [paste token from Step 1]
4. **Repository:**
   - Remote: `https://github.com/smaluhn/productivity-system.git`
   - Branch: `main`
5. Test pull operation
6. Test push operation
7. Enable auto-sync if working

### Step 4: Verify Auto-Sync
1. Make a change on desktop → push
2. Pull on mobile → verify change appears
3. Make a change on mobile → push
4. Pull on desktop → verify change appears
5. Enable automatic sync on both devices

---

## Troubleshooting

If sync still doesn't work:
- Check personal access token has correct scopes (repo, workflow)
- Verify mobile has network connectivity
- Check if 2FA is interfering
- Try manual pull/push first before enabling auto-sync
- Consider using SSH keys instead of HTTPS

---

## Notes

- Desktop sync working perfectly
- Mobile sync configuration pending
- All changes pushed from desktop are available in remote
- smaluhn account has full admin access to repository

---

## Auto-Sync Setup (Desktop/VS Code)

**Automatic sync every 15 minutes** is configured using launchd on macOS:

- **Script:** `/Users/simon/git/simon/.auto-sync.sh`
- **Service:** `com.smaluhn.git-autosync`
- **Interval:** Every 15 minutes (900 seconds)
- **Log:** `/Users/simon/git/simon/.auto-sync.log`

**Manage the service:**
```bash
# Check status
launchctl list | grep smaluhn

# Stop auto-sync
launchctl unload ~/Library/LaunchAgents/com.smaluhn.git-autosync.plist

# Start auto-sync
launchctl load ~/Library/LaunchAgents/com.smaluhn.git-autosync.plist

# View sync log
tail -f /Users/simon/git/simon/.auto-sync.log
```

**Obsidian Settings:**
- Auto pull on startup: **Enabled**
- Auto push on exit: **Enabled**
- No interval-based auto-sync (uses manual sync or startup/exit only)

---

**Last Updated:** 2025-10-24
