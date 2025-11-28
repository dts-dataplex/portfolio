# Career Portfolio Management System

A multi-agent system for automating job search activities while maintaining structured career data and human decision authority.

## Overview

This repository contains a 6-agent career management framework that:
- Researches and analyzes job opportunities
- Generates ATS-optimized, targeted resumes
- Creates personalized cover letters
- Tracks applications through their lifecycle
- Maintains validated career data in JSON format
- Provides strategic career guidance

## Key Features

- **PII Protection**: Strict separation between public framework and private career data
- **Structured Data**: JSON Schema-validated career portfolio extending JSON Resume standard
- **Multi-Agent Workflow**: 6 specialized agents coordinating via message queue
- **Human Oversight**: Critical decisions (applications, negotiations, offers) require human approval
- **ATS Optimization**: Resume generation optimized for Applicant Tracking Systems
- **Export Profiles**: Multiple resume variants (public, recruiter, full) from single data source

## Directory Structure

```
portfolio/
├── .agent-system/          # Agent workflow infrastructure (excluded from git)
│   ├── queue/             # Inter-agent message queue
│   ├── status/            # Agent status tracking
│   ├── output/            # Generated materials
│   └── README.md          # System status and usage
├── .claude/               # Claude Code agent definitions
│   └── agents/           # Active agent specifications
├── docs/                  # Documentation
│   ├── agentic-workflow.md    # System architecture
│   └── portfolio-schema.md    # Schema documentation
├── input/                 # Source data (excluded from git)
│   ├── resumes/          # Resume files in various formats
│   └── jobs/             # Job posting data
├── output/                # Generated materials (excluded from git)
│   ├── resumes/          # Generated resume files
│   ├── cover_letters/    # Generated cover letters
│   └── reports/          # Analysis and quality reports
├── schemas/               # Validation schemas
│   └── portfolio.schema.json  # Career data JSON Schema
├── scripts/               # Utility scripts
│   └── validate.py       # Portfolio validation script
├── templates/             # Template files (version-controlled examples)
│   ├── agents/           # Agent definition templates
│   ├── portfolio.template.json  # Example career data
│   └── data_quality_report.md   # Report template
├── portfolio.json         # Real career data (EXCLUDED from git)
└── CLAUDE.md             # Instructions for Claude Code
```

## Quick Start

### 1. Setup Career Data

Create your `portfolio.json` from the template:

```bash
cp templates/portfolio.template.json portfolio.json
# Edit portfolio.json with your career information
```

### 2. Validate Career Data

```bash
python3 scripts/validate.py
```

### 3. Use Agents

With Claude Code, reference agents to perform tasks:

```bash
# Analyze job opportunities
@job-market-analyst analyze jobs in ./input/jobs/ and provide match scores

# Generate targeted resume
@resume-generator create resume for Principal Security Architect role

# Write cover letter
@cover-letter-writer draft cover letter for Acme Corp position

# Track application
@application-tracker update status for Acme Corp to "interview scheduled"
```

## The Six Agents

1. **Job Market Analyst** - Identifies opportunities, researches companies, calculates match scores
2. **Career Strategy Advisor** - Provides strategic guidance on career direction and opportunities
3. **Resume Generator** - Creates ATS-optimized resumes targeted to specific roles
4. **Cover Letter Writer** - Generates personalized, compelling cover letters
5. **Application Tracker** - Manages application lifecycle, follow-ups, and metrics
6. **Career Data Manager** - Maintains portfolio.json integrity and data quality

## Privacy & Security

### What's in Git (Public Framework)
- Agent definitions and templates
- JSON Schema for validation
- Documentation and scripts
- Directory structure (.gitkeep files)

### What's NOT in Git (Private Data)
- `portfolio.json` - Your real career data
- `input/resumes/*` - Your resume files
- `input/jobs/**/*` - Job posting data
- `output/**/*` - Generated materials
- `.agent-system/` runtime data

See `.gitignore` for complete exclusion list.

## Portfolio Schema

The career data uses an extended JSON Resume schema with:

- **Cross-referenced data**: Work entries link via IDs to compensation, projects
- **Organizational grouping**: Multiple roles at same company linked via `organizationId`
- **Privacy controls**: Field-level `_visibility` settings (private/recruiter/public)
- **Export profiles**: Generate different resume variants from single data source
- **Tagging system**: Multi-dimensional tags for targeted resume generation

See `docs/portfolio-schema.md` for detailed documentation.

## Agent Workflow

Agents coordinate via:
- **Message Queue**: JSON messages in `.agent-system/queue/`
- **Status Files**: Agent state in `.agent-system/status/`
- **Output Directory**: Generated materials in `.agent-system/output/`
- **Human Review**: Critical decisions in `.agent-system/human-review/`

See `docs/agentic-workflow.md` for detailed architecture.

## Requirements

- Python 3.8+ (for validation)
- jsonschema library (`pip install jsonschema`)
- Claude Code (claude.ai/code) for agent execution

## Contributing

This is a personal career management system. The public repository contains only the framework and templates. To use this system:

1. Clone the repository
2. Copy templates to create your private data files
3. Customize agents to your needs
4. Keep your private data local (already excluded via .gitignore)

## License

Framework: MIT License (see LICENSE file if added)

Your career data: Private, not included in repository

## Documentation

- [Agent Workflow Architecture](docs/agentic-workflow.md)
- [Portfolio Schema Documentation](docs/portfolio-schema.md)
- [Claude Code Instructions](CLAUDE.md)
- [Agent System Status](.agent-system/README.md)

## Support

For questions about the framework itself, open an issue. For questions about your private career data or agent usage, consult the documentation in `docs/`.
