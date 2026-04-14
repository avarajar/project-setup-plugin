# Backend Rules

Cross-reference with project code — include rules the project follows, skip rules it doesn't use.

## Node.js / Express
- Async/await throughout — no callbacks
- Centralized error handler as last middleware
- Request validation at route level (zod, joi)
- Route → Controller → Service → Repository layering
- Env config: load once at startup, validate, fail fast
- Structured JSON logging with correlation IDs
- Graceful shutdown: `SIGTERM`/`SIGINT`, close connections
- Rate limiting, CORS per environment, Helmet.js, body size limits
- Health check endpoint

## Node.js / Fastify
- Schema validation via JSON Schema/TypeBox (built-in)
- Decorators for shared state, plugins for modular routes
- Lifecycle hooks: `onRequest`, `preValidation`, `preHandler`, `onSend`
- Serialization schemas on responses for performance

## Node.js / NestJS
- Module per domain, constructor DI
- DTOs with class-validator, guards for auth, interceptors for transformation
- Custom decorators, pipes, exception filters
- Repository pattern with TypeORM or Prisma

## Python — General
- Type hints on all signatures and returns
- f-strings, context managers, comprehensions over map/filter
- `pathlib.Path` over `os.path`, `dataclasses`/`pydantic` over raw dicts
- Logging module, not print

## Python / Django
- Fat models, thin views — logic in models or services
- ORM: `select_related()` FK, `prefetch_related()` M2M — avoid N+1
- One migration per logical change, never edit applied migrations
- `get_object_or_404()`, settings split, signals sparingly
- Security: CSRF, `SECURE_SSL_REDIRECT`, rotate `SECRET_KEY`

### Django Anti-patterns
- Don't put logic in views/serializers — extract to services
- Don't raw SQL unless ORM can't express it
- Don't skip migrations or `migrate --fake` without understanding

## Python / FastAPI
- Pydantic v2 for all request/response schemas
- `Depends()` for DI: auth, db sessions, config
- Async for I/O-bound, sync for CPU-bound
- One router per resource in `routers/`
- `BackgroundTasks` for fire-and-forget
- `pydantic-settings` with `.env` support
- Lifespan context manager for startup/shutdown
- `response_model_exclude_unset=True` for partial responses

### FastAPI Anti-patterns
- Don't `async def` for sync blocking code
- Don't skip Pydantic models for raw dicts
- Don't create db sessions outside DI

## Python / Flask
- Application factory (`create_app()`), blueprints
- Flask-SQLAlchemy + Flask-Migrate
- `before_request`/`after_request` hooks, `@app.errorhandler()`

## Go
- `if err != nil` — return errors, never panic
- `fmt.Errorf("context: %w", err)` for error chains
- Interfaces at consumer, accept interfaces return structs
- Table-driven tests with `t.Run()`
- `ctx context.Context` as first parameter everywhere
- Goroutines: channels for communication, `sync.Mutex` for shared state
- `defer` for cleanup, short lowercase singular package names
- Value receiver for reads, pointer for mutations
- DI via struct fields, `internal/` for private code
- Structured logging: `slog` or zerolog/zap

### Go Anti-patterns
- Don't `init()` — explicit init in `main()`
- Don't `panic` for error handling
- Don't ignore errors with `_` unless deliberate
- Don't goroutines without lifecycle management

## Rust
- `Result<T, E>` + `?` for propagation, `thiserror`/`anyhow` for errors
- Exhaustive `match` over `if let` chains
- Move by default, `&` for reads, `&mut` for mutations
- `clippy` clean: `cargo clippy -- -D warnings`
- `#[derive()]` for Debug, Clone, PartialEq, Serialize
- Iterator chains over manual loops, avoid `.unwrap()` in production
- Doc comments `///` on public items

### Rust Anti-patterns
- Don't `.unwrap()` in library code — return `Result`
- Don't clone to satisfy borrow checker without understanding why
- Don't `unsafe` without `// SAFETY:` comment

## Ruby on Rails
- RESTful `resources`, thin controllers + service objects
- ActiveRecord validations, scopes, strong parameters
- `includes()`/`eager_load()` for N+1, Bullet gem in dev
- Sidekiq/ActiveJob for background, RSpec with factories

## PHP / Laravel
- PSR-12, Eloquent, Form Requests for validation
- Resource controllers, service classes, events/listeners
- Queue jobs for background, Blade components
- Config caching in production

## Java / Spring Boot
- Constructor injection, `@RestController`/`@Service`/`@Repository`
- DTOs (never expose entities), `@ControllerAdvice` for errors
- `@Valid` + Bean Validation, Spring Data JPA
- Flyway/Liquibase for migrations, Actuator for health

## Elixir / Phoenix
- Contexts for business boundaries, Ecto changesets
- LiveView for real-time, PubSub, GenServer + supervisors
- Pattern matching in function heads, pipeline `|>`
- ExUnit with setup callbacks
