# Schemas Directory

This directory contains JSON Schema files for validating career portfolio data.

## Files

### portfolio.schema.json
JSON Schema (Draft 2020-12) for validating `portfolio.json` career data.

**Purpose:**
- Define structure and validation rules for career data
- Ensure data quality and completeness
- Enable automated validation
- Provide clear field specifications

**Validation Coverage:**
- Required vs. optional fields
- Data types (string, number, boolean, object, array)
- Date formats (YYYY-MM pattern)
- Enum value validation
- Cross-reference integrity
- URI and email format validation

## Usage

### Python Validation

```bash
# Using included validation script
python3 ../scripts/validate.py

# Using jsonschema directly
pip install jsonschema
python3 -c "import json; from jsonschema import validate; \
validate(json.load(open('../portfolio.json')), \
json.load(open('portfolio.schema.json')))"
```

### Node.js Validation

```bash
# Install dependencies
npm install ajv ajv-formats

# Validate
node -e "const Ajv = require('ajv'); \
const addFormats = require('ajv-formats'); \
const ajv = new Ajv(); \
addFormats(ajv); \
const schema = require('./portfolio.schema.json'); \
const data = require('../portfolio.json'); \
console.log(ajv.validate(schema, data) ? 'Valid' : ajv.errors);"
```

### Command Line (ajv-cli)

```bash
npm install -g ajv-cli
ajv validate -s portfolio.schema.json -d ../portfolio.json
```

## Schema Structure

The schema defines validation rules for all portfolio sections:

### Core Sections
- `basics` - Personal information and contact details
- `work` - Employment history with cross-references
- `education` - Academic background
- `skills` - Technical and soft skills with categorization

### Extended Sections
- `contracts` - Consulting and contract work
- `compensation` - Salary and benefits (with privacy controls)
- `projects` - Personal and professional projects
- `certificates` - Professional certifications
- `awards` - Recognition and achievements
- `publications` - Published works
- `presentations` - Speaking engagements
- `volunteer` - Community involvement
- `languages` - Language proficiency
- `interests` - Professional interests
- `references` - Professional references (with privacy controls)

### Metadata
- `meta` - Schema version and update tracking
- `metadata` - Career goals and preferences
- `exportProfiles` - Resume variant definitions

## Validation Rules

### Date Formats
All dates must use `YYYY-MM` format:
```json
{
  "startDate": "2024-03",
  "endDate": "2025-01"
}
```

Current positions:
```json
{
  "startDate": "2024-03",
  "endDate": null,
  "isCurrent": true
}
```

### Enums
Predefined value sets for consistency:
- `employmentType`: full-time, part-time, contract, internship, freelance
- `skillLevel`: beginner, intermediate, advanced, expert
- `fluency`: elementary, limited, professional, native, bilingual

### Cross-References
IDs must be unique within their section:
```json
{
  "work": [
    {"id": "work_001", ...}
  ],
  "compensation": [
    {"workId": "work_001", ...}  // Must reference existing work ID
  ]
}
```

### Privacy Controls
Fields with `_visibility` property:
```json
{
  "compensation": [{
    "_visibility": "private",  // private | recruiter | public
    "baseSalary": {...}
  }],
  "references": [{
    "_visibility": "recruiter",
    "name": "...",
    "email": "..."
  }]
}
```

## Schema Evolution

### Version Management
The schema version is tracked in `meta.version`:
```json
{
  "$schema": "https://example.com/career-schema/v1.0.0",
  "meta": {
    "version": "1.0.0",
    "lastUpdated": "2025-11-27"
  }
}
```

### Adding New Fields
When extending the schema:
1. Add field to schema definition
2. Mark as optional if not required for existing data
3. Add validation rules and description
4. Update schema version
5. Document in `docs/portfolio-schema.md`
6. Test validation with existing portfolio data

### Breaking Changes
For changes that invalidate existing data:
1. Create new major version (e.g., v1.0.0 → v2.0.0)
2. Provide migration script or documentation
3. Maintain old version for backward compatibility period

## Related Files

- `../portfolio.json` - Your career data (validated against this schema)
- `../templates/portfolio.template.json` - Example data structure
- `../scripts/validate.py` - Validation script
- `../docs/portfolio-schema.md` - Detailed schema documentation

## Validation in Agent Workflow

### Career Data Manager
The Career Data Manager agent uses this schema to:
- Validate changes before committing to portfolio.json
- Suggest corrections for invalid data
- Ensure data quality standards
- Check cross-reference integrity

### Resume Generator
Uses schema to:
- Understand available data fields
- Extract structured information
- Validate export profile configurations
- Ensure required fields are present

## Troubleshooting

### Common Validation Errors

**Date Format Error:**
```
Error: '2024-03-15' is not valid under 'YYYY-MM'
Fix: Use '2024-03' instead
```

**Missing Required Field:**
```
Error: 'name' is a required property
Fix: Add the required field to the object
```

**Invalid Enum Value:**
```
Error: 'fulltime' is not one of ['full-time', 'part-time', ...]
Fix: Use exact enum value 'full-time'
```

**Cross-Reference Error:**
```
Error: workId 'work_099' does not exist
Fix: Ensure referenced ID exists in work array
```

### Validation Tips

1. **Start with template**: Copy `templates/portfolio.template.json`
2. **Validate frequently**: Run validation after each major change
3. **Check examples**: Review template for field format examples
4. **Read errors carefully**: Error messages include field path and expected format
5. **Use JSON linter**: Check for syntax errors before schema validation

## Schema Development

For modifying the schema itself:

1. **Edit**: Update `portfolio.schema.json`
2. **Validate schema**: Ensure schema is valid JSON Schema
3. **Test**: Validate example data against new schema
4. **Document**: Update `docs/portfolio-schema.md`
5. **Version**: Bump version in schema `$id` and examples
