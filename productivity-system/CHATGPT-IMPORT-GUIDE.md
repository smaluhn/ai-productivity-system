# ChatGPT Data Import Guide

**Purpose:** Import your ChatGPT conversations so Claude Code has better context about you, your projects, and your thinking.

---

## Step 1: Export Your ChatGPT Data

1. **Go to ChatGPT Settings**
   - Open https://chat.openai.com
   - Click your profile icon (bottom left)
   - Click "Settings"

2. **Navigate to Data Controls**
   - Click "Data controls" in the left sidebar
   - Find "Export data" section

3. **Request Export**
   - Click "Export" button
   - Confirm your email address
   - OpenAI will process your request (can take a few hours to a day)

4. **Download the ZIP**
   - You'll receive an email when ready
   - Download the ZIP file (contains all conversations in JSON format)

---

## Step 2: Extract and Organize

1. **Extract the ZIP file**
   ```bash
   # After downloading, extract to Downloads
   unzip ~/Downloads/chatgpt-export-*.zip -d ~/Downloads/ChatGPT-Export
   ```

2. **The export contains:**
   - `conversations.json` - All your chat conversations
   - `user.json` - Your user data
   - `message_feedback.json` - Your feedback on responses
   - Other metadata files

---

## Step 3: Import to Productivity System

### Option A: Copy to Productivity System (Recommended)

```bash
# Create ChatGPT archive folder
mkdir -p ~/git/simon/archive/chatgpt-conversations

# Copy the conversations file
cp ~/Downloads/ChatGPT-Export/conversations.json ~/git/simon/archive/chatgpt-conversations/

# Optionally copy other files
cp ~/Downloads/ChatGPT-Export/*.json ~/git/simon/archive/chatgpt-conversations/
```

### Option B: Create Summary Documents

If the conversations.json is too large, you can create topic-based summaries:

```bash
mkdir -p ~/git/simon/archive/chatgpt-summaries
```

Then manually create markdown files for key topics:
- `akunindo-discussions.md`
- `printora-discussions.md`
- `fundefi-discussions.md`
- `business-strategy.md`
- `technical-decisions.md`

---

## Step 4: Let Claude Index It

Once imported, Claude Code can read and reference these conversations to:
- Understand your project history
- Learn your communication style and preferences
- Reference past decisions and context
- Provide more personalized assistance

Simply tell Claude: "I've imported my ChatGPT conversations to `~/git/simon/archive/chatgpt-conversations/`. Please index them for context."

---

## Step 5: Keep It Updated (Optional)

You can export your ChatGPT data periodically (monthly/quarterly) to keep Claude Code up to date with your latest conversations.

---

## Privacy Note

- The export contains ALL your ChatGPT conversations
- Review the data before sharing if you're concerned about sensitive information
- You can selectively copy only relevant conversations if preferred
- Keep the export in your local system (not shared publicly)

---

## Alternative: Manual Import of Key Conversations

If you don't want to export everything:

1. Find important ChatGPT conversations
2. Copy the conversation text
3. Create markdown files in `~/git/simon/archive/chatgpt-summaries/`
4. Paste and organize by topic

Example structure:
```markdown
# Conversation: AkunIndo Business Model Discussion
**Date:** 2025-09-15
**Summary:** Discussion about target market and pricing strategy

## Key Points:
- Target SMEs with 1-50 employees
- Focus on Indonesian market first
- Pricing: $10/month freemium model
...
```

---

## Next Steps

1. ☐ Export data from ChatGPT
2. ☐ Wait for email confirmation
3. ☐ Download and extract ZIP
4. ☐ Copy to ~/git/simon/archive/chatgpt-conversations/
5. ☐ Notify Claude Code to index the data

---

**Last Updated:** 2025-10-23
