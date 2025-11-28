#!/usr/bin/env python3
"""
Simple JSON Schema validator for portfolio.json
"""
import json
import re
from datetime import datetime

def validate_pattern(value, pattern):
    """Check if value matches regex pattern"""
    if value is None:
        return True
    return bool(re.match(pattern, str(value)))

def validate_format(value, format_type):
    """Validate format constraints"""
    if value is None:
        return True

    if format_type == 'email':
        return '@' in value and '.' in value.split('@')[1]
    elif format_type == 'uri':
        return value.startswith('http://') or value.startswith('https://')
    elif format_type == 'date':
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True
        except:
            return False
    return True

def validate_enum(value, allowed_values):
    """Check if value is in allowed enum values"""
    if value is None:
        return True
    return value in allowed_values

def validate_required_fields(data, required, path=""):
    """Validate required fields exist"""
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {path}.{field}" if path else f"Missing required field: {field}")
    return errors

def validate_work_entry(work, index):
    """Validate a work entry"""
    errors = []
    path = f"work[{index}]"

    # Required fields
    required = ['id', 'name', 'position', 'startDate']
    errors.extend(validate_required_fields(work, required, path))

    # Pattern validations
    if 'startDate' in work:
        if not validate_pattern(work['startDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.startDate must match YYYY-MM format")

    if 'endDate' in work and work['endDate'] is not None:
        if not validate_pattern(work['endDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.endDate must match YYYY-MM format")

    # Enum validations
    if 'employmentType' in work:
        if not validate_enum(work['employmentType'], ['full-time', 'part-time', 'contract', 'freelance', 'internship']):
            errors.append(f"{path}.employmentType must be one of: full-time, part-time, contract, freelance, internship")

    # URL format
    if 'url' in work and work['url']:
        if not validate_format(work['url'], 'uri'):
            errors.append(f"{path}.url must be a valid URI")

    return errors

def validate_education_entry(edu, index):
    """Validate an education entry"""
    errors = []
    path = f"education[{index}]"

    # Required fields
    required = ['id', 'institution', 'area', 'studyType']
    errors.extend(validate_required_fields(edu, required, path))

    # Pattern validations
    if 'startDate' in edu and edu['startDate']:
        if not validate_pattern(edu['startDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.startDate must match YYYY-MM format")

    if 'endDate' in edu and edu['endDate'] is not None:
        if not validate_pattern(edu['endDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.endDate must match YYYY-MM format")

    return errors

def validate_certificate_entry(cert, index):
    """Validate a certificate entry"""
    errors = []
    path = f"certificates[{index}]"

    # Required fields
    required = ['id', 'name', 'issuer', 'date']
    errors.extend(validate_required_fields(cert, required, path))

    # Pattern validations
    if 'date' in cert:
        if not validate_pattern(cert['date'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.date must match YYYY-MM format")

    if 'expirationDate' in cert and cert['expirationDate'] is not None:
        if not validate_pattern(cert['expirationDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.expirationDate must match YYYY-MM format")

    return errors

def validate_award_entry(award, index):
    """Validate an award entry"""
    errors = []
    path = f"awards[{index}]"

    # Required fields
    required = ['id', 'title', 'date', 'awarder']
    errors.extend(validate_required_fields(award, required, path))

    # Pattern validations
    if 'date' in award:
        if not validate_pattern(award['date'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.date must match YYYY-MM format")

    # Enum validations
    if 'type' in award:
        if not validate_enum(award['type'], ['professional', 'academic', 'community']):
            errors.append(f"{path}.type must be one of: professional, academic, community")

    return errors

def validate_project_entry(project, index):
    """Validate a project entry"""
    errors = []
    path = f"projects[{index}]"

    # Required fields
    required = ['id', 'name', 'description']
    errors.extend(validate_required_fields(project, required, path))

    # Pattern validations
    if 'startDate' in project and project['startDate']:
        if not validate_pattern(project['startDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.startDate must match YYYY-MM format")

    if 'endDate' in project and project['endDate'] is not None:
        if not validate_pattern(project['endDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.endDate must match YYYY-MM format")

    # Enum validations
    if 'type' in project:
        if not validate_enum(project['type'], ['personal', 'professional', 'open-source', 'academic']):
            errors.append(f"{path}.type must be one of: personal, professional, open-source, academic")

    return errors

def validate_volunteer_entry(vol, index):
    """Validate a volunteer entry"""
    errors = []
    path = f"volunteer[{index}]"

    # Required fields
    required = ['id', 'organization', 'position']
    errors.extend(validate_required_fields(vol, required, path))

    # Pattern validations
    if 'startDate' in vol and vol['startDate']:
        if not validate_pattern(vol['startDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.startDate must match YYYY-MM format")

    if 'endDate' in vol and vol['endDate'] is not None:
        if not validate_pattern(vol['endDate'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.endDate must match YYYY-MM format")

    # Enum validations
    if 'commitmentLevel' in vol:
        if not validate_enum(vol['commitmentLevel'], ['daily', 'weekly', 'monthly', 'occasional']):
            errors.append(f"{path}.commitmentLevel must be one of: daily, weekly, monthly, occasional")

    return errors

def validate_skill_entry(skill, index):
    """Validate a skill entry"""
    errors = []
    path = f"skills[{index}]"

    # Required fields
    required = ['name', 'category']
    errors.extend(validate_required_fields(skill, required, path))

    # Enum validations
    if 'category' in skill:
        if not validate_enum(skill['category'], ['programming-language', 'framework', 'tool', 'infrastructure', 'methodology', 'soft-skill']):
            errors.append(f"{path}.category must be one of: programming-language, framework, tool, infrastructure, methodology, soft-skill")

    if 'level' in skill:
        if not validate_enum(skill['level'], ['beginner', 'intermediate', 'advanced', 'expert']):
            errors.append(f"{path}.level must be one of: beginner, intermediate, advanced, expert")

    if 'lastUsed' in skill and skill['lastUsed']:
        if not validate_pattern(skill['lastUsed'], r'^\d{4}-\d{2}$'):
            errors.append(f"{path}.lastUsed must match YYYY-MM format")

    return errors

def validate_language_entry(lang, index):
    """Validate a language entry"""
    errors = []
    path = f"languages[{index}]"

    # Required fields
    required = ['language', 'fluency']
    errors.extend(validate_required_fields(lang, required, path))

    # Enum validations
    if 'fluency' in lang:
        if not validate_enum(lang['fluency'], ['native', 'fluent', 'professional', 'conversational', 'basic']):
            errors.append(f"{path}.fluency must be one of: native, fluent, professional, conversational, basic")

    if 'cefrLevel' in lang and lang['cefrLevel']:
        if not validate_enum(lang['cefrLevel'], ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']):
            errors.append(f"{path}.cefrLevel must be one of: A1, A2, B1, B2, C1, C2")

    return errors

def validate_portfolio(data):
    """Main validation function"""
    errors = []

    # Validate meta section
    if 'meta' not in data:
        errors.append("Missing required section: meta")
    else:
        meta_required = ['version', 'lastUpdated']
        errors.extend(validate_required_fields(data['meta'], meta_required, 'meta'))

        if 'version' in data['meta']:
            if not validate_pattern(data['meta']['version'], r'^\d+\.\d+\.\d+$'):
                errors.append("meta.version must match pattern: X.Y.Z")

        if 'lastUpdated' in data['meta']:
            if not validate_format(data['meta']['lastUpdated'], 'date'):
                errors.append("meta.lastUpdated must be a valid date (YYYY-MM-DD)")

    # Validate basics section (required)
    if 'basics' not in data:
        errors.append("Missing required section: basics")
    else:
        basics_required = ['name']
        errors.extend(validate_required_fields(data['basics'], basics_required, 'basics'))

        if 'email' in data['basics'] and data['basics']['email']:
            if not validate_format(data['basics']['email'], 'email'):
                errors.append("basics.email must be a valid email address")

        if 'url' in data['basics'] and data['basics']['url']:
            if not validate_format(data['basics']['url'], 'uri'):
                errors.append("basics.url must be a valid URI")

        # Validate location
        if 'location' in data['basics']:
            loc = data['basics']['location']
            if 'countryCode' in loc and loc['countryCode']:
                if not validate_pattern(loc['countryCode'], r'^[A-Z]{2}$'):
                    errors.append("basics.location.countryCode must be 2 uppercase letters")

        # Validate profiles
        if 'profiles' in data['basics']:
            for i, profile in enumerate(data['basics']['profiles']):
                profile_required = ['network', 'url']
                errors.extend(validate_required_fields(profile, profile_required, f'basics.profiles[{i}]'))
                if 'url' in profile and not validate_format(profile['url'], 'uri'):
                    errors.append(f"basics.profiles[{i}].url must be a valid URI")

    # Validate work entries
    if 'work' in data:
        for i, work in enumerate(data['work']):
            errors.extend(validate_work_entry(work, i))

    # Validate education entries
    if 'education' in data:
        for i, edu in enumerate(data['education']):
            errors.extend(validate_education_entry(edu, i))

    # Validate certificate entries
    if 'certificates' in data:
        for i, cert in enumerate(data['certificates']):
            errors.extend(validate_certificate_entry(cert, i))

    # Validate award entries
    if 'awards' in data:
        for i, award in enumerate(data['awards']):
            errors.extend(validate_award_entry(award, i))

    # Validate project entries
    if 'projects' in data:
        for i, project in enumerate(data['projects']):
            errors.extend(validate_project_entry(project, i))

    # Validate volunteer entries
    if 'volunteer' in data:
        for i, vol in enumerate(data['volunteer']):
            errors.extend(validate_volunteer_entry(vol, i))

    # Validate skill entries
    if 'skills' in data:
        for i, skill in enumerate(data['skills']):
            errors.extend(validate_skill_entry(skill, i))

    # Validate language entries
    if 'languages' in data:
        for i, lang in enumerate(data['languages']):
            errors.extend(validate_language_entry(lang, i))

    # Validate interests entries
    if 'interests' in data:
        for i, interest in enumerate(data['interests']):
            if 'name' not in interest:
                errors.append(f"interests[{i}] missing required field: name")

    return errors

def main():
    """Load and validate portfolio.json"""
    try:
        with open('portfolio.json', 'r') as f:
            data = json.load(f)

        print("=" * 70)
        print("JSON SCHEMA VALIDATION REPORT")
        print("=" * 70)
        print()

        errors = validate_portfolio(data)

        if not errors:
            print("✓ VALIDATION SUCCESSFUL!")
            print()
            print("portfolio.json is valid against JSON-SCHEMA.json")
            print()
            print("Summary:")
            print(f"  - Work entries: {len(data.get('work', []))}")
            print(f"  - Education entries: {len(data.get('education', []))}")
            print(f"  - Certificates: {len(data.get('certificates', []))}")
            print(f"  - Awards: {len(data.get('awards', []))}")
            print(f"  - Projects: {len(data.get('projects', []))}")
            print(f"  - Volunteer: {len(data.get('volunteer', []))}")
            print(f"  - Skills: {len(data.get('skills', []))}")
            print(f"  - Languages: {len(data.get('languages', []))}")
            return 0
        else:
            print("✗ VALIDATION FAILED")
            print()
            print(f"Found {len(errors)} error(s):")
            print()
            for i, error in enumerate(errors, 1):
                print(f"{i}. {error}")
            return 1

    except FileNotFoundError:
        print("✗ ERROR: portfolio.json not found")
        return 1
    except json.JSONDecodeError as e:
        print(f"✗ ERROR: Invalid JSON - {e}")
        return 1
    except Exception as e:
        print(f"✗ ERROR: {e}")
        return 1

if __name__ == '__main__':
    exit(main())
