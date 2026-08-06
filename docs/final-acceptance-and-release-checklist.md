# Final Acceptance and Release Checklist

**Project:** Smart Digital Product Recommendation Platform  
**Release coordination and meeting record:** @Chu-Junjie  
**Authoritative implementation branch:** `feature/product-database`  
**Checklist state:** Incomplete items remain unchecked until actual evidence exists

## 1. Evidence rule

This checklist is maintained from repository evidence and the team meeting notes recorded by @Chu-Junjie. Meeting decisions and formal document reviews do not replace executed CI, database, deployment, E2E or external-acceptance evidence.

## 2. Release identification

- [ ] @Chu-Junjie records the release-candidate branch.
- [ ] @Chu-Junjie records the full release-candidate SHA.
- [ ] @Chu-Junjie records the freeze date and timezone.
- [ ] @Chu-Junjie records included Pull Requests and merge commits.
- [ ] @Chu-Junjie records known limitations, including deferred US-09.
- [ ] @Chu-Junjie confirms no feature change entered after freeze without a new candidate SHA.

## 3. Formal GitHub reviews

- [ ] @ZhengZaikun approves PR #35 for CI and the canonical test scope.
- [ ] @ZhengZaikun and @Guanyu-Lu approve PR #47 for the US-09 scope decision.
- [ ] @tiantian09091 and @ZhengZaikun approve PR #48 for database and API integration wording.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #52 for their named architecture sections.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #54 for their named iteration records.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #58 for their named toolchain sections.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #44 for reconciliation boundaries.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #60 for technical mappings.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #46 for the evidence index.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #50 for the project closeout review record.
- [ ] @Chu-Junjie confirms every Approval applies to the current PR head.

## 4. Approved record merges into V3

- [ ] @Chu-Junjie merges approved PRs in the recorded sequence.
- [ ] @Chu-Junjie records every merged PR number and commit SHA.
- [ ] @Chu-Junjie confirms changed files match each approved scope.
- [ ] @Chu-Junjie confirms no unapproved implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu was changed.

## 5. Canonical CI

- [ ] @ZhengZaikun runs `python -m pytest --collect-only -q test_server.py` for the frozen candidate.
- [ ] @ZhengZaikun runs `python -m pytest -q test_server.py` for the frozen candidate.
- [ ] @ZhengZaikun runs `git diff --exit-code` after tests.
- [ ] @ZhengZaikun records the workflow run ID, tested SHA/ref, runner, Python version and pytest version.
- [ ] @ZhengZaikun records 12 tests collected and 12 tests passed.
- [ ] @ZhengZaikun records tracked-file integrity as passed.
- [ ] @Chu-Junjie links the final CI evidence from the release index.

The historical `test_mock.py` audit remains non-release evidence and must not be reported as a V3 regression.

## 6. Catalogue and local database integrity

Run against a disposable copy only.

- [ ] @tiantian09091 records `products = 11,000`.
- [ ] @tiantian09091 records `product_specs = 2,000`.
- [ ] @tiantian09091 records 2,000 joined recommendation-ready rows.
- [ ] @tiantian09091 records category counts `800 / 833 / 300 / 61 / 6`.
- [ ] @tiantian09091 confirms duplicate product IDs = 0.
- [ ] @tiantian09091 confirms duplicate specification IDs = 0.
- [ ] @tiantian09091 confirms orphan specifications = 0.
- [ ] @tiantian09091 confirms source metadata is present.
- [ ] @tiantian09091 confirms generated private tables are empty.
- [ ] @tiantian09091 records repeated-generation behaviour.
- [ ] @tiantian09091 confirms no tracked source database was unintentionally modified.

## 7. Deployed frontend, API and PostgreSQL identity

- [ ] @Guanyu-Lu records the GitHub Pages URL, source branch/folder and visible frontend commit.
- [ ] @ZhengZaikun records the Render API URL, deployed commit, build command and start command.
- [ ] @ZhengZaikun records the non-sensitive `/api/health` response.
- [ ] @tiantian09091 confirms `DATABASE_URL` is configured without exposing its value.
- [ ] @tiantian09091 confirms the active deployed database dialect is PostgreSQL.
- [ ] @tiantian09091 confirms all expected tables exist.
- [ ] @tiantian09091 records deployed product and specification counts.
- [ ] @ZhengZaikun confirms the API is using the recorded PostgreSQL environment.
- [ ] @Chu-Junjie confirms the deployment evidence is tied to the frozen candidate or approved release commit.

## 8. Persistence and privacy

Use non-sensitive demonstration accounts and do not retain credentials or tokens.

- [ ] @ZhengZaikun verifies registration and login for Account A.
- [ ] @ZhengZaikun verifies creation of a favorite, history entry, saved result snapshot and feedback record.
- [ ] @tiantian09091 records the data before restart or redeployment.
- [ ] @tiantian09091 confirms the account data remains after restart or redeployment.
- [ ] @ZhengZaikun verifies Account B cannot access Account A history or favorites.
- [ ] @Guanyu-Lu verifies the corresponding browser behaviour before and after logout.
- [ ] @Chu-Junjie records evidence IDs and statuses without private values.

## 9. Deployed browser E2E

### Foundation

- [ ] @Guanyu-Lu confirms the frontend loads without blocking console errors.
- [ ] @Guanyu-Lu confirms Network requests reach the intended Render API.
- [ ] @Guanyu-Lu records loading, empty and error states.
- [ ] @tiantian09091 confirms product-source and historical-price wording is accurate.

### Authentication

- [ ] @Guanyu-Lu completes register, login, current identity and logout flows.
- [ ] @ZhengZaikun confirms unauthenticated protected requests are rejected.

### Recommendation

- [ ] @Guanyu-Lu submits a valid recommendation request.
- [ ] @ZhengZaikun confirms category and budget compliance.
- [ ] @Guanyu-Lu confirms the separate Top 5 is identifiable.
- [ ] @Guanyu-Lu confirms next/previous pagination preserves the query.
- [ ] @ZhengZaikun confirms invalid input and invalid-page responses follow the API contract.

### Compare, favorites and history

- [ ] @Guanyu-Lu compares two products.
- [ ] @Guanyu-Lu compares three products.
- [ ] @ZhengZaikun confirms invalid comparison is rejected.
- [ ] @Guanyu-Lu adds and removes a favorite.
- [ ] @Guanyu-Lu compares supported same-category favorites.
- [ ] @Guanyu-Lu creates, restores and deletes history.
- [ ] @ZhengZaikun confirms API authorization for favorites and history.

### Feedback and sharing

- [ ] @Guanyu-Lu submits positive or negative feedback.
- [ ] @ZhengZaikun confirms the API response and validation.
- [ ] @tiantian09091 confirms feedback persistence.
- [ ] @Guanyu-Lu opens shared recommendation state in an isolated session.
- [ ] @ZhengZaikun confirms private account data is not exposed.

### Responsive and accessibility

- [ ] @Guanyu-Lu completes the critical flow on desktop.
- [ ] @Guanyu-Lu completes the critical flow on mobile.
- [ ] @Guanyu-Lu records keyboard access and visible focus.
- [ ] @Guanyu-Lu records label, error-text and zoom/reflow observations.

## 10. External acceptance

- [ ] @Chu-Junjie records two non-team participant IDs without unnecessary personal information.
- [ ] @Chu-Junjie records date, device and browser for each participant.
- [ ] Each participant attempts account, recommendation, pagination, comparison, favorite, history, feedback and share tasks.
- [ ] @Chu-Junjie records independent completion, prompts, observations and defects.
- [ ] Frontend defects are assigned to @Guanyu-Lu.
- [ ] Backend/API/test defects are assigned to @ZhengZaikun.
- [ ] Database/PostgreSQL defects are assigned to @tiantian09091.
- [ ] @Chu-Junjie records retest outcomes.

## 11. Security and recovery

- [ ] @Chu-Junjie confirms repository and evidence records contain no passwords, JWTs, cookies or connection strings.
- [ ] @ZhengZaikun confirms runtime secrets are read from environment configuration.
- [ ] @tiantian09091 records the database backup and recovery approach.
- [ ] @tiantian09091 confirms the importer was not run against production user data.
- [ ] @Chu-Junjie records rollback steps for the candidate and final merge.

## 12. Release decision

- [ ] @ZhengZaikun confirms backend/API/test gates.
- [ ] @tiantian09091 confirms database/PostgreSQL/persistence gates.
- [ ] @Guanyu-Lu confirms frontend/browser/accessibility gates.
- [ ] @Chu-Junjie confirms external acceptance, open defects and known limitations.
- [ ] @Chu-Junjie records `Go`, `Conditional Go` or `No-Go` in the team meeting notes and release record.

`Go` requires every mandatory gate to pass. `Conditional Go` permits only explicitly accepted non-critical limitations. `No-Go` applies when a mandatory gate fails or evidence is incomplete.

## 13. Reconciliation to `main`

- [ ] @Chu-Junjie creates the approved reconciliation branch from the verified candidate.
- [ ] @Chu-Junjie refreshes the branch comparison and changed-file inventory.
- [ ] @ZhengZaikun approves backend/test/dependency conflict decisions.
- [ ] @tiantian09091 approves database/catalogue/importer conflict decisions.
- [ ] @Guanyu-Lu approves frontend conflict decisions.
- [ ] @Chu-Junjie updates README, meeting notes, status, traceability and release records.
- [ ] Affected CI and smoke checks are rerun.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve the final PR to `main`.
- [ ] The final PR passes required checks and is merged.

## 14. Final tag and package

- [ ] @Chu-Junjie records the final `main` SHA.
- [ ] @Chu-Junjie creates the release tag and release notes.
- [ ] @Guanyu-Lu confirms the deployed frontend reference.
- [ ] @ZhengZaikun confirms the final CI/API reference.
- [ ] @tiantian09091 confirms the database/recovery reference.
- [ ] @Chu-Junjie creates the final archive without secrets, virtual environments or temporary test data.
- [ ] @Chu-Junjie records the checksum.
- [ ] @Chu-Junjie closes completed Issues and retains deferred items in the backlog.

## 15. Final record

```text
Final main commit:
Release tag:
Canonical CI:
Catalogue verification:
PostgreSQL identity and counts:
Persistence and privacy:
Desktop/mobile E2E:
External acceptance:
Known limitations:
Release decision:
Final archive:
Checksum:
```

No unchecked item may be inferred as complete from a meeting decision, implementation presence or document approval.