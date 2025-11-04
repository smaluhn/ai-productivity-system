# Inbox Processing

## Quick Start
```bash
# 1. Generate routing suggestions
make inbox-scan

# 2. Review (optional - edit triage/inbox_triage_*.yaml)
# Change "action", "target", or add "decision: SKIP"

# 3. Preview changes
make inbox-apply

# 4. Execute
make inbox-apply-now
```

## How It Works
- Scans `inbox/` folder
- Matches files against keywords in `config/inbox_rules.yaml`
- Suggests MOVE/APPEND/REVIEW actions
- Creates reviewable YAML in `triage/`
- Executes moves with `--apply` flag
