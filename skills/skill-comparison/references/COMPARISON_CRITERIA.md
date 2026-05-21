# Skill Comparison Criteria

This document provides a detailed framework for evaluating and comparing skills systematically.

## Evaluation Dimensions

### 1. Scope & Purpose

**What to assess:**
- Primary problem the skill solves
- Breadth vs. depth of coverage
- Stated use cases and scenarios
- Target audience (beginners, experts, specific domains)

**Questions to answer:**
- Is this a general-purpose or specialized skill?
- Does it solve one problem well or many problems adequately?
- Are the use cases clearly defined?
- Does the scope match the user's needs?

**Rating scale:**
- **Narrow**: Single, well-defined task
- **Medium**: Related set of tasks within a domain
- **Broad**: Multiple tasks across different contexts

### 2. Complexity

**What to assess:**
- Number of steps in the workflow
- Cognitive load required to understand
- External dependencies (tools, libraries, services)
- Setup/configuration requirements
- Learning curve

**Questions to answer:**
- Can a user execute this skill immediately?
- How much prerequisite knowledge is needed?
- Are there multiple moving parts to coordinate?
- What's the time investment to get started?

**Rating scale:**
- **Low**: <5 steps, no dependencies, clear instructions
- **Medium**: 5-15 steps, minimal dependencies, some configuration
- **High**: >15 steps, multiple dependencies, significant setup

### 3. Quality Indicators

**Documentation clarity:**
- Clear, unambiguous instructions
- Logical flow and organization
- Appropriate level of detail
- Grammar and formatting

**Completeness:**
- Examples provided
- Edge cases addressed
- Error handling guidance
- Troubleshooting tips

**Robustness:**
- Input validation
- Graceful failure modes
- Alternative approaches for different scenarios
- Known limitations documented

**Rating scale (1-5 stars):**
- ⭐: Minimal documentation, unclear instructions
- ⭐⭐: Basic documentation, some gaps
- ⭐⭐⭐: Good documentation, covers main cases
- ⭐⭐⭐⭐: Excellent documentation, comprehensive
- ⭐⭐⭐⭐⭐: Outstanding, publication-quality documentation

### 4. Flexibility & Adaptability

**What to assess:**
- Configuration options
- Parameterization
- Extensibility
- Platform/environment compatibility
- Customization potential

**Questions to answer:**
- Can this skill adapt to different contexts?
- Are there configuration points for user preferences?
- Can it be easily modified for edge cases?
- Does it work across different environments?

**Rating scale:**
- **Rigid**: Fixed workflow, no customization
- **Moderate**: Some configuration options
- **Flexible**: Highly configurable, adaptable to various scenarios

### 5. Dependencies & Requirements

**What to assess:**
- External tools required
- Programming language/runtime dependencies
- Operating system constraints
- Network/internet requirements
- Credentials or API keys needed

**Questions to answer:**
- What must be installed before using this skill?
- Are dependencies commonly available?
- Are there platform-specific limitations?
- What are the security implications?

**Impact assessment:**
- **None**: Pure instructions, no external dependencies
- **Light**: Common tools (git, curl, standard CLI utilities)
- **Moderate**: Specific languages/runtimes (Python, Node.js)
- **Heavy**: Multiple tools, services, or specialized software

### 6. Maintenance & Provenance

**What to assess:**
- Author/source information
- Version number
- Last update date (if available)
- License information
- Community/support availability

**Questions to answer:**
- Is this actively maintained?
- Who created it and are they credible?
- Is there a support channel?
- What's the license (can I use/modify it)?

**Trust indicators:**
- Known author or organization
- Version history
- Clear license
- Active maintenance
- User feedback/reviews

### 7. Performance & Efficiency

**What to assess:**
- Execution time
- Resource usage
- Optimization level
- Scalability

**Questions to answer:**
- How fast does this skill execute?
- Does it handle large inputs efficiently?
- Are there performance bottlenecks?
- Will it scale with increased usage?

**Rating scale:**
- **Fast**: Immediate execution, minimal resources
- **Moderate**: Reasonable execution time, standard resources
- **Slow**: Long execution time or high resource usage

## Comparison Matrix Template

Use this template to structure your comparison:

```markdown
| Criterion | Skill A | Skill B | Skill C |
|-----------|---------|---------|---------|
| **Scope** | [Narrow/Medium/Broad] | [Narrow/Medium/Broad] | [Narrow/Medium/Broad] |
| **Complexity** | [Low/Medium/High] | [Low/Medium/High] | [Low/Medium/High] |
| **Documentation** | [⭐⭐⭐⭐] | [⭐⭐⭐] | [⭐⭐⭐⭐⭐] |
| **Flexibility** | [Rigid/Moderate/Flexible] | [Rigid/Moderate/Flexible] | [Rigid/Moderate/Flexible] |
| **Dependencies** | [None/Light/Moderate/Heavy] | [None/Light/Moderate/Heavy] | [None/Light/Moderate/Heavy] |
| **Maintenance** | [Active/Stable/Unknown] | [Active/Stable/Unknown] | [Active/Stable/Unknown] |
| **Performance** | [Fast/Moderate/Slow] | [Fast/Moderate/Slow] | [Fast/Moderate/Slow] |
```

## Contextual Factors

Consider these user-specific factors when making recommendations:

### User Skill Level
- **Beginner**: Prioritize simplicity, clear documentation, minimal dependencies
- **Intermediate**: Balance features with complexity
- **Advanced**: Flexibility and power may outweigh simplicity

### Use Case Frequency
- **One-time use**: Favor simplicity over optimization
- **Occasional use**: Balance ease of use with capability
- **Frequent use**: Efficiency and automation become important

### Environment Constraints
- **Restricted environment**: Minimize dependencies
- **Standard development setup**: More flexibility
- **Cloud/CI environment**: Consider automation and reproducibility

### Time Constraints
- **Immediate need**: Choose ready-to-use, well-documented options
- **Long-term project**: Invest in more comprehensive solutions
- **Learning opportunity**: Consider skills that teach transferable concepts

## Decision Framework

### When Skills Are Similar
If skills score similarly across dimensions:
1. Identify the user's top priority (speed, simplicity, features, etc.)
2. Check for deal-breakers (incompatible dependencies, licensing issues)
3. Consider ecosystem fit (matches user's existing tools/workflows)
4. Recommend based on best alignment with priorities

### When There's a Clear Winner
If one skill significantly outperforms others:
1. Clearly state the recommendation
2. Explain the key advantages
3. Acknowledge any trade-offs
4. Mention when alternatives might be better

### When It Depends
If the best choice varies by context:
1. Present decision criteria clearly
2. Map each skill to specific scenarios
3. Provide "choose X if..." guidance
4. Offer to help narrow down based on more information

## Red Flags

Watch for these warning signs:

- **No examples**: Suggests untested or theoretical skill
- **Vague descriptions**: May indicate unclear purpose or poor design
- **Missing error handling**: Could fail unpredictably
- **Undocumented dependencies**: Setup will be frustrating
- **No version info**: May be outdated or unmaintained
- **Overly complex for simple tasks**: Possible over-engineering
- **No license**: Legal/usage uncertainty

## Best Practices

1. **Be objective**: Base comparisons on observable characteristics
2. **Provide evidence**: Quote specific examples from skills
3. **Consider context**: User needs trump abstract "best"
4. **Acknowledge uncertainty**: If information is missing, say so
5. **Stay current**: Note when information might be outdated
6. **Respect trade-offs**: Every design choice has pros and cons
7. **Empower users**: Give them tools to decide, not just answers
