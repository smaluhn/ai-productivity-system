#!/usr/bin/env node

/**
 * Fireflies.ai Webhook Processing Script
 *
 * This script processes incoming webhooks from Fireflies.ai when new meetings are transcribed.
 * It extracts action items, creates GitHub issues, updates daily notes, and manages delegated tasks.
 *
 * Setup Instructions:
 * 1. Install dependencies: npm install (see package.json in this directory)
 * 2. Configure webhook URL in Fireflies.ai dashboard
 * 3. Set up endpoint (local: ngrok, cloud: Vercel/Netlify/Lambda)
 * 4. Set required environment variables (see below)
 *
 * Environment Variables Required:
 * - FIREFLIES_API_KEY: Your Fireflies.ai API key (already set in ~/.zshrc)
 * - GITHUB_PERSONAL_ACCESS_TOKEN: GitHub PAT for creating issues (already set)
 * - WEBHOOK_SECRET: Optional secret for validating webhook requests
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

const CONFIG = {
  // GitHub settings
  github: {
    defaultOwner: 'simon', // Update with your GitHub username
    // Map meeting keywords to GitHub repos
    projectMapping: {
      'funde.fi': 'fundefi',
      'printora': 'printora',
      'akunindo': 'akunindo-org/akunindo',
      'favors': 'favors.ventures',
      'simon': 'simon', // Personal repo
    }
  },

  // File paths
  paths: {
    dailyNotes: '/Users/simon/git/simon/daily',
    meetings: '/Users/simon/git/simon/meetings',
  },

  // Fireflies API
  fireflies: {
    apiUrl: 'https://api.fireflies.ai/graphql',
    apiKey: process.env.FIREFLIES_API_KEY,
  }
};

// ============================================================================
// WEBHOOK PAYLOAD PROCESSING
// ============================================================================

/**
 * Main webhook handler
 * @param {Object} payload - Webhook payload from Fireflies
 */
async function processWebhook(payload) {
  console.log('📨 Received Fireflies webhook:', payload.event);

  if (payload.event !== 'transcript.completed') {
    console.log('⏭️  Skipping non-transcript event');
    return;
  }

  const transcriptId = payload.transcript_id;

  try {
    // 1. Fetch full transcript details
    const transcript = await fetchTranscriptDetails(transcriptId);

    // 2. Extract structured information
    const meetingData = extractMeetingData(transcript);

    // 3. Save meeting notes
    await saveMeetingNotes(meetingData);

    // 4. Create GitHub issues for action items
    await createGitHubIssues(meetingData);

    // 5. Update daily notes
    await updateDailyNotes(meetingData);

    // 6. Process delegated items
    await processDelegatedItems(meetingData);

    console.log('✅ Meeting processed successfully');

  } catch (error) {
    console.error('❌ Error processing webhook:', error);
    throw error;
  }
}

// ============================================================================
// FIREFLIES API INTEGRATION
// ============================================================================

/**
 * Fetch full transcript details from Fireflies API
 * @param {string} transcriptId
 */
async function fetchTranscriptDetails(transcriptId) {
  // TODO: Implement GraphQL query to Fireflies API
  // See: https://docs.fireflies.ai/api-graphql

  const query = `
    query Transcript($transcriptId: String!) {
      transcript(id: $transcriptId) {
        id
        title
        date
        duration
        participants
        summary
        sentences {
          text
          speaker_name
        }
        action_items
        questions
        keywords
      }
    }
  `;

  console.log('🔍 Fetching transcript details for:', transcriptId);

  // Placeholder - implement actual API call
  return {
    id: transcriptId,
    title: 'Sample Meeting',
    date: new Date().toISOString(),
    participants: [],
    summary: '',
    action_items: [],
  };
}

// ============================================================================
// DATA EXTRACTION
// ============================================================================

/**
 * Extract and structure meeting data
 * @param {Object} transcript
 */
function extractMeetingData(transcript) {
  const title = transcript.title;
  const date = new Date(transcript.date);

  // Identify project from meeting title/content
  const project = identifyProject(title, transcript.summary);

  // Extract action items with assignees
  const actionItems = parseActionItems(transcript.action_items);

  // Extract key decisions
  const decisions = extractDecisions(transcript.summary);

  return {
    id: transcript.id,
    title,
    date,
    project,
    participants: transcript.participants,
    summary: transcript.summary,
    actionItems,
    decisions,
    keywords: transcript.keywords || [],
  };
}

/**
 * Identify which project this meeting relates to
 */
function identifyProject(title, summary) {
  const text = `${title} ${summary}`.toLowerCase();

  for (const [keyword, repo] of Object.entries(CONFIG.github.projectMapping)) {
    if (text.includes(keyword.toLowerCase())) {
      return { keyword, repo };
    }
  }

  return { keyword: 'general', repo: CONFIG.github.projectMapping.simon };
}

/**
 * Parse action items and identify assignees
 */
function parseActionItems(items) {
  // TODO: Parse action items from Fireflies format
  // Extract: description, assignee, deadline, priority

  return items.map(item => ({
    text: item,
    assignee: null, // Extract from item text
    deadline: null,
    priority: 'medium',
  }));
}

/**
 * Extract key decisions from summary
 */
function extractDecisions(summary) {
  // TODO: Use AI or keyword matching to identify decisions
  return [];
}

// ============================================================================
// FILE OPERATIONS
// ============================================================================

/**
 * Save meeting notes to meetings directory
 */
async function saveMeetingNotes(meetingData) {
  const fs = require('fs').promises;
  const path = require('path');

  const dateStr = meetingData.date.toISOString().split('T')[0];
  const filename = `${dateStr}-${sanitizeFilename(meetingData.title)}.md`;
  const filepath = path.join(CONFIG.paths.meetings, filename);

  const content = formatMeetingNotes(meetingData);

  await fs.writeFile(filepath, content, 'utf8');
  console.log('📝 Saved meeting notes:', filepath);
}

/**
 * Format meeting data as markdown
 */
function formatMeetingNotes(data) {
  return `# ${data.title}

**Date:** ${data.date.toLocaleDateString()}
**Project:** ${data.project.keyword}
**Participants:** ${data.participants.join(', ')}

## Summary
${data.summary}

## Action Items
${data.actionItems.map(item => `- [ ] ${item.text}${item.assignee ? ` (@${item.assignee})` : ''}`).join('\n')}

## Key Decisions
${data.decisions.map(d => `- ${d}`).join('\n') || 'None recorded'}

## Keywords
${data.keywords.join(', ')}

---
*Processed by Fireflies webhook automation*
*Transcript ID: ${data.id}*
`;
}

/**
 * Update today's daily note with meeting reference
 */
async function updateDailyNotes(meetingData) {
  // TODO: Append meeting reference to today's daily note
  console.log('📅 Updated daily notes');
}

// ============================================================================
// GITHUB INTEGRATION
// ============================================================================

/**
 * Create GitHub issues for action items
 */
async function createGitHubIssues(meetingData) {
  const { execSync } = require('child_process');

  for (const item of meetingData.actionItems) {
    // Skip if no clear action or already tracked
    if (!shouldCreateIssue(item)) continue;

    const repo = meetingData.project.repo;
    const title = item.text.substring(0, 100); // Truncate long titles
    const body = `From meeting: ${meetingData.title}
Date: ${meetingData.date.toLocaleDateString()}

## Action Item
${item.text}

${item.assignee ? `**Assignee:** @${item.assignee}` : ''}
${item.deadline ? `**Deadline:** ${item.deadline}` : ''}

---
*Auto-created from Fireflies meeting transcript*
*Transcript ID: ${meetingData.id}*
`;

    try {
      // Use gh CLI to create issue
      const command = `gh issue create --repo ${repo} --title "${title}" --body "${body}" --label "meeting-action-item"`;

      console.log('🎫 Creating GitHub issue:', title);
      // Uncomment when ready to test:
      // execSync(command, { stdio: 'inherit' });

    } catch (error) {
      console.error('❌ Failed to create issue:', error.message);
    }
  }
}

/**
 * Determine if action item should become a GitHub issue
 */
function shouldCreateIssue(item) {
  // TODO: Implement logic to filter out non-actionable items
  return item.text.length > 10; // Placeholder
}

// ============================================================================
// DELEGATION MANAGEMENT
// ============================================================================

/**
 * Process delegated items (tasks assigned to others)
 */
async function processDelegatedItems(meetingData) {
  // TODO: Extract items delegated to team members
  // Add to tracking file or system
  console.log('📋 Processed delegated items');
}

// ============================================================================
// UTILITIES
// ============================================================================

function sanitizeFilename(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .substring(0, 50);
}

// ============================================================================
// WEBHOOK SERVER (for local testing)
// ============================================================================

/**
 * Simple Express server for receiving webhooks
 * For production, deploy to Vercel/Netlify/Lambda
 */
function startWebhookServer(port = 3000) {
  const express = require('express');
  const app = express();

  app.use(express.json());

  app.post('/webhook/fireflies', async (req, res) => {
    try {
      await processWebhook(req.body);
      res.json({ success: true });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: error.message });
    }
  });

  app.listen(port, () => {
    console.log(`🚀 Webhook server listening on port ${port}`);
    console.log(`📡 Endpoint: http://localhost:${port}/webhook/fireflies`);
  });
}

// ============================================================================
// MAIN
// ============================================================================

if (require.main === module) {
  // If run directly, start webhook server
  // For production, export processWebhook function

  const args = process.argv.slice(2);

  if (args[0] === 'server') {
    startWebhookServer();
  } else if (args[0] === 'test') {
    // Test with sample payload
    processWebhook({
      event: 'transcript.completed',
      transcript_id: 'test-123',
    }).catch(console.error);
  } else {
    console.log(`
Fireflies Webhook Processor

Usage:
  node process-fireflies-webhook.js server  - Start webhook server
  node process-fireflies-webhook.js test    - Test with sample payload

For production deployment, see docs/fireflies-mcp-setup.md
    `);
  }
}

module.exports = { processWebhook };
