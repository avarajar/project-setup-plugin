# Stack Indicator Files

Comprehensive mapping of project files to technologies. Use Glob to check for these files, then Read key dependency files to confirm frameworks and versions.

## Runtime Detection

| File(s) | Technology | Notes |
|---------|-----------|-------|
| `package.json`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `bun.lockb` | **Node.js** | Read package.json for engine version |
| `pyproject.toml`, `requirements.txt`, `setup.py`, `Pipfile`, `poetry.lock` | **Python** | Check pyproject.toml `[tool.poetry]` or `[project]` for version |
| `Cargo.toml`, `Cargo.lock` | **Rust** | Read edition field in Cargo.toml |
| `go.mod`, `go.sum` | **Go** | First line of go.mod has module path and Go version |
| `Gemfile`, `Gemfile.lock` | **Ruby** | Check ruby version constraint |
| `*.csproj`, `*.sln`, `global.json` | **C# / .NET** | TargetFramework in csproj |
| `composer.json`, `composer.lock` | **PHP** | Check require.php version |
| `pubspec.yaml`, `pubspec.lock` | **Dart / Flutter** | sdk constraint in environment |
| `build.gradle`, `build.gradle.kts`, `pom.xml` | **Java / Kotlin** | Check sourceCompatibility or maven compiler |
| `mix.exs` | **Elixir** | Check elixir version in mix.exs |
| `Package.swift` | **Swift** | swift-tools-version comment |
| `Makefile` only (no other lang files) | **C / C++** | Look for gcc/g++/clang references |

## Framework Detection

Read the dependency file to find framework names.

### JavaScript / TypeScript Frameworks
| Dependency | Framework | Config file |
|-----------|-----------|-------------|
| `next` | **Next.js** | `next.config.{js,ts,mjs}` |
| `react` (without next) | **React** (CRA/Vite) | `vite.config.*` or `react-scripts` |
| `vue` | **Vue.js** | `vue.config.js`, `vite.config.*` |
| `nuxt` | **Nuxt** | `nuxt.config.{ts,js}` |
| `@angular/core` | **Angular** | `angular.json` |
| `svelte` | **Svelte** | `svelte.config.js` |
| `astro` | **Astro** | `astro.config.{mjs,ts}` |
| `solid-js` | **SolidJS** | `vite.config.*` |
| `express` | **Express** | — |
| `fastify` | **Fastify** | — |
| `hono` | **Hono** | — |
| `@nestjs/core` | **NestJS** | `nest-cli.json` |
| `remix` or `@remix-run/*` | **Remix** | `remix.config.js` |

### Python Frameworks
| Dependency | Framework | Indicator |
|-----------|-----------|-----------|
| `django` | **Django** | `manage.py`, `settings.py`, `wsgi.py` |
| `fastapi` | **FastAPI** | `uvicorn` in deps |
| `flask` | **Flask** | — |
| `starlette` | **Starlette** | — |
| `tornado` | **Tornado** | — |

### Other Language Frameworks
| Dependency / File | Framework |
|-----------|-----------|
| `rails` in Gemfile | **Ruby on Rails** — also `config/routes.rb` |
| `gin-gonic/gin` in go.mod | **Gin** (Go) |
| `actix-web` in Cargo.toml | **Actix** (Rust) |
| `axum` in Cargo.toml | **Axum** (Rust) |
| `spring-boot` in pom.xml/build.gradle | **Spring Boot** (Java) |
| `laravel/framework` in composer.json | **Laravel** (PHP) |
| `phoenix` in mix.exs | **Phoenix** (Elixir) |

## Database & ORM Detection

| File(s) | Technology |
|---------|-----------|
| `prisma/schema.prisma` | **Prisma** |
| `drizzle.config.{ts,js}` | **Drizzle ORM** |
| `knexfile.{js,ts}` | **Knex.js** |
| `ormconfig.{json,js,ts}` or `typeorm` in deps | **TypeORM** |
| `.sequelizerc` or `sequelize` in deps | **Sequelize** |
| `alembic.ini`, `alembic/` | **SQLAlchemy + Alembic** |
| `sqlalchemy` in deps | **SQLAlchemy** |
| `tortoise` in deps | **Tortoise ORM** (Python) |
| `mongoose` in deps | **Mongoose** (MongoDB) |
| `mongoid` in Gemfile | **Mongoid** (Ruby/MongoDB) |
| `supabase/` or `@supabase/supabase-js` | **Supabase** |
| `firebase` in deps | **Firebase** |

## Styling Detection

| File(s) | Technology |
|---------|-----------|
| `tailwind.config.{js,ts,cjs,mjs}` | **Tailwind CSS** |
| `styled-components` in deps | **styled-components** |
| `@emotion/react` in deps | **Emotion** |
| `*.module.css` or `*.module.scss` files | **CSS Modules** |
| `*.scss` files, `sass` in deps | **Sass/SCSS** |
| `postcss.config.*` | **PostCSS** (check plugins) |
| `@chakra-ui/react` in deps | **Chakra UI** |
| `@mantine/core` in deps | **Mantine** |
| `@mui/material` in deps | **Material UI** |
| `shadcn` config or `components/ui/` pattern | **shadcn/ui** |

## Testing Detection

| File(s) | Technology |
|---------|-----------|
| `jest.config.{js,ts,cjs,mjs}` or `jest` in deps | **Jest** |
| `vitest.config.{js,ts}` or `vitest` in deps | **Vitest** |
| `cypress.config.{ts,js}`, `cypress/` | **Cypress** |
| `playwright.config.{ts,js}` | **Playwright** |
| `pytest.ini`, `pyproject.toml` with `[tool.pytest]` | **pytest** |
| `spec/` dir + `rspec` in Gemfile | **RSpec** |
| `.mocharc.*` or `mocha` in deps | **Mocha** |
| `testing-library` in deps | **Testing Library** |
| `storybook` in deps or `.storybook/` | **Storybook** |

## Linting & Formatting Detection

| File(s) | Technology |
|---------|-----------|
| `.eslintrc*`, `eslint.config.*` | **ESLint** |
| `.prettierrc*`, `prettier.config.*` | **Prettier** |
| `biome.json`, `biome.jsonc` | **Biome** |
| `.stylelintrc*` | **Stylelint** |
| `.pylintrc`, `pylintrc` | **Pylint** |
| `pyproject.toml` with `[tool.black]` | **Black** |
| `pyproject.toml` with `[tool.ruff]`, `ruff.toml` | **Ruff** |
| `rustfmt.toml`, `.rustfmt.toml` | **Rustfmt** |
| `clippy.toml` | **Clippy** (Rust) |
| `.editorconfig` | **EditorConfig** |
| `.rubocop.yml` | **RuboCop** |
| `golangci.yml`, `.golangci.yml` | **golangci-lint** |

## Infrastructure Detection

| File(s) | Technology |
|---------|-----------|
| `Dockerfile`, `.dockerignore` | **Docker** |
| `docker-compose.{yml,yaml}`, `compose.{yml,yaml}` | **Docker Compose** |
| `vercel.json`, `.vercel/` | **Vercel** |
| `netlify.toml` | **Netlify** |
| `fly.toml` | **Fly.io** |
| `Procfile` | **Heroku** |
| `render.yaml` | **Render** |
| `railway.json`, `railway.toml` | **Railway** |
| `firebase.json`, `.firebaserc` | **Firebase** |
| `serverless.yml`, `serverless.ts` | **Serverless Framework** |
| `*.tf`, `terraform.tfvars` | **Terraform** |
| `pulumi.yaml`, `Pulumi.yaml` | **Pulumi** |
| `k8s/`, `kubernetes/`, `kustomization.yaml` | **Kubernetes** |
| `Chart.yaml` | **Helm** |

## CI/CD Detection

| File(s) | Technology |
|---------|-----------|
| `.github/workflows/*.yml` | **GitHub Actions** |
| `.gitlab-ci.yml` | **GitLab CI** |
| `.circleci/config.yml` | **CircleCI** |
| `Jenkinsfile` | **Jenkins** |
| `.travis.yml` | **Travis CI** |
| `azure-pipelines.yml` | **Azure Pipelines** |
| `bitbucket-pipelines.yml` | **Bitbucket Pipelines** |

## Monorepo Detection

| File(s) | Technology |
|---------|-----------|
| `turbo.json` | **Turborepo** |
| `nx.json` | **Nx** |
| `lerna.json` | **Lerna** |
| `pnpm-workspace.yaml` | **pnpm Workspaces** |
| `package.json` with `workspaces` field | **npm/Yarn Workspaces** |
