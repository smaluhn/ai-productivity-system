#!/usr/bin/env python3
"""
Fireflies.ai Meeting Import Script
Fetches meeting transcriptions and creates meeting notes in Obsidian
"""

import os
import sys
import requests
import json
from datetime import datetime

# Fireflies GraphQL API endpoint
API_URL = "https://api.fireflies.ai/graphql"

def get_api_key():
    """Get Fireflies API key from environment"""
    api_key = os.getenv('FIREFLIES_API_KEY')
    if not api_key:
        print("Error: FIREFLIES_API_KEY environment variable not set")
        sys.exit(1)
    return api_key

def make_request(query, variables=None):
    """Make a GraphQL request to Fireflies API"""
    api_key = get_api_key()
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'query': query,
        'variables': variables or {}
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"Error: API request failed with status {response.status_code}")
        print(response.text)
        sys.exit(1)

    return response.json()

def list_meetings(limit=10):
    """List recent meetings"""
    query = """
    query Transcripts($limit: Int) {
      transcripts(limit: $limit) {
        id
        title
        date
        duration
        sentences {
          text
        }
      }
    }
    """

    variables = {'limit': limit}
    result = make_request(query, variables)

    if 'data' in result and 'transcripts' in result['data']:
        meetings = result['data']['transcripts']
        print(f"\nFound {len(meetings)} recent meetings:\n")
        for i, meeting in enumerate(meetings, 1):
            # Handle date as Unix timestamp (integer)
            if isinstance(meeting['date'], int):
                date_obj = datetime.fromtimestamp(meeting['date'] / 1000)  # Convert from ms
                date_str = date_obj.strftime('%Y-%m-%d')
            else:
                date_str = datetime.fromisoformat(meeting['date'].replace('Z', '+00:00')).strftime('%Y-%m-%d')

            duration_min = meeting['duration'] // 60 if meeting['duration'] else 0
            print(f"{i}. [{date_str}] {meeting['title']} ({duration_min} min)")
            print(f"   ID: {meeting['id']}\n")
        return meetings
    else:
        print("No meetings found or error in response")
        print(json.dumps(result, indent=2))
        return []

def get_meeting_details(transcript_id):
    """Get detailed meeting information including transcript"""
    query = """
    query Transcript($transcriptId: String!) {
      transcript(id: $transcriptId) {
        id
        title
        date
        duration
        host_email
        participants
        summary {
          keywords
          action_items
          outline
          shorthand_bullet
          overview
        }
        sentences {
          text
          speaker_name
          start_time
        }
      }
    }
    """

    variables = {'transcriptId': transcript_id}
    result = make_request(query, variables)

    if 'data' in result and 'transcript' in result['data']:
        return result['data']['transcript']
    else:
        print("Error fetching meeting details")
        print(json.dumps(result, indent=2))
        return None

def create_meeting_note(meeting):
    """Create a meeting note in the meetings folder"""
    # Handle date as Unix timestamp (integer) or ISO string
    if isinstance(meeting['date'], int):
        date_obj = datetime.fromtimestamp(meeting['date'] / 1000)  # Convert from ms
    else:
        date_obj = datetime.fromisoformat(meeting['date'].replace('Z', '+00:00'))

    date_str = date_obj.strftime('%Y-%m-%d')
    time_str = date_obj.strftime('%H:%M')
    duration_min = meeting['duration'] // 60 if meeting['duration'] else 0

    # Clean filename
    safe_title = "".join(c for c in meeting['title'] if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title.replace(' ', '-').lower()
    filename = f"{safe_title}-{date_str}.md"
    filepath = os.path.join('meetings', filename)

    # Build content
    content = f"""# {meeting['title']}
**Date:** {date_str} {time_str}
**Duration:** {duration_min} minutes
**Host:** {meeting.get('host_email', 'N/A')}
**Participants:** {', '.join(meeting.get('participants', [])) if meeting.get('participants') else 'N/A'}

## Summary

"""

    # Add AI summary if available
    if meeting.get('summary'):
        summary = meeting['summary']

        if summary.get('overview'):
            content += f"### Overview\n{summary['overview']}\n\n"

        if summary.get('action_items') and len(summary['action_items']) > 0:
            content += "### Action Items\n"
            for item in summary['action_items']:
                content += f"- [ ] {item}\n"
            content += "\n"

        if summary.get('keywords') and len(summary['keywords']) > 0:
            content += f"### Keywords\n{', '.join(summary['keywords'])}\n\n"

        if summary.get('shorthand_bullet') and len(summary['shorthand_bullet']) > 0:
            content += "### Key Points\n"
            for point in summary['shorthand_bullet']:
                content += f"- {point}\n"
            content += "\n"

    # Add transcript
    content += "## Transcript\n\n"
    if meeting.get('sentences'):
        current_speaker = None
        for sentence in meeting['sentences']:
            speaker = sentence.get('speaker_name', 'Unknown')
            text = sentence.get('text', '')

            if speaker != current_speaker:
                content += f"\n**{speaker}:**  \n"
                current_speaker = speaker

            content += f"{text} "

    content += "\n\n---\n\n*Imported from Fireflies.ai*\n"

    # Write file
    with open(filepath, 'w') as f:
        f.write(content)

    print(f"\n✓ Meeting note created: {filepath}")
    return filepath

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Fireflies.ai Meeting Import")
        print("\nUsage:")
        print("  python fireflies-import.py list              - List recent meetings")
        print("  python fireflies-import.py import <id>       - Import specific meeting")
        print("  python fireflies-import.py import-latest     - Import most recent meeting")
        sys.exit(0)

    command = sys.argv[1]

    if command == 'list':
        list_meetings()

    elif command == 'import' and len(sys.argv) == 3:
        transcript_id = sys.argv[2]
        print(f"Fetching meeting {transcript_id}...")
        meeting = get_meeting_details(transcript_id)
        if meeting:
            create_meeting_note(meeting)

    elif command == 'import-latest':
        print("Fetching latest meeting...")
        meetings = list_meetings(1)
        if meetings:
            meeting_id = meetings[0]['id']
            meeting = get_meeting_details(meeting_id)
            if meeting:
                create_meeting_note(meeting)

    else:
        print("Unknown command. Use 'list', 'import <id>', or 'import-latest'")
        sys.exit(1)

if __name__ == '__main__':
    main()
