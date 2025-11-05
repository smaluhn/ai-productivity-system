#!/usr/bin/env python3
"""
Test ClickUp API connection and list workspace info
Usage: python3 scripts/clickup_test_connection.py
"""
import os
import sys
import requests
from pathlib import Path

def load_env():
    """Load .env file if exists"""
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

def test_connection():
    """Test ClickUp API connection"""
    load_env()

    token = os.getenv("CLICKUP_API_TOKEN")
    if not token:
        print("❌ CLICKUP_API_TOKEN not found in .env")
        print("\nTo fix:")
        print("1. Go to ClickUp → Settings → Apps → API Token")
        print("2. Generate a new token")
        print("3. Add to .env file:")
        print("   CLICKUP_API_TOKEN=pk_your_token_here")
        return False

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    print("🔄 Testing ClickUp API connection...")

    # Test 1: Get authenticated user
    try:
        response = requests.get("https://api.clickup.com/api/v2/user", headers=headers)
        response.raise_for_status()
        user = response.json()["user"]
        print(f"✅ Connected as: {user['username']} ({user['email']})")
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return False

    # Test 2: List workspaces
    try:
        response = requests.get("https://api.clickup.com/api/v2/team", headers=headers)
        response.raise_for_status()
        teams = response.json()["teams"]
        print(f"\n📋 Found {len(teams)} workspace(s):")
        for team in teams:
            print(f"   - {team['name']} (ID: {team['id']})")

        if teams:
            workspace_id = teams[0]["id"]
            print(f"\n💡 Add to .env file:")
            print(f"   CLICKUP_WORKSPACE_ID={workspace_id}")
    except Exception as e:
        print(f"❌ Failed to list workspaces: {e}")
        return False

    # Test 3: List spaces in first workspace
    if teams:
        try:
            workspace_id = teams[0]["id"]
            response = requests.get(
                f"https://api.clickup.com/api/v2/team/{workspace_id}/space",
                headers=headers
            )
            response.raise_for_status()
            spaces = response.json()["spaces"]
            print(f"\n📁 Found {len(spaces)} space(s) in {teams[0]['name']}:")
            for space in spaces:
                print(f"   - {space['name']} (ID: {space['id']})")
        except Exception as e:
            print(f"⚠️  Could not list spaces: {e}")

    print("\n✅ ClickUp connection test successful!")
    print("\n🎯 Next steps:")
    print("1. Create spaces for: AkunIndo, Printora, FunDeFi, FavOS")
    print("2. Create lists within each space")
    print("3. Run: python3 scripts/clickup_create_initial_tasks.py")

    return True

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
