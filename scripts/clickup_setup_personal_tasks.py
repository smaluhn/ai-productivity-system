#!/usr/bin/env python3
"""
Setup Simon's personal tasks: assign all tasks and add labels
Usage: python3 scripts/clickup_setup_personal_tasks.py [--dry-run]
"""
import os
import sys
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

def get_headers():
    """Get API headers"""
    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def get_space_tags(space_id):
    """Get all tags in a space"""
    headers = get_headers()
    try:
        response = requests.get(
            f"https://api.clickup.com/api/v2/space/{space_id}/tag",
            headers=headers
        )
        response.raise_for_status()
        return response.json().get("tags", [])
    except Exception as e:
        print(f"⚠️  Failed to fetch tags: {e}")
        return []

def create_tag(space_id, tag_name, dry_run=False):
    """Create a tag in a space"""
    if dry_run:
        return {"name": tag_name}

    headers = get_headers()
    try:
        response = requests.post(
            f"https://api.clickup.com/api/v2/space/{space_id}/tag",
            headers=headers,
            json={"tag": {"name": tag_name}}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️  Failed to create tag '{tag_name}': {e}")
        return None

def add_tag_to_task(task_id, tag_name, dry_run=False):
    """Add a tag to a task"""
    if dry_run:
        return True

    headers = get_headers()
    try:
        response = requests.post(
            f"https://api.clickup.com/api/v2/task/{task_id}/tag/{tag_name}",
            headers=headers
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"⚠️  Failed to add tag '{tag_name}' to task: {e}")
        return False

def assign_task(task_id, user_id, dry_run=False):
    """Assign a task to a user"""
    if dry_run:
        return True

    headers = get_headers()
    try:
        response = requests.post(
            f"https://api.clickup.com/api/v2/task/{task_id}/assignee/{user_id}",
            headers=headers
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"⚠️  Failed to assign task: {e}")
        return False

def get_tasks_in_list(list_id):
    """Get all tasks in a list"""
    headers = get_headers()
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

def main():
    """Main function"""
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made\n")

    print("🔧 Setting up Simon's personal tasks...\n")

    # Get Simon's user ID
    user_id = "3759916"  # Simon's ClickUp user ID

    # Get Simon list ID
    space_id = clickup_structure.SPACES["Team"]["id"]
    simon_list_id = clickup_structure.SPACES["Team"]["lists"]["Simon"]

    print(f"📋 Processing Simon list (ID: {simon_list_id})...\n")

    # Step 1: Create tags
    print("🏷️  Step 1: Creating tags...")

    existing_tags = get_space_tags(space_id)
    existing_tag_names = [tag["name"] for tag in existing_tags]

    recommended_tags = [
        "mindfulness-app",
        "productivity-system",
        "life-admin",
        "fundefi",
        "printora",
        "akunindo",
        "health",
        "learning",
        "fundraising",
        "personal-dev"
    ]

    for tag_name in recommended_tags:
        if tag_name in existing_tag_names:
            print(f"   ✓ Tag '{tag_name}' already exists")
        else:
            if create_tag(space_id, tag_name, dry_run):
                if dry_run:
                    print(f"   Would create tag: {tag_name}")
                else:
                    print(f"   ✅ Created tag: {tag_name}")

    print()

    # Step 2: Get all tasks
    print("📥 Step 2: Fetching tasks from Simon list...")
    tasks = get_tasks_in_list(simon_list_id)
    print(f"   Found {len(tasks)} tasks\n")

    # Step 3: Assign all tasks to Simon
    print("👤 Step 3: Assigning all tasks to Simon...")
    assigned_count = 0

    for task in tasks:
        task_name = task["name"]
        assignees = task.get("assignees", [])
        is_assigned = any(a.get("id") == int(user_id) for a in assignees)

        if is_assigned:
            print(f"   ✓ Already assigned: {task_name}")
        else:
            if assign_task(task["id"], user_id, dry_run):
                if dry_run:
                    print(f"   Would assign: {task_name}")
                else:
                    print(f"   ✅ Assigned: {task_name}")
                assigned_count += 1

    print(f"\n   Assigned {assigned_count} task(s)\n")

    # Step 4: Add tags to tasks
    print("🏷️  Step 4: Adding tags to tasks...")

    # Define tag mappings
    tag_mappings = {
        "Create 8 ClickUp Views for Team Workflow": ["productivity-system"],
        "fix testnet": ["fundefi"],
        "Bonding Curve Simulation": ["fundefi"],
        "Organize Fundraising-Notion": ["fundraising"],
        "Solana Devnet": ["fundefi"],
        "KOL-Deck": ["fundefi", "fundraising"],
        "Source Links": ["fundefi"],
        "Whitepaper": ["fundefi"],
        "Projections": ["fundefi"],
        "Update FAQs": ["fundefi"],
        "USPs and Blurb (and possibly Deck Slide)": ["fundefi"],
        "Outreach to 5 Advisors & Angels": ["fundraising"],
        "Pitch Deck": ["fundefi", "fundraising"],
        "Buy small mic for Mac and Galaxy can use for both": ["life-admin"],
        "Kindle Mac JLA book": ["learning"],
        "favxbot on MBA": ["personal-dev"],
        "Irem Artiffine Material": ["personal-dev"],
    }

    tagged_count = 0
    for task in tasks:
        task_name = task["name"]
        task_id = task["id"]

        # Get existing tags
        existing_task_tags = [tag["name"] for tag in task.get("tags", [])]

        # Get recommended tags for this task
        recommended = tag_mappings.get(task_name, [])

        if not recommended:
            print(f"   ⚪ No tags defined for: {task_name}")
            continue

        for tag_name in recommended:
            if tag_name in existing_task_tags:
                print(f"   ✓ Already tagged '{tag_name}': {task_name}")
            else:
                if add_tag_to_task(task_id, tag_name, dry_run):
                    if dry_run:
                        print(f"   Would tag '{tag_name}': {task_name}")
                    else:
                        print(f"   ✅ Tagged '{tag_name}': {task_name}")
                    tagged_count += 1

    print(f"\n   Added {tagged_count} tag(s)\n")

    # Summary
    if dry_run:
        print("✅ Dry run complete!")
    else:
        print("✅ Setup complete!")
        print(f"\n📊 Summary:")
        print(f"   - Created {len([t for t in recommended_tags if t not in existing_tag_names])} new tags")
        print(f"   - Assigned {assigned_count} tasks to Simon")
        print(f"   - Added {tagged_count} tags to tasks")
        print(f"\n💡 Next: Run `make morning` to see your tagged tasks in today's note!")

if __name__ == "__main__":
    main()
