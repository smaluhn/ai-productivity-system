# GitHub Projects ↔ ClickUp Lists Mapping
# This defines which GitHub repos/projects sync to which ClickUp lists

# GitHub Organization/Repo → ClickUp List mapping
GITHUB_TO_CLICKUP = {
    # AkunIndo
    "DiverseProjects/akunindo": {
        "clickup_list": "AkunIndo",
        "github_project_number": None,  # Will auto-detect
    },

    # Printora - Development issues go to GitHub, Operations to ClickUp
    "Printora/printora": {
        "clickup_dev_list": "Printora",      # Development tasks
        "clickup_ops_list": "Printora Ops",  # Operations/business tasks
        "github_project_number": None,
    },

    # FunDeFi
    "FUNDEdotFI/fundefi": {
        "clickup_dev_list": "FunDeFi",
        "clickup_ops_list": "FunDeFi Ops",
        "github_project_number": 2,  # From fundefi-view.md
    },

    # FavOS
    "Favos/Favos": {
        "clickup_list": "FavOS",
        "github_project_number": None,
    },
}

# Task Type Classification
# Determines whether a task goes to "Dev" or "Ops" list
DEV_LABELS = [
    "bug", "feature", "enhancement", "technical", "code", "backend",
    "frontend", "api", "database", "smart-contract", "blockchain"
]

OPS_LABELS = [
    "business", "marketing", "sales", "content", "design", "documentation",
    "hiring", "fundraising", "partnerships", "legal", "compliance"
]

# ClickUp Custom Field IDs (will be auto-detected on first run)
CLICKUP_CUSTOM_FIELDS = {
    "github_issue": None,  # URL field linking to GitHub issue
    "priority": None,      # Priority dropdown
    "project": None,       # Project dropdown
}

# Sync Settings
SYNC_SETTINGS = {
    "github_to_clickup": True,   # Sync GitHub issues → ClickUp tasks
    "clickup_to_github": False,  # Don't create GitHub issues from ClickUp (one-way for now)
    "update_existing": True,     # Update existing tasks when syncing
    "close_completed": True,     # Close GitHub issues when ClickUp task marked done
    "sync_comments": False,      # Don't sync comments (too noisy for now)
}
