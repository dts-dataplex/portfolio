# Building the ultimate career data schema for targeted resumes

**JSON Resume has emerged as the dominant open standard** for structured career data, but it lacks key features needed for dynamic resume generation—notably compensation tracking, privacy controls, and intelligent filtering. A comprehensive schema should extend JSON Resume's **12-section foundation** with salary history, contract work structures, tagging systems, and export profiles that enable generating targeted resumes from a single master data source.

The core challenge is balancing **ATS-parseability** (flat structures, standard keywords) with **rich data modeling** (nested relationships, privacy controls, relevance scoring). This report analyzes existing standards and provides a complete schema recommendation covering all requested sections.

## JSON Resume dominates but has notable gaps

The **JSON Resume standard** (v1.0.0) has become the de facto open-source schema with **400+ themes**, CLI tools, and broad adoption. It defines 12 main sections: basics, work, volunteer, education, awards, certificates, publications, skills, languages, interests, references, and projects. The schema uses JSON Schema draft-07 validation and ISO 8601 dates with flexible precision (YYYY, YYYY-MM, or YYYY-MM-DD).

Other standards serve specific niches. **HR-XML/HR Open Standards** (v4.5) targets enterprise ATS integration with ~350 elements and up to 28 nesting levels—comprehensive but complex. **Europass** provides EU-standardized CVs with CEFR language levels and ISCED education codes. **FRESH/FRESCA** extends beyond JSON Resume with 22 sections including speaking engagements, governance, and work samples—ideal for technical candidates.

**Critical gaps in JSON Resume** for targeted resume generation:
- No compensation/salary fields
- No privacy or visibility controls
- No tagging system for filtering
- No support for contract work with multiple clients
- No mechanism for multiple roles at same organization
- Presentations/speaking not separated from publications

## Date handling requires flexible precision and current-role indicators

All major schemas converge on **ISO 8601** as the date standard, but JSON Resume's implementation stands out for allowing partial dates through a regex pattern: `^([1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]|[1-2][0-9]{3}-[0-1][0-9]|[1-2][0-9]{3})$`. This enables entries like `"2023-04"` (month precision) or `"2023"` (year only) when exact dates aren't known or relevant.

For current positions, the standard approach is **omitting the `endDate` field** rather than using placeholder strings like "present." ATS systems parse "Month YYYY – Present" reliably in rendered output, but the underlying JSON should use null/absent values. Adding an explicit `isCurrent: true` flag provides redundancy for applications that need it.

Employment gaps present an interesting design choice. No standard schema explicitly tracks gaps—they're implicit between entries. For applications tracking career continuity, adding a `breaks` array with `reason` and `type` fields (sabbatical, layoff, caregiving) enables richer narrative generation.

## Multiple roles at one organization need both flat and nested support

JSON Resume uses a **flat structure** where multiple positions at the same company appear as separate work entries with identical `name` fields. This is ATS-optimized but loses the relationship context. HR-XML takes the opposite approach with deeply nested employer containers holding multiple position records.

The recommended hybrid approach uses **flat entries with organizational linking**:

```json
{
  "work": [
    {
      "id": "work_001",
      "organizationId": "org_google",
      "name": "Google",
      "position": "Senior Software Engineer",
      "startDate": "2022-01",
      "promotedFrom": "work_002",
      "transitionType": "promotion"
    },
    {
      "id": "work_002", 
      "organizationId": "org_google",
      "name": "Google",
      "position": "Software Engineer",
      "startDate": "2019-06",
      "endDate": "2021-12"
    }
  ]
}
```

This preserves ATS compatibility (each entry stands alone) while enabling rich display logic (group by `organizationId`, show promotion chains via `promotedFrom`). Adding a `transitionType` enum (promotion, lateral, restructure, acquisition) captures why roles changed.

## Skill proficiency scales vary but categorical levels work best

Research shows **4-5 level categorical scales** outperform numeric ratings. The Dreyfus model (Novice → Advanced Beginner → Competent → Proficient → Expert) has psychological research backing, while simpler scales (Beginner → Intermediate → Advanced → Expert) suffice for most uses. Numeric 1-10 scales are ambiguous and ATS-unfriendly.

JSON Resume's skill structure groups technologies under named categories with a free-text `level` field:

```json
{
  "name": "Backend Development",
  "level": "Expert", 
  "keywords": ["Python", "Node.js", "PostgreSQL"]
}
```

An enhanced structure adds **years of experience** (more objective than self-assessed levels), **last used date** (currency indicator), and **category taxonomy**:

```json
{
  "name": "Python",
  "category": "programming_language",
  "level": "expert",
  "yearsExperience": 7,
  "lastUsed": "2025-11",
  "keywords": ["Django", "FastAPI", "pandas", "asyncio"]
}
```

Include both acronyms and full forms ("JavaScript (JS)") for ATS matching. Avoid creative titles like "Python Ninja"—standard terminology parses reliably.

## Privacy controls require field-level visibility and export profiles

Neither JSON Resume nor most alternatives include privacy controls—a significant gap for schemas storing salary data, personal details, and reference contacts. GDPR requirements demand explicit consent tracking and data classification.

The recommended approach uses **field-level visibility flags** combined with **export profiles**:

```json
{
  "compensation": {
    "baseSalary": {
      "value": 175000,
      "currency": "USD",
      "_visibility": "private"
    }
  },
  "exportProfiles": {
    "public": {
      "include": ["basics.name", "work", "education", "skills"],
      "exclude": ["basics.phone", "compensation"]
    },
    "recruiter": {
      "include": ["*"],
      "exclude": ["compensation.equity"]
    }
  }
}
```

Visibility levels should include: `public` (anyone), `recruiter` (during active job search), `private` (personal records only), and `anonymized` (skills/experience without identifying details). Sensitive fields like salary, SSN, and date of birth should never be schema-required.

## Tagging enables targeted resume generation from master data

The key innovation for generating targeted resumes is a **comprehensive tagging system** at both global and entry levels. Each work experience, project, and skill can carry tags indicating relevance to specific roles, industries, or domains:

```json
{
  "work": [{
    "position": "Data Engineer",
    "tags": ["python", "aws", "data-pipelines", "etl"],
    "industryTags": ["fintech", "payments"],
    "relevantFor": ["senior-data-engineer", "ml-engineer", "backend-lead"]
  }]
}
```

This enables filtering logic: "Generate a resume for Senior ML Engineer roles in healthcare" → include entries where `relevantFor` contains "ml-engineer" OR `industryTags` contains "healthcare" OR `tags` intersects with job description keywords.

Adding **relevance scores** per target role enables intelligent ordering and selection:

```json
{
  "relevanceScores": {
    "data-engineer": 0.95,
    "backend-engineer": 0.70,
    "devops-engineer": 0.40
  }
}
```

## Comprehensive schema recommendation

The following schema extends JSON Resume with all requested sections. It maintains backward compatibility (JSON Resume fields unchanged) while adding compensation, enhanced tagging, privacy controls, and better structure for contracts and presentations.

```json
{
  "$schema": "https://example.com/career-schema/v1.0.0",
  "meta": {
    "version": "1.0.0",
    "lastUpdated": "2025-11-27",
    "canonical": true
  },
  
  "basics": {
    "name": "Full Name",
    "label": "Professional Title",
    "email": "email@example.com",
    "phone": "+1-555-123-4567",
    "url": "https://personalsite.com",
    "summary": "Professional summary paragraph...",
    "location": {
      "city": "San Francisco",
      "region": "California", 
      "countryCode": "US"
    },
    "profiles": [
      {"network": "LinkedIn", "url": "https://linkedin.com/in/username"},
      {"network": "GitHub", "url": "https://github.com/username"}
    ]
  },

  "work": [{
    "id": "work_001",
    "organizationId": "org_001",
    "name": "Company Name",
    "position": "Job Title",
    "employmentType": "full-time",
    "url": "https://company.com",
    "location": "San Francisco, CA",
    "startDate": "2022-01",
    "endDate": null,
    "isCurrent": true,
    "summary": "Role description...",
    "highlights": [
      "Achievement with quantified impact",
      "Led team of 5 engineers"
    ],
    "technologies": ["Python", "AWS", "Kubernetes"],
    "tags": ["backend", "distributed-systems", "leadership"],
    "relevantFor": ["senior-engineer", "tech-lead", "engineering-manager"],
    "promotedFrom": null,
    "transitionType": null
  }],

  "contracts": [{
    "id": "contract_001",
    "type": "consulting",
    "businessName": "Your Consulting LLC",
    "startDate": "2020-01",
    "endDate": "2022-01",
    "summary": "Independent consulting in data engineering",
    "engagements": [{
      "clientName": "Client A",
      "clientIndustry": "fintech",
      "isConfidential": false,
      "engagementType": "project",
      "duration": "6 months",
      "summary": "Built real-time data pipeline",
      "highlights": ["Reduced latency by 80%"],
      "technologies": ["Kafka", "Spark", "AWS"]
    }],
    "tags": ["consulting", "data-engineering"]
  }],

  "compensation": [{
    "workId": "work_001",
    "effectiveDate": "2024-01",
    "baseSalary": {
      "value": 185000,
      "currency": "USD",
      "period": "year"
    },
    "bonus": {
      "target": 30000,
      "currency": "USD",
      "type": "annual"
    },
    "equity": {
      "type": "RSU",
      "grantValue": 200000,
      "vestingSchedule": "4 years with 1-year cliff"
    },
    "_visibility": "private"
  }],

  "projects": [{
    "id": "project_001",
    "name": "Project Name",
    "description": "What the project does...",
    "url": "https://project.com",
    "repository": "https://github.com/user/project",
    "startDate": "2023-06",
    "endDate": "2023-12",
    "highlights": ["Won hackathon", "1000+ GitHub stars"],
    "technologies": ["React", "Node.js", "PostgreSQL"],
    "roles": ["Lead Developer", "Designer"],
    "associatedWork": "work_001",
    "type": "personal",
    "tags": ["open-source", "web-app", "ai"]
  }],

  "education": [{
    "id": "edu_001",
    "institution": "University Name",
    "url": "https://university.edu",
    "area": "Computer Science",
    "studyType": "Bachelor of Science",
    "startDate": "2010-09",
    "endDate": "2014-06",
    "score": "3.8 GPA",
    "honors": ["Magna Cum Laude", "Dean's List"],
    "courses": ["Machine Learning", "Distributed Systems"],
    "thesis": "Thesis title if applicable"
  }],

  "certificates": [{
    "id": "cert_001",
    "name": "AWS Solutions Architect Professional",
    "issuer": "Amazon Web Services",
    "date": "2024-03",
    "expirationDate": "2027-03",
    "credentialId": "ABC123XYZ",
    "url": "https://verify.aws/credential",
    "tags": ["cloud", "aws", "architecture"]
  }],

  "awards": [{
    "id": "award_001",
    "title": "Employee of the Year",
    "date": "2023-12",
    "awarder": "Company Name",
    "summary": "Recognized for technical leadership",
    "type": "professional",
    "url": "https://announcement.url"
  }],

  "publications": [{
    "id": "pub_001",
    "name": "Publication Title",
    "publisher": "Journal/Conference Name",
    "releaseDate": "2023-06",
    "url": "https://doi.org/xxxxx",
    "summary": "Abstract or description",
    "type": "conference-paper",
    "authors": ["Your Name", "Co-author Name"],
    "tags": ["machine-learning", "nlp"]
  }],

  "presentations": [{
    "id": "pres_001",
    "title": "Talk Title",
    "event": "Conference Name 2024",
    "date": "2024-05-15",
    "location": "San Francisco, CA",
    "type": "conference-talk",
    "audience": "500+ attendees",
    "url": "https://conference.com/talk",
    "slidesUrl": "https://slides.com/deck",
    "videoUrl": "https://youtube.com/watch",
    "summary": "Talk description",
    "tags": ["technical", "architecture"]
  }],

  "volunteer": [{
    "id": "vol_001",
    "organization": "Code for America",
    "position": "Technical Mentor",
    "url": "https://codeforamerica.org",
    "startDate": "2021-01",
    "endDate": "2023-06",
    "summary": "Mentored developers on civic tech projects",
    "highlights": ["Mentored 20+ developers"],
    "commitmentLevel": "weekly",
    "tags": ["mentorship", "civic-tech"]
  }],

  "skills": [{
    "name": "Python",
    "category": "programming-language",
    "level": "expert",
    "yearsExperience": 8,
    "lastUsed": "2025-11",
    "keywords": ["Django", "FastAPI", "pandas", "asyncio"]
  },
  {
    "name": "Cloud Architecture",
    "category": "infrastructure",
    "level": "advanced",
    "yearsExperience": 5,
    "lastUsed": "2025-11",
    "keywords": ["AWS", "GCP", "Kubernetes", "Terraform"]
  }],

  "languages": [{
    "language": "English",
    "fluency": "native"
  },
  {
    "language": "Spanish", 
    "fluency": "professional",
    "cefrLevel": "B2"
  }],

  "interests": [{
    "name": "Open Source",
    "keywords": ["Linux", "CNCF projects"]
  }],

  "references": [{
    "name": "Reference Name",
    "relationship": "Former Manager at Company",
    "email": "ref@email.com",
    "phone": "+1-555-000-0000",
    "_visibility": "recruiter"
  }],

  "metadata": {
    "tags": ["software-engineering", "backend", "data", "leadership"],
    "industries": ["fintech", "healthcare", "enterprise-saas"],
    "targetRoles": ["senior-engineer", "staff-engineer", "tech-lead"],
    "workPreferences": {
      "remote": true,
      "hybrid": true,
      "onsite": false,
      "willingToRelocate": ["New York", "Seattle"],
      "visaStatus": "US Citizen"
    }
  },

  "exportProfiles": {
    "public": {
      "include": ["basics", "work", "education", "skills", "projects"],
      "exclude": ["basics.phone", "compensation", "references"]
    },
    "full": {
      "include": ["*"],
      "exclude": ["compensation"]
    }
  }
}
```

## Key schema design decisions explained

**IDs on all entries** enable cross-referencing (projects linking to work entries, compensation records linking to positions) without deep nesting. This maintains the flat, ATS-friendly structure while capturing relationships.

**Separate contracts section** handles freelance/consulting work better than forcing it into the work array. The nested `engagements` array allows tracking multiple clients under one business entity while respecting NDAs with the `isConfidential` flag.

**Compensation as linked records** keeps sensitive salary data separate from work entries, making privacy controls cleaner and enabling historical compensation tracking as salaries change.

**Presentations split from publications** recognizes these as distinct activities with different metadata needs (slides, video, audience size vs. DOI, authors, journal).

**Dual skill metrics** (categorical level + years) provides both the human-readable assessment and objective measure. The `lastUsed` date flags skills that may be rusty.

**Export profiles** at the schema level define what gets included in different resume variants, enabling automatic filtering without manual curation each time.

## Implementation enables targeted resume generation

With this schema populated, generating a targeted resume becomes a filtering and formatting exercise:

1. **Match job posting keywords** against `tags`, `technologies`, and `skills.keywords`
2. **Filter entries** by `relevantFor` arrays matching target role
3. **Select appropriate export profile** based on context (public portfolio vs. recruiter package)
4. **Order by relevance scores** if populated, otherwise by date
5. **Apply template** matching target format (ATS-optimized plain text, designed PDF, LinkedIn import)

The schema's combination of comprehensive data capture, intelligent tagging, and privacy controls creates a **single source of truth** from which any resume variant can be generated—eliminating the need to maintain multiple resume versions manually.

## Using the JSON Schema

The formal JSON Schema definition is available in [`JSON-SCHEMA.json`](./JSON-SCHEMA.json). This schema follows JSON Schema draft 2020-12 and can be used for validation, IDE autocompletion, and generating type definitions.

### Getting started

**1. Create your career data file**

Create a new JSON file (e.g., `my-career.json`) and reference the schema:

```json
{
  "$schema": "./JSON-SCHEMA.json",
  "meta": {
    "version": "1.0.0",
    "lastUpdated": "2025-11-26"
  },
  "basics": {
    "name": "Your Name",
    "label": "Your Professional Title",
    "email": "you@example.com",
    "summary": "Your professional summary..."
  }
}
```

**2. Validate your data**

Using Node.js with [ajv](https://ajv.js.org/):

```bash
npm install ajv ajv-formats
```

```javascript
const Ajv = require("ajv");
const addFormats = require("ajv-formats");
const schema = require("./JSON-SCHEMA.json");
const careerData = require("./my-career.json");

const ajv = new Ajv({ allErrors: true });
addFormats(ajv);

const validate = ajv.compile(schema);
const valid = validate(careerData);

if (!valid) {
  console.error(validate.errors);
} else {
  console.log("Career data is valid!");
}
```

Using Python with [jsonschema](https://python-jsonschema.readthedocs.io/):

```bash
pip install jsonschema
```

```python
import json
from jsonschema import validate, ValidationError

with open("JSON-SCHEMA.json") as f:
    schema = json.load(f)

with open("my-career.json") as f:
    career_data = json.load(f)

try:
    validate(instance=career_data, schema=schema)
    print("Career data is valid!")
except ValidationError as e:
    print(f"Validation error: {e.message}")
```

**3. Enable IDE autocompletion**

Most modern editors (VS Code, JetBrains IDEs) automatically provide autocompletion when you include the `$schema` property pointing to the schema file. For VS Code, you can also configure this in `.vscode/settings.json`:

```json
{
  "json.schemas": [
    {
      "fileMatch": ["*-career.json", "resume.json", "portfolio.json"],
      "url": "./JSON-SCHEMA.json"
    }
  ]
}
```

### Required fields

The schema enforces minimal required fields to stay flexible:

| Section | Required Fields |
|---------|-----------------|
| `basics` | `name` |
| `work[]` | `id`, `name`, `position`, `startDate` |
| `contracts[]` | `id`, `type`, `startDate` |
| `projects[]` | `id`, `name`, `description` |
| `education[]` | `id`, `institution`, `area`, `studyType` |
| `certificates[]` | `id`, `name`, `issuer`, `date` |
| `awards[]` | `id`, `title`, `date`, `awarder` |
| `publications[]` | `id`, `name`, `publisher` |
| `presentations[]` | `id`, `title`, `event`, `date` |
| `volunteer[]` | `id`, `organization`, `position` |
| `skills[]` | `name`, `category` |
| `languages[]` | `language`, `fluency` |
| `interests[]` | `name` |
| `references[]` | `name`, `relationship` |

### Building a complete career record

Start with the basics and incrementally add sections. A recommended order:

1. **basics** — Name, contact info, professional summary
2. **work** — Employment history with highlights and technologies
3. **skills** — Technical and soft skills with proficiency levels
4. **education** — Degrees and relevant coursework
5. **projects** — Side projects, open source contributions
6. **certificates** — Professional certifications
7. **presentations** — Conference talks, workshops, podcasts
8. **publications** — Papers, articles, book chapters
9. **volunteer** — Community involvement
10. **compensation** — Salary history (keep `_visibility: "private"`)
11. **metadata** — Tags, target roles, work preferences
12. **exportProfiles** — Define what to include in different resume variants

### Generating targeted resumes

Once your career data is complete, use the tagging system to generate targeted resumes:

```javascript
function filterForRole(careerData, targetRole) {
  return {
    ...careerData,
    work: careerData.work.filter(job =>
      job.relevantFor?.includes(targetRole) ||
      job.tags?.some(tag => targetRole.includes(tag))
    ),
    projects: careerData.projects.filter(project =>
      project.tags?.some(tag => targetRole.includes(tag))
    ),
    skills: careerData.skills.filter(skill =>
      skill.keywords?.some(kw => targetRole.includes(kw.toLowerCase()))
    )
  };
}

// Generate a resume for "senior-data-engineer" role
const targetedResume = filterForRole(careerData, "senior-data-engineer");
```

### Privacy-aware exports

Use export profiles to control what data is shared:

```javascript
function applyExportProfile(careerData, profileName) {
  const profile = careerData.exportProfiles[profileName];
  if (!profile) return careerData;

  const result = {};
  for (const [key, value] of Object.entries(careerData)) {
    if (profile.exclude?.includes(key)) continue;
    if (profile.include?.includes("*") || profile.include?.includes(key)) {
      result[key] = value;
    }
  }
  return result;
}

// Export public-safe version (no phone, compensation, references)
const publicResume = applyExportProfile(careerData, "public");
```

