# GitHub Actions Best Practices

This reference provides detailed best practices for creating efficient, maintainable GitHub Actions workflows.

## Workflow Optimization

### Caching Strategies

#### Node.js Projects
```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

#### Python Projects
```yaml
- name: Cache pip dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

#### Build Artifacts
```yaml
- name: Cache build output
  uses: actions/cache@v3
  with:
    path: |
      .next/cache
      dist/
      build/
    key: ${{ runner.os }}-build-${{ github.sha }}
    restore-keys: |
      ${{ runner.os }}-build-
```

### Concurrency Control

Prevent multiple workflows from running simultaneously:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

For deployments, ensure only one deployment runs at a time:

```yaml
concurrency:
  group: production-deployment
  cancel-in-progress: false
```

### Job Dependencies and Parallelization

Run independent jobs in parallel:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test

  build:
    needs: [lint, test]  # Only run after lint and test succeed
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run build
```

### Matrix Builds

Test across multiple versions:

```yaml
jobs:
  test:
    strategy:
      matrix:
        node-version: [18, 20, 22]
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm test
```

## Security Best Practices

### Secrets Management

Never hardcode secrets:

```yaml
# ❌ Bad
- run: curl -H "Authorization: Bearer ghp_abc123..." https://api.example.com

# ✅ Good
- run: curl -H "Authorization: Bearer ${{ secrets.API_TOKEN }}" https://api.example.com
```

### Minimal Permissions

Use the principle of least privilege:

```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

### Dependency Pinning

Pin action versions to specific commits or tags:

```yaml
# ❌ Bad - uses latest, can break unexpectedly
- uses: actions/checkout@v3

# ✅ Good - pinned to specific version
- uses: actions/checkout@v3.5.2

# ✅ Better - pinned to commit SHA
- uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
```

## Workflow Triggers

### Common Trigger Patterns

```yaml
# Run on push to main and PRs
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

# Run on schedule (daily at 2 AM UTC)
on:
  schedule:
    - cron: '0 2 * * *'

# Manual trigger with inputs
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy to'
        required: true
        type: choice
        options:
          - staging
          - production
```

### Path Filtering

Only run workflows when specific files change:

```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'package.json'
      - '.github/workflows/**'
  pull_request:
    paths-ignore:
      - 'docs/**'
      - '**.md'
```

## Error Handling and Notifications

### Continue on Error

```yaml
- name: Run tests
  run: npm test
  continue-on-error: true

- name: Upload test results even if tests fail
  if: always()
  uses: actions/upload-artifact@v3
  with:
    name: test-results
    path: test-results/
```

### Conditional Steps

```yaml
- name: Deploy to production
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  run: npm run deploy

- name: Comment on PR
  if: github.event_name == 'pull_request'
  uses: actions/github-script@v6
  with:
    script: |
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: 'Build completed successfully! ✅'
      })
```

### Slack/Discord Notifications

```yaml
- name: Notify on failure
  if: failure()
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "Build failed for ${{ github.repository }}",
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "Build failed on branch `${{ github.ref_name }}`\n<${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|View Run>"
            }
          }
        ]
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Environment Management

### Environment Variables

```yaml
env:
  NODE_ENV: production
  API_URL: https://api.example.com

jobs:
  build:
    env:
      BUILD_ENV: production
    steps:
      - name: Build
        env:
          SPECIFIC_VAR: value
        run: npm run build
```

### GitHub Environments

```yaml
jobs:
  deploy:
    environment:
      name: production
      url: https://example.com
    steps:
      - name: Deploy
        run: ./deploy.sh
```

## Reusable Workflows

### Creating a Reusable Workflow

```yaml
# .github/workflows/reusable-test.yml
name: Reusable Test Workflow

on:
  workflow_call:
    inputs:
      node-version:
        required: true
        type: string
    secrets:
      npm-token:
        required: true

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ inputs.node-version }}
      - run: npm ci
        env:
          NPM_TOKEN: ${{ secrets.npm-token }}
      - run: npm test
```

### Using a Reusable Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '20'
    secrets:
      npm-token: ${{ secrets.NPM_TOKEN }}
```

## Composite Actions

Create reusable action steps:

```yaml
# .github/actions/setup-node-project/action.yml
name: 'Setup Node Project'
description: 'Setup Node.js and install dependencies with caching'
inputs:
  node-version:
    description: 'Node.js version'
    required: true
    default: '20'
runs:
  using: 'composite'
  steps:
    - uses: actions/setup-node@v3
      with:
        node-version: ${{ inputs.node-version }}
        cache: 'npm'
    - run: npm ci
      shell: bash
```

Usage:

```yaml
- uses: ./.github/actions/setup-node-project
  with:
    node-version: '20'
```

## Performance Tips

### 1. Use Appropriate Runners

```yaml
jobs:
  # Use ubuntu for most tasks (fastest and cheapest)
  test:
    runs-on: ubuntu-latest

  # Use specific OS only when needed
  test-windows:
    runs-on: windows-latest
    if: contains(github.event.head_commit.message, '[test-windows]')
```

### 2. Skip Redundant Workflows

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    # Skip if commit message contains [skip ci]
    if: "!contains(github.event.head_commit.message, '[skip ci]')"
    runs-on: ubuntu-latest
```

### 3. Artifact Management

```yaml
- name: Upload artifacts
  uses: actions/upload-artifact@v3
  with:
    name: build-output
    path: dist/
    retention-days: 7  # Don't keep artifacts forever
```

## Debugging Workflows

### Enable Debug Logging

Set repository secrets:
- `ACTIONS_RUNNER_DEBUG`: `true`
- `ACTIONS_STEP_DEBUG`: `true`

### SSH Debugging

```yaml
- name: Setup tmate session
  if: failure()
  uses: mxschmitt/action-tmate@v3
  timeout-minutes: 15
```

## Common Patterns

### Monorepo Support

```yaml
jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      frontend: ${{ steps.filter.outputs.frontend }}
      backend: ${{ steps.filter.outputs.backend }}
    steps:
      - uses: actions/checkout@v3
      - uses: dorny/paths-filter@v2
        id: filter
        with:
          filters: |
            frontend:
              - 'apps/frontend/**'
            backend:
              - 'apps/backend/**'

  build-frontend:
    needs: detect-changes
    if: needs.detect-changes.outputs.frontend == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: npm run build:frontend

  build-backend:
    needs: detect-changes
    if: needs.detect-changes.outputs.backend == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: npm run build:backend
```

### Docker Build and Push

```yaml
- name: Build and push Docker image
  uses: docker/build-push-action@v4
  with:
    context: .
    push: true
    tags: |
      user/app:latest
      user/app:${{ github.sha }}
    cache-from: type=registry,ref=user/app:buildcache
    cache-to: type=registry,ref=user/app:buildcache,mode=max
```

### Semantic Versioning

```yaml
- name: Bump version and push tag
  uses: anothrNick/github-tag-action@1.61.0
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    WITH_V: true
    DEFAULT_BUMP: patch
```
