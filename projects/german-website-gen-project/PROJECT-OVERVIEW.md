# German Business Website Generator

**Status:** 🚀 Launch Phase (Week 1 Validation)
**Started:** 2025-11-05
**Validation Deadline:** 2025-11-12

## 🎯 Business Model

### Value Proposition
Find German businesses with no/outdated websites, auto-generate modern professional sites, and offer them as a package.

### Pricing
- **One-time website creation:** TBD (estimate €500-1500)
- **Annual hosting + maintenance:** €100/year
- **Domain included** in hosting fee

### Target Market
- **Location:** Germany (higher profit margins than Indonesia)
- **Business Type:** Local businesses (restaurants, craftsmen, small shops, services)
- **Qualification:** No website OR very outdated website

## 🔬 Validation Goals (1 Week)

**Success Criteria:**
- [ ] Scrape 50-100 potential leads from Google Maps
- [ ] Manually reach out to 10-20 businesses
- [ ] Get 2-3 positive responses/meetings
- [ ] Generate 1-2 sample websites (automated)
- [ ] Validate pricing appetite

**If successful → Automate everything**
**If not → Pivot or abandon**

## 🛠️ Tech Stack

### Lead Generation
- **Google Maps Scraper** (Python)
- Target: businesses without websites or with poor sites

### Website Analysis
- **Claude API** to analyze existing sites/business info
- Extract: name, services, photos, hours, contact info

### Website Generation (Compare Both)
1. **Claude Code API** (via Anthropic)
   - Generate React/Next.js sites
   - Full customization with branding
   - Auto-deploy to Vercel/Netlify

2. **landingsite.ai** (for comparison)
   - Quick template approach
   - See which produces better results

### Hosting
- Vercel/Netlify free tier initially
- Scale to paid plans as needed

### Outreach
- Email templates (German)
- WhatsApp templates (optional)

## 📊 Current Phase: Week 1 Validation

### This Week Tasks
1. Set up Google Maps API key (Google Startup Program)
2. Build Google Maps scraper
3. Create website generator pipeline (Claude + landingsite.ai)
4. Draft German outreach templates
5. Find 50+ leads
6. Reach out to 10-20 businesses
7. Generate 2-3 sample sites

## 🔗 Links
- Repo: `/Users/simon/git/german-website-gen/`
- Planning: Current directory
- Scripts: `repo/scripts/`
- Leads: `repo/leads/`

## 📝 Notes
- Focus on SPEED for validation
- Manual outreach first, automate only if validated
- Track all metrics (response rate, interest level, objections)
