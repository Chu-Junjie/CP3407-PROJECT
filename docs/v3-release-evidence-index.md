# V3 Release Evidence Index

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Recorded:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Implementation baseline inspected:** `7c406515bd4b657372fe519869596825cdf91d56`  
**Tracking Issue:** #45

## 1. Purpose

This index records the current V3 implementation, repository-derived project decisions, prepared verification material and release activities that still require execution.

Repository inspection may resolve questions about what the code and contracts contain. It cannot prove deployed identity, PostgreSQL persistence, browser behaviour or external acceptance.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| `Implemented` | The relevant code, data or document exists on the authoritative branch. |
| `Repository verified` | The statement is directly supported by version-controlled source, tests or contracts. |
| `CI verified` | A named workflow check passed for a named commit or PR merge ref. |
| `Prepared` | A plan, template or procedure exists but has not been executed. |
| `Deferred` | The item is outside the current release scope and retained in the backlog. |
| `Blocked` | A missing execution result or unresolved external dependency prevents completion. |
| `Not Run` | The required runtime check has not been executed. |
| `Unverified` | The value cannot be confirmed from retained evidence. |
| `Done` | All applicable implementation, review, test, deployment and acceptance gates passed. |

## 3. Current release position

| Area | Current status | Evidence boundary |
|---|---|---|
| V3 implementation branch | Implemented | `feature/product-database` at inspected head `7c4065...`; not proof of deployed identity. |
| V3 API suite | CI verified for PR #35's earlier ref | 12 tests passed; new workflow commit must run again. |
| Legacy `test_mock.py` | Historical / non-release audit | File declares itself Practical 8, Task 7 and targets removed V2 Pandas/raw-SQLite interfaces. |
| US-09 budget alternative | Deferred | Backend contract and tests do not implement it; frontend has optional rendering scaffolding only. |
| Database/catalogue/importer | Implemented and repository verified | Runtime counts, PostgreSQL identity and persistence are still not executed. |
| Frontend V3 flows | Implemented | Deployed commit and browser E2E remain unverified. |
| Review package | Prepared | Actual GitHub approvals remain deferred. |
| Reconciliation to `main` | Not started | Requires explicit approval and later release evidence. |

## 4. Draft package inventory

| PR | Purpose | Current evidence state |
|---|---|---|
| #35 | CI workflow | Updated to separate the canonical V3 suite from the historical mock audit. |
| #44 | Safe branch reconciliation | Prepared; no integration branch created. |
| #46 | This evidence index | Updated from repository-derived decisions. |
| #47 | US-09 decision | Option C — Deferred from current V3 release. |
| #48 | Database verification | Repository findings recorded; runtime verification blocked. |
| #50 | Coordinated review and closeout | Prepared; review deferred. |
| #52 | Architecture and design | Prepared from current implementation. |
| #54 | Agile delivery record | Prepared from retained repository evidence. |
| #58 | Development toolchain | Prepared from repository dependencies and workflows. |

All listed PRs remain independently reviewable. No approval is inferred from this index.

## 5. Automated testing decision

### 5.1 Canonical V3 release suite

```bash
python -m pytest -q test_server.py
```

Repository basis:

- `test_server.py` creates isolated temporary SQLite databases;
- covers database setup, health, budget/category parsing, pagination, registration/login, private history, history deletion, feedback, comparison and favorites;
- the existing CI evidence recorded 12 collected and 12 passed;
- tracked-file integrity passed.

### 5.2 Historical mock audit

`test_mock.py` is retained as historical Practical 8, Task 7 evidence. It imports or patches removed V2 interfaces such as `get_connection`, Pandas CSV loading, `fetch_candidate_products`, the older integer `setup_database()` result and the old recommendation contract.

Decision:

- it is not part of the V3 release suite;
- it remains visible as a non-release compatibility audit;
- the workflow logs its failures instead of presenting them as V3 regressions;
- no teammate-owned test file is modified by this decision.

### 5.3 Current CI gate

PR #35 workflow commit `4e698826dbeac719b56f1ff5cea060109d0bdd60` must complete a new run. The release test gate remains open until the canonical job passes for the current PR/ref and later for the frozen release candidate.

## 6. US-09 scope decision

**Decision:** Option C — Defer  
**Backlog milestone:** Unscheduled

Repository basis:

- `api-contract.md` does not define a budget-alternative field;
- `/api/recommend` returns filters, counts, pagination, Top 5, data and optional history ID, but no alternative object;
- `test_server.py` has no cheaper-alternative acceptance test;
- `index.html` can display an optional alternative field but the backend does not produce it.

Current release wording:

> The release filters recommendations by maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

US-09 must not be demonstrated or reported as implemented for the current V3 release.

## 7. Database and catalogue findings

### 7.1 Repository-verified implementation

- SQLAlchemy selects PostgreSQL through `DATABASE_URL` and otherwise uses bundled SQLite.
- Seven tables are defined: products, product specifications, users, favorites, history, saved results and feedback.
- The public catalogue importer defines 2,000 rows:
  - 800 laptops;
  - 833 smartphones;
  - 300 smart watches;
  - 61 headphones;
  - 6 tablets.
- Imported IDs begin at `10,000,001`.
- With the original 9,000 behavioural rows retained, the implementation target is 11,000 products and 2,000 specifications.
- The importer records source/licence metadata and fixed EUR/INR conversion rules.
- `verify_database()` checks specification count, category quotas and the absence of private rows in the generated catalogue artifact.

### 7.2 Important operational boundary

The importer deletes private rows from the generated catalogue artifact and replaces imported products/specifications. It is suitable for building a clean seed copy, not for direct execution against a live production database containing user data.

### 7.3 Runtime checks still open

- actual SQLite release counts and joins;
- actual Render PostgreSQL dialect and deployed commit;
- schema/data initialization in PostgreSQL;
- persistence after restart/redeploy;
- cross-user deployed isolation;
- production backup and restore;
- final secret scan.

The database release gate remains blocked on executed runtime evidence.

## 8. Deployed frontend, API and browser acceptance

Repository configuration identifies candidate endpoints, but GitHub source cannot establish which commits are currently deployed.

Still required for a frozen release candidate:

- confirm the GitHub Pages commit;
- confirm the Render API commit;
- confirm PostgreSQL rather than SQLite;
- run authentication, recommendation, pagination, comparison, favorites, history, feedback and share scenarios;
- run mobile, keyboard, error and empty-state checks;
- retain browser Network evidence without secrets.

Status: `Not Run` / `Unverified`.

## 9. External acceptance

The UAT template exists, but no retained participant execution record is present.

Still required:

- two non-team participant sessions;
- identical task script;
- independent/prompted outcome recording;
- usability observations and ratings;
- defect or accepted-limitation decisions.

Status: `Not Run`.

## 10. Conditional closeout sequence

1. Complete the new PR #35 workflow run and record the canonical result.
2. Retain US-09 as deferred and update coordinator-owned status files.
3. Run the local catalogue verification commands against a disposable database copy.
4. Confirm deployed frontend, API and PostgreSQL identity.
5. Freeze a release-candidate commit.
6. Run the canonical suite for the frozen commit.
7. Execute PostgreSQL persistence and cross-user checks.
8. Execute deployed E2E and external acceptance.
9. Update README, project status, traceability and final acceptance from actual evidence.
10. Resume actual review when the team is ready.
11. Create the Issue #43 reconciliation branch only after explicit approval.
12. Preserve V3 implementation, integrate useful `main` evidence, rerun checks and merge to `main`.
13. Create the final tag and package.

## 11. Current blocker register

| Blocker | Current owner/action |
|---|---|
| New canonical CI run | Junjie tracks PR #35 workflow result. |
| Runtime SQLite catalogue output | Execute documented commands against a disposable copy. |
| PostgreSQL identity and persistence | Requires deployed environment access. |
| Deployed frontend/API identity | Requires hosting confirmation or deployment evidence. |
| Browser E2E | Requires stable deployed candidate. |
| External UAT | Requires stable deployed candidate and participants. |
| Actual review approvals | Deferred by current project operating decision. |
| `main` reconciliation | Requires separate explicit approval. |

## 12. Evidence restrictions

This index does not authorize:

- modifying teammate-owned backend, frontend, tests, datasets, database files, importers or deployment settings;
- recording review approval that does not exist;
- marking runtime verification as passed from source inspection;
- running the catalogue importer against production user data;
- creating the reconciliation branch or merging to `main` without separate approval.
