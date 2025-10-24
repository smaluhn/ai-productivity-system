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
- [ ] Test sync from mobile to `zee-mon/simon` repository
- [ ] Verify pull/push operations work on mobile
- [ ] Document final working configuration

---

## Repository Details

**Repository:** https://github.com/zee-mon/simon
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

1. Open Obsidian mobile app
2. Go to Settings → Community Plugins → Git
3. Update username from `sudosimonglitch` to `smaluhn`
4. Verify repository URL: `https://github.com/zee-mon/simon.git`
5. Update personal access token if needed
6. Test pull operation
7. Test push operation
8. Verify auto-sync is working

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

**Last Updated:** 2025-10-24
