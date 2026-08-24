# Repository Guidelines

## Project Structure & Module Organization

Product requirements and UX references live in `docs/`:

- `Khep_PRD.md` is the source of truth for Phase 1 scope, architecture, schema, security, and testing.
- `staff-flow-spec.md` and `admin-flow-spec.md` define staff packing and admin ingestion behavior.
- `*.html` are prototypes; `Khep_Master_Catalog.xlsx` is catalog input.
- Build the app in `web/` (Next.js 14 App Router) and parser in `parse-service/` (Python/FastAPI). Keep tests in `web/tests/` and `parse-service/tests/`.

Keep extractors behind `extract(pages) -> List[RawOrder]`. Check in migrations and RLS policies. Phase 1 is a mobile PWA, not a native app.

## Admin Flow Rules

- Flag orders with unknown SKUs, do not insert them, and correct them by re-uploading the invoice after fixing the catalog.
- Use the upload date as the dispatch-date fallback for Myntra.
- Read dispatch dates for other platforms from the invoice PDF and route each order by its own date.
- Store valid orders in Supabase and update admin/staff views through Realtime.

## Build, Test, and Development Commands

No commands run because the repository is not scaffolded. Intended commands are:

```text
cd web; npm install; npm run dev       # run Next.js
cd web; npm test                        # run Jest or Vitest
cd parse-service; pip install -r requirements.txt
cd parse-service; pytest                # run parser tests
npx playwright test                     # run realtime browser tests
```

Use environment variables; never commit secrets.

## Coding Style & Naming Conventions

Use the configured formatter and linter. Prefer TypeScript `camelCase`, `PascalCase` components/types, and `kebab-case` routes/files. In Python, use PEP 8, `snake_case`, type hints, and platform-specific extractors.

## Testing Guidelines

Test external behavior. Cover PDF parsing with pytest, API routes with Jest/Vitest, anti-double-packing with two Playwright contexts, and RLS with SQL tests or pgTAP. Include malformed PDFs, unknown SKUs, combos, multi-date routing, Myntra proxy dates, AWB penalties, re-upload correction, and role isolation.

## Commit & Pull Request Guidelines

Use short, scoped conventional messages following `doc(readme) add new readme file`, for example `feat(parser) add myntra extractor`. Keep commits focused. Pull requests must explain the change, list verification commands, link issues, and include UI screenshots. Update docs when decisions change.

## Scope & Security

Do not implement deferred inventory, courier APIs, returns, analytics, multi-warehouse, or customer-facing pages. Enforce admin/staff access through Auth and RLS. Route order status changes through server APIs for AWB validation, points, audit events, and realtime broadcasts. Treat image watermarks and screenshot blocking as deterrents.
