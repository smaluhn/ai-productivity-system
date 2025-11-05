#!/usr/bin/env python3
"""
Explore ClickUp workspace structure and get all list IDs
Usage: python3 scripts/clickup_explore_workspace.py
"""
import os
import sys
import requests
from pathlib import Path

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

def explore_workspace():
    """Explore workspace structure"""
    load_env()

    token = os.getenv("CLICKUP_API_TOKEN")
    workspace_id = os.getenv("CLICKUP_WORKSPACE_ID")

    if not token or not workspace_id:
        print("❌ Missing CLICKUP_API_TOKEN or CLICKUP_WORKSPACE_ID in .env")
        return False

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    print(f"🔍 Exploring Workspace ID: {workspace_id}\n")

    # Get spaces
    try:
        response = requests.get(
            f"https://api.clickup.com/api/v2/team/{workspace_id}/space?archived=false",
            headers=headers
        )
        response.raise_for_status()
        spaces = response.json()["spaces"]

        print(f"📁 Found {len(spaces)} space(s):\n")

        for space in spaces:
            print(f"   📂 {space['name']} (ID: {space['id']})")

            # Get folders in space
            folder_response = requests.get(
                f"https://api.clickup.com/api/v2/space/{space['id']}/folder?archived=false",
                headers=headers
            )
            folder_response.raise_for_status()
            folders = folder_response.json()["folders"]

            if folders:
                print(f"      └─ Folders:")
                for folder in folders:
                    print(f"         📁 {folder['name']} (ID: {folder['id']})")

                    # Get lists in folder
                    list_response = requests.get(
                        f"https://api.clickup.com/api/v2/folder/{folder['id']}/list?archived=false",
                        headers=headers
                    )
                    list_response.raise_for_status()
                    lists = list_response.json()["lists"]

                    if lists:
                        for list_item in lists:
                            print(f"            └─ 📋 {list_item['name']} (ID: {list_item['id']})")

            # Get folderless lists (lists directly in space)
            list_response = requests.get(
                f"https://api.clickup.com/api/v2/space/{space['id']}/list?archived=false",
                headers=headers
            )
            list_response.raise_for_status()
            lists = list_response.json()["lists"]

            if lists:
                print(f"      └─ Lists (no folder):")
                for list_item in lists:
                    print(f"         📋 {list_item['name']} (ID: {list_item['id']})")

            print()

        # Save to config file
        config = {
            "workspace_id": workspace_id,
            "spaces": {}
        }

        for space in spaces:
            space_data = {
                "id": space["id"],
                "lists": {}
            }

            # Get all lists in space (both in folders and folderless)
            folder_response = requests.get(
                f"https://api.clickup.com/api/v2/space/{space['id']}/folder?archived=false",
                headers=headers
            )
            folders = folder_response.json()["folders"]

            for folder in folders:
                list_response = requests.get(
                    f"https://api.clickup.com/api/v2/folder/{folder['id']}/list?archived=false",
                    headers=headers
                )
                lists = list_response.json()["lists"]
                for list_item in lists:
                    space_data["lists"][list_item["name"]] = list_item["id"]

            # Folderless lists
            list_response = requests.get(
                f"https://api.clickup.com/api/v2/space/{space['id']}/list?archived=false",
                headers=headers
            )
            lists = list_response.json()["lists"]
            for list_item in lists:
                space_data["lists"][list_item["name"]] = list_item["id"]

            config["spaces"][space["name"]] = space_data

        # Save config
        config_file = Path(__file__).parent.parent / "config" / "clickup_structure.py"
        config_file.parent.mkdir(exist_ok=True)

        with open(config_file, "w") as f:
            f.write("# Auto-generated ClickUp workspace structure\n")
            f.write("# Run scripts/clickup_explore_workspace.py to regenerate\n\n")
            f.write(f"WORKSPACE_ID = '{workspace_id}'\n\n")
            f.write("SPACES = {\n")
            for space_name, space_data in config["spaces"].items():
                f.write(f"    '{space_name}': {{\n")
                f.write(f"        'id': '{space_data['id']}',\n")
                f.write(f"        'lists': {{\n")
                for list_name, list_id in space_data["lists"].items():
                    f.write(f"            '{list_name}': '{list_id}',\n")
                f.write(f"        }}\n")
                f.write(f"    }},\n")
            f.write("}\n")

        print(f"✅ Config saved to: config/clickup_structure.py")
        print(f"\n🎯 You can now use this in your scripts!")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = explore_workspace()
    sys.exit(0 if success else 1)
