---
name: project-setup
description: >
  Set up and configure Claude Code for a project — detect tech stack, find and install skills from registries (aitmpl.com,
  skills.sh), create custom coding-rules skills, and generate CLAUDE.md with project conventions. MUST use this skill for ANY
  request involving Claude Code project configuration, including: "configure this project", "set up Claude", "bootstrap this
  repo", "detect my stack", "project setup", "create CLAUDE.md", "find skills for [tech]", "what skills exist", "improve my
  Claude setup", "add rules", "generate project config", onboarding to a codebase, or when no CLAUDE.md exists. Also use for
  requests in any language about configuring Claude for a project (e.g. "configura este proyecto", "genera las reglas",
  "configura Claude Code"). If the user mentions skills, CLAUDE.md, project rules, stack detection, or Claude Code setup in
  any form, use this skill.
---

# Project Setup

Detect stack → search registries → install/create skills → generate CLAUDE.md. Confirm with the user before installing or creating anything.

---

## Phase 1: Detect Stack

Use Glob to find indicator files, then Read dependency files to extract frameworks and versions.

| Layer | Indicators |
|-------|-----------|
| Runtime | package.json, pyproject.toml, Cargo.toml, go.mod, Gemfile, *.csproj, composer.json |
| Framework | Read deps for: next, react, vue, django, fastapi, rails, gin, actix, etc. |
| Database | prisma/, knexfile, alembic.ini, ormconfig, drizzle config |
| Styling | tailwind.config, postcss.config, styled-components in deps |
| Testing | jest.config, vitest.config, pytest.ini, cypress.config, playwright.config |
| Linting | .eslintrc*, .prettierrc*, biome.json, .pylintrc, rustfmt.toml |
| Infra | Dockerfile, docker-compose*, vercel.json, .github/workflows/ |
| Monorepo | turbo.json, nx.json, pnpm-workspace.yaml |

See `${CLAUDE_PLUGIN_ROOT}/skills/project-setup/references/stack-indicators.md` for the full file-to-technology mapping.

**Approach:** Glob root + first-level dirs (avoid node_modules). Read the primary dep file. Glob config files in root. Present detected stack as a table and ask the user to confirm.

---

## Phase 2: Search Online Registries

### aitmpl.com (primary — has full JSON API)

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/project-setup/scripts/search_registries.py --stack "nextjs,prisma,tailwind" --types "skills,commands,agents,hooks"
```

Fetches `https://www.aitmpl.com/components.json`, caches 24h, returns scored matches.

### skills.sh (secondary — web search)

```
site:skills.sh {technology}
```

Install format: `npx skills add https://github.com/{owner}/{repo} --skill {skillId}`

Present what exists vs what needs custom creation. Let the user choose.

---

## Phase 3: Install & Create

**Install:** `npx cct@latest --skill|--agent|--command|--hook` (aitmpl.com) or `npx skills add` (skills.sh).

**Create custom skills** for gaps. The process merges two sources:

1. **Rules catalog** — Read ONLY the relevant reference files for the detected stack:
   - Frontend project? → `${CLAUDE_PLUGIN_ROOT}/skills/project-setup/references/rules-frontend.md`
   - Backend project? → `${CLAUDE_PLUGIN_ROOT}/skills/project-setup/references/rules-backend.md`
   - Has DB/testing/infra? → `${CLAUDE_PLUGIN_ROOT}/skills/project-setup/references/rules-shared.md`
   - Skip files for technologies not in the project.

2. **Actual project code** — Read 3-5 representative source files to observe real patterns.

3. **Merge intelligently:**
   - Catalog rules the project follows → include (reinforces conventions)
   - Catalog rules the project violates → skip (project has reasons)
   - Project patterns NOT in catalog → add (most valuable, project-specific)

Place at `.claude/skills/{skill-name}/SKILL.md` with frontmatter. Every rule should be actionable and project-specific.

---

## Phase 4: Generate CLAUDE.md

If none exists, generate. If one exists, offer to enhance.

### What to read from the project

| Source | Extract |
|--------|---------|
| package.json scripts / Makefile / pyproject.toml | Dev commands |
| README.md | Project description |
| Source directory structure (`ls`) | Architecture map |
| Linter/formatter configs | Code style rules |
| 2-3 test files | Testing patterns |
| .env.example | Environment vars |
| CI config | Pipeline info |

### Structure

```markdown
# {Project Name}
{One paragraph: what it does, main technologies}

## Commands
{Actual commands from project scripts/Makefile — use real package manager}

## Architecture
{Actual directories and their purpose — describe what exists}

## Code Conventions
### Frontend
{From rules catalog + project observation — only if project has frontend}
### Backend
{From rules catalog + project observation}

## Testing
{Framework, commands, file patterns, observed conventions}

## Important Patterns
{Non-obvious project-specific patterns only — omit if nothing special}
```

### Code Conventions merge process

Same intelligent merge as custom skills: read the relevant rules catalog files for detected technologies, read actual source files, cross-reference. Include integration patterns (e.g., "Next.js + Prisma" section) when technologies interact.

### Quality criteria

- Every line applies to THIS project — no generic filler
- Every command/path verified against actual codebase
- Under 200 lines for most projects
- Most important conventions first

---

## Phase 5: Summary

Present: what was detected, installed, created, generated. List all files created/modified.

---

## Edge Cases

- **Monorepo**: Detect per package/app, root CLAUDE.md for structure, per-package skills if stacks differ.
- **Empty project**: Ask the user what they're building, create starter CLAUDE.md.
- **Existing CLAUDE.md**: Read first, add missing sections without overwriting.
- **Multiple frameworks**: Detect both (e.g., Next.js FE + Python BE), create skills for each layer.
- **No internet**: Skip registry search, create custom skills offline.
