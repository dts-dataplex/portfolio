# Documentation Directory

This directory contains comprehensive documentation for the career portfolio management system.

## Available Documentation

### [agentic-workflow.md](agentic-workflow.md)
Complete multi-agent system architecture and workflow documentation.

**Contents:**
- System overview and design philosophy
- Agent specifications and responsibilities
- Communication protocols and message formats
- Human oversight and approval workflows
- State management and coordination
- Example workflows and use cases

**Read this to understand:**
- How the 6 agents work together
- When human approval is required
- How agents communicate via message queue
- System state management
- Workflow orchestration patterns

### [portfolio-schema.md](portfolio-schema.md)
JSON Schema documentation for structured career data.

**Contents:**
- Schema design and philosophy
- Field definitions and relationships
- Data validation rules
- Export profiles and privacy controls
- Tagging and categorization system
- Cross-referencing and linking strategies

**Read this to understand:**
- How to structure your career data
- Privacy control options
- Export profile configurations
- Validation requirements
- Best practices for data organization

## Quick Reference

### For New Users

1. **Start here**: Read [portfolio-schema.md](portfolio-schema.md) to understand the data structure
2. **Then read**: [agentic-workflow.md](agentic-workflow.md) to understand agent operations
3. **Finally review**: `../CLAUDE.md` for Claude Code integration details

### For Agent Development

1. **Review**: [agentic-workflow.md](agentic-workflow.md) - Agent specifications section
2. **Check**: `../.claude/agents/` - Active agent definitions
3. **Reference**: `../templates/agents/` - Agent template examples

### For Data Management

1. **Schema**: [portfolio-schema.md](portfolio-schema.md) - Complete field reference
2. **Template**: `../templates/portfolio.template.json` - Example structure
3. **Validation**: `../scripts/validate.py` - Validation script usage

### For Workflow Customization

1. **Architecture**: [agentic-workflow.md](agentic-workflow.md) - Message protocols
2. **System Config**: `../.agent-system/README.md` - System configuration
3. **Agent Specs**: `../.claude/agents/*.md` - Individual agent definitions

## Documentation Standards

### Format
All documentation uses **Markdown** with:
- Clear heading hierarchy (H1, H2, H3)
- Code blocks for examples
- Tables for structured data
- Lists for sequential or grouped information

### Organization
- **Overview first**: Start with purpose and key concepts
- **Details next**: Provide comprehensive specifications
- **Examples last**: Include practical usage examples

### Cross-References
- Link between related documentation
- Reference actual file paths for code examples
- Point to templates and schemas when relevant

## Contributing to Documentation

When updating documentation:

1. **Keep in sync**: Update all related docs when making changes
2. **Version appropriately**: Note significant changes in CLAUDE.md
3. **Test examples**: Verify code examples and commands work
4. **Maintain clarity**: Write for users at different experience levels

## Documentation Maintenance

- Review quarterly for accuracy
- Update when agent specifications change
- Refresh examples with current data patterns
- Expand based on common questions or issues

## Related Files

- `../README.md` - Main project README
- `../CLAUDE.md` - Instructions for Claude Code
- `../.agent-system/README.md` - Agent system status and runtime info
- `../templates/` - Template files referenced in documentation
