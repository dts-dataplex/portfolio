# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a multi-agent career management system that automates job searching, resume generation, cover letter writing, and application tracking using structured career data. The system consists of 6 specialized agents working together to help manage the job search process while maintaining human oversight at critical decision points.

## Key Files and Directories

### Core Configuration
- **schemas/portfolio.schema.json** — JSON Schema (draft 2020-12) for validating career data
- **templates/portfolio.template.json** — Example career data document showing all available fields
- **portfolio.json** — Real career data (EXCLUDED from git - contains PII)
- **scripts/validate.py** — Python script to validate portfolio.json against schema

### Documentation
- **docs/agentic-workflow.md** — Multi-agent system architecture and workflow documentation
- **docs/portfolio-schema.md** — Schema design documentation and usage instructions

### Agent Definitions
- **.claude/agents/** — Agent definitions for Claude Code integration
- **templates/agents/** — Template versions of agent definitions

### Data Storage
- **input/resumes/** — Resume files in various formats (EXCLUDED from git - contains PII)
- **input/jobs/** — Job posting data organized by source (EXCLUDED from git - may contain sensitive data)
- **output/** — Generated resumes, cover letters, and reports (EXCLUDED from git - contains PII)
- **.agent-system/** — Agent workflow infrastructure and state management

## Schema Architecture

The schema uses a flat-with-linking approach for ATS compatibility while preserving relationships:

- **Cross-references via IDs**: Work entries have `id` fields; compensation records link via `workId`; projects link to work via `associatedWork`
- **Organizational grouping**: Multiple roles at same company share `organizationId` and link via `promotedFrom`
- **Privacy controls**: Fields with `_visibility` property (`private`, `recruiter`, `public`)
- **Export profiles**: Define include/exclude rules for different resume variants
- **Tagging system**: `tags`, `relevantFor`, and `industryTags` arrays enable filtering for targeted resumes

## Schema Sections

The 16 top-level sections: `basics`, `work`, `contracts`, `compensation`, `projects`, `education`, `certificates`, `awards`, `publications`, `presentations`, `volunteer`, `skills`, `languages`, `interests`, `references`, `metadata`, `exportProfiles`

## Date Format

All dates use ISO 8601 with YYYY-MM precision (e.g., `"2024-03"`). Current positions use `null` for `endDate` with `isCurrent: true`.

## PII Protection

**CRITICAL**: This repository separates public framework code from private career data.

### Files EXCLUDED from Git (contain PII):
- `portfolio.json` — Real career data with personal information
- `input/resumes/*` — All resume files (PDF, DOCX, TXT, etc.)
- `input/jobs/**/*` — Job posting data (may contain company-specific information)
- `output/**/*` — Generated resumes, cover letters, reports
- `.agent-system/applications.json` — Application tracking data
- `.agent-system/config.json` — Personal configuration and preferences
- `.agent-system/output/**/*` — Agent-generated materials
- `.agent-system/status/system.json` — System state

### Files INCLUDED in Git (templates and framework):
- `templates/portfolio.template.json` — Example structure with placeholder data
- `templates/agents/*.md` — Agent definition templates
- `.claude/agents/*.md` — Active agent definitions
- `schemas/portfolio.schema.json` — Validation schema
- Documentation and scripts

## Multi-Agent System

### Agent Roster
1. **Job Market Analyst** — Researches opportunities, calculates match scores
2. **Career Strategy Advisor** — Provides strategic guidance and recommendations
3. **Resume Generator** — Creates ATS-optimized, targeted resumes
4. **Cover Letter Writer** — Generates personalized cover letters
5. **Application Tracker** — Manages application lifecycle and follow-ups
6. **Career Data Manager** — Maintains portfolio.json integrity

### Workflow Integration
Agents communicate via JSON messages in `.agent-system/queue/` and maintain state in `.agent-system/status/`. See `docs/agentic-workflow.md` for detailed architecture.

### Human Oversight
The system requires human approval for:
- Submitting applications
- Responding to recruiters
- Interview scheduling
- Salary negotiations
- Strategic direction changes
- Final resume/cover letter versions

## Portfolio Data Validation

```bash
# Validate portfolio.json against schema
python3 scripts/validate.py

# Python validation from command line
pip install jsonschema
python -c "import json;from jsonschema import validate;validate(json.load(open('portfolio.json')),json.load(open('schemas/portfolio.schema.json')))"
```

## Repository Setup Decisions

### Directory Structure
- **Separation of concerns**: Public framework vs. private data
- **Agent definitions**: Duplicated in `.claude/agents/` (active) and `templates/agents/` (reference)
- **Input organization**: Separate directories for resumes and job postings
- **Output organization**: Structured by type (resumes, cover letters, reports)

### Privacy Strategy
- Comprehensive .gitignore to prevent PII leakage
- Template files use generic placeholder data
- Real data stays local and is excluded from version control
- .gitkeep files maintain directory structure without committing contents

### Workflow Philosophy
- Agents automate research and content generation
- Human maintains final decision authority
- State management enables asynchronous agent coordination
- Message queue enables inter-agent communication
