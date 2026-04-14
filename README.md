# project-setup

Claude Code plugin that bootstraps any project for Claude Code — detects your tech stack, searches online registries for existing skills, installs what's available, creates custom coding-rules skills for gaps, and generates a CLAUDE.md with project-specific conventions.

## Install

```bash
claude plugin marketplace add avarajar/project-setup-plugin
claude plugin install project-setup@project-setup-marketplace
```

## Usage

In any repo, say something like:

- `configure this project`
- `set up Claude Code for this repo`
- `detect my stack and add skills`
- `/project-setup`

## What it does

1. **Detect stack** — scans project files (package.json, pyproject.toml, go.mod, etc.) to identify frameworks, databases, testing, infra
2. **Search registries** — queries aitmpl.com and skills.sh for existing skills matching your stack
3. **Install & create skills** — installs available skills, creates custom ones for gaps by merging a rules catalog with your actual code patterns
4. **Generate CLAUDE.md** — produces a project-specific config with commands, architecture, conventions, and testing info
