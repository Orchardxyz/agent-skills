# GitHub Actions Workflow Templates

This directory contains pre-built GitHub Actions workflow templates for different project types.

## Available Templates

### web-app-ci.yml
For frontend web applications (React, Next.js, Vue, etc.)

**Features:**
- Lint, test, and build jobs
- Preview deployments for pull requests
- Production deployment on main branch
- Coverage reporting with Codecov
- Build artifact caching

**Required Secrets:**
- `DEPLOY_TOKEN` - Token for production deployment
- (Optional) `CODECOV_TOKEN` - For coverage reporting

### backend-ci.yml
For backend services (Node.js, Python, Go, etc.)

**Features:**
- Lint, test, and security scanning
- PostgreSQL and Redis service containers
- Docker image building and pushing
- Staging and production deployments
- Database migration support

**Required Secrets:**
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub password/token
- `STAGING_DEPLOY_TOKEN` - Staging deployment token
- `PRODUCTION_DEPLOY_TOKEN` - Production deployment token
- `STAGING_DATABASE_URL` - Staging database connection string
- `PRODUCTION_DATABASE_URL` - Production database connection string

### full-stack-ci.yml
For full-stack applications with separate frontend and backend

**Features:**
- Path-based change detection (only run jobs for changed code)
- Parallel frontend and backend workflows
- E2E testing with Playwright
- Coordinated deployments
- Monorepo support

**Required Secrets:**
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub password/token
- `API_URL` - API endpoint URL
- `FRONTEND_DEPLOY_TOKEN` - Frontend deployment token
- `BACKEND_DEPLOY_TOKEN` - Backend deployment token

### test-and-lint.yml
Standalone testing and linting workflow

**Features:**
- ESLint and Prettier checks
- TypeScript type checking
- Unit tests with coverage
- Matrix testing across Node.js versions
- Security auditing with npm audit and Snyk

**Required Secrets:**
- (Optional) `SNYK_TOKEN` - For Snyk security scanning
- (Optional) `CODECOV_TOKEN` - For coverage reporting

## Usage

1. Choose the appropriate template for your project type
2. Copy the template to `.github/workflows/` in your project
3. Customize the workflow:
   - Update environment variables (Node version, Python version, etc.)
   - Modify build commands to match your project
   - Adjust deployment steps for your infrastructure
   - Configure caching paths if needed
4. Add required secrets to your GitHub repository settings
5. Test the workflow by pushing to a branch or creating a pull request

## Customization Tips

### Changing Node.js Version
```yaml
env:
  NODE_VERSION: '20'  # Change to your desired version
```

### Changing Python Version
```yaml
env:
  PYTHON_VERSION: '3.11'  # Change to your desired version
```

### Modifying Build Commands
Replace the build commands with your project's specific commands:
```yaml
- name: Build application
  run: npm run build  # Change to your build command
```

### Adding Additional Jobs
Add new jobs to the workflow:
```yaml
jobs:
  custom-job:
    name: Custom Job
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: echo "Custom step"
```

### Configuring Deployment
Update deployment steps with your specific deployment logic:
```yaml
- name: Deploy to production
  run: |
    # Add your deployment commands here
    # Examples:
    # - Vercel: vercel --prod --token=${{ secrets.VERCEL_TOKEN }}
    # - Netlify: netlify deploy --prod --auth=${{ secrets.NETLIFY_TOKEN }}
    # - AWS: aws s3 sync dist/ s3://bucket-name
    # - Custom: ./deploy.sh
```

## Best Practices

1. **Use caching** - All templates include dependency caching to speed up workflows
2. **Pin versions** - Consider pinning action versions to specific commits for security
3. **Minimal permissions** - Add `permissions:` block to limit workflow permissions
4. **Concurrency control** - Templates include concurrency settings to prevent duplicate runs
5. **Environment protection** - Use GitHub environments for deployment approvals
6. **Secrets management** - Never hardcode secrets; always use GitHub Secrets
7. **Status badges** - Add workflow status badges to your README

## Adding Status Badges

Add a status badge to your README.md:

```markdown
![CI](https://github.com/username/repo/workflows/CI/badge.svg)
```

Replace `username`, `repo`, and `CI` with your repository details and workflow name.

## Troubleshooting

### Workflow fails on first run
- Check that all required secrets are configured in repository settings
- Verify build commands match your project structure
- Review workflow logs for specific error messages

### Caching not working
- Ensure cache key includes the correct lock file path
- Verify the cache path exists in your project
- Check that dependencies are installed before caching

### Deployment fails
- Verify deployment credentials are correct
- Check that deployment target is accessible
- Review deployment logs for specific errors

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [GitHub Actions Best Practices](../references/github-actions-best-practices.md)
