# Resume Input Directory

This directory stores source resume files in various formats for reference and analysis.

## Purpose

- **Historical Reference**: Archive of resume versions over time
- **Data Extraction**: Source material for populating `portfolio.json`
- **Format Examples**: Various formats (PDF, DOCX, TXT, MD) for output generation reference

## Privacy Notice

**⚠️ All files in this directory are EXCLUDED from git via .gitignore**

Resume files contain personally identifiable information (PII) including:
- Full name, contact information
- Employment history and dates
- Educational background
- Skills and certifications
- References

These files remain on your local system only and are never committed to version control.

## Supported Formats

- **PDF** (.pdf) - Most common format for submissions
- **DOCX** (.docx) - Microsoft Word format, editable
- **DOC** (.doc) - Legacy Word format
- **TXT** (.txt) - Plain text, ATS-friendly
- **RTF** (.rtf) - Rich Text Format
- **Markdown** (.md) - With `.ignore` suffix for working drafts

## File Naming Convention

Suggested naming pattern for organization:

```
YYYYMMDD-CompanyName-PositionTitle-YourName.pdf
YYYYMMDD-YourName-Resume.pdf
YourName-PositionType.pdf
```

Examples:
```
20250115-Acme-SeniorEngineer-JohnDoe.pdf
20250115-JohnDoe-Resume.pdf
JohnDoe-SecurityArchitect.pdf
```

## Usage

### With Career Data Manager Agent

The Career Data Manager can analyze resumes in this directory to:
- Extract employment history
- Identify skills and technologies
- Parse certifications and education
- Suggest portfolio.json updates

```bash
@career-data-manager analyze resumes in input/resumes/ and suggest portfolio updates
```

### With Resume Generator Agent

Historical resumes provide examples for formatting and style:

```bash
@resume-generator review previous resume versions in input/resumes/ for formatting reference
```

## Maintenance

- Keep only relevant versions (delete very old or irrelevant files)
- Archive superseded versions periodically
- Maintain at least one current version in multiple formats
- Use `.ignore` suffix for work-in-progress markdown files

## Data Flow

```
input/resumes/*.pdf  →  [Career Data Manager]  →  portfolio.json
                                                        ↓
                                                  [Resume Generator]
                                                        ↓
                                               output/resumes/*.pdf
```

Resume files here are INPUT for data extraction. Generated resumes go to `output/resumes/`.
