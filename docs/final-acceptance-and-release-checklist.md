# Final Acceptance and Release Checklist

**Project:** Smart Digital Product Recommendation Platform  
**Release coordination and meeting record:** @Chu-Junjie  
**Authoritative implementation branch:** `feature/product-database`  
**Checklist state:** Incomplete items remain unchecked until actual evidence exists

## 1. Evidence rule

This checklist is maintained from repository evidence and the team meeting notes recorded by @Chu-Junjie. Meeting decisions and formal document reviews do not replace executed CI, database, deployment, E2E or external-acceptance evidence.

## 2. Release identification

- [X] @Chu-Junjie records the release-candidate branch.
- [X] @Chu-Junjie records the full release-candidate SHA.
- [X] @Chu-Junjie records the freeze date and timezone.
- [X] @Chu-Junjie records included Pull Requests and merge commits.
- [X] @Chu-Junjie records known limitations, including deferred US-09.
- [X] @Chu-Junjie confirms no feature change entered after freeze without a new candidate SHA.

## 3. Formal GitHub reviews

- [X] @ZhengZaikun approves PR #35 for CI and the canonical test scope.
- [X] @ZhengZaikun and @Guanyu-Lu approve PR #47 for the US-09 scope decision.
- [X] @tiantian09091 and @ZhengZaikun approve PR #48 for database and API integration wording.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #52 for their named architecture sections.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #54 for their named iteration records.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #58 for their named toolchain sections.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #44 for reconciliation boundaries.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #60 for technical mappings.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #46 for the evidence index.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve PR #50 for the project closeout review record.
- [X] @Chu-Junjie confirms every Approval applies to the current PR head.

## 4. Approved record merges into the release branch

- [X] @Chu-Junjie merges approved PRs in the recorded sequence.
- [X] @Chu-Junjie records every merged PR number and commit SHA.
- [X] @Chu-Junjie confirms changed files match each approved scope.
- [X] @Chu-Junjie confirms no unapproved implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu was changed.

## 5. Canonical CI

- [X] @ZhengZaikun runs `python -m pytest --collect-only -q test_server.py` for the frozen candidate.
- [X] @ZhengZaikun runs `python -m pytest -q test_server.py` for the frozen candidate.
- [X] @ZhengZaikun runs `git diff --exit-code` after tests.
- [X] @ZhengZaikun records the workflow run ID, tested SHA/ref, runner, Python version and pytest version.
- [X] @ZhengZaikun records 12 tests collected and 12 tests passed.
- [X] @ZhengZaikun records tracked-file integrity as passed.
- [X] @Chu-Junjie links the final CI evidence from the release index.

The historical `test_mock.py` audit remains non-release evidence and must not be reported as a V3 regression.

## 6. Catalogue and local database integrity

Run against a disposable copy only.

- [X] @tiantian09091 records `products = 11,000`.
- [X] @tiantian09091 records `product_specs = 2,000`.
- [X] @tiantian09091 records 2,000 joined recommendation-ready rows.
- [X] @tiantian09091 records category counts `800 / 833 / 300 / 61 / 6`.
- [X] @tiantian09091 confirms duplicate product IDs = 0.
- [X] @tiantian09091 confirms duplicate specification IDs = 0.
- [X] @tiantian09091 confirms orphan specifications = 0.
- [X] @tiantian09091 confirms source metadata is present.
- [X] @tiantian09091 confirms generated private tables are empty.
- [X] @tiantian09091 records repeated-generation behaviour.
- [X] @tiantian09091 confirms no tracked source database was unintentionally modified.

## 7. Deployed frontend, API and PostgreSQL identity

- [X] @Guanyu-Lu records the GitHub Pages URL, source branch/folder and visible frontend commit.
- [X] @ZhengZaikun records the Render API URL, deployed commit, build command and start command.
- [X] @ZhengZaikun records the non-sensitive `/api/health` response.
- [X] @tiantian09091 confirms `DATABASE_URL` is configured without exposing its value.
- [X] @tiantian09091 confirms the active deployed database dialect is PostgreSQL.
- [X] @tiantian09091 confirms all expected tables exist.
- [X] @tiantian09091 records deployed product and specification counts.
- [X] @ZhengZaikun confirms the API is using the recorded PostgreSQL environment.
- [X] @Chu-Junjie confirms the deployment evidence is tied to the frozen candidate or approved release commit.

## 8. Persistence and privacy

Use non-sensitive demonstration accounts and do not retain credentials or tokens.

- [X] @ZhengZaikun verifies registration and login for Account A.
- [X] @ZhengZaikun verifies creation of a favorite, history entry, saved result snapshot and feedback record.
- [X] @tiantian09091 records the data before restart or redeployment.
- [X] @tiantian09091 confirms the account data remains after restart or redeployment.
- [X] @ZhengZaikun verifies Account B cannot access Account A history or favorites.
- [X] @Guanyu-Lu verifies the corresponding browser behaviour before and after logout.
- [X] @Chu-Junjie records evidence IDs and statuses without private values.

## 9. Deployed browser E2E

### Foundation

- [X] @Guanyu-Lu confirms the frontend loads without blocking console errors.
- [X] @Guanyu-Lu confirms Network requests reach the intended Render API.
- [X] @Guanyu-Lu records loading, empty and error states.
- [X] @tiantian09091 confirms product-source and historical-price wording is accurate.

### Authentication

- [X] @Guanyu-Lu completes register, login, current identity and logout flows.
- [X] @ZhengZaikun confirms unauthenticated protected requests are rejected.

### Recommendation

- [X] @Guanyu-Lu submits a valid recommendation request.
- [X] @ZhengZaikun confirms category and budget compliance.
- [X] @Guanyu-Lu confirms the separate Top 5 is identifiable.
- [X] @Guanyu-Lu confirms next/previous pagination preserves the query.
- [X] @ZhengZaikun confirms invalid input and invalid-page responses follow the API contract.

### Compare, favorites and history

- [X] @Guanyu-Lu compares two products.
- [X] @Guanyu-Lu compares three products.
- [X] @ZhengZaikun confirms invalid comparison is rejected.
- [X] @Guanyu-Lu adds and removes a favorite.
- [X] @Guanyu-Lu compares supported same-category favorites.
- [X] @Guanyu-Lu creates, restores and deletes history.
- [X] @ZhengZaikun confirms API authorization for favorites and history.

### Feedback and sharing

- [X] @Guanyu-Lu submits positive or negative feedback.
- [X] @ZhengZaikun confirms the API response and validation.
- [X] @tiantian09091 confirms feedback persistence.
- [X] @Guanyu-Lu opens shared recommendation state in an isolated session.
- [X] @ZhengZaikun confirms private account data is not exposed.

### Responsive and accessibility

- [X] @Guanyu-Lu completes the critical flow on desktop.
- [X] @Guanyu-Lu completes the critical flow on mobile.
- [X] @Guanyu-Lu records keyboard access and visible focus.
- [X] @Guanyu-Lu records label, error-text and zoom/reflow observations.

## 10. External acceptance

- [X] @Chu-Junjie records two non-team participant IDs without unnecessary personal information.
- [X] @Chu-Junjie records date, device and browser for each participant.
- [X] Each participant attempts account, recommendation, pagination, comparison, favorite, history, feedback and share tasks.
- [X] @Chu-Junjie records independent completion, prompts, observations and defects.
- [X] Frontend defects are assigned to @Guanyu-Lu.
- [X] Backend/API/test defects are assigned to @ZhengZaikun.
- [X] Database/PostgreSQL defects are assigned to @tiantian09091.
- [X] @Chu-Junjie records retest outcomes.

## 11. Security and recovery

- [X] @Chu-Junjie confirms repository and evidence records contain no passwords, JWTs, cookies or connection strings.
- [X] @ZhengZaikun confirms runtime secrets are read from environment configuration.
- [X] @tiantian09091 records the database backup and recovery approach.
- [X] @tiantian09091 confirms the importer was not run against production user data.
- [X] @Chu-Junjie records rollback steps for the candidate and final merge.

## 12. Release decision

- [X] @ZhengZaikun confirms backend/API/test gates.
- [X] @tiantian09091 confirms database/PostgreSQL/persistence gates.
- [X] @Guanyu-Lu confirms frontend/browser/accessibility gates.
- [X] @Chu-Junjie confirms external acceptance, open defects and known limitations.
- [X] @Chu-Junjie records `Go`, `Conditional Go` or `No-Go` in the team meeting notes and release record.

`Go` requires every mandatory gate to pass. `Conditional Go` permits only explicitly accepted non-critical limitations. `No-Go` applies when a mandatory gate fails or evidence is incomplete.

## 13. Reconciliation to `main`

- [X] @Chu-Junjie creates the approved reconciliation branch from the verified candidate.
- [X] @Chu-Junjie refreshes the branch comparison and changed-file inventory.
- [X] @ZhengZaikun approves backend/test/dependency conflict decisions.
- [X] @tiantian09091 approves database/catalogue/importer conflict decisions.
- [X] @Guanyu-Lu approves frontend conflict decisions.
- [X] @Chu-Junjie updates README, meeting notes, status, traceability and release records.
- [X] Affected CI and smoke checks are rerun.
- [X] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve the final PR to `main`.
- [X] The final PR passes required checks and is merged.

## 14. Final tag and package

- [X] @Chu-Junjie records the final `main` SHA.
- [X] @Chu-Junjie creates the release tag and release notes.
- [X] @Guanyu-Lu confirms the deployed frontend reference.
- [X] @ZhengZaikun confirms the final CI/API reference.
- [X] @tiantian09091 confirms the database/recovery reference.
- [X] @Chu-Junjie creates the final archive without secrets, virtual environments or temporary test data.
- [X] @Chu-Junjie records the checksum.
- [X] @Chu-Junjie closes completed Issues and retains deferred items in the backlog.

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
