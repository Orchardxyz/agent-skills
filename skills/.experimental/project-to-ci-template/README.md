# Project to CI Template Skill

This skill helps AI agents analyze projects, create comprehensive summaries, and convert them into reusable CI template projects with GitHub Actions workflows.

## What This Skill Does

When a user asks to "summarize this project" or "make this a CI template", this skill guides the agent through:

1. **Project Analysis** - Understanding the tech stack, architecture, and structure
2. **Documentation Generation** - Creating comprehensive PROJECT_SUMMARY.md with setup instructions
3. **CI/CD Configuration** - Adding GitHub Actions workflows tailored to the project type
4. **Template Preparation** - Making the project reusable with proper documentation and checklists

## Supported Project Types

- **Web Applications** - React, Next.js, Vue, and other frontend frameworks
- **Backend Services** - Node.js, Python, Go APIs and microservices
- **Full-Stack Applications** - Combined frontend and backend projects

## What Gets Generated

### Documentation
- `PROJECT_SUMMARY.md` - Complete project overview with tech stack, architecture, and setup
- Updated `README.md` - Template usage instructions and CI/CD documentation
- `TEMPLATE_CHECKLIST.md` - Step-by-step guide for template users
- `.env.example` - Environment variable template

### CI/CD Workflows
- GitHub Actions workflows customized for the project type
- Lint, test, build, and deployment jobs
- Preview deployments for pull requests
- Production deployment automation

## Directory Structure

```
project-to-ci-template/
├── SKILL.md                    # Main skill instructions
├── README.md                   # This file
├── scripts/                    # (Empty - reserved for future automation scripts)
├── references/
│   ├── github-actions-best-practices.md  # Detailed CI/CD optimization guide
│   └── template-checklist.md             # Complete template conversion checklist
└── assets/
    └── github-actions/
        ├── web-app-ci.yml      # Frontend application workflow
        ├── backend-ci.yml      # Backend service workflow
        ├── full-stack-ci.yml   # Full-stack application workflow
        ├── test-and-lint.yml   # Standalone testing workflow
        └── README.md           # Template usage guide
```

## Example Usage

**User Request:**
> "Summarize this Next.js project and make it a CI template"

**Agent Actions:**
1. Analyzes the project structure and identifies Next.js 14 with TypeScript
2. Generates `PROJECT_SUMMARY.md` with complete tech stack and architecture
3. Copies and customizes `assets/github-actions/web-app-ci.yml` to `.github/workflows/ci.yml`
4. Updates `README.md` with template usage instructions
5. Creates `.env.example` with all required environment variables
6. Generates `TEMPLATE_CHECKLIST.md` for users who clone the template

## Key Features

- **Smart Project Detection** - Automatically identifies frameworks and tools
- **Comprehensive Documentation** - Generates detailed summaries with setup instructions
- **Production-Ready Workflows** - Includes caching, testing, and deployment
- **Security Best Practices** - Proper secrets management and minimal permissions
- **Customizable Templates** - Easy to adapt for specific project needs

## When to Use This Skill

Trigger this skill when users say:
- "Summarize this project"
- "Make this a CI template"
- "Create a template from this project"
- "Document this project with CI/CD setup"
- "Add GitHub Actions to this project"
- "Convert this to a reusable template"

## Requirements

This skill works best when:
- The project has a clear structure and build process
- Dependencies are properly defined in package files
- The project builds successfully locally
- There are no hardcoded secrets or sensitive data

## Related Resources

- [GitHub Actions Best Practices](references/github-actions-best-practices.md)
- [Template Checklist](references/template-checklist.md)
- [Workflow Templates](assets/github-actions/README.md)
