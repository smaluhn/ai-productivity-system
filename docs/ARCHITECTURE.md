# Architecture

- **PARA-inspired**: Projects, Areas, Resources, Archives + time-indexed journals
- **Journals**: Daily/Weekly/Monthly with ISO naming (YYYY-MM-DD, W##, YYYY-MM)
- **Inbox**: Smart routing based on keywords in config/inbox_rules.yaml
- **Validation**: Front-matter schemas, structure checks, pre-commit hooks
- **Automation**: Auto-sync, metrics rollup, index generation

## Daily Workflow
1. `make daily` - Create today's note
2. Work in today's note, track metrics
3. `make inbox-scan` - Route inbox items
4. `make sync` - Commit and push

## Weekly Review
1. `make weekly` - Create this week's note
2. `make rollup` - Auto-generate metrics
3. Review and plan
4. `make sync`
