## Agent Collaboration Workflow

### 1. Opportunity Discovery Flow
```
Job Market Analyst
  → identifies opportunities
  → sends to Career Strategy Advisor for strategic review
  → Career Strategy Advisor prioritizes
  → high-priority opportunities sent to Resume Generator + Cover Letter Writer
  → final materials sent to Application Tracker
```

### 2. Application Generation Flow
```
Human selects opportunity from Application Tracker
  → Resume Generator creates targeted resume (pulls from Career Data Manager)
  → Cover Letter Writer creates personalized letter (pulls from Career Data Manager)
  → Human reviews and approves
  → Application Tracker stores materials and updates status
```

### 3. Data Maintenance Flow
```
Human provides new experience/skill
  → Career Data Manager validates and updates schema
  → notifies Career Strategy Advisor for gap analysis update
  → Job Market Analyst refreshes match scores for active opportunities
```

### 4. Strategy Review Flow
```
Weekly: Application Tracker generates metrics
  → Career Strategy Advisor analyzes success patterns
  → recommends strategy adjustments
  → Job Market Analyst adjusts search criteria
  → Resume Generator updates template priorities
```

## Initial Setup Requirements

Each agent requires:
1. Access to career JSON schema (managed by Career Data Manager)
2. Shared configuration file with preferences:
   - Target roles and industries
   - Geographic preferences
   - Salary requirements
   - Work arrangement preferences (remote/hybrid/onsite)
   - Companies to exclude/prioritize
3. API keys and credentials (job boards, research tools)
4. Output directory structure for generated materials
5. Human approval workflows for sensitive operations

## Communication Protocol

Agents communicate via:
- **Structured files**: JSON messages in shared queue directory
- **Status files**: Each agent maintains a status.json with current state
- **Shared database**: Application Tracker maintains central state
- **Human review queue**: Critical decisions placed in review directory

## Human Oversight Points

Human approval required for:
1. Submitting applications
2. Responding to recruiters
3. Accepting/declining interviews
4. Final resume/cover letter approval
5. Salary negotiations
6. Offer acceptance/rejection
7. Strategic career direction changes
8. Sensitive data updates (compensation, employment dates)
