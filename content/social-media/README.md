# Social Media Automation

Automated posting system for X (Twitter), LinkedIn, and Threads.

## Structure

```
social-media/
├── twitter/
│   ├── posts/
│   │   └── YYYY-MM-DD-post-title.md
│   └── threads/
│       └── YYYY-MM-DD-thread-title.md
├── linkedin/
│   ├── posts/
│   │   └── YYYY-MM-DD-post-title.md
│   └── articles/
│       └── YYYY-MM-DD-article-title.md
├── threads/
│   └── posts/
│       └── YYYY-MM-DD-post-title.md
└── drafts/
    └── YYYY-MM-DD-draft-title.md
```

## Post Format

Each post is a markdown file with frontmatter:

```markdown
---
platform: twitter  # or linkedin, threads
status: draft      # draft, scheduled, published
scheduled_date: 2025-10-26T10:00:00
tags: [ai, productivity, build-in-public]
cross_post: [linkedin]  # optional: cross-post to other platforms
---

Post content here...
```

## Twitter Post Template

```markdown
---
platform: twitter
status: draft
scheduled_date: 2025-10-26T10:00:00
tags: [ai, productivity]
---

Your tweet content (280 chars max)

Optional thread continuation (if thread)...
```

## LinkedIn Post Template

```markdown
---
platform: linkedin
status: draft
scheduled_date: 2025-10-26T10:00:00
tags: [AI, Productivity, StartupLife]
---

Your LinkedIn post content...

Can be longer, more professional tone.
```

## Automation Workflow

1. **Create post** - Write in drafts/ folder
2. **Review** - Move to platform folder when ready
3. **Schedule** - Set scheduled_date in frontmatter
4. **Auto-post** - MCP automation posts at scheduled time
5. **Archive** - Move to platform/posts/archive/ after posting

## Future Features
- [ ] Auto-generate posts from blog articles
- [ ] Cross-posting to multiple platforms
- [ ] Analytics tracking
- [ ] A/B testing for post variations
- [ ] Image generation for posts
- [ ] Hashtag optimization
