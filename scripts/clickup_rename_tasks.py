#!/usr/bin/env python3
"""
Remove [GH#XX] prefix from all ClickUp tasks
Usage: python3 scripts/clickup_rename_tasks.py [--dry-run]
"""
import os
import sys
import re
import requests
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "config"))
import clickup_structure

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

def get_all_tasks_in_list(list_id):
    """Fetch all tasks from a list"""
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
        print(f"⚠️  Failed to fetch tasks: {e}")
        return []

def rename_task(task_id, new_name, dry_run=False):
    """Rename a task in ClickUp"""
    if dry_run:
        return True

    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(
            f"https://api.clickup.com/api/v2/task/{task_id}",
            headers=headers,
            json={"name": new_name}
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"⚠️  Failed to rename task: {e}")
        return False

def main():
    """Main function"""
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made\n")

    print("🔄 Removing [GH#XX] prefixes from ClickUp tasks...\n")

    # Lists to process
    main_lists = {
        "Printora": clickup_structure.SPACES["Team"]["lists"].get("Printora"),
        "Printora Ops": clickup_structure.SPACES["Team"]["lists"].get("Printora Ops"),
        "FunDeFi": clickup_structure.SPACES["Team"]["lists"].get("FunDeFi"),
        "FunDeFi Ops": clickup_structure.SPACES["Team"]["lists"].get("FunDeFi Ops"),
        "AkunIndo": clickup_structure.SPACES["Team"]["lists"].get("AkunIndo"),
        "FavOS": clickup_structure.SPACES["Team"]["lists"].get("FavOS"),
    }

    total_renamed = 0
    pattern = re.compile(r'^\[GH#\d+\]\s*')

    for list_name, list_id in main_lists.items():
        if not list_id:
            continue

        print(f"📋 Processing {list_name}...")
        tasks = get_all_tasks_in_list(list_id)

        renamed_in_list = 0
        for task in tasks:
            task_name = task.get("name", "")
            match = pattern.match(task_name)

            if match:
                # Remove the [GH#XX] prefix
                new_name = pattern.sub("", task_name)

                if dry_run:
                    print(f"   Would rename: {task_name}")
                    print(f"            → {new_name}")
                else:
                    if rename_task(task["id"], new_name):
                        print(f"   ✅ {new_name}")
                        renamed_in_list += 1
                    else:
                        print(f"   ❌ Failed: {task_name}")

        if renamed_in_list > 0:
            print(f"   Renamed {renamed_in_list} task(s) in {list_name}\n")
        elif not dry_run:
            print(f"   No tasks to rename\n")

        total_renamed += renamed_in_list

    if dry_run:
        print(f"\n✅ Dry run complete! Would rename {total_renamed} task(s)")
    else:
        print(f"\n✅ Renamed {total_renamed} task(s) across all lists")

if __name__ == "__main__":
    main()
