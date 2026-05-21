# Pull Request Format

This document specifies the format for pull requests in this project.

## PR Title

Use the conventional commit format as the PR title:

```
<type>(<scope>): <subject>
```

Examples:
- `feat(auth): add OAuth2 login support`
- `fix(api): resolve null pointer in user endpoint`

## PR Body

Every pull request should include the following sections:

### Summary

A brief description of the changes (1-2 sentences). What does this PR do and why?

### Type

Mark the applicable type(s):

- [ ] Feature (new functionality)
- [ ] Fix (bug fix)
- [ ] Chore (maintenance, dependencies, config)
- [ ] Docs (documentation only)
- [ ] Refactor (code restructuring)
- [ ] Test (test additions or changes)
- [ ] Performance (performance improvements)

### Changes

A bullet list of the key changes included in this PR. Be specific about what was modified.

Example:
- Added OAuth2 authentication flow
- Created new login component with Google/GitHub providers
- Updated auth service to handle OAuth callbacks
- Added error handling for failed OAuth attempts

### Testing

Describe how the changes were tested. If manual testing was performed, describe the steps taken. If automated tests were added, reference them.

Example:
- Tested locally with Google OAuth provider
- Verified token storage and retrieval
- Added unit tests for `OAuthService`
- All existing tests pass

### Checklist

Before submitting, confirm:

- [ ] Code follows project style guidelines
- [ ] Changes have been tested locally
- [ ] Documentation has been updated (if applicable)
- [ ] Changeset has been added (for versioned changes)
- [ ] No sensitive information (API keys, tokens) included

### Related Issues

If this PR addresses an issue, reference it:

- Closes #123
- Related to #456

---

## Example PR

```markdown
## Summary

Adds OAuth2 login support allowing users to authenticate using Google and GitHub accounts.

## Type

- [x] Feature
- [ ] Fix
- [ ] Chore
- [ ] Docs
- [ ] Refactor
- [ ] Test
- [ ] Performance

## Changes

- Added OAuth2 authentication flow
- Created new login component with Google/GitHub providers
- Updated auth service to handle OAuth callbacks
- Added error handling for failed OAuth attempts
- Updated environment configuration with OAuth client IDs

## Testing

- Tested locally with Google OAuth provider
- Verified token storage and retrieval
- Added unit tests for `OAuthService`
- All existing tests pass

### Checklist

- [x] Code follows project style guidelines
- [x] Changes have been tested locally
- [ ] Documentation has been updated (if applicable)
- [x] Changeset has been added (for versioned changes)
- [x] No sensitive information (API keys, tokens) included

### Related Issues

Closes #42
```
