# Historical `main` Branch Project Status Record

**Project:** Smart Digital Product Recommendation Platform  
**Record basis:** Repository evidence and team meeting notes  
**Meeting record maintained by:** @Chu-Junjie  
**Status:** Historical branch record; current V3 release work remains on `feature/product-database`

## 1. Purpose

This file records the historical Task 1–3 state retained on `main`. It is not the current V3 release status and must not be used to replace the records being reviewed on `feature/product-database`.

The responsibilities and interpretation rules are documented in the team meeting notes maintained by @Chu-Junjie.

## 2. Named responsibilities

- @ZhengZaikun confirms backend, API, recommendation, automated-test and CI interpretation.
- @tiantian09091 confirms database, catalogue, specifications, importer, provenance and PostgreSQL interpretation.
- @Guanyu-Lu confirms frontend, interface, GitHub Pages and browser interpretation.
- @Chu-Junjie maintains meeting notes, historical status, traceability and release-record separation.

## 3. Historical Task 1 status

| Item | Historical record |
|---|---|
| Coordinator | @Chu-Junjie |
| Tracking Issue | #16 — Closed |
| Foundation Pull Request | #17 — Merged |
| Foundation branch | `docs/project-foundation` |
| Closeout branch | `docs/task1-closeout` |
| Target branch | `main` |
| Review result | Approved |
| Merge commit | `ae9366d` |
| Implementation verification | Not verified in Task 1 |
| Automated checks | Not Run |

This documentation work recorded an agreed direction only. It did not prove implementation, deployment or acceptance.

## 4. Historical Task 2 status

| Item | Historical record |
|---|---|
| Coordination | @Chu-Junjie |
| Database Pull Request | #19 — Merged |
| Merge commit | `f798bd7` |
| Recorded counts | `products=9000; product_specs=33` |
| ProductID integrity | Passed — 0 unmatched IDs |
| Feedback persistence | Passed in the retained Task 2 evidence |
| Invalid-vote rejection | Passed in the retained Task 2 evidence |
| Task 2 status | Historical completion record |

@tiantian09091 confirms the database interpretation of this historical record. It is not a substitute for the current 11,000/2,000 V3 database verification.

## 5. Historical Task 3 status

| Item | Historical record |
|---|---|
| Coordination branch | `feature/share-ci-evidence` |
| Dependency installation | Passed in the recorded environment |
| Dependency consistency | Passed in the recorded environment |
| Python compilation | Passed in the recorded environment |
| Test collection | 21 tests collected |
| Historical full-suite result | Failed — 5 failed, 1 passed, 15 errors |
| Later recorded result | Failed — 4 failed, 2 passed, 15 errors |
| Test database isolation | Failed — tracked SQLite file was modified and restored |
| Evidence Pull Request | #25 |
| Historical Task 3 state | In Progress |

@ZhengZaikun confirms the backend/test interpretation of the retained Task 3 evidence. These results target an older contract and are not the current V3 canonical CI result.

## 6. Historical implementation direction

The retained `main` record describes an earlier two-table direction with:

- 9,000 behavioural product rows;
- 33 product-specification rows;
- joined recommendation data;
- comparison support;
- feedback persistence;
- product-source links.

This is a historical branch state. Current V3 records on `feature/product-database` describe SQLAlchemy, accounts, JWT, private history, favorites, 11,000 products, 2,000 specifications, pagination and PostgreSQL support.

## 7. Historical limitations

- the 33 specification rows represented a small demonstration catalogue;
- prices were historical data and not live inventory;
- source and licence evidence was incomplete;
- inner joins restricted recommendation-ready products;
- browser integration and deployment evidence were incomplete;
- legacy tests were incompatible with later API/database contracts;
- tests modified a tracked SQLite file before it was restored.

## 8. Historical risk routing

| Risk area | Named confirmation |
|---|---|
| Backend/API/test compatibility and test isolation | @ZhengZaikun |
| Database counts, ProductID relationships and source limitations | @tiantian09091 |
| Frontend integration and live-interface claims | @Guanyu-Lu |
| Meeting notes, historical/current separation and release wording | @Chu-Junjie |

## 9. Current V3 direction

For current work, use:

- branch: `feature/product-database`;
- canonical test: `python -m pytest -q test_server.py`;
- recorded CI run: `31096706920` with 12/12 passed;
- current catalogue targets: 11,000 products and 2,000 specifications;
- US-09: Deferred / `Unscheduled`;
- runtime gates: PostgreSQL, persistence, privacy, browser E2E and external acceptance remain pending.

## 10. Record rule

Historical evidence remains valuable, but it must not:

- replace current V3 implementation;
- be presented as final V3 CI or deployed evidence;
- change implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu;
- mark a current release gate Passed or Done.

Final reconciliation decisions are recorded in the team meeting notes and require formal GitHub Approvals from @ZhengZaikun, @tiantian09091 and @Guanyu-Lu.