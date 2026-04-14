# Shared Rules — Database, Testing, Infra, Security, Integration

Cross-reference with project code — include rules the project follows, skip rules it doesn't use.

## Database & ORM

### Prisma
- Schema as source of truth, `prisma migrate dev` for changes
- Explicit `@relation` with fields/references, `@@index` on queried columns
- `select` specific fields, cursor-based pagination for large datasets
- `$transaction` for atomic multi-model ops, connection pooling in prod

### Drizzle ORM
- TypeScript schema files, `drizzle-kit` for migrations
- Type-safe query builder, `relations()` helper, prepared statements

### SQLAlchemy + Alembic
- Session-per-request, `alembic revision --autogenerate` for changes
- `mapped_column()` (2.0 style), explicit relationship loading
- `create_async_engine` + `AsyncSession` for async frameworks

### TypeORM
- Entities define schema, `typeorm migration:generate`
- Repository pattern, query builder for complex queries
- `@Index()` on queried columns, subscribers for lifecycle hooks

### MongoDB / Mongoose
- Schema with types/validation/defaults, virtuals, pre/post middleware
- `.lean()` for read-only queries, aggregation pipeline
- Compound indexes, population (avoid deep nesting)

---

## Testing

### Jest / Vitest
- `describe`/`it`, Arrange-Act-Assert, `beforeEach`/`afterEach`
- `vi.mock()`/`jest.mock()` at module level, `vi.spyOn()` for methods
- Snapshots only for stable outputs, `data-testid` for selection
- Meaningful coverage — test behavior, not implementation

### pytest
- Fixtures with scope, `@pytest.mark.parametrize` for inputs
- `conftest.py` for shared fixtures, markers for categorization
- `tmp_path`, factory fixtures, `monkeypatch` for env vars

### Cypress / Playwright (E2E)
- Page Object pattern, test isolation, `data-testid` selectors
- Wait for elements/network — never `sleep`
- Intercept network, visual regression, separate from unit in CI

### Testing Library
- Query by role/label/text first, `screen` for queries
- `userEvent` over `fireEvent`, `waitFor` for async
- Test behavior, not implementation details

---

## Infrastructure

### Docker
- Multi-stage builds, non-root user, `.dockerignore`
- Layer caching: deps first, then source
- Health checks, pin base versions, one process per container

### CI/CD — GitHub Actions
- Separate CI/CD workflows, matrix strategy
- Cache deps, secrets via `${{ secrets.NAME }}`
- Concurrency groups, status checks on main

### Kubernetes
- Deployments for stateless, StatefulSets for DBs
- Resource requests+limits, liveness+readiness probes
- ConfigMaps/Secrets, HPA, network policies

---

## Security

### Auth
- bcrypt/argon2 (work factor ≥12), JWT short expiry (15min access, 7d refresh)
- Session regeneration, RBAC/ABAC on every endpoint
- API keys hashed, OAuth validated server-side

### Input Validation
- Validate at system boundaries, parameterized queries
- HTML sanitization for user content, file upload validation
- SSRF prevention with URL allowlists

### HTTP Security
- HTTPS everywhere, security headers (HSTS, CSP, X-Content-Type-Options)
- CORS explicit origins (never `*` with credentials), CSRF tokens
- Rate limiting on auth endpoints, request size limits
- Cookies: Secure, HttpOnly, SameSite=Lax

### Secrets
- No secrets in code/VCS, `.env.example` with dummies
- Different per environment, rotate periodically

---

## Integration Patterns

### Next.js + Prisma
- Prisma singleton in `lib/prisma.ts`, Server Components query directly
- Server Actions for mutations, connection pooling in prod
- Import Prisma generated types in frontend

### Next.js + Tailwind + shadcn/ui
- `cn()` (clsx + tailwind-merge), shadcn in `components/ui/`
- CSS variable theme in `tailwind.config`, dark mode via `next-themes`

### FastAPI + SQLAlchemy
- Async session dependency, Pydantic ↔ SQLAlchemy model mapping
- Alembic configured for async driver

### Django + DRF
- Serializers for validation+serialization, ViewSets for CRUD
- Permissions per view, pagination in settings, django-filter

### React + Testing Library + MSW
- MSW for API mocking, handlers in `src/mocks/`
- Reset between tests, override in specific tests

### Docker + CI/CD
- Build in CI → push to registry → deploy image
- Layer caching with `--cache-from`, health checks in both
- Scan images for vulnerabilities in CI
