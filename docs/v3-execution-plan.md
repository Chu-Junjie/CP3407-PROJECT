# V3 Execution Plan

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Updated:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Inspected baseline:** `7c406515bd4b657372fe519869596825cdf91d56`

## 1. Objective

Move the implemented V3 platform through evidence consolidation, runtime verification, review, safe branch reconciliation and final release without modifying teammate-owned implementation from coordinator branches.

## 2. Current scope

Included in the V3 release candidate:

- Flask and SQLAlchemy API;
- SQLite local seed/demo support;
- PostgreSQL support through `DATABASE_URL`;
- 11,000 target products and 2,000 recommendation-ready specifications;
- accounts, password hashes and JWT authentication;
- favorites, private search history, result snapshots and feedback;
- budget/category/brand filtering, ranking, pagination and separate Top 5;
- comparison of two or three products;
- frontend account, recommendation, compare, history, favorite, feedback and share flows.

Deferred:

- **US-09 Budget Alternatives** — backlog milestone `Unscheduled`.

Release limitation:

> The current release filters recommendations by maximum budget but does not separately identify a cheaper alternative that preserves equivalent specifications.

## 3. Engineering rules

1. `feature/product-database` remains the V3 technical baseline until reviewed integration completes.
2. V2 implementation and tests are historical evidence and must not silently replace V3 files.
3. Repository evidence may resolve source-level questions but cannot replace runtime verification.
4. Every member retains ownership of their technical component.
5. Coordinator branches modify only governance, evidence, CI configuration and release records.
6. Review approval, deployment identity and acceptance results are never inferred.
7. No catalogue importer execution is permitted against a live production database containing private user data.
8. No reconciliation branch or merge to `main` occurs without separate explicit approval.

## 4. Team responsibilities

| Member | Primary responsibility | Current closeout dependency |
|---|---|---|
| Chu Junjie | Scope, schedule, evidence, CI coordination, acceptance and release | Maintain consistent records and execute release process |
| Yuyang Zhou | Catalogue, schema, importer, SQLite/PostgreSQL and provenance | Runtime counts, PostgreSQL, persistence and recovery evidence |
| Zaikun Zheng | Backend, authentication, recommendation, API and tests | Remaining negative/boundary coverage and deployed API support |
| Guanyu Lu | Frontend, responsive UI and browser E2E | Deployment identity and end-to-end evidence |

## 5. Stage overview

| Stage | Status | Exit gate |
|---|---|---|
| V3-0 Scope and test decisions | **Completed from repository evidence** | US-09 deferred; canonical suite defined and CI successful |
| V3-1 Coordinator documentation alignment | In Progress | Status, traceability, plan and checklist agree |
| V3-2 Local catalogue verification | Not Run | Actual counts, joins, duplicates and importer output retained |
| V3-3 Deployed environment identification | Unverified | Frontend/API commits and PostgreSQL dialect confirmed |
| V3-4 Release-candidate automated verification | Pending | Canonical suite passes for frozen release commit |
| V3-5 PostgreSQL persistence/privacy | Not Run | Restart persistence and cross-user isolation pass |
| V3-6 Browser E2E | Not Run | Required desktop/mobile flows pass |
| V3-7 External acceptance | Not Run | Two non-team participant records complete |
| V3-8 Review and documentation merge | Deferred | Actual review comments resolved and approved PRs merged |
| V3-9 Reconciliation and final release | Not started | Reviewed integration, final checks, tag and package complete |

## 6. Completed scope and CI decisions

### 6.1 Canonical test suite

```bash
python -m pytest -q test_server.py
```

Successful GitHub Actions evidence:

- run `31096706920`;
- source commit `4e698826dbeac719b56f1ff5cea060109d0bdd60`;
- tested merge ref `8ecdb5fea8829a85521825b864a9bfe6e630a4ff`;
- Ubuntu 24.04.4;
- Python 3.11.15;
- 12 collected, 12 passed in 1.23s;
- tracked-file integrity passed;
- overall workflow conclusion `success`.

`test_mock.py` remains a visible non-release Practical 8 compatibility audit. Its six V2 contract failures do not belong to the V3 release gate.

### 6.2 US-09

US-09 is deferred because the current API contract, backend response and automated tests do not implement an alternative-selection feature. Existing optional frontend rendering remains untouched and is not presented as end-to-end evidence.

## 7. V3-1 — Coordinator documentation alignment

**Lead:** Junjie

- [x] Update project status with current CI and US-09 decision.
- [x] Update requirements traceability.
- [x] Update execution plan.
- [x] Update final acceptance checklist structure.
- [ ] Open Draft PR and retain review-deferred status.
- [ ] Update README only during final shared release consolidation.

Exit gate: coordinator documents agree without claiming unexecuted deployment or acceptance.

## 8. V3-2 — Local catalogue verification

**Technical ownership:** Yuyang  
**Coordinator:** retains commands/results

Run against a disposable output copy:

```bash
python import_real_catalog.py \
  --source digital_products.db \
  --output digital_products_real.db \
  --csv-output real_product_catalog.csv
```

Required evidence:

- [ ] exact branch and commit;
- [ ] Python/dependency environment;
- [ ] importer exit code and output;
- [ ] 11,000 products;
- [ ] 2,000 specifications;
- [ ] category distribution 800/833/300/61/6;
- [ ] zero duplicate product/spec IDs;
- [ ] zero orphan specifications;
- [ ] 2,000 recommendation-ready joins;
- [ ] tracked files unchanged unless the output change is intentional and reviewed.

Exit gate: expected repository targets are confirmed by actual output.

## 9. V3-3 — Deployed environment identification

Required before browser acceptance:

- [ ] GitHub Pages source branch/folder confirmed;
- [ ] deployed frontend commit recorded;
- [ ] Render API deployed commit recorded;
- [ ] API health endpoint recorded;
- [ ] active database dialect confirmed safely;
- [ ] `DATABASE_URL` presence confirmed without exposing its value;
- [ ] CORS production origin confirmed.

Exit gate: all E2E evidence can be tied to one known frontend/API/database environment.

## 10. V3-4 — Frozen release-candidate CI

After a release candidate is selected:

- [ ] record branch and commit SHA;
- [ ] run `python -m pytest -q test_server.py` in GitHub Actions;
- [ ] retain environment and collection output;
- [ ] require zero blocking failures;
- [ ] require tracked-file integrity success;
- [ ] record any warning or accepted limitation;
- [ ] link the workflow run in the final checklist.

Exit gate: canonical V3 suite passes for the actual release candidate.

## 11. V3-5 — PostgreSQL persistence and privacy

Using non-sensitive demonstration data:

- [ ] confirm all seven tables exist;
- [ ] confirm catalogue counts and joined candidates;
- [ ] register one test account;
- [ ] create one favorite, history entry and feedback record;
- [ ] restart/redeploy through the approved process;
- [ ] confirm all data remains;
- [ ] verify a second user cannot read/delete the first user's history;
- [ ] verify a second user cannot access the first user's favorites;
- [ ] retain backup/recovery and rollback procedure;
- [ ] retain final secret-scan result.

Exit gate: production persistence and privacy have actual evidence.

## 12. V3-6 — Browser E2E

Required deployed flows:

- [ ] frontend load and API health;
- [ ] registration/login/logout;
- [ ] recommendation success, empty and error states;
- [ ] Top 5 and pagination boundaries;
- [ ] general comparison;
- [ ] favorite save/list/remove/compare;
- [ ] history list/open/delete;
- [ ] feedback;
- [ ] share/restore in an isolated session;
- [ ] mobile layout;
- [ ] keyboard and focus path;
- [ ] browser console/network review;
- [ ] no US-09 alternative-selection claim.

Exit gate: all critical browser flows pass against the identified release environment.

## 13. V3-7 — External acceptance

**Lead:** Junjie

- [ ] recruit two non-team participants;
- [ ] use the same task script;
- [ ] record device/browser and date;
- [ ] record independent and prompted completion;
- [ ] retain observations and ratings;
- [ ] create Issues for blocking defects;
- [ ] retest fixes or record accepted limitations.

Exit gate: two genuine acceptance records exist and blocking findings are resolved or accepted.

## 14. V3-8 — Review and document integration

Review remains deferred; no approval is inferred.

When review resumes:

1. review PRs #35, #44, #46, #47, #48, #50, #52, #54, #58 and the Issue #59 PR;
2. resolve component-specific comments;
3. keep every PR independent;
4. merge only actually approved work into `feature/product-database`;
5. update Issue states from real merge/evidence results;
6. prepare final README consolidation.

Exit gate: current release documentation is reviewed and merged into the V3 branch.

## 15. V3-9 — Reconciliation and release

After separate explicit approval:

- [ ] create a reconciliation branch from the approved V3 baseline;
- [ ] preserve Yuyang's V3 data/database/importer implementation;
- [ ] preserve current V3 backend and frontend decisions;
- [ ] bring across only useful `main` historical evidence;
- [ ] resolve overlapping files under component ownership;
- [ ] rerun canonical CI and required runtime checks;
- [ ] merge to `main` through a reviewed PR;
- [ ] update changelog and final README;
- [ ] create release tag;
- [ ] create and inspect final ZIP/package;
- [ ] record final limitations and release sign-off.

Exit gate: `main`, deployed environment, documentation and release package refer to the same verified release.

## 16. Immediate next priorities

1. Open the Issue #59 Draft PR.
2. Run local catalogue verification against a disposable copy.
3. Confirm deployed frontend, API and PostgreSQL identity.
4. Freeze a release candidate.
5. Execute persistence, E2E and external acceptance.
6. Resume real review and proceed to controlled integration.

## 17. Evidence integrity

A checked item must have an actual source, command, workflow, deployment observation, review or participant record. Repository implementation is not converted into runtime or acceptance evidence without execution.
