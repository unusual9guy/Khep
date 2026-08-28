# Khep

Khep is an internal packing and shipping automation tool for Chitra Goenka Crafts & Creations, a D2C home decor brand selling through Amazon, Myntra, Flipkart, and Pepperfry.

## What It Does

Khep turns platform shipping-invoice PDFs into a shared, date-organized packing queue:

1. An admin uploads an invoice PDF.
2. Khep detects the platform and extracts orders, AWBs, SKUs, quantities, and dispatch dates.
3. Platform SKUs are mapped to the Master Catalog, and combo products are expanded into components.
4. Staff view consolidated products and platform-grouped orders on a mobile PWA.
5. Staff scan the shipping-label barcode to validate the AWB before marking an order packed.
6. Supabase Realtime removes packed orders from all staff screens and notifies the admin.

The system also provides role-based access, audit logging for AWB mismatches, watermarked product images, staff points, and a leaderboard.

## Architecture

- **Frontend:** Next.js 14 App Router, deployed to Vercel
- **Parser:** Python/FastAPI with PyMuPDF, deployed to Render
- **Database and authentication:** Supabase PostgreSQL, Auth, Realtime, and Storage
- **Product images:** Cloudflare R2 with short-lived signed URLs

The repository is currently in the planning and specification stage. Implementation details and approved Phase 1 scope are documented in [`docs/Khep_PRD.md`](docs/Khep_PRD.md).

## Documentation

- [`docs/Khep_PRD.md`](docs/Khep_PRD.md) - product requirements, architecture, schema, security, and testing decisions
- [`docs/admin-flow-spec.md`](docs/admin-flow-spec.md) - admin invoice-upload flow
- [`docs/staff-flow-spec.md`](docs/staff-flow-spec.md) - staff packing flow and data model
- [`docs/khep-flows.html`](docs/khep-flows.html) - product flow reference
- [`docs/staff-flow-prototype.html`](docs/staff-flow-prototype.html) - staff interface prototype
- [`AGENTS.md`](AGENTS.md) - contributor guidelines

## Local Development

The repository contains two independently runnable services. Copy each
`.env.example` to `.env` or `.env.local` as appropriate and add credentials
only to your local environment.

### Web app

```text
cd web
npm install
npm run dev
```

The web app runs at `http://localhost:3000`.

```text
npm run format:check
npm run lint
npm test
npm run build
```

### Parse service

```text
cd parse-service
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The liveness endpoint is `GET http://localhost:8000/health` and returns the
service status. `POST /parse` is intentionally a typed placeholder until the
parser contract and extractors are implemented in issue #4. It requires the
`X-Parser-Api-Key` header matching the server-only `PARSER_API_KEY` value and
accepts HTTPS URLs only.

```text
pytest
ruff check app tests
ruff format --check app tests
```

GitHub Actions runs the same formatting, linting, test, and build checks for
web changes and parser changes on pushes and pull requests.

## Phase 1 Boundaries

Phase 1 does not include inventory management, courier API integrations, returns/RTO, analytics dashboards, multiple warehouses, customer-facing features, or a native mobile app.
