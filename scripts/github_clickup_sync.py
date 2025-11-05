#!/usr/bin/env python3
"""
Sync GitHub Project issues to ClickUp lists
Usage: python3 scripts/github_clickup_sync.py [--dry-run]
"""
import os
import sys
import json
import subprocess
import requests
from pathlib import Path

# Add config to path
sys.path.insert(0, str(Path(__file__).parent.parent / "config"))
import clickup_structure
import github_clickup_mapping

def load_env():
    """Load .env file"""
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

def run_gh_command(args):
    """Run gh CLI command and return JSON output"""
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout) if result.stdout else None
    except subprocess.CalledProcessError as e:
        print(f"⚠️  gh command failed: {e}")
        return None
    except json.JSONDecodeError:
        return result.stdout

def get_github_issues(repo, project_number=None):
    """Fetch GitHub issues from repo"""
    print(f"📥 Fetching GitHub issues from {repo}...")

    if project_number:
        # Fetch from specific project
        owner, repo_name = repo.split("/")
        issues = run_gh_command([
            "project", "item-list", str(project_number),
            "--owner", owner,
            "--format", "json",
            "--limit", "100"
        ])
    else:
        # Fetch all open issues from repo
        issues = run_gh_command([
            "issue", "list",
            "--repo", repo,
            "--state", "open",
            "--json", "number,title,labels,assignees,createdAt,updatedAt,url,body",
            "--limit", "100"
        ])

    return issues if issues else []

def classify_issue(issue):
    """Determine if issue is Dev or Ops based on labels"""
    labels = [label.get("name", "").lower() for label in issue.get("labels", [])]

    # Check for dev labels
    for label in labels:
        if any(dev in label for dev in github_clickup_mapping.DEV_LABELS):
            return "dev"

    # Check for ops labels
    for label in labels:
        if any(ops in label for ops in github_clickup_mapping.OPS_LABELS):
            return "ops"

    # Default to ops if no clear classification
    return "ops"

def get_clickup_tasks(list_id):
    """Fetch existing tasks from ClickUp list"""
    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(
            f"https://api.clickup.com/api/v2/list/{list_id}/task",
            headers=headers,
            params={"include_closed": False}
        )
        response.raise_for_status()
        return response.json().get("tasks", [])
    except Exception as e:
        print(f"⚠️  Failed to fetch ClickUp tasks: {e}")
        return []

def create_clickup_task(list_id, title, description, github_url, dry_run=False):
    """Create a new task in ClickUp"""
    if dry_run:
        print(f"   [DRY RUN] Would create: {title}")
        return None

    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    data = {
        "name": title,
        "description": f"{description}\n\n**GitHub Issue:** {github_url}",
        "markdown_description": f"{description}\n\n**GitHub Issue:** [{github_url}]({github_url})",
    }

    try:
        response = requests.post(
            f"https://api.clickup.com/api/v2/list/{list_id}/task",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        task = response.json()
        print(f"   ✅ Created: {title} (ID: {task['id']})")
        return task
    except Exception as e:
        print(f"   ❌ Failed to create task: {e}")
        return None

def sync_repo_to_clickup(repo, config, dry_run=False):
    """Sync one GitHub repo to ClickUp"""
    print(f"\n📦 Syncing {repo}...")

    # Get GitHub issues
    issues = get_github_issues(repo, config.get("github_project_number"))

    if not issues:
        print(f"   ℹ️  No issues found")
        return

    print(f"   Found {len(issues)} issue(s)")

    # Determine target lists
    has_split_lists = "clickup_dev_list" in config and "clickup_ops_list" in config

    if has_split_lists:
        dev_list_id = clickup_structure.SPACES["Team"]["lists"].get(config["clickup_dev_list"])
        ops_list_id = clickup_structure.SPACES["Team"]["lists"].get(config["clickup_ops_list"])
    else:
        single_list_id = clickup_structure.SPACES["Team"]["lists"].get(config["clickup_list"])

    # Sync each issue
    for issue in issues:
        title = issue.get("title", "")
        number = issue.get("number", "")
        url = issue.get("url", "")
        body = issue.get("body", "")[:500]  # Limit description length

        # Classify and determine target list
        if has_split_lists:
            classification = classify_issue(issue)
            target_list_id = dev_list_id if classification == "dev" else ops_list_id
            list_name = config["clickup_dev_list"] if classification == "dev" else config["clickup_ops_list"]
        else:
            target_list_id = single_list_id
            list_name = config["clickup_list"]

        if not target_list_id:
            print(f"   ⚠️  List '{list_name}' not found in ClickUp")
            continue

        # Check if task already exists (by checking description contains GitHub URL)
        existing_tasks = get_clickup_tasks(target_list_id)
        task_exists = any(url in task.get("description", "") for task in existing_tasks)

        if task_exists:
            print(f"   ⏭️  Skipped (exists): #{number} {title}")
            continue

        # Create new task
        full_title = f"[GH#{number}] {title}"
        create_clickup_task(target_list_id, full_title, body, url, dry_run)

def main():
    """Main sync function"""
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made\n")

    print("🔄 Starting GitHub → ClickUp sync...\n")

    # Sync each configured repo
    for repo, config in github_clickup_mapping.GITHUB_TO_CLICKUP.items():
        try:
            sync_repo_to_clickup(repo, config, dry_run)
        except Exception as e:
            print(f"❌ Error syncing {repo}: {e}")

    print("\n✅ Sync complete!")

if __name__ == "__main__":
    main()
