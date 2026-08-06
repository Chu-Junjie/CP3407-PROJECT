# Final Acceptance and Release Checklist

**Project:** Smart Digital Product Recommendation Platform  
**Release coordinator:** Chu Junjie  
**Authoritative implementation branch:** `feature/product-database`  
**Checklist state:** Prepared; incomplete items must remain unchecked until evidence exists

## 1. Release identification

| Field | Value |
|---|---|
| Release name/version | Pending |
| Release-candidate branch | Pending |
| Release-candidate SHA | Pending |
| Freeze date/timezone | Pending |
| Target branch | `main` |
| Final `main` SHA | Pending |
| Release tag | Pending |
| Frontend URL | Pending verification |
| API URL | Pending verification |
| Production database | Pending verification |
| Release decision | Pending |

## 2. Scope and requirements

- [x] Current V3 scope is recorded in `docs/requirements-traceability.md`.
- [x] Implemented, deferred and runtime-pending requirements are distinguished.
- [x] US-09 Budget Alternatives is recorded as Deferred / `Unscheduled`.
- [x] Current-release US-09 limitation wording is defined.
- [ ] Technical owners approve the requirement mappings.
- [ ] Every current-release requirement has implementation evidence.
- [ ] Every mandatory requirement has applicable runtime acceptance evidence.
- [ ] Accepted limitations are approved and visible in final documentation.
- [ ] No historical iteration statement is presented as current release status.

## 3. Architecture and design

- [x] System context is documented.
- [x] Logical component architecture is documented.
- [x] Deployment architecture is documented.
- [x] Database entities and relationships are documented.
- [x] Authentication and privacy boundaries are documented.
- [x] Recommendation and pagination flow is documented.
- [x] Desktop/mobile interface structure is documented.
- [x] Major engineering decisions and limitations are documented.
- [ ] Zaikun approves backend/API/authentication descriptions.
- [ ] Yuyang approves schema/catalogue/PostgreSQL descriptions.
- [ ] Guanyu approves interface/responsive/accessibility descriptions.
- [ ] Any required external UML, ERD or prototype links are current and accessible.

## 4. Code and implementation integrity

- [ ] Release-candidate SHA is frozen.
- [ ] Working tree is clean for the candidate.
- [ ] No unreviewed feature change entered after freeze.
- [ ] V3 backend implementation is preserved.
- [ ] V3 frontend implementation is preserved.
- [ ] V3 database, catalogue and importer implementation is preserved.
- [ ] Owner-controlled technical conflicts are resolved by the relevant owner.
- [ ] No development credentials or secrets are committed.
- [ ] Generated and binary files have an approved release treatment.

## 5. Dependencies and environment

- [x] Runtime dependencies are documented.
- [x] Supported Python version is recorded.
- [x] Local setup procedure is documented.
- [x] Production start command is documented.
- [x] Environment-variable names are documented without values.
- [ ] Clean-environment dependency installation succeeds for the candidate.
- [ ] `python -m pip check` succeeds or any limitation is recorded.
- [ ] Final dependency list is retained.
- [ ] Zaikun approves backend/runtime dependency strategy.
- [ ] Yuyang approves PostgreSQL driver and database configuration.

## 6. Automated testing

Canonical command:

```bash
python -m pytest -q test_server.py
```

Historical audit:

```bash
python -m pytest -q test_mock.py
```

- [x] Canonical V3 test scope is defined.
- [x] Historical V2 mock audit is retained separately.
- [x] Workflow run `31096706920` recorded 12/12 passing for a named PR ref.
- [x] Tracked-file integrity passed for the recorded workflow run.
- [ ] Canonical suite is rerun for the final release candidate.
- [ ] Candidate test collection count is recorded.
- [ ] Candidate test result and duration are recorded.
- [ ] Candidate tracked-file integrity passes.
- [ ] Required GitHub Actions checks are successful.
- [ ] Zaikun approves the final automated-test result.

## 7. Catalogue and local database verification

Run catalogue checks only against a disposable copy.

- [ ] Importer command and environment are recorded.
- [ ] Input and output database paths are recorded without personal data.
- [ ] `products` count is 11,000.
- [ ] `product_specs` count is 2,000.
- [ ] Joined recommendation candidates count is 2,000.
- [ ] Category distribution is 800 laptops, 833 smartphones, 300 smart watches, 61 headphones and 6 tablets.
- [ ] Duplicate product IDs count is 0.
- [ ] Duplicate specification IDs count is 0.
- [ ] Orphan specification count is 0.
- [ ] Missing source metadata count is 0.
- [ ] Generated catalogue artifact contains no private user rows.
- [ ] Repeated generation behaviour is recorded.
- [ ] Original tracked database remains unchanged unless an approved update is intended.
- [ ] Yuyang approves the catalogue verification result.

## 8. Deployment identity

### GitHub Pages

- [ ] Frontend URL is recorded.
- [ ] Source branch and deployed commit are identified.
- [ ] Deployment date/time is recorded.
- [ ] Page loads without blocking console errors.
- [ ] Browser Network evidence confirms the intended API destination.

### Render API

- [ ] API URL is recorded.
- [ ] Deployed commit is identified.
- [ ] Build command is confirmed.
- [ ] Start command is confirmed.
- [ ] Service state is healthy.
- [ ] `/api/health` succeeds.
- [ ] No credential value is retained in evidence.

## 9. PostgreSQL verification

- [ ] `DATABASE_URL` is configured without exposing its value.
- [ ] `/api/health` reports PostgreSQL.
- [ ] Expected application tables exist.
- [ ] Deployed product/specification counts are recorded.
- [ ] Schema initialization succeeds for the candidate.
- [ ] The web service is not relying on ephemeral SQLite for user data.
- [ ] Yuyang approves the deployed database result.
- [ ] Zaikun approves API/database integration behaviour.

## 10. Persistence and privacy

Using non-sensitive demonstration accounts:

- [ ] Account A can register and log in.
- [ ] Account A can save a favorite.
- [ ] Account A can create a search-history record.
- [ ] Account A can restore its saved result snapshot.
- [ ] Account A can submit feedback.
- [ ] Before-restart evidence is retained.
- [ ] Service restart or redeploy is performed.
- [ ] Account A can log in after restart/redeploy.
- [ ] Favorite persists.
- [ ] History and snapshot persist.
- [ ] Feedback persists.
- [ ] Account B has no access to Account A favorites.
- [ ] Account B cannot access Account A history ID.
- [ ] Tokens, passwords and personal data are absent from retained evidence.

## 11. Browser end-to-end acceptance

### Foundation and network

- [ ] Frontend loads successfully.
- [ ] Intended API receives requests.
- [ ] Loading state is observed.
- [ ] Empty state is observed.
- [ ] Error state is observed.
- [ ] Source and historical-price wording is accurate.

### Authentication

- [ ] Register succeeds.
- [ ] Login succeeds.
- [ ] Current identity is displayed correctly.
- [ ] Invalid credentials are rejected.
- [ ] Protected endpoints reject unauthenticated access.
- [ ] Logout removes access to private views.

### Recommendation

- [ ] Valid recommendation request succeeds.
- [ ] Returned category matches the request.
- [ ] Returned prices obey the maximum budget.
- [ ] Excluded brand does not appear.
- [ ] Separate Top 5 is visible.
- [ ] Next and previous page controls work.
- [ ] Pagination retains the same query and filters.
- [ ] Invalid input and no-result behaviour are acceptable.

### Comparison

- [ ] Two products can be compared.
- [ ] Three products can be compared.
- [ ] Invalid comparison is rejected.
- [ ] Available specifications are displayed accurately.

### Favorites and history

- [ ] Favorite can be added.
- [ ] Favorite can be removed.
- [ ] Same-category favorites can be compared.
- [ ] History entry is created.
- [ ] History snapshot can be restored.
- [ ] History entry can be deleted.

### Feedback and sharing

- [ ] Helpful or Not Helpful feedback succeeds.
- [ ] Share state can be generated.
- [ ] Shared state opens in an isolated session.
- [ ] Private account data is not exposed by sharing.
- [ ] US-09 is not presented as an active feature.

### Responsive and accessibility

- [ ] Critical flow succeeds on desktop.
- [ ] Critical flow succeeds on mobile viewport/device.
- [ ] Major controls are keyboard accessible.
- [ ] Visible focus is present.
- [ ] Labels and errors are readable.
- [ ] Basic zoom/reflow behaviour is acceptable or documented.

## 12. External acceptance

### Participant 1

- [ ] Non-team participant confirmed.
- [ ] Device/browser recorded.
- [ ] Required tasks attempted.
- [ ] Independent completion recorded.
- [ ] Prompts and difficulties recorded.
- [ ] Feedback recorded without unnecessary personal data.
- [ ] Related defects created and retested where required.

### Participant 2

- [ ] Non-team participant confirmed.
- [ ] Device/browser recorded.
- [ ] Required tasks attempted.
- [ ] Independent completion recorded.
- [ ] Prompts and difficulties recorded.
- [ ] Feedback recorded without unnecessary personal data.
- [ ] Related defects created and retested where required.

## 13. Defect and risk closure

- [ ] Every failed or blocked check has an Issue or accepted limitation.
- [ ] Severity and release impact are recorded.
- [ ] Defects are assigned to the correct technical owner.
- [ ] Release-blocking defects are closed and retested.
- [ ] Accepted limitations have explicit rationale and approval.
- [ ] No critical unresolved defect remains.

## 14. Documentation consistency

- [ ] README clearly identifies the current V3 release.
- [ ] Historical iteration material is labelled as historical.
- [ ] README test commands match the approved strategy.
- [ ] README deployment links identify the intended environment.
- [ ] Project status matches actual evidence.
- [ ] Requirements traceability matches actual evidence.
- [ ] Architecture and toolchain records are current.
- [ ] Release evidence index is current.
- [ ] Deferred US-09 wording is consistent.
- [ ] No unsupported completion claim remains.

## 15. Reconciliation to `main`

- [ ] Reviewed V3 package is merged into `feature/product-database`.
- [ ] Release candidate is frozen and verified.
- [ ] Reconciliation branch is created from V3.
- [ ] `main`-only files are inventoried and classified.
- [ ] Useful historical evidence is retained.
- [ ] Older code does not overwrite V3 implementation.
- [ ] Backend conflicts are resolved by Zaikun.
- [ ] Database/catalogue conflicts are resolved by Yuyang.
- [ ] Frontend conflicts are resolved by Guanyu.
- [ ] Coordinator documentation conflicts are resolved by Junjie.
- [ ] Final reconciliation PR includes evidence and rollback information.
- [ ] Final PR has required approvals.
- [ ] Required tests/checks pass.
- [ ] Final PR is merged to `main`.

## 16. Release package

- [ ] Final `main` SHA is recorded.
- [ ] Release tag is created.
- [ ] Release notes identify scope and limitations.
- [ ] Final project archive is created.
- [ ] Virtual environments, secrets and temporary test data are excluded.
- [ ] Archive checksum is recorded.
- [ ] Database backup/recovery information is retained.
- [ ] Final deployed version is identified where applicable.
- [ ] Completed Issues are closed.
- [ ] Deferred backlog items remain traceable.

## 17. Go/No-Go decision

| Gate | Result | Evidence |
|---|---|---|
| Formal team review | Pending | Pending |
| Canonical CI for candidate | Pending | Pending |
| Catalogue integrity | Pending | Pending |
| PostgreSQL identity/counts | Pending | Pending |
| Persistence/privacy | Pending | Pending |
| Desktop/mobile E2E | Pending | Pending |
| External acceptance | Pending | Pending |
| Critical defects | Pending | Pending |
| Accepted limitations | Pending | Pending |

**Decision:** Pending  
**Decision date/timezone:** Pending  
**Release coordinator:** Chu Junjie  
**Technical-owner confirmations:** Pending

Decision values:

- **Go:** every mandatory gate passes;
- **Conditional Go:** only approved non-critical limitations remain;
- **No-Go:** a mandatory gate fails, evidence is incomplete or a release-blocking defect remains.

## 18. Sign-off

| Role | Name | Outcome | Date | GitHub evidence |
|---|---|---|---|---|
| Project Manager / Release Coordinator | Chu Junjie | Pending | Pending | Pending |
| Backend / Algorithm / Test Owner | Zaikun Zheng | Pending | Pending | Pending |
| Database / Catalogue / PostgreSQL Owner | Yuyang Zhou | Pending | Pending | Pending |
| Frontend / UI / Browser Verification Owner | Guanyu Lu | Pending | Pending | Pending |

This checklist is ready for execution. Unchecked items must not be completed from implementation presence, informal agreement or inference alone.
