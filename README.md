# project-setup

> Claude Code plugin that bootstraps any project — detects your stack, finds skills, generates CLAUDE.md.

---

## What it does

| Phase | Description |
|-------|-------------|
| **Detect** | Scans project files (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, etc.) to identify frameworks, databases, testing tools, and infrastructure |
| **Search** | Queries [aitmpl.com](https://aitmpl.com) and [skills.sh](https://skills.sh) for existing skills that match your stack |
| **Install & Create** | Installs available skills from registries, creates custom coding-rules skills for anything not covered — merging a rules catalog with patterns observed in your actual code |
| **Generate** | Produces a `CLAUDE.md` tailored to your project with commands, architecture, conventions, and testing info |

## Install

```bash
claude plugin marketplace add avarajar/project-setup-plugin
claude plugin install project-setup@project-setup-marketplace
```

## Usage

Open Claude Code in any repo and say:

```
set up Claude Code for this project
```

Other triggers that work:

- `configure this project` / `configura este proyecto`
- `detect my stack and add skills`
- `bootstrap this repo`
- `create CLAUDE.md`
- `find skills for [technology]`
- `improve my Claude setup`

## Supported stacks

Works with any combination of:

**Frontend** — React, Next.js, Vue, Nuxt, Angular, Svelte, Tailwind CSS

**Backend** — Express, Fastify, NestJS, Django, FastAPI, Flask, Rails, Laravel, Spring Boot, Gin, Actix, Phoenix

**Database** — Prisma, Drizzle, SQLAlchemy, TypeORM, Mongoose

**Testing** — Jest, Vitest, pytest, Cypress, Playwright, Testing Library

**Infrastructure** — Docker, GitHub Actions, Kubernetes, Vercel

**Monorepos** — Turborepo, Nx, pnpm workspaces

## License

MIT
