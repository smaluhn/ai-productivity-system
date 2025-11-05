#!/usr/bin/env python3
"""
Fetch Simon's ClickUp tasks for today and insert into daily note
Usage: python3 scripts/clickup_daily_fetch.py [YYYY-MM-DD]
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

def get_all_tasks_for_user(user_email="simon@favourse.com"):
    """Fetch all tasks assigned to Simon across all lists"""
    load_env()
    token = os.getenv("CLICKUP_API_TOKEN")
    workspace_id = os.getenv("CLICKUP_WORKSPACE_ID")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    all_tasks = []

    # Get all lists from Team space
    space_id = clickup_structure.SPACES["Team"]["id"]
    lists = clickup_structure.SPACES["Team"]["lists"]

    # Focus on main project lists only
    main_lists = {
        "Printora": lists.get("Printora"),
        "Printora Ops": lists.get("Printora Ops"),
        "FunDeFi": lists.get("FunDeFi"),
        "FunDeFi Ops": lists.get("FunDeFi Ops"),
        "AkunIndo": lists.get("AkunIndo"),
        "FavOS": lists.get("FavOS"),
        "Simon": lists.get("Simon"),
    }

    for list_name, list_id in main_lists.items():
        if not list_id:
            continue

        try:
            response = requests.get(
                f"https://api.clickup.com/api/v2/list/{list_id}/task",
                headers=headers,
                params={"include_closed": False}
            )
            response.raise_for_status()
            tasks = response.json().get("tasks", [])

            # Filter for Simon's tasks
            for task in tasks:
                assignees = task.get("assignees", [])
                if any(a.get("email") == user_email for a in assignees):
                    task["list_name"] = list_name
                    all_tasks.append(task)

        except Exception as e:
            print(f"⚠️  Failed to fetch from {list_name}: {e}", file=sys.stderr)
            continue

    return all_tasks

def classify_tasks(tasks):
    """Classify tasks by urgency and project"""
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_week = today + timedelta(days=(6 - today.weekday()))  # Sunday

    classified = {
        "overdue": [],
        "due_today": [],
        "this_week": [],
        "no_due_date": []
    }

    for task in tasks:
        due_date_str = task.get("due_date")

        if not due_date_str:
            classified["no_due_date"].append(task)
            continue

        # Parse due date (milliseconds timestamp)
        due_date = datetime.fromtimestamp(int(due_date_str) / 1000)
        due_date = due_date.replace(hour=0, minute=0, second=0, microsecond=0)

        if due_date < today:
            classified["overdue"].append(task)
        elif due_date == today:
            classified["due_today"].append(task)
        elif due_date <= end_of_week:
            classified["this_week"].append(task)
        else:
            classified["no_due_date"].append(task)

    return classified

def get_project_from_list(list_name):
    """Extract project name from list name"""
    if "Printora" in list_name:
        return "Printora"
    elif "AkunIndo" in list_name:
        return "AkunIndo"
    elif "FunDeFi" in list_name:
        return "FunDeFi"
    elif "FavOS" in list_name:
        return "FavOS"
    elif "Simon" in list_name:
        return "Personal"
    else:
        return "Other"

def get_day_focus(date):
    """Get project focus for the day"""
    weekday = date.weekday()  # 0=Mon, 6=Sun
    focus_map = {
        0: "Printora",      # Monday
        1: "AkunIndo",      # Tuesday
        2: "FunDeFi",       # Wednesday
        3: "Printora",      # Thursday
        4: "FunDeFi",       # Friday
        5: "Printora",      # Saturday
        6: "OFF"            # Sunday
    }
    return focus_map.get(weekday, "Unknown")

def format_task_line(task):
    """Format task as markdown checkbox with tags and ClickUp ID"""
    task_id = task["id"]
    task_name = task["name"]
    list_name = task["list_name"]
    project = get_project_from_list(list_name)

    # Get tags (for Simon's personal projects)
    tags = task.get("tags", [])
    tag_str = ""
    if tags:
        tag_names = [f"#{tag['name']}" for tag in tags]
        tag_str = f"[{', '.join(tag_names)}] "

    # Get priority emoji
    priority = task.get("priority", {})
    priority_emoji = ""
    if priority:
        priority_name = priority.get("priority", "").lower()
        if "urgent" in priority_name or priority.get("id") == "1":
            priority_emoji = "🔴 "
        elif "high" in priority_name or priority.get("id") == "2":
            priority_emoji = "🟠 "
        elif "normal" in priority_name or priority.get("id") == "3":
            priority_emoji = "🟡 "

    # For Simon's personal tasks, show tags instead of project
    if project == "Personal" and tag_str:
        return f"- [ ] {priority_emoji}{tag_str}{task_name} [CU-{task_id}]"
    else:
        return f"- [ ] {priority_emoji}[{project}] {task_name} [CU-{task_id}]"

def insert_into_daily_note(date, tasks_text):
    """Insert tasks into daily note"""
    daily_file = Path(__file__).parent.parent / "journal" / "daily" / str(date.year) / f"{date.strftime('%Y-%m-%d')}.md"

    if not daily_file.exists():
        print(f"⚠️  Daily note doesn't exist: {daily_file}")
        print(f"   Run: make daily")
        return False

    # Read existing content
    content = daily_file.read_text()

    # Find insertion point (after ## Morning or at end of front-matter)
    if "## ClickUp Tasks" in content:
        # Already has ClickUp section, replace it
        lines = content.split("\n")
        start_idx = None
        end_idx = None

        for i, line in enumerate(lines):
            if "## ClickUp Tasks" in line:
                start_idx = i
            elif start_idx is not None and line.startswith("## ") and "ClickUp" not in line:
                end_idx = i
                break

        if start_idx is not None:
            if end_idx is None:
                end_idx = len(lines)

            # Replace section
            new_lines = lines[:start_idx] + [tasks_text] + lines[end_idx:]
            content = "\n".join(new_lines)
    else:
        # Add after front-matter or Morning section
        if "## Morning" in content:
            content = content.replace("## Morning", f"{tasks_text}\n\n## Morning")
        else:
            # Add after front-matter
            parts = content.split("---\n", 2)
            if len(parts) >= 3:
                content = parts[0] + "---\n" + parts[1] + "---\n" + tasks_text + "\n\n" + parts[2]
            else:
                content = tasks_text + "\n\n" + content

    # Write back
    daily_file.write_text(content)
    return True

def main():
    """Main function"""
    # Get date from args or use today
    if len(sys.argv) > 1:
        date = datetime.strptime(sys.argv[1], "%Y-%m-%d")
    else:
        date = datetime.now()

    print(f"🔄 Fetching ClickUp tasks for Simon ({date.strftime('%Y-%m-%d')})...")

    # Get day focus
    day_focus = get_day_focus(date)
    if day_focus == "OFF":
        print("🏖️  Sunday - OFF day! No tasks to fetch.")
        return

    # Fetch tasks
    tasks = get_all_tasks_for_user()

    if not tasks:
        print("ℹ️  No tasks found assigned to Simon")
        return

    print(f"   Found {len(tasks)} task(s) assigned to Simon")

    # Classify
    classified = classify_tasks(tasks)

    # Build markdown output
    output = [f"## ClickUp Tasks - {date.strftime('%A')} ({day_focus} Day)"]
    output.append("")

    # Overdue
    if classified["overdue"]:
        output.append("### ⏰ OVERDUE")
        for task in sorted(classified["overdue"], key=lambda t: t.get("due_date", 0)):
            output.append(format_task_line(task))
        output.append("")

    # Due today
    if classified["due_today"]:
        output.append("### 🔴 Due Today")
        for task in classified["due_today"]:
            output.append(format_task_line(task))
        output.append("")

    # This week
    if classified["this_week"]:
        output.append("### 🟡 This Week")
        for task in sorted(classified["this_week"], key=lambda t: t.get("due_date", 0)):
            output.append(format_task_line(task))
        output.append("")

    # No due date - show focus day project and personal tasks
    focus_tasks = [t for t in classified["no_due_date"] if get_project_from_list(t["list_name"]) == day_focus]
    personal_tasks = [t for t in classified["no_due_date"] if get_project_from_list(t["list_name"]) == "Personal"]

    if focus_tasks:
        output.append(f"### 📋 {day_focus} Backlog")
        for task in focus_tasks[:5]:  # Limit to 5
            output.append(format_task_line(task))
        output.append("")

    if personal_tasks:
        output.append("### 📋 Personal Tasks")
        for task in personal_tasks[:10]:  # Show up to 10 personal tasks
            output.append(format_task_line(task))
        output.append("")

    tasks_text = "\n".join(output)

    # Insert into daily note
    if insert_into_daily_note(date, tasks_text):
        print(f"✅ Tasks added to daily note")

        # Print summary
        print(f"\n📊 Summary:")
        if classified["overdue"]:
            print(f"   ⏰ {len(classified['overdue'])} overdue")
        if classified["due_today"]:
            print(f"   🔴 {len(classified['due_today'])} due today")
        if classified["this_week"]:
            print(f"   🟡 {len(classified['this_week'])} due this week")
        if focus_tasks:
            print(f"   📋 {len(focus_tasks)} {day_focus} backlog tasks")
        if personal_tasks:
            print(f"   📋 {len(personal_tasks)} personal tasks")
    else:
        print("❌ Failed to insert into daily note")
        sys.exit(1)

if __name__ == "__main__":
    main()
