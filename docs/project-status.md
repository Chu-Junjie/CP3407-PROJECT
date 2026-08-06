# CP3407 Project Status — Teacher Feedback Revision v3.0

**Evidence date:** 6 August 2026  
**Coordinator:** Chu Junjie  
**Authoritative implementation baseline:** `feature/product-database`  
**Governance working branch:** `docs/junjie-v3-governance`  
**Historical integration branch:** `main`

## 1. Status boundary

The team has adopted `feature/product-database` as the latest technical baseline. The earlier 9,000-product / 33-specification Yuyang Unified v2 baseline is retained only as historical evidence.

This governance update does not claim that the v3 baseline has been reviewed, merged into `main`, deployed, or accepted. The implementation branch documentation records local test evidence, but clean-environment, full-repository, CI, production and end-to-end verification still require retained evidence.

The coordinator branch is documentation-only. It does not modify teammate-owned backend, frontend, tests, datasets, database files or deployment configuration.

## 2. Adopted v3 technical direction

| Area | Adopted direction | Current evidence status |
|---|---|---|
| Backend | Python, Flask and SQLAlchemy | Implemented on `feature/product-database`; final review pending |
| Local database | Bundled SQLite demonstration database | Implemented; release-state integrity check pending |
| Production database | PostgreSQL selected through `DATABASE_URL` | Designed and implemented; deployed persistence not yet evidenced |
| Catalogue | 11,000 `products` rows, including 2,000 joined recommendation-ready public-dataset records | Branch documentation records the counts; independent release verification pending |
| Specifications | 2,000 `product_specs` rows with `DataSource` | Importer and catalogue evidence exist; provenance review pending |
| Accounts | Password-hashed registration/login and JWT authentication | Implemented; security and deployment verification pending |
| Persistence | Favorites, private search history, result snapshots and feedback | Implemented; deployed persistence and privacy acceptance pending |
| Recommendations | Pagination, default 20 per page, maximum 100, with a separate Top 5 | Implemented; cross-layer acceptance pending |
| Frontend | HTML/CSS/JavaScript hosted through GitHub Pages and calling Render | Implemented candidate; deployed E2E evidence pending |

## 3. Current database tables

| Table | Purpose | Current status |
|---|---|---|
| `products` | Original behavioural observations plus imported catalogue products | Implemented |
| `product_specs` | Joined product names, technical fields, source and product/dataset URL | Implemented |
| `users` | Account identity and password hashes | Implemented |
| `favorites` | User-owned saved products | Implemented |
| `search_history` | User-owned query, filters and summary metadata | Implemented |
| `search_results` | Saved ranked result snapshots linked to history | Implemented |
| `feedback` | Helpful/not-helpful votes, optionally linked to a user/search | Implemented |

## 4. Evidence currently present on the authoritative branch

- `teacher-feedback-change-request.md` records the teacher-feedback scope revision and states that review, merge and production deployment remain required.
- `api-contract.md` records accounts, recommendations, pagination, history, comparison, favorites, feedback and database selection.
- `import_real_catalog.py` provides the reproducible public-catalogue import path.
- `real_product_catalog.csv` contains the 2,000-row human-inspection catalogue output.
- `test_server.py` contains isolated tests for database creation, health, pagination, authentication, history, feedback, comparison and favorites.
- Branch documentation records `.venv/bin/pytest -q` with `12 passed`; this result must be reconfirmed as the complete intended suite in a clean environment or CI before release.

## 5. Programme-level stage status

| Stage | Owner | Current status | Completion gap |
|---|---|---|---|
| V3 change control and governance | Junjie | In Progress | Team review, PR and merge evidence |
| Public catalogue and database revision | Yuyang | Implemented | Independent counts, provenance review, PostgreSQL seed/deployment evidence |
| Backend, authentication and API revision | Zaikun | Implemented | Full relevant tests, review and production verification |
| Frontend account, history and pagination revision | Guanyu | Implemented | Browser/network evidence, responsive testing and deployed E2E |
| Complete automated testing and CI | Technical owners + Junjie tracking | In Progress | Clean environment, intended full suite, CI success and database-state check |
| External acceptance | Junjie | Not Started | Two non-team testers and retained results |
| Documentation consolidation | All owners; Junjie coordinates | In Progress | Architecture, ERD, test, deployment and user-guide consistency |
| Final release | Junjie coordinates | Not Started | All release gates, tag, changelog and verified backup |

## 6. Current User Story status

`Implemented` means code exists on the authoritative feature branch. It does not mean the story is reviewed, deployed, accepted or Done.

| Story | Current v3 status | Evidence still required |
|---|---|---|
| US-01 Natural-language input | Implemented | Invalid/boundary regression evidence and integrated acceptance |
| US-02 Database setup/import | Implemented | 11,000/2,000 count evidence in release environment, repeat initialization and PostgreSQL verification |
| US-03 Recommendations | Implemented | Pagination and Top 5 deployed E2E evidence |
| US-04 Explanations | Implemented | Reason/score automated evidence and UI acceptance |
| US-05 Comparison | Implemented | Exact 2–3 ID validation, missing-ID handling and frontend comparison evidence |
| US-06 Exclusions | Implemented candidate | Text plus explicit exclusion regression evidence |
| US-07 Product/source links | Implemented candidate | Safe URL handling and limitation wording acceptance |
| US-08 Feedback | Implemented | Validation, persistence, aggregate response and deployed evidence |
| US-09 Budget alternatives | Scope confirmation required | Confirm whether it remains required under the teacher-feedback revision and retain acceptance evidence if kept |
| US-10 Share results | Implemented candidate | Special-character, exclusions and second-browser restoration evidence |
| V3 Accounts and private history | Implemented | Authentication, authorization, privacy and persistence acceptance |
| V3 Favorites | Implemented | Ownership, idempotency and same-category comparison acceptance |

## 7. Current blockers

1. `feature/product-database` is the adopted baseline but has not yet been reviewed and merged into `main`.
2. The branch diverges from `main`; integration strategy must preserve the v3 implementation without silently restoring outdated v2 files.
3. The recorded `12 passed` result must be reconfirmed against the intended full test set. The old `test_mock.py` contract must be updated, archived or explicitly excluded by the responsible test/backend owner.
4. No successful GitHub Actions workflow is currently retained as release evidence.
5. PostgreSQL production configuration, schema seeding and persistence across redeploy/restart are not yet evidenced.
6. Render and GitHub Pages end-to-end smoke tests are not yet retained.
7. The existing architecture, project-status, traceability and Definition of Done documents contain outdated v2 statements and require coordinated replacement.
8. Two non-team acceptance tests have not yet been recorded.
9. No final release tag, changelog or verified ZIP backup exists.

## 8. Risk register

| ID | Risk | Impact | Technical owner | Tracking owner | Status |
|---|---|---|---|---|---|
| V3-R01 | Old 9,000/33 documents are mistaken for the current baseline | Conflicting implementation and marking evidence | Relevant document owner | Junjie | Open |
| V3-R02 | The v3 branch is merged without owner review | Teammate work may be overwritten or unverified | All technical owners | Junjie | Open |
| V3-R03 | Local `12 passed` is reported as complete CI evidence without confirming the intended suite | False completion claim | Zaikun / test owner | Junjie | Open |
| V3-R04 | PostgreSQL secrets or persistence are configured incorrectly | Login/history data loss or security exposure | Zaikun + Yuyang | Junjie | Open |
| V3-R05 | Public data is described as live inventory or live pricing | Misleading product claims | Yuyang + documentation owners | Junjie | Open |
| V3-R06 | Authentication or history endpoints expose another user's records | Privacy and security failure | Zaikun | Junjie | Open |
| V3-R07 | Frontend works locally but fails against deployed CORS/API configuration | Failed demonstration | Guanyu + Zaikun | Junjie | Open |
| V3-R08 | Coordinator edits teammate implementation to make evidence appear complete | Ownership conflict and unreliable contribution record | Junjie | Junjie | Controlled — prohibited |
| V3-R09 | Release occurs without external acceptance and backup validation | Submission defects are discovered too late | All members | Junjie | Open |

## 9. Ownership and modification rule

- Junjie may update governance, planning, traceability, acceptance and release documents.
- Junjie does not directly modify `server.py`, recommendation logic, authentication implementation, frontend implementation, automated test implementation, datasets, database files or teammate technical explanations.
- Problems in teammate-owned files are reported to the responsible owner through review notes or a proposed Issue after approval.
- A status changes to `Verified` or `Done` only when the required evidence exists and is reviewed.

## 10. Verification rule

The v3 implementation is the adopted direction. A feature is not Done merely because it exists on `feature/product-database`. Done requires applicable automated tests, integrated acceptance, non-author review, merge evidence, deployment verification, documentation and honest limitation statements.
