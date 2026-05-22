# AGENTS.md

本仓库用于存放可复用的 Agent Skills。对这个仓库的修改，默认以“保持 skill 规范正确、结构简单清晰”为优先。

## 仓库约定

- 所有 skill 放在 `skills/` 目录下。
- 一个目录对应一个 skill。
- 新增或修改 skill 时，优先保持最小结构，不要引入无关文件。

## 每个 Skill 必须遵循的格式

目录结构至少应为：

```text
skills/<skill-name>/
  SKILL.md
  README.md
```

可选目录：

- `scripts/`
- `references/`
- `assets/`

### 命名规则

- skill 目录名必须与 `SKILL.md` frontmatter 中的 `name` 完全一致。
- 目录名只能使用 kebab-case：小写字母、数字、连字符。
- 不允许空格、下划线、大写、首尾连字符、连续连字符。

## SKILL.md 最低要求

`SKILL.md` 必须以 YAML frontmatter 开头，至少包含：

```yaml
---
name: skill-name
description: 说明这个 skill 做什么，以及什么情况下应该使用它。
---
```

要求：

- `name` 必须等于目录名。
- `description` 不能含糊，必须同时写清“做什么”和“何时使用”。
- 正文保持聚焦，一个 skill 只解决一类问题。
- 说明尽量明确，少写模糊表述，必要时给出步骤或示例。

## README 要求

- 每个 skill 都必须有 `README.md`。
- `README.md` 至少要包含 `Installation` 部分。
- 如果 skill 依赖脚本、运行时或外部工具，要在 README 中写清楚。

## 校验

新增或修改 skill 后，提交前运行：

```bash
npx skills-ref validate ./skills/<skill-name>
```

这一步用于确认：

- 目录名与 `name` 一致
- `description` 存在且格式有效
- frontmatter YAML 合法
- 必填字段没有缺失

如果你不确定某个 skill 是否符合规范，先修到能通过这条校验命令。

## 安全与提交

- 不要写入任何密钥、token、密码或个人敏感信息。
- 需要凭据时，改为从环境变量读取。
- 脚本若会联网或写文件，需在文档中明确说明。
- 不要直接提交到 `main`。
