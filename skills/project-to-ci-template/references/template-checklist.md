# Template Checklist

This checklist ensures that a project is properly converted into a reusable CI template.

## Pre-Conversion Checklist

- [ ] Project builds successfully locally
- [ ] All tests pass
- [ ] Dependencies are up to date
- [ ] No hardcoded secrets or sensitive data
- [ ] Project structure is clean and organized

## Documentation Requirements

### PROJECT_SUMMARY.md
- [ ] Overview section with clear project description
- [ ] Complete tech stack listing (frontend, backend, devops)
- [ ] Architecture description with directory structure
- [ ] Key components documented
- [ ] Setup instructions with prerequisites
- [ ] Running locally instructions
- [ ] Deployment instructions
- [ ] Environment variables table
- [ ] API documentation (if applicable)
- [ ] Database schema (if applicable)

### README.md Updates
- [ ] "Using This Template" section added
- [ ] Quick start instructions
- [ ] CI/CD documentation section
- [ ] Required GitHub secrets documented
- [ ] Customization guide included
- [ ] Status badges added (optional but recommended)
- [ ] Links to PROJECT_SUMMARY.md

### TEMPLATE_CHECKLIST.md
- [ ] Step-by-step setup instructions for template users
- [ ] Configuration tasks listed
- [ ] Verification steps included
- [ ] Common issues and solutions

## Configuration Files

### Environment Configuration
- [ ] `.env.example` created with all required variables
- [ ] Each variable has a descriptive comment
- [ ] Example values provided (non-sensitive)
- [ ] `.env` added to `.gitignore`

### Git Configuration
- [ ] `.gitignore` is comprehensive
- [ ] No build artifacts committed
- [ ] No `node_modules/`, `__pycache__/`, etc.
- [ ] No IDE-specific files (unless intentional)

### Package Management
- [ ] Lock files committed (`package-lock.json`, `pnpm-lock.yaml`, etc.)
- [ ] Dependencies are properly categorized (dev vs production)
- [ ] Version ranges are appropriate
- [ ] Scripts are documented in README

## CI/CD Configuration

### GitHub Actions Workflows
- [ ] `.github/workflows/` directory created
- [ ] Main CI workflow added (test, lint, build)
- [ ] Deployment workflow added (if applicable)
- [ ] Workflows use appropriate triggers
- [ ] Caching configured for dependencies
- [ ] Caching configured for build artifacts
- [ ] Matrix builds configured (if testing multiple versions)
- [ ] Concurrency control configured
- [ ] Error handling and notifications set up

### Required Secrets Documentation
- [ ] All required secrets listed in README
- [ ] Purpose of each secret explained
- [ ] Instructions for obtaining secret values
- [ ] Example values provided where safe

### Workflow Testing
- [ ] Workflows syntax is valid
- [ ] Test workflow runs successfully
- [ ] Build workflow runs successfully
- [ ] Deployment workflow runs successfully (in test environment)

## Security Checklist

### Secrets and Credentials
- [ ] No API keys in code
- [ ] No passwords in code
- [ ] No access tokens in code
- [ ] No private keys committed
- [ ] No `.env` files committed
- [ ] Secrets properly referenced via `${{ secrets.SECRET_NAME }}`

### Dependencies
- [ ] No known security vulnerabilities (`npm audit`, `pip-audit`, etc.)
- [ ] Dependencies are from trusted sources
- [ ] Dependency versions are pinned or use safe ranges

### Permissions
- [ ] GitHub Actions permissions are minimal
- [ ] File permissions are appropriate
- [ ] No overly permissive access controls

## Template-Specific Files

### For Template Users
- [ ] `TEMPLATE_CHECKLIST.md` created
- [ ] Clear instructions for first-time setup
- [ ] Customization points identified
- [ ] Verification steps provided

### Cleanup Tasks
- [ ] Remove project-specific code/comments
- [ ] Remove hardcoded values (replace with env vars)
- [ ] Remove personal/company-specific references
- [ ] Generalize naming (if too specific)

## Testing the Template

### Local Testing
- [ ] Clone template to fresh directory
- [ ] Follow setup instructions exactly as written
- [ ] Verify all commands work
- [ ] Run tests successfully
- [ ] Build project successfully
- [ ] Run project locally successfully

### CI/CD Testing
- [ ] Push to GitHub triggers workflows
- [ ] All workflow jobs complete successfully
- [ ] Artifacts are generated correctly
- [ ] Deployments work (if applicable)
- [ ] Notifications work (if configured)

## Final Review

### Code Quality
- [ ] Code follows consistent style
- [ ] No commented-out code blocks
- [ ] No TODO comments (or documented in issues)
- [ ] No debug logging left in production code

### Documentation Quality
- [ ] All documentation is clear and concise
- [ ] No broken links
- [ ] No outdated information
- [ ] Examples are accurate and helpful

### Template Usability
- [ ] Template can be used without modification
- [ ] Customization points are clear
- [ ] Common use cases are covered
- [ ] Edge cases are documented

## Post-Conversion Tasks

### Repository Settings
- [ ] Template repository option enabled on GitHub
- [ ] Topics/tags added for discoverability
- [ ] Description added
- [ ] License file present
- [ ] Contributing guidelines added (optional)

### Maintenance
- [ ] Dependabot configured for dependency updates
- [ ] Issue templates added (optional)
- [ ] PR templates added (optional)
- [ ] Branch protection rules configured (optional)

## Project Type-Specific Checklists

### Web Applications (React, Next.js, Vue)
- [ ] Build output directory in `.gitignore`
- [ ] Static assets properly configured
- [ ] Environment variables for API endpoints
- [ ] Build optimization configured
- [ ] Production build tested

### Backend Services (Node.js, Python, Go)
- [ ] Database connection properly configured
- [ ] Migration scripts documented
- [ ] API documentation generated/updated
- [ ] Health check endpoint implemented
- [ ] Logging configured appropriately

### Full-Stack Applications
- [ ] Frontend and backend coordination documented
- [ ] API contracts defined
- [ ] CORS configuration documented
- [ ] Authentication flow documented
- [ ] Database seeding scripts provided

## Common Issues and Solutions

### Issue: Workflows fail on first run
**Solution**: Check that all required secrets are set in repository settings

### Issue: Build fails with missing dependencies
**Solution**: Ensure lock files are committed and up to date

### Issue: Environment variables not working
**Solution**: Verify `.env.example` is complete and instructions are clear

### Issue: Tests fail in CI but pass locally
**Solution**: Check for environment-specific dependencies or configurations

### Issue: Deployment fails
**Solution**: Verify deployment credentials and target configuration

## Verification Commands

Run these commands to verify the template is ready:

```bash
# Check for hardcoded secrets
git grep -i "api_key\|password\|secret\|token" | grep -v ".md\|.example"

# Check for committed .env files
find . -name ".env" -not -path "*/node_modules/*"

# Validate GitHub Actions workflows
actionlint .github/workflows/*.yml

# Check for security vulnerabilities (Node.js)
npm audit

# Check for security vulnerabilities (Python)
pip-audit

# Verify build works
npm run build  # or appropriate build command

# Verify tests pass
npm test  # or appropriate test command
```

## Success Criteria

The template is ready when:
- ✅ A new user can clone and set up the project in under 10 minutes
- ✅ All workflows pass on first push
- ✅ Documentation answers common questions
- ✅ No secrets or sensitive data are exposed
- ✅ The template is generic enough for reuse
- ✅ Customization points are clear and documented
