# V3 Final Acceptance and Release Checklist

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Authoritative implementation branch:** `feature/product-database`  
**Status date:** 6 August 2026, Singapore time (UTC+8)

This checklist records actual release evidence. A checked item must be supported by a commit, workflow, command output, deployment observation, review or acceptance record.

## 1. Current fixed decisions

- [x] Authoritative implementation branch is `feature/product-database`.
- [x] Earlier V2 implementation is historical and must not overwrite V3.
- [x] Canonical V3 automated suite is `python -m pytest -q test_server.py`.
- [x] `test_mock.py` is retained as a historical non-release compatibility audit.
- [x] US-09 Budget Alternatives is Deferred from this release.
- [x] US-09 backlog milestone is `Unscheduled`.
- [x] The catalogue importer is classified as a build-artifact tool and must not run against live production user data.

Known release limitation:

> The current release filters recommendations by a user's maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

## 2. Release candidate identity

Complete after the candidate is frozen:

- [ ] Release candidate branch:
- [ ] Release candidate commit SHA:
- [ ] Freeze date/timezone:
- [ ] GitHub Pages deployed commit:
- [ ] Render API deployed commit:
- [ ] Production database dialect/version:
- [ ] GitHub Pages URL:
- [ ] Render API URL:
- [ ] Reviewers:
- [x] Deferred requirement: US-09 Budget Alternatives
- [ ] Other accepted limitations:

## 3. Repository and review

- [ ] All intended release work is present on reviewed branches.
- [ ] Each PR states scope, evidence and limitations.
- [ ] Each affected technical component has an actual non-author review.
- [ ] Requested changes are resolved or documented.
- [ ] Coordinator-owned documents are merged into the V3 baseline.
- [ ] Teammate-owned implementation was not changed from coordinator branches.
- [ ] Reconciliation plan is approved before an integration branch is created.
- [ ] V3 is integrated into `main` without restoring obsolete V2 implementation.
- [ ] Release commit is frozen after integration.
- [ ] Related Issues are closed or retain an explicit accepted-risk statement.

Review is currently deferred. No approval is inferred.

## 4. Canonical CI evidence already retained

| Field | Retained result |
|---|---|
| Workflow | `V3 Test Evidence` |
| Run | `31096706920` |
| Workflow source commit | `4e698826dbeac719b56f1ff5cea060109d0bdd60` |
| Tested PR merge ref | `8ecdb5fea8829a85521825b864a9bfe6e630a4ff` |
| Runner | Ubuntu 24.04.4 |
| Python | 3.11.15 |
| pytest | 9.1.1 |
| Canonical test command | `python -m pytest -q test_server.py` |
| Collected | 12 |
| Passed | 12 |
| Failed/errors/skipped | 0 / 0 / 0 |
| Elapsed | 1.23s |
| Exit code | 0 |
| Tracked-file integrity | Passed |
| Workflow conclusion | Success |

- [x] Runtime dependencies installed in the workflow.
- [x] pytest installed explicitly.
- [x] Canonical tests collected.
- [x] Canonical tests passed.
- [x] Tracked-file integrity passed.
- [x] Historical audit failures remained visible.
- [x] Historical audit was separated from the release gate.

This run verifies the PR #35 ref, not the final release candidate.

## 5. Release-candidate CI gate

For the frozen release candidate:

- [ ] Run `python -m pytest -q test_server.py` in GitHub Actions.
- [ ] Record workflow/run ID.
- [ ] Record tested commit SHA.
- [ ] Record runner, Python, pytest and dependency results.
- [ ] Confirm 12 intended tests collect, unless a reviewed change updates the count.
- [ ] Confirm all intended tests pass.
- [ ] Confirm tracked database and catalogue files remain unchanged.
- [ ] Confirm overall required workflow conclusion is successful.
- [ ] Record warnings and accepted limitations.

Historical `test_mock.py` may continue to fail against removed V2 interfaces and does not block this gate.

## 6. Catalogue and local database verification

Run the importer only against a disposable output copy:

```bash
python import_real_catalog.py \
  --source digital_products.db \
  --output digital_products_real.db \
  --csv-output real_product_catalog.csv
```

### Expected results derived from source

| Item | Expected | Observed | Result |
|---|---:|---:|---|
| Total products | 11,000 |  |  |
| Product specifications | 2,000 |  |  |
| Imported laptops | 800 |  |  |
| Imported smartphones | 833 |  |  |
| Imported smart watches | 300 |  |  |
| Imported headphones | 61 |  |  |
| Imported tablets | 6 |  |  |
| Recommendation-ready joins | 2,000 |  |  |
| Duplicate product IDs | 0 |  |  |
| Duplicate specification IDs | 0 |  |  |
| Orphan specification rows | 0 |  |  |

### Verification record

- [ ] Tested branch and commit recorded.
- [ ] Python/dependency environment recorded.
- [ ] Import command and exit result retained.
- [ ] Built-in `verify_database()` output retained.
- [ ] Count queries retained.
- [ ] Duplicate and orphan queries retained.
- [ ] Distinct `DataSource` values retained.
- [ ] Missing fields use honest placeholders.
- [ ] Historical price wording is retained.
- [ ] Source/licence records are reviewed.
- [ ] Source database and tracked files remain safe.
- [ ] Importer was not pointed at a live production user database.

## 7. PostgreSQL deployment identity

- [ ] Render service name recorded.
- [ ] Deployed API commit recorded.
- [ ] `DATABASE_URL` presence confirmed without exposing its value.
- [ ] Active database dialect confirmed as PostgreSQL.
- [ ] PostgreSQL version recorded where safely available.
- [ ] All seven required tables exist.
- [ ] Catalogue counts match the accepted release dataset.
- [ ] Health output contains no secret or stack trace.
- [ ] CORS permits the intended production frontend origin.
- [ ] CORS does not expose unnecessary credential behaviour.

## 8. PostgreSQL persistence and recovery

Use non-sensitive demonstration accounts and data.

- [ ] Register a test account.
- [ ] Create one favorite.
- [ ] Create one saved search/history record.
- [ ] Confirm a result snapshot can be restored.
- [ ] Submit one feedback record.
- [ ] Record all entries before restart/redeploy.
- [ ] Restart or redeploy through the approved process.
- [ ] Confirm account persists.
- [ ] Confirm favorite persists.
- [ ] Confirm history and snapshot persist.
- [ ] Confirm feedback persists.
- [ ] Record current backup mechanism.
- [ ] Record recovery/restore procedure.
- [ ] Record application rollback method.
- [ ] Record database/catalogue recovery method.
- [ ] Record hosting limitations and mitigation.

## 9. Authentication and privacy

### Repository/CI evidence

- [x] Registration/login/current-user path has automated coverage.
- [x] Passwords are designed to be stored as hashes.
- [x] Private history requires authentication in the canonical tests.
- [x] Private favorites require authentication in the canonical tests.

### Remaining release evidence

- [ ] Required-field registration validation.
- [ ] Duplicate username and email behaviour.
- [ ] Password rule matches the contract.
- [ ] Invalid credentials are rejected safely.
- [ ] Missing/malformed/invalid token handling.
- [ ] Production `JWT_SECRET_KEY` is a random environment value of at least 32 characters.
- [ ] User A cannot read User B's history.
- [ ] User A cannot delete User B's history.
- [ ] User A cannot read or mutate User B's favorites.
- [ ] Passwords, bearer tokens and secrets are absent from logs/evidence.

## 10. Recommendation and pagination

### Repository/CI evidence

- [x] Category and budget parsing have automated coverage.
- [x] Page one returns 20 results in the isolated test dataset.
- [x] Page two is available.
- [x] A separate Top 5 is returned.

### Remaining release evidence

- [ ] Invalid numeric values.
- [ ] Text and explicit brand exclusions.
- [ ] Combined exclusion behaviour.
- [ ] Match scores and reasons are understandable.
- [ ] Maximum page size is enforced.
- [ ] Page metadata is consistent.
- [ ] Middle, last, empty and out-of-range pages behave as documented.
- [ ] Deployed Network evidence matches the API contract.
- [ ] No budget-alternative object is promised or demonstrated.

## 11. Comparison

### Repository/CI evidence

- [x] One product is rejected.
- [x] Two valid products succeed.
- [x] Same-category favorite comparison is covered.
- [x] Mixed-category favorite comparison is rejected.

### Remaining release evidence

- [ ] Three valid products succeed.
- [ ] More than three products are rejected.
- [ ] Duplicate IDs are rejected.
- [ ] Invalid and missing IDs are rejected.
- [ ] Required specification fields are returned.
- [ ] Two-product frontend display works.
- [ ] Three-product frontend display works.
- [ ] Missing values display honestly.

## 12. Favorites

### Repository/CI evidence

- [x] Authenticated add/list/remove is covered.
- [x] Unauthenticated list is rejected.
- [x] Same-category favorite comparison is covered.

### Remaining release evidence

- [ ] Repeated save is idempotent or returns the documented result.
- [ ] Invalid product ID is rejected.
- [ ] Unowned favorites cannot be compared.
- [ ] Cross-user access is rejected.
- [ ] Deployed frontend state updates correctly.
- [ ] Favorite persists after restart/redeploy.

## 13. Search history

### Repository/CI evidence

- [x] Authenticated search creates a history record.
- [x] Unauthenticated history list is rejected.
- [x] History detail restores query and saved data.
- [x] Owner can delete history.

### Remaining release evidence

- [ ] History list boundary/pagination behaviour.
- [ ] Cross-user detail access is rejected.
- [ ] Cross-user delete is rejected.
- [ ] Frontend open/delete flow works.
- [ ] History and snapshots persist after restart/redeploy.

## 14. Feedback

### Repository/CI evidence

- [x] `up` feedback returns creation success in the canonical test.
- [x] Aggregate count is covered.

### Remaining release evidence

- [ ] `down` feedback.
- [ ] Invalid vote rejection.
- [ ] Optional user/history/top-product linkage.
- [ ] Frontend pending/success/error states.
- [ ] Persistence after restart/redeploy.

## 15. Product/source links and data limitations

- [x] Importer retains source/licence metadata in code.
- [x] Fixed EUR/INR conversion rules are documented.
- [x] Historical-price limitation is documented.
- [ ] `DataSource` is populated for all active recommendation records in the tested database.
- [ ] Product/source URLs use safe `http` or `https` schemes.
- [ ] Invalid/missing URL fallback is clear.
- [ ] Links do not imply guaranteed checkout, availability or live price.
- [ ] Frontend and documentation use consistent limitation wording.

## 16. Share and restore

- [ ] Share creates a valid URL.
- [ ] Query restores in an isolated browser/private window.
- [ ] Spaces and special characters restore correctly.
- [ ] Budget/category/brand restore correctly.
- [ ] Multiple excluded brands restore correctly.
- [ ] Restored state behaves as designed.
- [ ] URL contains no password, token or private history data.
- [ ] Clipboard failure has a usable fallback.

## 17. Frontend usability and deployed E2E

### Deployment identity

- [ ] GitHub Pages source branch/folder recorded.
- [ ] GitHub Pages commit recorded.
- [ ] Render API commit recorded.
- [ ] PostgreSQL environment recorded.

### Browser checks

- [ ] Desktop layout usable.
- [ ] Mobile layout usable.
- [ ] Loading state visible.
- [ ] Empty state visible.
- [ ] Validation error visible.
- [ ] Backend unavailable/timeout state visible.
- [ ] Registration/login/logout works.
- [ ] Recommendation and pagination work.
- [ ] Comparison works.
- [ ] Favorites work.
- [ ] History works.
- [ ] Feedback works.
- [ ] Share/restore works.
- [ ] Keyboard navigation reaches primary controls.
- [ ] Focus indicators are visible.
- [ ] Important controls have meaningful labels.
- [ ] Browser console has no release-blocking errors.
- [ ] Network evidence shows intended endpoints and status codes.

## 18. External acceptance

### Participant 1

- Identifier/role:
- Date/timezone:
- Device/browser:
- Independent tasks:
- Prompted tasks:
- Problems/observations:
- Rating:
- Linked Issues:
- Retest:

### Participant 2

- Identifier/role:
- Date/timezone:
- Device/browser:
- Independent tasks:
- Prompted tasks:
- Problems/observations:
- Rating:
- Linked Issues:
- Retest:

### Gate

- [ ] Two non-team participant records are complete.
- [ ] The same task script was used.
- [ ] Results were not fabricated or backdated.
- [ ] Blocking findings were fixed/retested or formally accepted.

## 19. Documentation consistency

- [x] Project status reflects canonical CI and US-09 deferral in the Issue #59 branch.
- [x] Requirements traceability reflects canonical CI and US-09 deferral in the Issue #59 branch.
- [x] Execution plan reflects the current release path in the Issue #59 branch.
- [x] This checklist separates completed and open evidence.
- [ ] Architecture/design PR is reviewed and merged.
- [ ] Agile delivery record is reviewed and merged.
- [ ] Development toolchain record is reviewed and merged.
- [ ] Release evidence index is reviewed and merged.
- [ ] Database verification record is reviewed and merged.
- [ ] README matches the final release.
- [ ] API contract matches the final implementation.
- [ ] User guide and deployment instructions are current.
- [ ] Known limitations are listed consistently.

## 20. Security and repository safety

- [ ] No database password or full connection string is tracked.
- [ ] No production JWT secret is tracked.
- [ ] No API token is tracked.
- [ ] No private account password or bearer token appears in evidence.
- [ ] `.env` and equivalent secret files are ignored.
- [ ] Production environment variables are configured outside GitHub source.
- [ ] Error responses expose no stack traces or connection details.
- [ ] Relevant tracked files and recent history have been scanned.
- [ ] Any discovered credential was rotated rather than merely deleted.

## 21. Reconciliation and final release

Requires separate explicit approval before branch creation.

- [ ] Reconciliation branch created from the approved V3 baseline.
- [ ] V3 database/catalogue/importer implementation preserved.
- [ ] V3 backend/frontend decisions preserved.
- [ ] Useful `main` historical evidence retained selectively.
- [ ] Conflicts resolved by the responsible component owners.
- [ ] Canonical CI rerun after reconciliation.
- [ ] Required runtime checks rerun after reconciliation.
- [ ] Reviewed PR merged into `main`.
- [ ] Final deployed commits match the release commit.
- [ ] Changelog updated.
- [ ] Release tag created.
- [ ] Final ZIP/package created.
- [ ] ZIP/package opened and checked.
- [ ] Final links checked.
- [ ] Final limitations recorded.

## 22. Final sign-off

| Role | Name | Decision | Date | Evidence/comment |
|---|---|---|---|---|
| Project Manager | Chu Junjie |  |  |  |
| Database owner | Yuyang Zhou |  |  |  |
| Backend owner | Zaikun Zheng |  |  |  |
| Frontend owner | Guanyu Lu |  |  |  |

## 23. Release decision

Current decision: **Not ready for final release**.

Open critical gates:

- actual review and merge;
- release-candidate CI;
- local catalogue output;
- deployed PostgreSQL identity/persistence;
- browser E2E;
- external acceptance;
- reconciliation to `main`;
- release tag and package.

A blank box is incomplete. Repository implementation does not substitute for deployment, persistence, review or acceptance evidence.
