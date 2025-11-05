#!/usr/bin/env python3
"""
Create tomorrow's MITs (Most Important Tasks)
Usage: python3 scripts/create_tomorrow_mits.py
"""
import os
import sys
import requests
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent / "config"))
import clickup_structure

def load_env():
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

def get_headers():
    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def create_task(list_id, task_data):
    headers = get_headers()
    try:
        response = requests.post(
            f"https://api.clickup.com/api/v2/list/{list_id}/task",
            headers=headers,
            json=task_data
        )
        response.raise_for_status()
        task_id = response.json()["id"]
        print(f"   ✅ Created: {task_data['name']} [CU-{task_id}]")
        return True
    except Exception as e:
        print(f"   ⚠️  Failed: {task_data['name']} - {e}")
        return False

def main():
    print("🎯 Creating tomorrow's MITs (Nov 6, 2025)...\n")

    simon_id = 3759916
    team_space = clickup_structure.SPACES["Team"]
    lists = team_space["lists"]

    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_ts = int(tomorrow.timestamp() * 1000)

    created = 0

    # FunDeFi MITs
    print("💎 FunDeFi MITs:\n")
    fundefi_tasks = [
        {
            "list": "FunDeFi",
            "name": "Clarify spec docs for FunDeFi",
            "description": "Review and clarify technical specifications",
            "priority": 2,  # High
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
        {
            "list": "FunDeFi",
            "name": "Work on pitch deck for FunDeFi",
            "description": "Continue developing pitch deck v2 for investors",
            "priority": 2,  # High
            "tags": ["fundraising"],
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
    ]

    for task_data in fundefi_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data):
            created += 1

    print()

    # AkunIndo MITs
    print("🟢 AkunIndo MITs:\n")
    akunindo_tasks = [
        {
            "list": "AkunIndo",
            "name": "Update and export AkunIndo Pitch Deck PDF",
            "description": "Finalize and export pitch deck as PDF",
            "priority": 2,  # High
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
        {
            "list": "AkunIndo",
            "name": "Create social media accounts (Instagram, Facebook, YouTube, TikTok)",
            "description": "Create accounts and add to BitWarden with Yosua as role",
            "priority": 2,  # High
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
        {
            "list": "AkunIndo",
            "name": "Add Yosua to BitWarden for all AkunIndo social accounts",
            "description": "Give Yosua access to manage social media",
            "priority": 2,  # High
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
    ]

    for task_data in akunindo_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data):
            created += 1

    print()

    # Nate / FavOS Tasks
    print("🔵 Nate Follow-up (FavOS/FunDeFi):\n")
    nate_tasks = [
        {
            "list": "FavOS",
            "name": "Follow up with Nate on tasks",
            "description": "Check status of Nate's tasks and blockers",
            "priority": 2,  # High
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
        {
            "list": "FunDeFi",
            "name": "Update pitch deck for AllinX with FunDeFi pivot",
            "description": "Update FavOS pitch deck showing FunDeFi pivot with specific offer for AllinX",
            "priority": 2,  # High
            "tags": ["fundraising"],
            "assignees": [simon_id],
            "due_date": tomorrow_ts
        },
    ]

    for task_data in nate_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data):
            created += 1

    print()
    print(f"✅ Created {created} MITs for tomorrow!\n")
    print("💡 Run `make morning` tomorrow to see all tasks organized by urgency")

if __name__ == "__main__":
    main()
