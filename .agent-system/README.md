# Agent Workflow System

This directory contains the infrastructure for the multi-agent career management system described in `agent-workflow.md`.

## System Status

✅ **INITIALIZED** - All agents ready for operation

## Directory Structure

```
.agent-system/
├── config.json              # System configuration and preferences
├── applications.json        # Application tracking database
├── queue/                   # Inter-agent message queue
├── status/                  # Agent status files
│   └── system.json         # Overall system status
├── output/                  # Generated materials
│   ├── resumes/            # Generated resume files
│   ├── cover-letters/      # Generated cover letters
│   └── applications/       # Complete application packages
├── human-review/            # Items awaiting human approval
└── logs/                    # Agent activity logs
```

## Configuration

The `config.json` file contains:
- Target roles and industries
- Geographic and salary preferences
- Work arrangement preferences (remote/hybrid/onsite)
- Agent enablement flags
- Human oversight requirements

**Career Data Source:** `portfolio.json` (validated against JSON-SCHEMA.json)

## Agents

All 6 agents are configured and ready:

1. **Job Market Analyst** - Identifies and researches opportunities
2. **Career Strategy Advisor** - Provides strategic career guidance
3. **Resume Generator** - Creates targeted, ATS-optimized resumes
4. **Cover Letter Writer** - Generates personalized cover letters
5. **Application Tracker** - Manages application lifecycle
6. **Career Data Manager** - Maintains career data integrity

## Usage

### Initialize Workflow
The system is already initialized. To use specific agents:

```bash
# Use Claude Code with agent references
@job-market-analyst analyze the jobs in ./jobs/ and provide match scores
@resume-generator create a resume targeted for Principal Security Architect roles
@cover-letter-writer write a cover letter for the Upstart position
```

### Human Oversight Points

Per `agent-workflow.md`, human approval is required for:
- Submitting applications
- Responding to recruiters
- Accepting/declining interviews
- Final resume/cover letter approval
- Salary negotiations
- Offer acceptance/rejection
- Strategic career direction changes
- Sensitive data updates

Items requiring approval will appear in `human-review/` directory.

## Workflow Flows

### 1. Opportunity Discovery
```
Job Market Analyst → Career Strategy Advisor → Resume/Cover Letter Writers → Application Tracker
```

### 2. Application Generation
```
Human selects opportunity → Resume Generator + Cover Letter Writer → Human reviews → Application Tracker
```

### 3. Data Maintenance
```
Human provides update → Career Data Manager validates → Notifies other agents
```

### 4. Strategy Review (Weekly)
```
Application Tracker metrics → Career Strategy Advisor → Recommendations
```

## Current State

- ✅ Portfolio data validated and loaded (portfolio.json)
- ✅ 9 work history entries (2010-2025)
- ✅ 42 technical skills categorized
- ✅ Job postings collected in `./jobs/` directory
- 📥 Ready to analyze opportunities and generate materials

## Next Steps

1. Run Job Market Analyst on existing job postings
2. Generate targeted resumes for high-priority opportunities
3. Create personalized cover letters
4. Track applications through lifecycle

## API Keys / Credentials

API keys should be stored as environment variables or in a secure vault (not in config.json). Required keys:
- Job board APIs (if using automated searching)
- Web research tools
- Any third-party services

## Maintenance

- Review `applications.json` regularly
- Check `human-review/` for pending decisions
- Monitor `logs/` for agent activity
- Update `config.json` preferences as needed
- Keep `portfolio.json` current via Career Data Manager
