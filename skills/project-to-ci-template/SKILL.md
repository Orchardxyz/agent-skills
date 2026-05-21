---
name: project-to-ci-template
description: This skill should be used when the user wants to summarize a project and convert it into a CI template project. It analyzes project structure, tech stack, and architecture, then generates comprehensive documentation and GitHub Actions CI/CD workflows for web applications and backend services. Use this when users say things like "summarize this project", "make this a CI template", "create a template from this project", or "document this project with CI/CD setup".
metadata:
  author: Orchard
  version: "1.0"
---

# Project to CI Template

This skill helps you analyze a project, create a comprehensive summary, and convert it into a reusable CI template with GitHub Actions workflows.

## When to use this skill

Use this skill when the user wants to:
- Summarize an existing project's architecture, tech stack, and structure
- Convert a project into a reusable CI template
- Generate GitHub Actions workflows for a project
- Document a project with setup and deployment instructions
- Create a template repository from an existing codebase

## Workflow

### Step 1: Analyze the Project

First, understand the project structure and technology stack:

1. **Identify the project type**:
   - Check for `package.json` (Node.js/JavaScript/TypeScript)
   - Check for `requirements.txt`, `pyproject.toml`, or `setup.py` (Python)
   - Check for `go.mod` (Go)
   - Check for framework-specific files (Next.js, React, Express, FastAPI, etc.)

2. **Map the directory structure**:
   - List the top-level directories
   - Identify key folders: `src/`, `app/`, `components/`, `api/`, `tests/`, etc.
   - Note configuration files and their purposes

3. **Identify the tech stack**:
   - Frontend framework (React, Next.js, Vue, etc.)
   - Backend framework (Express, FastAPI, Django, etc.)
   - Database (PostgreSQL, MongoDB, Redis, etc.)
   - Build tools (Webpack, Vite, esbuild, etc.)
   - Testing frameworks (Jest, Pytest, Vitest, etc.)

4. **Understand the architecture**:
   - Monorepo vs single package
   - Frontend-only, backend-only, or full-stack
   - API structure and endpoints
   - Database schema and models
   - Authentication/authorization approach

### Step 2: Generate Project Summary

Create a comprehensive `PROJECT_SUMMARY.md` file in the project root with the following sections:

```markdown
# Project Summary

## Overview
[Brief description of what the project does]

## Tech Stack

### Frontend
- Framework: [e.g., Next.js 14, React 18]
- UI Libraries: [e.g., Tailwind CSS, shadcn/ui]
- State Management: [e.g., React Context, Zustand, Redux]

### Backend
- Framework: [e.g., Express.js, FastAPI]
- Runtime: [e.g., Node.js 20, Python 3.11]
- Database: [e.g., PostgreSQL, MongoDB]
- ORM/ODM: [e.g., Prisma, Mongoose]

### DevOps
- Package Manager: [e.g., npm, pnpm, poetry]
- Build Tool: [e.g., Vite, Webpack]
- Testing: [e.g., Jest, Vitest, Pytest]

## Architecture

[Describe the high-level architecture]

### Directory Structure

```
project-root/
├── src/              - [Description]
├── components/       - [Description]
├── api/              - [Description]
├── tests/            - [Description]
└── ...
```

### Key Components

- **[Component/Module Name]**: [Description and purpose]
- **[Component/Module Name]**: [Description and purpose]

## Setup Instructions

### Prerequisites
- [e.g., Node.js 20+, Python 3.11+]
- [e.g., PostgreSQL 15+]

### Installation

```bash
# Clone the repository
git clone [repo-url]

# Install dependencies
[installation commands]

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration
```

### Running Locally

```bash
# Development mode
[dev command]

# Production build
[build command]

# Run tests
[test command]
```

## Deployment

[Deployment instructions and considerations]

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| [VAR_NAME] | [Description] | Yes/No | [Default] |

## API Documentation

[If applicable, describe key API endpoints]

## Database Schema

[If applicable, describe database structure]
```

### Step 3: Create CI/CD Configuration

Generate appropriate GitHub Actions workflows based on the project type. Reference the templates in `assets/github-actions/` and customize them for the specific project.

For **web applications** (React, Next.js, Vue):
- Use the `web-app-ci.yml` template
- Configure build, test, and deployment steps
- Add environment-specific workflows if needed

For **backend services** (Node.js, Python, Go):
- Use the `backend-ci.yml` template
- Configure linting, testing, and deployment
- Add database migration steps if applicable

For **full-stack projects**:
- Combine both templates or create separate workflows
- Ensure proper dependency ordering
- Configure environment variables for both frontend and backend

### Step 4: Add Template Documentation

Create or update `README.md` to include:

1. **Template Usage Section**:
   ```markdown
   ## Using This Template
   
   This repository serves as a CI template for [project type] projects.
   
   ### Quick Start
   1. Click "Use this template" on GitHub
   2. Clone your new repository
   3. Follow the setup instructions below
   4. Customize the CI/CD workflows in `.github/workflows/`
   ```

2. **CI/CD Documentation**:
   - Explain what each workflow does
   - Document required GitHub secrets
   - Provide troubleshooting tips

3. **Customization Guide**:
   - How to modify workflows for specific needs
   - How to add new jobs or steps
   - How to configure deployment targets

### Step 5: Prepare Template Files

1. **Create `.env.example`** if it doesn't exist:
   - List all required environment variables
   - Provide example values (non-sensitive)
   - Add comments explaining each variable

2. **Add `.github/workflows/` directory**:
   - Copy appropriate templates from `assets/github-actions/`
   - Customize for the specific project
   - Test workflows if possible

3. **Create `TEMPLATE_CHECKLIST.md`**:
   - List steps for users who clone the template
   - Include configuration tasks
   - Add verification steps

## Best Practices

### Project Analysis
- Always read the main configuration files (`package.json`, `requirements.txt`, etc.)
- Check for existing CI/CD configurations to understand current setup
- Look for documentation files that might provide context
- Identify dependencies and their versions

### Summary Generation
- Be specific about versions (e.g., "React 18.2" not just "React")
- Include both development and production dependencies
- Document any special setup requirements
- Highlight potential gotchas or common issues

### CI/CD Configuration
- Use caching to speed up workflows (dependencies, build artifacts)
- Implement proper error handling and notifications
- Add status badges to README
- Configure workflows to run on appropriate triggers (push, PR, schedule)
- Use matrix builds for testing multiple versions if applicable

### Template Preparation
- Remove sensitive information (API keys, credentials)
- Use `.env.example` for environment variable templates
- Add clear comments in configuration files
- Include a comprehensive `.gitignore`

## Reference Files

For detailed CI/CD best practices and template structures, see:
- `references/github-actions-best-practices.md` - GitHub Actions optimization and patterns
- `references/template-checklist.md` - Complete checklist for template creation

## Asset Templates

Pre-built GitHub Actions workflow templates are available in `assets/github-actions/`:
- `web-app-ci.yml` - For frontend applications (React, Next.js, Vue)
- `backend-ci.yml` - For backend services (Node.js, Python, Go)
- `full-stack-ci.yml` - For full-stack applications
- `test-and-lint.yml` - Standalone testing and linting workflow

## Example Usage

**User**: "Summarize this Next.js project and make it a CI template"

**Agent Actions**:
1. Analyze the project structure and identify it's a Next.js 14 app with TypeScript
2. Generate `PROJECT_SUMMARY.md` with tech stack, architecture, and setup instructions
3. Copy `assets/github-actions/web-app-ci.yml` to `.github/workflows/ci.yml`
4. Customize the workflow for Next.js (build commands, caching strategy)
5. Update `README.md` with template usage instructions
6. Create `.env.example` with required environment variables
7. Generate `TEMPLATE_CHECKLIST.md` for template users

## Troubleshooting

### Missing Dependencies
If the project analysis is incomplete, check for:
- Monorepo structure (look for `pnpm-workspace.yaml`, `lerna.json`, etc.)
- Multiple package managers (check lock files)
- Custom build scripts in `package.json` or `Makefile`

### Complex Project Structures
For complex projects:
- Break down the summary by modules or packages
- Create separate workflow files for different components
- Document the relationships between components

### CI/CD Configuration Issues
- Verify the project has a working build process locally first
- Check for platform-specific dependencies
- Ensure all required secrets are documented
