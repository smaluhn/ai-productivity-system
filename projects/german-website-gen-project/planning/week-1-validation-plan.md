# Week 1 Validation Plan

**Dates:** Nov 5 - Nov 12, 2025
**Goal:** Validate business model with minimal automation

## Day 1-2: Setup (Nov 5-6)

### Technical Setup
- [x] Create project structure
- [ ] Set up Google Maps API key
- [ ] Build basic Google Maps scraper
- [ ] Test scraper with 5-10 businesses

### Content Setup
- [ ] Draft German email templates (3 variants)
- [ ] Create business qualification criteria
- [ ] Set up lead tracking spreadsheet

## Day 3-4: Lead Generation (Nov 7-8)

### Scraping Targets
- [ ] Scrape 50-100 German businesses
- **Cities to target:**
  - Munich (high-value market)
  - Berlin (tech-forward but underserved)
  - Hamburg
  - Cologne

- **Business types:**
  - Restaurants/Cafes
  - Handwerker (craftsmen: electricians, plumbers, carpenters)
  - Small retail shops
  - Professional services (lawyers, accountants, consultants)

### Qualification
- [ ] Filter for businesses without websites
- [ ] Check Google Maps reviews (prefer 10+ reviews = established)
- [ ] Note hours, phone, photos available

## Day 5-6: Outreach + Website Generation (Nov 9-10)

### Manual Outreach
- [ ] Select top 20 qualified leads
- [ ] Send personalized emails to 20 businesses
- [ ] Track: sent, opened, replied, interested

### Website Generation Tests
- [ ] Pick 2-3 businesses
- [ ] Generate website using Claude Code API
- [ ] Generate website using landingsite.ai
- [ ] Compare quality, speed, customization

## Day 7: Follow-up & Analysis (Nov 11-12)

### Follow-up
- [ ] Send follow-up emails to non-responders
- [ ] Schedule calls with interested businesses

### Analysis
- [ ] Response rate calculation
- [ ] Common objections identified
- [ ] Pricing feedback
- [ ] Website generation comparison results

### Decision Point
**Success criteria:**
- At least 2-3 positive responses
- At least 1 business wants to see their sample site
- Website generation works smoothly (under 10 min per site)

**If success → Day 8+:** Build automation pipeline
**If failure:** Document learnings, pivot or abandon

## Metrics to Track

| Metric | Target | Actual |
|--------|--------|--------|
| Leads scraped | 50-100 | - |
| Qualified leads | 20-30 | - |
| Emails sent | 20 | - |
| Responses | 2-3 | - |
| Interested | 1-2 | - |
| Meetings booked | 1 | - |
| Sample sites generated | 2-3 | - |
| Time per website | <10 min | - |

## Risk Mitigation

**Risk:** Low response rate
- **Mitigation:** Test multiple email templates, try phone calls

**Risk:** Businesses don't see value
- **Mitigation:** Generate sample site FIRST, send it in outreach

**Risk:** Pricing too high/low
- **Mitigation:** Ask "What would you pay?" in conversations

**Risk:** Website generation takes too long
- **Mitigation:** Optimize prompts, use faster models, compare tools
