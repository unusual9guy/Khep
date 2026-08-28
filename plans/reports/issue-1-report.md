---
issue: 1
title: Scaffold the workspace
url: https://github.com/unusual9guy/Khep/issues/1
repo: unusual9guy/Khep
state: OPEN
labels: [enhancement, tech-debt]
assignee: none
reportGenerated: 2026-08-28
generatedBy: claude-code /issue-report
---

# Issue 1 — Scaffold the workspace

## 1. TL;DR
The repository has no application runtime yet: `web/` and `parse-service/` do not exist. Issue #1 requests the Phase 1 foundation—a Next.js 14 App Router TypeScript app, a FastAPI/PyMuPDF parser health endpoint, local environment examples, runnable quality commands, and mobile-first styling.

Blast radius is repository-wide and blocks all subsequent Phase 1 work, including database, parser, admin, and staff flows. This is planned foundational work rather than a regression.

## 2. Raw Facts (from issue + comments)
- Reporter intent: Establish the initial Next.js web app and Python/FastAPI parser service with shared local development conventions.
- Expected behavior: `web/` runs a Next.js 14 App Router development server with TypeScript; `parse-service/` exposes a FastAPI health endpoint; environment examples document Supabase, Render, and Cloudflare R2 configuration without secrets; formatter, linter, baseline tests, and mobile-first styling are available and runnable.
- Actual behavior: The repository is still in the planning/specification stage; no `web/` or `parse-service/` directories or package manifests are present.
- Reproduction steps: Not applicable; this is initial scaffolding, not a runtime defect.
- Error text / logs: none.
- Environment hints: Issue identifies the platform as Mobile App and module as Infrastructure. Repository guidance defines a mobile PWA, with Next.js hosted on Vercel, the parser on Render, Supabase for database/auth/realtime/storage, and Cloudflare R2 for product images.
- Comments signal: No comments were posted.

## 3. Research & Deductions
### Implicated code (graph + grep)
- `AGENTS.md:7-12` — repository structure — directs implementation into `web/` and `parse-service/`, with tests in each service, and establishes mobile PWA scope.
- `AGENTS.md:21-30` — development commands — explicitly states the repository is not scaffolded and lists the intended Next.js, parser, and test commands.
- `README.md:20-23` — architecture — confirms the required frontend, parser, Supabase, and R2 technology boundaries.
- `docs/Khep_PRD.md:150-167` — approved architecture — specifies Next.js 14 App Router, stateless FastAPI/PyMuPDF parsing, environment-integrated services, and parser behavior.
- `docs/superpowers/plans/2026-08-25-khep-phase1.md:25-34` — existing implementation plan — maps this issue to creation of `web/`, `parse-service/`, env examples, quality commands, and verification of the dev server, health endpoint, and empty test suites.
- `docs/admin-flow-spec.md:14-15,46-48,114-118` — admin integration flow — establishes the future Next.js-to-Render parser boundary and Supabase persistence/realtime conventions that the scaffold must support.
- Code-review graph — no implicated entities found; graph state was `0 nodes, 0 edges across 0 files`, so targeted `rg`/file inspection was used as the fallback.

### Related flows
- Local development flow: `web/` Next.js dev server → frontend/API layer; `parse-service/` FastAPI service → health and future parse routes.
- Future invoice ingestion: admin UI/API → Supabase Storage → Next.js → Render parser → PyMuPDF extraction → Supabase persistence → Realtime, as described in `docs/admin-flow-spec.md:46-65` and `docs/Khep_PRD.md:279-287`.

### Prior art
- Related issues: `#4 — Build parser contract and fixture harness — OPEN` — follows this scaffold by defining parser models, extractors, and fixtures; `#2 — Establish database and RLS — OPEN` — follows this scaffold with Supabase schema and access policies.
- Linked PRs: None found. The `fixes #1` search and fallback issue-number search returned no pull requests.

## 4. Root-Cause Hypotheses
1. The workspace has not yet received the initial application/service scaffold — evidence: the tracked file list contains documentation only, `AGENTS.md:23` says the repository is not scaffolded, and no `web/` or `parse-service/` paths exist — confidence: high.
2. Baseline developer tooling and environment conventions are absent — evidence: `AGENTS.md:21-30` lists intended commands but no manifests, env examples, formatter/linter configuration, or test runners are present — confidence: high.
3. The mobile-first frontend foundation is deferred with the rest of the scaffold — evidence: issue acceptance criteria require it, while `README.md:29-38` identifies only planning/specification artifacts and no frontend implementation — confidence: high.

## 5. Questions Resolved (from grilling)
- Q: What severity should apply? → A: High-priority foundational enhancement.
- Q: What defines “fixed”? → A: The issue’s acceptance checklist is the complete definition: runnable Next.js app, FastAPI health endpoint, env examples, documented/runnable formatter, linter, baseline tests, and mobile-first styling.
- Q: Is there a reproducible failure and what is the scope? → A: No issue-specific reproduction applies; scope is all developers and environments because the workspace is unscaffolded.
- Q: Is this a regression? → A: No; it is planned initial work.
- Q: Should the stated labels be recorded? → A: Yes; record `enhancement` and `tech-debt` as intended labels, while noting GitHub’s actual label metadata is empty.

## 6. Open Questions / Unknowns
- Exact package-manager choice, Node/Python versions, formatter/linter selections, and test-runner choices are not specified in issue #1; they require an implementation decision or maintainer confirmation.
- Exact health endpoint path and response schema are not specified in issue #1.
- Deployment configuration details for Vercel, Render, Supabase, and R2 are architectural constraints but are not required to resolve the local scaffold acceptance criteria.

## 7. Suggested Next Steps
First, reproduce the baseline by confirming the absence of `web/` and `parse-service/`, then create a `/plan:hard` implementation plan that resolves the package-manager, runtime-tooling, health-route, and env-variable conventions. After `/plan:validate` and user approval, implement the scaffold with TDD and verify every acceptance command.

## 8. Env / Repo Metadata
- branch: `vanshgoenka-tech/scaffold-the-workspace`, commit: `6be3fab — data(catalog): align master catalog with PRD`
- graph: `0 nodes / 0 edges across 0 files` at last build
- repro command(s):
  ```bash
  test ! -d web && test ! -d parse-service
  ```
