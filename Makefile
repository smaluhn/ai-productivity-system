.PHONY: daily weekly monthly sync rollup verify index validate inbox-scan inbox-apply inbox-apply-now clickup-sync clickup-explore clickup-test

daily:
	@scripts/new_daily.sh

weekly:
	@scripts/new_weekly.sh

monthly:
	@scripts/new_monthly.sh

sync:
	@scripts/auto-sync.sh

rollup:
	@python3 scripts/rollup_weekly.py

index:
	@python3 scripts/build_indexes.py

verify:
	@scripts/verify-structure.sh

validate:
	@scripts/verify-structure.sh && python3 scripts/validate_frontmatter.py

inbox-scan:
	@python3 scripts/inbox_suggest.py

inbox-apply:
	@python3 scripts/inbox_apply.py

inbox-apply-now:
	@python3 scripts/inbox_apply.py --apply

# ClickUp Integration
clickup-sync:
	@python3 scripts/github_clickup_sync.py

clickup-explore:
	@python3 scripts/clickup_explore_workspace.py

clickup-test:
	@python3 scripts/clickup_test_connection.py
