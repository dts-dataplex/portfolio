# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a career portfolio schema system for generating targeted resumes from structured career data. It extends the JSON Resume standard with additional features for compensation tracking, privacy controls, intelligent tagging, and export profiles.

## Key Files

- **JSON-SCHEMA.json** — Formal JSON Schema (draft 2020-12) for validating career data
- **EXAMPLE.json** — Example career data document showing all available fields
- **docs/SCHEMA.md** — Schema design documentation and usage instructions
- **YYYYMMDD-YYYYMMDD-CompanyName.md** — Individual work history files (date range format)

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

## Validation

```bash
# Node.js
npm install ajv ajv-formats
node -e "const Ajv=require('ajv');const f=require('ajv-formats');const a=new Ajv();f(a);console.log(a.compile(require('./JSON-SCHEMA.json'))(require('./SCHEMA.json')))"

# Python
pip install jsonschema
python -c "import json;from jsonschema import validate;validate(json.load(open('SCHEMA.json')),json.load(open('JSON-SCHEMA.json')))"
```
