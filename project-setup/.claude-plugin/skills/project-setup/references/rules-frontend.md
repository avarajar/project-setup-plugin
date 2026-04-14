# Frontend Rules

Cross-reference with project code — include rules the project follows, skip rules it doesn't use.

## React — Core
- Functional components exclusively — no class components
- Custom hooks for shared stateful logic; prefix with `use`
- One component per file; file name matches component name
- Props destructured in function signature
- Avoid inline object/array literals in JSX props — new references every render
- Conditional rendering: early returns for guards, ternaries inline, `&&` only when falsy can't be `0`
- Fragments over wrapper divs when no DOM node needed
- Key props: stable unique IDs, never array index for dynamic lists
- Controlled inputs by default
- Error boundaries around feature sections
- Avoid `useEffect` for derived state — compute inline or `useMemo`
- Lift state to lowest common ancestor

### React Anti-patterns
- Don't `useEffect` to sync state with props — derive instead
- Don't `setState` in `useEffect` without changing dependency — infinite loop
- Don't spread unknown props onto DOM elements
- Don't mutate state directly — create new references
- Don't create components inside other components — remount on every render

## Next.js — App Router
- Server Components by default — `'use client'` only for browser APIs/event handlers/hooks
- Data fetching: async Server Components with `await`, not `useEffect` + `fetch`
- Route handlers (`route.ts`) for API; Server Actions for form mutations
- `loading.tsx` / `error.tsx` for route-level boundaries
- Metadata: `export const metadata` static, `generateMetadata()` dynamic
- `next/image` with explicit dimensions, `next/link` for navigation
- Parallel routes (`@slot`) for independent loading states
- `notFound()` / `redirect()` from `next/navigation` — throw, don't return
- Middleware for auth/redirects/headers — keep fast
- Streaming via Suspense boundaries for slow sections
- Revalidation: `revalidatePath()` / `revalidateTag()` after mutations
- Env vars: `NEXT_PUBLIC_` for client, without prefix = server only

### Next.js Anti-patterns
- Don't fetch in Client Components when Server Component could
- Don't `router.push()` for simple nav — use `<Link>`
- Don't put `'use client'` at top just because a child needs it — push boundary down
- Don't use `getServerSideProps`/`getStaticProps` — Pages Router, not App Router
- Don't import server-only code in client components

## Vue.js
- Composition API with `<script setup>`
- Composables prefix `use`, return reactive refs
- `defineProps` with TypeScript types, `defineEmits` for typed events
- `computed()` for derived state, never methods for template values
- `watch` for old value/specific sources, `watchEffect` for auto-tracking
- `v-model` with `defineModel()`, `provide`/`inject` with `InjectionKey`
- Keep templates under ~50 lines

### Vue Anti-patterns
- Don't mutate props — emit or `v-model`
- Don't mix Options API and Composition API
- Don't destructure props without `toRefs()`/`toRef()`

## Angular
- Standalone components (Angular 17+), signals for state
- Smart/dumb component separation, services with `providedIn: 'root'`
- Lazy loading via `loadComponent`/`loadChildren`
- `OnPush` change detection, `DestroyRef` + `takeUntilDestroyed()`
- Control flow: `@if`, `@for`, `@switch` (17+)

## Svelte
- Runes (Svelte 5+): `$state()`, `$derived()`, `$effect()`, `$props()`
- `$effect` for side effects only — `$derived` for derived state
- `onclick={handler}` (Svelte 5+), `bind:` for form inputs
- `{#snippet}` for reusable template fragments

## Tailwind CSS
- Utility classes in markup, not CSS files
- Mobile-first: base = mobile, then `sm:`, `md:`, `lg:`
- Theme values over arbitrary values when design system exists
- `@apply` sparingly — only base layer
- Dark mode via `dark:` variant
- Consistent spacing scale

### Tailwind Anti-patterns
- Don't `@apply` to recreate component classes — make components instead
- Don't use arbitrary values for theme colors

## TypeScript (Frontend)
- `strict: true` — non-negotiable
- `interface` for shapes, `type` for unions/intersections
- No `any` — use `unknown` then narrow
- Discriminated unions for state: `{ status: 'loading' } | { status: 'success'; data: T }`
- `satisfies` for type checking with preserved inference
- Avoid `as` assertions — prefer type guards

## CSS General
- CSS custom properties for design tokens
- Logical properties for i18n, `clamp()` for fluid sizing
- `gap` over margins for flex/grid children
- `prefers-reduced-motion` for animation a11y

## Accessibility
- Semantic HTML: `button` for actions, `a` for nav, landmarks
- `aria-label` on interactive elements without visible text
- Keyboard nav: all interactive focusable, logical tab order
- Focus styles: never `outline: none` without replacement
- Color contrast: 4.5:1 normal, 3:1 large text
- Alt text: descriptive for content, `alt=""` for decorative
- Form labels on every input
