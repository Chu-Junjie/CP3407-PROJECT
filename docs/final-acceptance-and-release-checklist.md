# Final Acceptance and Release Checklist — V3.0

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Authoritative implementation baseline:** `feature/product-database`

This checklist records release evidence. It does not authorize the coordinator to modify teammate-owned backend, frontend, test, data or database files.

## 1. Release candidate identification

- [ ] Release candidate branch:
- [ ] Release candidate commit SHA:
- [ ] Test date and timezone:
- [ ] Deployment date and timezone:
- [ ] GitHub Pages URL:
- [ ] Render API URL:
- [ ] Production database type:
- [ ] Reviewer(s):
- [ ] Known deferred requirements:

## 2. Scope and governance

- [ ] The team confirms `feature/product-database` or its reviewed successor as the final v3 baseline.
- [ ] The earlier 9,000/33 baseline is labelled historical.
- [ ] Teacher-feedback changes are recorded.
- [ ] US-09 is explicitly retained, revised or deferred.
- [ ] Owner responsibilities are agreed.
- [ ] Project status, traceability and Definition of Done use the same status vocabulary.
- [ ] No coordinator governance commit changes teammate implementation.
- [ ] All release claims are tied to evidence.

## 3. Repository and review

- [ ] All final work is on reviewed branches.
- [ ] Pull Requests identify scope, evidence and limitations.
- [ ] Each technical component has a non-author review.
- [ ] Review comments are resolved or documented.
- [ ] The v3 baseline is merged into `main` without restoring outdated v2 files.
- [ ] Related Issues are closed or carry an approved remaining-risk statement.
- [ ] There are no unintended generated files or local secrets in the diff.
- [ ] The release commit is identified and frozen.

## 4. Clean-environment automated testing

### Environment record

- Python version:
- Operating system / runner:
- Dependency installation command:
- Test command:
- Collected test count:
- Passed:
- Failed:
- Errors:
- Skipped:
- Exit code:
- Elapsed time:
- Tested commit SHA:
- Evidence file / workflow URL:

### Checks

- [ ] Runtime dependencies install successfully.
- [ ] Test dependencies install successfully.
- [ ] The intended complete test set is documented.
- [ ] The disposition of legacy `test_mock.py` is documented.
- [ ] All intended tests collect.
- [ ] All blocking tests pass.
- [ ] No unexpected warning indicates a broken contract or insecure setup.
- [ ] Tracked `digital_products.db` remains unchanged unless an intentional reviewed release change occurred.
- [ ] Tracked CSV/catalogue files remain unchanged after tests.
- [ ] Git status is clean after the test run.

## 5. GitHub Actions / CI

- [ ] CI runs for Pull Requests.
- [ ] CI runs for the release integration branch or `main`.
- [ ] The release commit has a successful workflow run.
- [ ] Dependency installation succeeded.
- [ ] Test collection succeeded.
- [ ] The intended complete suite succeeded.
- [ ] Workflow logs are retained or accessible.
- [ ] Failed runs are not described as passed.
- [ ] Required status checks are enabled or their absence is documented.

## 6. Database and catalogue acceptance

### Required counts

| Table | Expected release count | Observed count | Result |
|---|---:|---:|---|
| `products` | 11,000 |  |  |
| `product_specs` | 2,000 |  |  |
| `users` | Environment-dependent |  |  |
| `favorites` | Environment-dependent |  |  |
| `search_history` | Environment-dependent |  |  |
| `search_results` | Environment-dependent |  |  |
| `feedback` | Environment-dependent |  |  |

### Integrity and provenance

- [ ] Required tables exist.
- [ ] Required columns exist.
- [ ] Product/specification IDs are unique where required.
- [ ] Every active specification joins to a product.
- [ ] No unintended duplicate rows are introduced by repeated initialization.
- [ ] `DataSource` is populated for active recommendation records.
- [ ] Public source names and licences are reviewed.
- [ ] Transformation and currency-normalization rules are documented.
- [ ] Historical prices are not represented as live retail prices.
- [ ] Missing technical fields are not fabricated.
- [ ] The importer/reproduction path is tested or its prerequisites are documented.
- [ ] Backup and rollback/recovery instructions exist.

## 7. PostgreSQL production persistence

- [ ] Render PostgreSQL is provisioned.
- [ ] `DATABASE_URL` is configured as an environment variable.
- [ ] The application reports PostgreSQL in production health output.
- [ ] Required tables and catalogue data are initialized.
- [ ] A user can register and log in.
- [ ] A search history record persists.
- [ ] A favorite persists.
- [ ] Feedback persists.
- [ ] The service/database is restarted or redeployed.
- [ ] The same user/history/favorite/feedback records remain available.
- [ ] No production credentials appear in GitHub.

## 8. Authentication and privacy acceptance

- [ ] Registration succeeds with valid data.
- [ ] Required-field validation works.
- [ ] Duplicate username/email behaviour matches the contract.
- [ ] Password length/format rule matches the contract.
- [ ] Stored password data is hashed, not plaintext.
- [ ] Login works by documented username/email identifier.
- [ ] Invalid credentials are rejected without revealing sensitive details.
- [ ] `/api/auth/me` requires a valid bearer token.
- [ ] Missing, malformed and invalid tokens are rejected.
- [ ] `JWT_SECRET_KEY` is a random production environment value of at least 32 characters.
- [ ] User A cannot read User B's history.
- [ ] User A cannot delete User B's history.
- [ ] User A cannot access or compare User B's favorites.
- [ ] API/log output does not expose passwords or tokens.

## 9. Recommendation and pagination acceptance

- [ ] A natural-language query returns a successful response.
- [ ] Category parsing works for supported categories.
- [ ] Budget parsing works with plain and comma-formatted values.
- [ ] Invalid numeric values receive the documented response.
- [ ] Excluded brands are applied.
- [ ] Explicit and text exclusions combine correctly if both are supplied.
- [ ] Each result contains required product and source fields.
- [ ] Match score and explanation are present and understandable.
- [ ] Default page size is correct.
- [ ] Maximum page size is enforced.
- [ ] `total_candidates`, `page`, `per_page` and `total_pages` are consistent.
- [ ] The separate Top 5 contains no more than five results.
- [ ] Page 1 works.
- [ ] A middle page works where available.
- [ ] The last page works.
- [ ] Empty/no-match behaviour is clear.
- [ ] Out-of-range page behaviour matches the contract.

## 10. Comparison acceptance

- [ ] Exactly two valid product IDs succeed.
- [ ] Exactly three valid product IDs succeed.
- [ ] One ID is rejected.
- [ ] More than three IDs are rejected.
- [ ] Duplicate IDs are rejected.
- [ ] Invalid/non-integer IDs are rejected.
- [ ] Missing/unjoined IDs are rejected.
- [ ] Comparison returns required specification fields.
- [ ] Frontend comparison displays two products correctly.
- [ ] Frontend comparison displays three products correctly.
- [ ] Missing values are shown honestly, for example as `N/A` or `Not specified`.

## 11. Favorites acceptance

- [ ] Authenticated user can add a favorite.
- [ ] Repeated favorite save is idempotent or returns the documented result.
- [ ] Authenticated user can list favorites.
- [ ] Authenticated user can remove a favorite.
- [ ] Unauthenticated requests are rejected.
- [ ] Another user's favorites are inaccessible.
- [ ] Two or three owned favorites in the same category can be compared.
- [ ] Mixed-category favorite comparison is rejected.
- [ ] Invalid or unowned favorite IDs are rejected.

## 12. Search history acceptance

- [ ] Authenticated page-one search saves history when documented.
- [ ] Unauthenticated behaviour matches the contract.
- [ ] History list is private and paginated where applicable.
- [ ] History detail restores query, filters and result snapshot.
- [ ] History delete removes only the owner's record.
- [ ] Cross-user detail access is rejected.
- [ ] Cross-user delete is rejected.
- [ ] Frontend can open a history result.
- [ ] Frontend can delete a history record and update the list.

## 13. Feedback acceptance

- [ ] `up` feedback returns HTTP 201.
- [ ] `down` feedback returns HTTP 201.
- [ ] Invalid vote is rejected.
- [ ] Feedback is stored.
- [ ] Optional user/history linkage behaves as documented.
- [ ] Aggregate up/down/total values are correct.
- [ ] Frontend prevents accidental duplicate submissions while pending.
- [ ] Frontend displays success and error states.

## 14. Product/source link acceptance

- [ ] Result contains `purchase_url` and `data_source` where applicable.
- [ ] Only safe `http` or `https` links are opened.
- [ ] Links open without replacing the current result page unexpectedly.
- [ ] Missing/invalid link fallback is clear.
- [ ] Link wording does not falsely promise live checkout or availability.
- [ ] Source and historical-price limitations are visible in documentation or UI.

## 15. Share and restore acceptance

- [ ] Share action creates a valid URL.
- [ ] Plain search query restores in another browser/private window.
- [ ] Spaces and special characters restore correctly.
- [ ] Budget restores correctly.
- [ ] Category and brand restore correctly where encoded.
- [ ] Multiple excluded brands restore correctly.
- [ ] Restored state reruns or displays results as designed.
- [ ] Share URL contains no password, token or private history data.
- [ ] Failure to use the clipboard has a usable fallback.

## 16. Frontend usability and compatibility

- [ ] Desktop layout is usable.
- [ ] Mobile layout is usable.
- [ ] Registration/login controls are understandable.
- [ ] Loading state is visible.
- [ ] Empty state is visible.
- [ ] Validation error is visible.
- [ ] Backend unavailable/timeout state is visible.
- [ ] Buttons cannot be accidentally activated while a request is pending where relevant.
- [ ] Keyboard navigation reaches primary controls.
- [ ] Focus indicators are visible.
- [ ] Important controls have meaningful labels.
- [ ] Browser console has no release-blocking errors.
- [ ] Browser Network evidence shows the expected deployed endpoints and status codes.

## 17. Deployment smoke test

| Flow | Result | Evidence |
|---|---|---|
| GitHub Pages loads |  |  |
| Render root/API health returns success |  |  |
| Registration/login |  |  |
| Recommendation page 1 |  |  |
| Recommendation page 2 |  |  |
| Comparison |  |  |
| Favorite save/list/compare |  |  |
| History list/detail/delete |  |  |
| Feedback |  |  |
| Share/restore |  |  |
| Restart/redeploy persistence |  |  |

- [ ] CORS permits the production frontend origin.
- [ ] CORS does not expose unnecessary credential behaviour.
- [ ] Production API responses contain no stack traces or secrets.
- [ ] Health output clearly states database backend and data limitations.

## 18. External acceptance testing

### Tester 1

- Name/identifier:
- Non-team role:
- Date:
- Device/browser:
- Tasks completed:
- Passed observations:
- Problems found:
- Linked Issues:
- Retest result:

### Tester 2

- Name/identifier:
- Non-team role:
- Date:
- Device/browser:
- Tasks completed:
- Passed observations:
- Problems found:
- Linked Issues:
- Retest result:

### Gate

- [ ] At least two non-team acceptance records are complete where available before submission.
- [ ] Blocking defects are fixed and retested or formally accepted with impact.
- [ ] Tester evidence is not fabricated or backdated.

## 19. Documentation acceptance

- [ ] README matches the final release.
- [ ] Installation and local-run instructions work.
- [ ] Test instructions identify runtime and test dependencies.
- [ ] Architecture document/diagram matches the deployed system.
- [ ] ERD/database document matches all release tables.
- [ ] API contract matches final routes and response fields.
- [ ] Data provenance/licence document is reviewed by Yuyang.
- [ ] Backend/security explanation is reviewed by Zaikun.
- [ ] Frontend/user-guide explanation is reviewed by Guanyu.
- [ ] Project status and traceability match final evidence.
- [ ] Agile/iteration evidence uses actual dates and results.
- [ ] Known limitations and deferred scope are listed.
- [ ] README links all final required documents.

## 20. Security and secret review

- [ ] No database password is committed.
- [ ] No JWT secret is committed.
- [ ] No API token is committed.
- [ ] No private user password or bearer token appears in evidence screenshots/logs.
- [ ] `.env` or equivalent secret files are ignored.
- [ ] Production environment variables are configured outside the repository.
- [ ] Error messages do not expose internal connection details.

## 21. Final release actions

- [ ] All required User Stories have a final honest status.
- [ ] All blockers are closed or formally accepted.
- [ ] CI is green for the release commit.
- [ ] Deployed smoke test passes.
- [ ] External acceptance is complete.
- [ ] Changelog is updated.
- [ ] Release tag is created.
- [ ] Final ZIP backup is created.
- [ ] ZIP backup is opened and checked.
- [ ] Submission/demo links are checked.
- [ ] Final known limitations are recorded.
- [ ] Team approves release/submission.

## 22. Final sign-off

| Role | Name | Decision | Date | Evidence/comment |
|---|---|---|---|---|
| Project Manager | Chu Junjie |  |  |  |
| Database owner | Yuyang Zhou |  |  |  |
| Backend owner | Zaikun Zheng |  |  |  |
| Frontend owner | Guanyu Lu |  |  |  |

## 23. Integrity statement

A blank box means the check is not complete. A local result is not labelled production evidence. A branch-reported result is not labelled CI evidence. No missing test, review, deployment or acceptance result may be inferred or invented.
