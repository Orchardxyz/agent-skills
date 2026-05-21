# Conventional Commit Format

This document specifies the conventional commit format used in this project.

## Format

```
<type>(<scope>): <subject>
```

- **type**: The category of change (required)
- **scope**: The module/component affected (optional but recommended)
- **subject**: A brief description of the change (required)

## Types

| Type | Description |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `chore` | Changes to the build process or auxiliary tools |
| `docs` | Documentation only changes |
| `refactor` | A code change that neither fixes a bug nor adds a feature |
| `style` | Changes that do not affect the meaning of the code |
| `test` | Adding missing tests or correcting existing tests |
| `perf` | A code change that improves performance |

## Scopes

Scopes should be brief and indicate the module or component affected. Common scopes include:

- `auth` - Authentication and authorization
- `api` - API endpoints and routes
- `ui` - User interface components
- `db` - Database schema and queries
- `config` - Configuration files
- `deps` - Dependencies
- `docs` - Documentation
- `tests` - Test files

## Subject

The subject line should:

- Use imperative mood ("add" not "added" or "adds")
- Start with a capital letter
- Not end with a period
- Be concise (50 characters or less)
- Describe what the change does, not why

## Examples

```
feat(auth): add OAuth2 login support
fix(api): resolve null pointer in user endpoint
chore(deps): update React to v18
docs(readme): add installation instructions
refactor(auth-service): simplify token validation
test(user): add tests for registration flow
style(ui): format component code
perf(api): optimize database query performance
```

## Breaking Changes

For breaking changes, add `!` after the type/scope and include a `BREAKING CHANGE:` footer:

```
feat(api)!: remove deprecated endpoint

BREAKING CHANGE: The /api/v1/users endpoint has been removed. Use /api/v2/users instead.
```
