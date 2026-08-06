# V3 Requirements Traceability Matrix

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation branch:** `feature/product-database`  
**Record maintained by:** @Chu-Junjie  
**Document state:** Prepared for formal review and final acceptance updates

## 1. Record basis

This matrix is maintained from repository evidence and the team meeting notes recorded by @Chu-Junjie. Meeting decisions define scope and responsibilities, but they do not replace formal GitHub Reviews, automated test output, deployed-environment checks or acceptance evidence.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| Implemented | The requirement is represented in the named repository baseline. |
| Verified | A named check passed for a named commit and environment. |
| Not Run | The required verification has not been executed. |
| Blocked | A required dependency or check prevents completion. |
| Deferred | The requirement is outside the current release commitment. |
| Done | All applicable implementation, review, verification and release gates have passed. |

## 3. Named responsibilities

| Area | Named responsibility |
|---|---|
| Backend, API, authentication, recommendation, automated tests and CI interpretation | @ZhengZaikun |
| Database schema, catalogue, importer, provenance, PostgreSQL, persistence and recovery | @tiantian09091 |
| Frontend, GitHub Pages, responsive behaviour, accessibility and browser flows | @Guanyu-Lu |
| Meeting notes, status, traceability, acceptance coordination and release records | @Chu-Junjie |

## 4. User-story traceability

| ID | Requirement | Repository evidence | Current status | Required review or verification |
|---|---|---|---|---|
| US-01 | Accept structured product preferences and validate input | `server.py`, `index.html`, `test_server.py` | Implemented; canonical API tests passed for the recorded PR ref | @ZhengZaikun confirms API behaviour; @Guanyu-Lu verifies deployed input and error states |
| US-02 | Import and query the product catalogue | `server.py`, `import_real_catalog.py`, `digital_products.db`, `product_specs` schema | Repository verified; runtime database gate open | @tiantian09091 verifies disposable counts, joins, duplicates, orphans and PostgreSQL initialization; @ZhengZaikun confirms API integration |
| US-03 | Present ranked recommendations, separate Top 5 and pagination | `server.py`, `index.html`, `test_server.py` | Implemented; API coverage exists; deployed E2E Not Run | @ZhengZaikun confirms ranking/pagination contract; @Guanyu-Lu verifies desktop/mobile behaviour |
| US-04 | Explain why a product was recommended | recommendation response and UI result-card rendering | Implemented; deployed presentation Not Run | @ZhengZaikun confirms explanation generation; @Guanyu-Lu verifies readable presentation |
| US-05 | Compare supported products | `/api/compare`, comparison interface, canonical API tests | Implemented; deployed E2E Not Run | @ZhengZaikun confirms API limits and validation; @Guanyu-Lu verifies two/three-product comparison |
| US-06 | Apply selected exclusions and preference filters | recommendation parsing/filtering and interface controls | Implemented; deployed boundary checks Not Run | @ZhengZaikun confirms filter semantics; @Guanyu-Lu verifies interface state and error handling |
| US-07 | Provide transparent product/source links | `PurchaseURL`, `DataSource`, product-card link handling | Implemented with historical-source limitation; deployed link review Not Run | @tiantian09091 confirms source/provenance fields; @Guanyu-Lu verifies link and fallback behaviour |
| US-08 | Record recommendation feedback | feedback endpoint, table and interface action | Implemented; deployed persistence Not Run | @ZhengZaikun confirms API validation; @tiantian09091 verifies persistence; @Guanyu-Lu verifies UI response |
| US-09 | Identify a cheaper equivalent alternative | no current backend response field or canonical acceptance case | Deferred; backlog `Unscheduled` | @ZhengZaikun and @Guanyu-Lu formally review PR #47; current E2E verifies budget filtering only |
| US-10 | Share and restore recommendation state | current frontend share-state flow | Implemented representation; deployed isolated-session restoration Not Run | @Guanyu-Lu executes share restoration; @ZhengZaikun confirms no private API data is exposed |

## 5. Cross-cutting traceability

| Requirement | Repository evidence | Current status | Required review or verification |
|---|---|---|---|
| Accounts and JWT authentication | `server.py`, `test_server.py`, `index.html` | Implemented; canonical API tests passed for the recorded PR ref | @ZhengZaikun confirms authentication; @Guanyu-Lu verifies deployed register/login/logout |
| Private favorites | database schema, authenticated endpoints, UI account view | Implemented; deployed privacy/persistence Not Run | @ZhengZaikun verifies authorization; @tiantian09091 verifies persistence; @Guanyu-Lu verifies UI |
| Private history and saved result snapshots | schema, authenticated history endpoints, UI history view | Implemented; deployed privacy/persistence Not Run | @ZhengZaikun verifies authorization and restore/delete; @tiantian09091 verifies persistence; @Guanyu-Lu verifies UI |
| SQLite local use | application fallback and bundled database | Implemented | @tiantian09091 retains disposable verification output |
| PostgreSQL deployed persistence | `DATABASE_URL` and SQLAlchemy support | Implemented configuration; deployed engine Unverified | @tiantian09091 records engine, counts and restart persistence; @ZhengZaikun confirms API integration |
| Catalogue provenance | `DataSource`, `LastUpdated`, importer source mappings | Implemented in repository | @tiantian09091 confirms retained source and licence wording |
| Responsive interface | CSS breakpoint and interface layout | Implemented representation; browser E2E Not Run | @Guanyu-Lu executes desktop/mobile verification |
| Accessibility | labels, focus treatment, status/error regions | Implemented representation; accessibility observations Not Run | @Guanyu-Lu executes keyboard, focus, zoom and readable-error checks |
| Canonical CI | `.github/workflows/tests.yml` and `test_server.py` | Verified for workflow run `31096706920` | @ZhengZaikun reviews PR #35; suite reruns for the frozen candidate |
| External acceptance | `docs/v3-external-uat-record.md` | Prepared; Not Run | @Chu-Junjie coordinates two non-team participants and records actual outcomes |
| Release reconciliation | Issue #43 and PR #44 | Planned; Not started | @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve file decisions; @Chu-Junjie maintains the inventory and meeting record |

## 6. Current evidence references

- PR #35 — canonical CI workflow and historical audit separation;
- PR #44 — controlled reconciliation plan;
- PR #46 — release evidence index;
- PR #47 — US-09 deferral record;
- PR #48 — database verification record;
- PR #50 — project closeout review record;
- PR #52 — architecture record;
- PR #54 — Agile and retrospective evidence;
- PR #58 — toolchain and dependency record;
- PR #60 — project status, traceability and release controls;
- Issue #42 — deployed E2E execution;
- `docs/final-acceptance-and-release-checklist.md` — final release gates.

## 7. Completion rule

No requirement is marked `Done` solely because code exists, a meeting decision was recorded or a document was approved. `Done` requires all applicable formal reviews, final-candidate tests, deployed checks, acceptance evidence and release controls.