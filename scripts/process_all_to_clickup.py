#!/usr/bin/env python3
"""
Process all inbox items and outstanding tasks into ClickUp
Creates a single source of truth in ClickUp
Usage: python3 scripts/process_all_to_clickup.py [--dry-run]
"""
import os
import sys
import requests
from pathlib import Path
from datetime import datetime, timedelta

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

def get_headers():
    """Get API headers"""
    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def create_task(list_id, task_data, dry_run=False):
    """Create a task in ClickUp"""
    if dry_run:
        print(f"   Would create: {task_data['name']}")
        return True

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
        print(f"   ⚠️  Failed to create '{task_data['name']}': {e}")
        return False

def get_user_id(email="simon@favourse.com"):
    """Get user ID from email"""
    # Simon's ID is 3759916
    return 3759916

def main():
    """Main function"""
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made\n")

    print("📋 Processing all inbox and outstanding tasks to ClickUp...\n")

    simon_id = get_user_id()
    team_space = clickup_structure.SPACES["Team"]
    lists = team_space["lists"]

    # Calculate dates
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    this_week = today + timedelta(days=7)
    nov_15 = datetime(2025, 11, 15)

    created_count = 0

    # ========================================
    # INBOX ITEMS → ClickUp
    # ========================================
    print("📥 Processing Inbox Items...\n")

    inbox_tasks = [
        {
            "list": "Simon",
            "name": "Enable GitHub Discussions on repositories",
            "description": "Enable Discussions feature on all active repositories",
            "priority": 2,  # High
            "tags": ["productivity-system"],
            "assignees": [simon_id],
            "due_date": int(today.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Define team roles and benefits structure",
            "description": "- Werner: CMC/CBDO\\n- Base girl: CMO/CBDO\\n- CTO needed\\n- CEO structure\\n- Define team benefits",
            "priority": 3,  # Normal
            "tags": ["fundefi", "fundraising"],
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Research and buy social media accounts",
            "description": "Clarify which social media accounts to purchase for AkunIndo",
            "priority": 3,
            "assignees": [simon_id],
        },
        {
            "list": "Simon",
            "name": "Explore Bio referral program for FunDeFi",
            "description": "$2K per researcher referred - looking for researchers seeking $50-500K funding",
            "priority": 3,
            "tags": ["fundefi", "fundraising"],
            "assignees": [simon_id],
        },
        {
            "list": "Simon",
            "name": "Watch AI business automation video",
            "description": "https://youtube.com/shorts/b_MaHJz1Hfk?si=LDDpC-UDZIm2qLQz",
            "priority": 4,  # Low
            "tags": ["learning"],
            "assignees": [simon_id],
        },
    ]

    for task_data in inbox_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data, dry_run):
            created_count += 1

    print()

    # ========================================
    # URGENT - Today/Tomorrow
    # ========================================
    print("🔴 Creating URGENT tasks...\n")

    urgent_tasks = [
        {
            "list": "Simon",
            "name": "Call sister",
            "priority": 1,  # Urgent
            "tags": ["life-admin"],
            "assignees": [simon_id],
            "due_date": int(today.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Setup tally.so for job applications",
            "description": "Sign up Simon bitwarden for AkunIndo, get tally.so, ask Yosua to do the same and integrate",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(tomorrow.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Check logo delivery timeline with Designer Gede",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(tomorrow.timestamp() * 1000)
        },
    ]

    for task_data in urgent_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data, dry_run):
            created_count += 1

    print()

    # ========================================
    # THIS WEEK - High Priority
    # ========================================
    print("🟠 Creating THIS WEEK tasks...\n")

    this_week_tasks = [
        # AkunIndo
        {
            "list": "AkunIndo",
            "name": "Setup Meta Ads account",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Setup social media accounts (admin@akunindo.com)",
            "description": "For Yosua to manage",
            "priority": 3,
            "assignees": [simon_id],  # Will reassign to Yosua
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Follow up on payment integration research (Xendit/Doku)",
            "description": "Check status with Kevin",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },

        # Printora
        {
            "list": "Printora",
            "name": "Stripe application decision (German entity or personal)",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Stripe sandbox setup",
            "description": "Kevin has GitHub issue for this",
            "priority": 3,
            "assignees": [simon_id],  # Will reassign to Kevin
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Define Nhung's role, payment, and weekly deliverables",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Prepare Merchize partnership discussion points",
            "description": "- Partnership structure\\n- API integration\\n- Revenue sharing model\\n- Our ask from Merchize",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(tomorrow.timestamp() * 1000)
        },

        # FunDeFi
        {
            "list": "FunDeFi",
            "name": "Send pitch deck v2 to Brent",
            "priority": 1,  # Urgent - OVERDUE
            "tags": ["fundraising"],
            "assignees": [simon_id],
            "due_date": int(today.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Follow up with Anjelito on emissions design",
            "priority": 2,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Werner meeting follow-up (CMC/CBDO role)",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Fair launch timeline planning",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(this_week.timestamp() * 1000)
        },

        # System
        {
            "list": "Simon",
            "name": "Show team ClickUp views in Thursday meeting",
            "priority": 3,
            "tags": ["productivity-system"],
            "assignees": [simon_id],
            "due_date": int((today + timedelta(days=2)).timestamp() * 1000)  # Thursday
        },
    ]

    for task_data in this_week_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data, dry_run):
            created_count += 1

    print()

    # ========================================
    # BY NOV 15 - Lower Priority
    # ========================================
    print("🟢 Creating BY NOV 15 tasks...\n")

    nov15_tasks = [
        # AkunIndo
        {
            "list": "AkunIndo",
            "name": "Apply logo to website",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Launch hiring campaign",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Get Meta Ads running",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Activate social media (Yosua managing)",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "AkunIndo",
            "name": "Mobile optimization",
            "description": "Kevin to complete",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },

        # Printora
        {
            "list": "Printora",
            "name": "Get website live",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Activate Stripe account",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Configure email system",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Onboard Nhung and get her productive",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "Printora",
            "name": "Define Merchize partnership agreement",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },

        # FunDeFi
        {
            "list": "FunDeFi",
            "name": "Finalize emissions design with Anjelito",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Complete fair launch plan",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Document team benefits structure",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
        {
            "list": "FunDeFi",
            "name": "Clarify Werner's role (CMC/CBDO)",
            "priority": 3,
            "assignees": [simon_id],
            "due_date": int(nov_15.timestamp() * 1000)
        },
    ]

    for task_data in nov15_tasks:
        list_name = task_data.pop("list")
        list_id = lists[list_name]
        if create_task(list_id, task_data, dry_run):
            created_count += 1

    print()

    # Summary
    if dry_run:
        print(f"✅ Dry run complete! Would create {created_count} tasks")
    else:
        print(f"✅ Created {created_count} tasks in ClickUp!")
        print(f"\n💡 Next steps:")
        print(f"   1. Run `make morning` to see all tasks in today's note")
        print(f"   2. Review tasks in ClickUp and adjust due dates/assignees")
        print(f"   3. Archive processed files: inbox/ and docs/2025-11-04-outstanding-tasks.md")

if __name__ == "__main__":
    main()
