# Google Calendar MCP Setup Guide

This guide will help you set up Google Calendar integration with Claude Code.

## Prerequisites
- Node.js and npm installed
- Google account with Calendar access

## Step 1: Google Cloud Console Setup

1. **Create/Select a Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select an existing one

2. **Enable Google Calendar API**
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Calendar API"
   - Click "Enable"

3. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop app" as the application type
   - Download the credentials JSON file
   - Save it somewhere secure (e.g., `~/.config/google-calendar/credentials.json`)

4. **Configure OAuth Consent Screen**
   - Go to "APIs & Services" > "OAuth consent screen"
   - Add your email as a test user
   - This is required while the app is in testing mode

## Step 2: Set Environment Variable

Add the following to your shell configuration file (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
export GOOGLE_OAUTH_CREDENTIALS="/path/to/your/downloaded/credentials.json"
```

Replace `/path/to/your/downloaded/credentials.json` with the actual path to your credentials file.

Then reload your shell:
```bash
source ~/.zshrc  # or ~/.bashrc
```

## Step 3: Test the Integration

The `.mcp.json` file has already been created in this directory with the proper configuration.

Next time you start Claude Code in this directory, it will:
1. Detect the Google Calendar MCP server
2. Prompt you to authenticate via browser
3. Store the access token locally

## Step 4: First Use

After setting up:
1. Restart your shell session
2. Run Claude Code from this directory
3. On first use, a browser window will open for OAuth authentication
4. Grant the requested permissions
5. The token will be stored and auto-refresh going forward

## Troubleshooting

### Token Expiry
Google Calendar tokens in "testing" mode expire after 7 days. To re-authenticate:
```bash
# Remove the stored token
rm -rf ~/.cache/google-calendar-mcp/token.json

# Restart Claude Code to trigger re-authentication
```

### Publishing the App (Optional)
To avoid 7-day token expiry, you can publish your Google Cloud app:
- Go to OAuth consent screen
- Click "Publish App"
- This removes the testing limitation

## Available Calendar Commands

Once set up, you can ask Claude to:
- "Show my calendar for today"
- "Create a meeting tomorrow at 2pm"
- "What's on my schedule this week?"
- "Check if I'm free on Friday afternoon"
- And more!

## Security Notes

- The credentials file contains sensitive information - keep it secure
- Never commit the credentials file to version control
- The `.mcp.json` file uses environment variable expansion for security
- Tokens are stored locally and encrypted

## Configuration File

The MCP configuration is stored in `.mcp.json`:
```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "npx",
      "args": ["@cocal/google-calendar-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS": "${GOOGLE_OAUTH_CREDENTIALS}"
      }
    }
  }
}
```

## Next Steps

Once set up, your daily notes can automatically include calendar events!

Check `templates/daily-template.md` - it has a section for calendar events that will be auto-populated.
