# V3 Release Evidence Index

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Recorded:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Implementation baseline inspected:** `7c406515bd4b657372fe519869596825cdf91d56`  
**Tracking Issue:** #45

## 1. Purpose

This index maps current V3 implementation claims, repository-derived decisions, automated evidence, prepared records and remaining release gates.

Source inspection can establish what the code, contracts and tests contain. It cannot prove deployed identity, PostgreSQL persistence, browser behaviour, external acceptance or review approval.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| `Implemented` | Code, data or documentation exists on the authoritative branch. |
| `Repository verified` | The statement is directly supported by version-controlled source, tests or contracts. |
| `CI verified` | A named workflow check passed for a named ref and environment. |
| `Prepared` | A plan, template or procedure exists but has not been executed. |
| `Deferred` | The item is outside the current release and retained in the backlog. |
| `Blocked` | Missing runtime evidence or a dependency prevents release completion. |
| `Not Run` | The required execution has not occurred. |
| `Unverified` | The target environment or result is not confirmed. |
| `Done` | All applicable review, test, deployment and acceptance gates passed. |

## 3. Current release position

| Area | Current status | Evidence boundary |
|---|---|---|
| V3 implementation | Implemented on `feature/product-database` | Not proof that the same commit is deployed |
| Canonical V3 tests | CI verified for PR #35 ref | Must be rerun for frozen release candidate |
| Legacy `test_mock.py` | Historical non-release audit | Six expected V2 compatibility failures remain visible |
| US-09 | Deferred, milestone `Unscheduled` | Not part of current release acceptance |
| Database/schema/importer | Repository verified | Runtime counts and PostgreSQL persistence remain open |
| Frontend V3 flows | Implemented | Deployed commit and browser E2E unverified |
| Coordinator status documents | Prepared in PR #60 | Review/merge deferred |
| Reconciliation to `main` | Not started | Separate approval required |

## 4. Draft package inventory

| PR | Purpose | Current state |
|---|---|---|
| #35 | Canonical CI and historical audit | Required job successful; Draft review deferred |
| #44 | Safe `main`/V3 reconciliation | Prepared; no integration branch created |
| #46 | Release evidence index | Current Draft |
| #47 | US-09 decision record | Option C — Deferred |
| #48 | Database verification record | Repository findings complete; runtime blocked |
| #50 | Coordinated review and closeout package | Prepared; review deferred |
| #52 | Design and architecture reference | Prepared |
| #54 | Agile delivery/evidence record | Prepared |
| #58 | Development toolchain reference | Prepared |
| #60 | Scope, CI and release-gate status alignment | Four coordinator-owned documents updated |

No approval is inferred. Each PR remains independently reviewable.

## 5. Canonical automated evidence

### 5.1 Test-scope decision

```bash
python -m pytest -q test_server.py
```

`test_server.py` is the V3 release suite because it uses isolated temporary databases and exercises the current SQLAlchemy/API contract.

`test_mock.py` is Practical 8, Task 7 evidence targeting removed V2 Pandas/raw-SQLite interfaces. It remains a non-release compatibility audit and is not silently deleted or modified.

### 5.2 Successful GitHub Actions result

| Field | Evidence |
|---|---|
| Workflow | `V3 Test Evidence` |
| Run | `31096706920` |
| Workflow source commit | `4e698826dbeac719b56f1ff5cea060109d0bdd60` |
| Tested PR merge ref | `8ecdb5fea8829a85521825b864a9bfe6e630a4ff` |
| Environment | Ubuntu 24.04.4, Python 3.11.15, pytest 9.1.1 |
| Required collection | 12 |
| Required result | 12 passed in 1.23s |
| Required-job exit | 0 |
| Tracked-file integrity | Passed |
| Overall workflow | Success |
| Legacy audit | 6 collected, 6 expected V2 failures, non-blocking |

Issue #34 is completed. The release-candidate CI gate remains open until the same canonical suite passes for the frozen release commit.

## 6. US-09 scope

**Decision:** Deferred from the current V3 release  
**Backlog milestone:** Unscheduled

Repository basis:

- no budget-alternative field in `api-contract.md`;
- no alternative object in `/api/recommend`;
- no cheaper-alternative acceptance test in `test_server.py`;
- optional frontend rendering scaffolding remains hidden without backend data.

Release limitation:

> The current release filters recommendations by a user's maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

Tracked by Issue #40 and PR #47. Coordinator status corrections are prepared in PR #60.

## 7. Database and catalogue evidence

Repository inspection confirms:

- SQLAlchemy PostgreSQL selection through `DATABASE_URL` with SQLite fallback;
- seven application tables;
- importer quotas of 800 laptops, 833 smartphones, 300 smart watches, 61 headphones and 6 tablets;
- imported IDs beginning at `10,000,001`;
- target counts of 11,000 products and 2,000 specifications;
- source/licence metadata and fixed currency rules;
- built-in `verify_database()` validation;
- historical-price rather than live-price semantics.

Operational restriction:

> The importer builds a clean catalogue artifact and must not run directly against a live production database containing private user data.

Still required:

- actual local count/join/duplicate/orphan output;
- deployed PostgreSQL dialect and commit;
- PostgreSQL schema/catalogue initialization;
- restart/redeploy persistence;
- cross-user deployed isolation;
- backup/restore and secret scan.

Tracked by Issue #41 and PR #48.

## 8. Deployed frontend, API and E2E

Candidate URLs exist in repository configuration, but deployed commits and database engine are unverified.

Required for one frozen candidate:

- GitHub Pages commit;
- Render API commit;
- active PostgreSQL dialect;
- frontend-to-API Network evidence;
- auth, recommendation, pagination, compare, favorites, history, feedback and share scenarios;
- mobile, keyboard, focus, error and empty-state observations.

Status: `Not Run` / `Unverified`. Tracked by Issue #42.

## 9. External acceptance

The UAT procedure is prepared. No retained participant execution exists.

Required:

- two non-team participant sessions;
- identical task script;
- independent/prompted completion results;
- observations and ratings;
- defect or accepted-limitation decisions.

Status: `Not Run`.

## 10. Coordinator status alignment

Issue #59 / PR #60 update only:

- `docs/project-status.md`;
- `docs/requirements-traceability.md`;
- `docs/v3-execution-plan.md`;
- `docs/final-acceptance-and-release-checklist.md`.

The documents now consistently record:

- successful canonical CI for the PR #35 ref;
- historical audit classification;
- US-09 deferral;
- database source-level findings versus runtime gates;
- review, deployment, E2E, UAT and reconciliation as open.

README remains outside PR #60 and will be handled during final shared release consolidation.

## 11. Conditional closeout sequence

1. Run local catalogue verification against a disposable copy.
2. Confirm deployed frontend, API and PostgreSQL identity.
3. Freeze a release candidate.
4. Rerun canonical CI for the frozen commit.
5. Execute PostgreSQL persistence and privacy checks.
6. Execute browser E2E.
7. Execute external acceptance.
8. Resume actual review and merge approved Draft PRs into the V3 baseline.
9. Update README and final documentation from actual evidence.
10. Obtain explicit approval for the Issue #43 reconciliation branch.
11. Preserve V3 implementation while integrating useful `main` evidence.
12. Rerun final checks, merge to `main`, tag and package.

## 12. Current blockers

| Blocker | Next evidence |
|---|---|
| Actual local catalogue counts | Importer/query output from a disposable copy |
| PostgreSQL identity/persistence | Deployed environment and restart results |
| Frontend/API deployed identity | Hosting commit confirmation |
| Browser E2E | Stable identified release environment |
| External acceptance | Two participant records |
| Actual review | Deferred GitHub review period |
| `main` reconciliation | Separate explicit approval |

## 13. Evidence restrictions

This index does not authorize:

- modification of teammate-owned backend, frontend, tests, datasets, databases, importers or deployment settings;
- recording approval or runtime success that does not exist;
- running the importer against production user data;
- creating a reconciliation branch or merging to `main` without separate approval.
