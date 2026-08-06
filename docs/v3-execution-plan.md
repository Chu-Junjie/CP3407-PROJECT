# CP3407 Teacher Feedback Revision — Unified Execution Plan v3.0

**Prepared by:** Chu Junjie  
**Date:** 6 August 2026  
**Authoritative implementation baseline:** `feature/product-database`  
**Governance branch:** `docs/junjie-v3-governance`

## 1. Purpose

This plan replaces the earlier 9,000-product / 33-specification execution baseline. It coordinates the teacher-feedback revision without changing teammate-owned implementation from the coordinator branch.

The current v3 direction includes:

- 11,000 `products` rows;
- 2,000 joined recommendation-ready public-dataset `product_specs` rows;
- SQLAlchemy;
- SQLite for the bundled local demonstration;
- PostgreSQL through `DATABASE_URL` for production persistence;
- password-hashed accounts and JWT authentication;
- favorites, private search history, result snapshots and feedback;
- paginated recommendations with a separate Top 5;
- GitHub Pages frontend and Render API deployment.

## 2. Non-negotiable governance rules

1. `feature/product-database` is the current technical baseline until the v3 work is reviewed and merged.
2. The earlier v2 baseline remains historical and must not be mixed into current status tables.
3. A coordinator status update does not equal technical verification.
4. Each member owns the implementation and technical explanation of their assigned component.
5. Junjie does not directly modify teammate-owned code, tests, datasets or database files.
6. Any GitHub write outside the approved governance-document scope requires Junjie's explicit approval first.
7. `Done` requires applicable evidence, non-author review and integration—not only code presence.

## 3. Team ownership boundaries

| Member | Primary v3 ownership | Coordinator interaction |
|---|---|---|
| Chu Junjie | Change control, execution tracking, traceability, Definition of Done, CI/acceptance coordination, Agile evidence and release management | Updates governance/evidence documents; does not fix teammate implementation |
| Yuyang Zhou | Public catalogue, data import, database schema, SQLite/PostgreSQL integration, provenance and database verification | Junjie records gaps and requests evidence; Yuyang changes data/database work |
| Zaikun Zheng | Flask/SQLAlchemy backend, authentication, recommendation logic, API validation and backend tests | Junjie audits evidence and proposes Issues/review notes; Zaikun changes backend/tests |
| Guanyu Lu | Frontend, responsive UI, account/history/favorites interactions, pagination and browser E2E | Junjie defines acceptance and records results; Guanyu changes frontend |

## 4. Branch and merge strategy

| Purpose | Branch | Rule |
|---|---|---|
| Authoritative v3 implementation | `feature/product-database` | Technical owners review before final integration |
| Junjie governance update | `docs/junjie-v3-governance` | Documentation-only; target `feature/product-database` after approval |
| Database fixes/evidence | Owner-created branch from the latest agreed v3 base | Yuyang-owned files only unless reviewed jointly |
| Backend/test fixes | Owner-created branch from the latest agreed v3 base | Zaikun-owned files only unless reviewed jointly |
| Frontend/E2E fixes | Owner-created branch from the latest agreed v3 base | Guanyu-owned files only unless reviewed jointly |
| Final integration | Agreed v3 branch to `main` | Must not silently restore outdated v2 files |

No force-push, history rewrite or direct `main` modification is part of this plan.

## 5. Stage overview

| Stage | Lead | Current status | Exit gate |
|---|---|---|---|
| V3-0 Change control and scope freeze | Junjie | In Progress | Team approves v3 scope, ownership and revised documents |
| V3-1 Catalogue/database verification | Yuyang | Implemented; verification pending | Counts, integrity, provenance and PostgreSQL evidence pass |
| V3-2 Backend/auth/API verification | Zaikun | Implemented; verification pending | Intended full backend suite and API acceptance pass |
| V3-3 Frontend and deployed E2E | Guanyu | Implemented; verification pending | Required browser flows pass against deployed API |
| V3-4 CI and regression baseline | Technical owners; Junjie tracks | Not verified | Clean-environment/CI run passes for release commit |
| V3-5 External acceptance | Junjie | Not Started | Two non-team tests recorded and defects triaged |
| V3-6 Documentation consolidation | All; Junjie coordinates | In Progress | All current docs agree with v3 implementation |
| V3-7 Final release | Junjie coordinates | Not Started | Release Definition of Done is complete |

## 6. V3-0 — Change control and scope freeze

**Lead:** Chu Junjie

### Coordinator tasks

- [x] Record `feature/product-database` as the authoritative v3 baseline.
- [x] Replace outdated project-status terminology in the governance branch.
- [x] Replace outdated requirements traceability in the governance branch.
- [x] Replace outdated Definition of Done in the governance branch.
- [x] Create this execution plan.
- [x] Create the final acceptance and release checklist.
- [ ] Obtain team review of the revised scope and ownership.
- [ ] Confirm whether US-09 budget alternatives remains required, is revised or is deferred.
- [ ] Confirm the intended final test set, including the disposition of legacy `test_mock.py`.
- [ ] Create the governance PR only after Junjie's additional approval.
- [ ] Merge only after non-author review and resolved comments.

### Exit gate

- V3 scope, status vocabulary, owners and deferred items are approved.
- Governance documents contain no current 9,000/33 baseline claim.
- No teammate implementation is changed by the governance PR.

## 7. V3-1 — Catalogue and database verification

**Lead:** Yuyang Zhou  
**Coordinator role:** Track evidence and blockers only.

### Required owner evidence

- [ ] Record the exact release counts for all required tables.
- [ ] Confirm 11,000 `products` and 2,000 `product_specs` for the release commit.
- [ ] Verify unique and matching ProductIDs.
- [ ] Verify required columns and `DataSource` fields.
- [ ] Review public source attribution, licence and transformation notes.
- [ ] Confirm historical-price wording and no live-inventory claim.
- [ ] Run and record the reproducible import path or document prerequisites/limitations.
- [ ] Confirm repeated local initialization does not duplicate data.
- [ ] Demonstrate PostgreSQL initialization/seed.
- [ ] Demonstrate persistence after a restart/redeploy.
- [ ] Provide backup and rollback/recovery instructions.

### Files controlled by the owner

Examples include `digital_products.db`, `import_real_catalog.py`, `real_product_catalog.csv`, source/cached catalogue data and database technical documentation.

### Exit gate

Database and catalogue checks pass for a named commit and environment, with limitations documented.

## 8. V3-2 — Backend, authentication and API verification

**Lead:** Zaikun Zheng  
**Coordinator role:** Audit test evidence and traceability; do not edit implementation.

### Required owner evidence

- [ ] Confirm the complete intended test set and collected count.
- [ ] Resolve, update, archive or explicitly exclude outdated mock tests.
- [ ] Verify `/api/health` and exact table/candidate counts.
- [ ] Verify registration, duplicate identity handling, login and `/api/auth/me`.
- [ ] Verify missing/invalid token handling and cross-user privacy denial.
- [ ] Verify recommendation pagination and Top 5 consistency.
- [ ] Verify invalid page, per-page and request values.
- [ ] Verify text and explicit brand exclusions.
- [ ] Verify compare accepts only 2 or 3 unique valid joined IDs.
- [ ] Verify feedback validation, persistence and summary.
- [ ] Verify history list/detail/delete and ownership.
- [ ] Verify favorites ownership, idempotency and same-category comparison.
- [ ] Verify no tracked database/data file changes after tests.
- [ ] Record command, commit SHA, environment, exit code and results.

### Exit gate

All intended backend tests pass in a clean environment or CI, with no unresolved blocking API defect.

## 9. V3-3 — Frontend and deployed end-to-end verification

**Lead:** Guanyu Lu  
**Coordinator role:** Define acceptance cases and retain results; do not edit frontend.

### Required owner evidence

- [ ] GitHub Pages loads the v3 interface without console-breaking errors.
- [ ] Register, login and account state work against the deployed API.
- [ ] Recommendation requests show loading, success, empty and error states.
- [ ] Pagination works on first, middle, final and empty/out-of-range cases.
- [ ] Top 5 is distinguishable from the full paginated result list.
- [ ] History can be listed, opened and deleted by its owner.
- [ ] Favorites can be added, removed and compared under documented rules.
- [ ] General comparison accepts 2 or 3 selected products.
- [ ] Feedback is submitted and reflected by the API.
- [ ] Safe product/source links and missing-link fallback work.
- [ ] Share/restore works with special characters and exclusions in a second browser.
- [ ] Mobile layout and keyboard flow are checked.
- [ ] Browser Network or equivalent request/response evidence is retained.

### Exit gate

Required frontend flows pass against the deployed API and production database, with screenshots/network evidence and known limitations.

## 10. V3-4 — Clean environment and CI

**Technical owners:** Relevant component owners  
**Coordinator:** Chu Junjie tracks evidence and status.

### Required checks

- [ ] Create a clean Python environment.
- [ ] Install documented runtime and test dependencies.
- [ ] Run compilation/static syntax checks where applicable.
- [ ] Run the intended complete automated test suite.
- [ ] Confirm zero unexpected failures/errors.
- [ ] Confirm tracked SQLite/CSV/data files remain unchanged.
- [ ] Configure GitHub Actions for pull requests and release integration.
- [ ] Retain the successful workflow run, job steps and tested commit SHA.
- [ ] Open Issues for failures instead of editing evidence to hide them.

### Suggested evidence commands

The responsible technical owner confirms the final commands. A typical baseline is:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

If test dependencies are documented separately, the exact installation command must be recorded.

### Exit gate

The release commit has a successful clean-environment or CI run and the intended test scope is explicit.

## 11. V3-5 — External acceptance

**Lead:** Chu Junjie

### Required acceptance coverage

- [ ] Recruit at least two non-team testers where available before submission.
- [ ] Record tester role, date, environment and consent to retain results.
- [ ] Test account creation/login.
- [ ] Test a recommendation and pagination flow.
- [ ] Test compare and favorites.
- [ ] Test history reopen/delete.
- [ ] Test feedback.
- [ ] Test share/restore.
- [ ] Record usability observations and failures.
- [ ] Create/approve defect Issues before any implementation changes.
- [ ] Retest blocking defects after owner fixes.

### Exit gate

Two acceptance records exist and blocking findings are closed or formally accepted with impact.

## 12. V3-6 — Documentation consolidation

**Coordinator:** Chu Junjie  
**Technical accuracy:** Each component owner

### Required documents

- [ ] README reflects the final v3 scope and run instructions.
- [ ] Architecture diagram matches GitHub Pages, Render, SQLAlchemy and PostgreSQL.
- [ ] ERD/database document matches all v3 tables and relationships.
- [ ] API contract matches final routes, fields and status codes.
- [ ] Data provenance and licence information is reviewed by Yuyang.
- [ ] Testing document records automated and manual evidence.
- [ ] Deployment guide records environment variables and persistence limitations.
- [ ] User guide covers accounts, recommendations, pagination, history, favorites, compare, feedback and share.
- [ ] Agile/iteration evidence matches actual dates and outcomes.
- [ ] Project status, traceability and Definition of Done match final evidence.

### Exit gate

No current document contradicts the release implementation; component owners approve technical sections.

## 13. V3-7 — Final release

**Coordinator:** Chu Junjie

### Required actions

- [ ] Freeze the release candidate commit.
- [ ] Confirm successful CI for that commit.
- [ ] Confirm deployed smoke test for that commit/environment.
- [ ] Confirm release Definition of Done.
- [ ] Confirm no repository secrets.
- [ ] Update changelog.
- [ ] Create release tag.
- [ ] Create final ZIP backup.
- [ ] Open and inspect the backup.
- [ ] Record final limitations and deferred items.

### Exit gate

All release checklist items are complete and the team approves submission.

## 14. Current immediate priorities

1. Obtain team agreement on the v3 scope and US-09 decision.
2. Ask each owner to review only their section of the revised governance documents.
3. Confirm the intended full test set and legacy mock-test disposition.
4. Obtain clean test and CI evidence.
5. Obtain deployed PostgreSQL and browser E2E evidence.
6. Complete external acceptance and final documentation.

## 15. Evidence integrity

A checkbox is completed only when evidence exists. Local implementation, branch documentation and planned deployment are not converted into `Verified` or `Done` without the corresponding command, review, merge, deployment or acceptance result.
