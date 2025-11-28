# Job Postings Input Directory

This directory stores job posting data collected from various sources for analysis and matching.

## Purpose

- **Opportunity Collection**: Centralized storage for job postings of interest
- **Match Analysis**: Input for Job Market Analyst to calculate fit scores
- **Resume Targeting**: Source data for tailoring resumes to specific roles
- **Tracking Reference**: Links applications to original job descriptions

## Privacy Notice

**⚠️ All files in this directory are EXCLUDED from git via .gitignore**

Job postings may contain:
- Company-specific information
- Confidential project details
- Salary ranges
- Application tracking URLs with tokens

These files remain on your local system only.

## Directory Organization

Organize job postings by source or company:

```
input/jobs/
├── greenhouse/           # Jobs from Greenhouse ATS
├── oracle/               # Oracle Taleo postings
├── ziprecruiter/         # ZipRecruiter listings
├── linkedin/             # LinkedIn job posts
├── company-direct/       # Direct company websites
└── recruiters/           # Recruiter-sourced opportunities
```

## Supported Formats

- **JSON** (.json) - Structured job data
- **Markdown** (.md) - Formatted job descriptions
- **HTML** (.html) - Raw HTML from job boards
- **PDF** (.pdf) - Saved job posting PDFs
- **TXT** (.txt) - Plain text job descriptions

## File Naming Convention

Recommended naming pattern:

```
YYYYMMDD-CompanyName-PositionTitle.json
CompanyName-JobID-PositionSlug.md
```

Examples:
```
20250115-Acme-SeniorSecurityArchitect.json
Acme-123456-senior-security-architect.md
```

## JSON Structure (Recommended)

```json
{
  "job_id": "acme_sec_arch_001",
  "posted_date": "2025-01-15",
  "company": "Acme Corporation",
  "position": "Senior Security Architect",
  "location": "Remote",
  "salary_range": "$150k-$200k",
  "url": "https://jobs.acme.com/posting/123456",
  "description": "Full job description text...",
  "requirements": [
    "8+ years security experience",
    "Cloud security expertise",
    "CISSP or equivalent"
  ],
  "technologies": ["AWS", "Azure", "Kubernetes", "Python"],
  "application_deadline": "2025-02-15",
  "source": "linkedin",
  "notes": "Strong cultural fit, emphasis on DevSecOps"
}
```

## Usage

### With Job Market Analyst

```bash
# Analyze all jobs in directory
@job-market-analyst analyze jobs in input/jobs/ and calculate match scores

# Focus on specific source
@job-market-analyst analyze greenhouse jobs for Principal Security roles

# Research specific company
@job-market-analyst research Acme Corporation and assess cultural fit
```

### With Resume Generator

```bash
# Generate targeted resume
@resume-generator create resume for input/jobs/acme/senior-security-architect.json
```

### With Cover Letter Writer

```bash
# Generate personalized cover letter
@cover-letter-writer write cover letter for input/jobs/acme/senior-security-architect.json
```

## Data Collection Methods

### Manual Collection
- Copy/paste job description into text file
- Save web page as PDF or HTML
- Screenshot and OCR if needed

### Automated Collection
- Browser extensions (save to folder)
- Web scraping scripts (check terms of service)
- Email parsing (forward jobs to processing folder)
- API integration (LinkedIn, Indeed, etc.)

## Best Practices

1. **Collect Early**: Save job postings as soon as you find them (they may be removed)
2. **Preserve Original**: Keep original formatting for accurate analysis
3. **Add Context**: Include notes about how you found the posting
4. **Track Deadlines**: Note application deadlines
5. **Link Applications**: Reference job file in application tracking

## Data Flow

```
Job Boards/Sites  →  input/jobs/*.json  →  [Job Market Analyst]
                                                    ↓
                                          Match scores + analysis
                                                    ↓
                              [Resume Generator] + [Cover Letter Writer]
                                                    ↓
                                           output/resumes/*.pdf
                                           output/cover_letters/*.pdf
                                                    ↓
                                          [Application Tracker]
```

## Maintenance

- Archive applied/rejected jobs periodically
- Keep current opportunities in main directories
- Delete duplicate entries
- Update job status as positions close
