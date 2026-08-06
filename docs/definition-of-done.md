# Definition of Done — Teacher Feedback Revision v3.0

**Project:** Smart Digital Product Recommendation Platform  
**Applies to:** All User Stories, bugs, data work, documentation tasks, deployment work and the final release  
**Authoritative implementation baseline:** `feature/product-database`

## 1. Purpose

This Definition of Done prevents code presence, a local screenshot or an unreviewed test result from being reported as complete. It aligns requirements, implementation, data, security, testing, integration, version control, deployment, documentation and acceptance evidence.

## 2. V3 baseline rule

The adopted v3 direction includes:

- Flask and SQLAlchemy;
- SQLite for the bundled local demonstration;
- PostgreSQL through `DATABASE_URL` for persistent production use;
- 11,000 `products` rows, including 2,000 joined recommendation-ready public-dataset records;
- 2,000 `product_specs` rows with source information;
- accounts, JWT authentication, favorites, private search history, saved result snapshots and feedback;
- paginated recommendations with a separate Top 5;
- GitHub Pages frontend and Render API deployment.

The earlier 9,000/33 Yuyang Unified baseline is historical and must not be described as the current final design.

The v3 baseline is not Done until it is reviewed, merged, tested in the intended complete environment, deployed where applicable and accepted with retained evidence.

## 3. Status definitions

| Status | Meaning |
|---|---|
| `Todo` | Not started or no active evidence exists. |
| `Planned` | Requirement and owner are agreed, but implementation has not started. |
| `Candidate` | An artifact exists, but applicable verification is incomplete. |
| `In Progress` | Work is actively being implemented, tested, reviewed or documented. |
| `Blocked` | A named dependency prevents progress or verification. |
| `Implemented` | Code/data exists on the authoritative branch, but one or more review, test, deployment or acceptance gates remain open. |
| `Verified` | Named evidence passed for a specified commit and environment. |
| `Done` | Every applicable item in this document is satisfied. |
| `Deferred` | Removed from final scope with an approved reason and impact statement. |

`Implemented`, `Verified` and `Done` are not interchangeable.

## 4. User Story Definition of Done

A User Story is Done only when every applicable section below is satisfied.

### 4.1 Requirements and scope

- [ ] Final wording and acceptance criteria are recorded.
- [ ] Priority, estimate, owner and dependencies are recorded.
- [ ] Teacher-feedback changes are reflected in the final scope.
- [ ] Any replaced v2 requirement is identified as historical or deferred.
- [ ] Unsupported product, price, licence or deployment claims are removed.

### 4.2 Design and contract

- [ ] API, database, architecture and UI documents match the implementation.
- [ ] Field, route and table names match the v3 contract.
- [ ] Security, privacy and persistence behaviour is documented where applicable.
- [ ] Error, empty, boundary and authorization behaviour is defined.
- [ ] Relevant diagrams have been updated.

### 4.3 Implementation

- [ ] The feature works with the v3 database and real integrated API path.
- [ ] Every acceptance criterion is implemented.
- [ ] Existing required behaviour has not regressed.
- [ ] Errors and boundary cases are handled safely.
- [ ] No secrets, passwords, tokens or production credentials are committed.
- [ ] Missing data is displayed honestly and is not invented.

### 4.4 Automated testing

- [ ] Normal behaviour is covered.
- [ ] At least one invalid or boundary case is covered.
- [ ] Authorization/privacy cases are covered for user-owned data.
- [ ] A regression test exists for each fixed defect where practical.
- [ ] All intended test files are collected and executed.
- [ ] The command, date, commit SHA, environment, exit code and passed/failed counts are saved.
- [ ] Tests leave tracked database and data files unchanged.
- [ ] A clean environment or CI run passes.
- [ ] TDD is claimed only when a failing test was genuinely observed before the implementation.

### 4.5 Integration and acceptance

- [ ] Frontend, backend and database agree with the v3 API contract.
- [ ] The feature passes a manual end-to-end test.
- [ ] The feature works in the deployed application when deployment applies.
- [ ] Browser Network/API evidence is retained for frontend flows.
- [ ] Tester name/role, date, steps and observed result are recorded.
- [ ] Failures are linked to an Issue or explicitly accepted limitation.

### 4.6 Version control and review

- [ ] Work is completed on an appropriate feature/fix/docs branch.
- [ ] Commits use descriptive messages.
- [ ] The Pull Request identifies scope, acceptance criteria, evidence and limitations.
- [ ] The PR links the applicable Issue or traceability entry.
- [ ] At least one non-author teammate reviews the work.
- [ ] Review comments are resolved or documented.
- [ ] The PR is merged into the agreed target branch.
- [ ] Related project status and traceability records are updated.

### 4.7 Documentation

- [ ] README and `docs/` pages match the final implementation.
- [ ] Installation, local run, test and deployment instructions are accurate.
- [ ] Known limitations and historical-data pricing are stated.
- [ ] Requirements Traceability is updated.
- [ ] The responsible member explains their own technical component.
- [ ] Links, screenshots and commands have been checked.

## 5. V3 database and catalogue Definition of Done

The data/database revision is Done only when:

- [ ] `products` and `product_specs` exact release counts are recorded.
- [ ] The intended 11,000/2,000 counts are independently verified for the release commit.
- [ ] Every active recommendation specification has a valid joined ProductID.
- [ ] Duplicate ProductIDs and required-column checks pass.
- [ ] `DataSource`, source licence and transformation notes are reviewed.
- [ ] Historical prices are not described as live retail prices.
- [ ] Missing fields remain honest values such as `Not specified`.
- [ ] `import_real_catalog.py` reproduces the expected catalogue or its prerequisites/limitations are documented.
- [ ] Repeated local initialization does not create duplicates.
- [ ] PostgreSQL initialization/seed is tested when production uses PostgreSQL.
- [ ] Production persistence survives a restart or redeploy test.
- [ ] Backup and rollback/recovery instructions are documented.

## 6. V3 accounts, privacy and security Definition of Done

Accounts and user-owned data are Done only when:

- [ ] Passwords are stored as hashes, never plaintext.
- [ ] Registration validates required fields and duplicate username/email behaviour.
- [ ] Login accepts the documented identifier and rejects invalid credentials.
- [ ] JWT authentication rejects missing, malformed and invalid tokens.
- [ ] Production `JWT_SECRET_KEY` is a random environment value of at least 32 characters.
- [ ] No development/default secret is relied on in production.
- [ ] A user cannot read, delete or compare another user's private history/favorites.
- [ ] History and favorites persist in the production database.
- [ ] Logs and error responses do not expose passwords, tokens or internal secrets.
- [ ] CORS permits the intended frontend origin without unnecessarily broad credentials access.

## 7. V3 recommendation, pagination and comparison Definition of Done

- [ ] Recommendation results contain the documented identity, category, brand, price, score, reason, specification, URL and source fields.
- [ ] `page` and `per_page` boundaries are validated.
- [ ] Default page size and maximum page size match the contract.
- [ ] `total_candidates`, `total_pages`, page data and separate Top 5 are internally consistent.
- [ ] Empty and out-of-range results are handled.
- [ ] Comparison accepts exactly 2 or 3 unique valid joined product IDs.
- [ ] Invalid, duplicate, missing and unjoined IDs are rejected consistently.
- [ ] Favorites comparison verifies ownership and same-category rules.
- [ ] Excluded brands are applied consistently from text and explicit fields.

## 8. V3 frontend Definition of Done

- [ ] The production frontend calls the deployed API rather than fixed final mock data.
- [ ] Registration, login, logout/account state and error states are usable.
- [ ] Recommendation pagination works across first, middle, last and empty states.
- [ ] Top 5 and full paginated results are clearly distinguished.
- [ ] History can be opened and deleted by its owner.
- [ ] Favorites can be added, removed and compared under the documented rules.
- [ ] Product/source links use safe `http` or `https` URLs and a clear fallback.
- [ ] Share/restore works with special characters and exclusions in another browser.
- [ ] Loading, success, empty, validation, timeout and backend-error states are visible.
- [ ] Mobile layout, keyboard navigation and basic accessibility are checked.
- [ ] Browser Network screenshots or equivalent request/response evidence are retained.

## 9. Bug Definition of Done

A bug is Done only when:

1. Reproduction steps and environment are recorded.
2. The root cause is identified.
3. A failing regression test is added where practical.
4. The responsible technical owner implements the smallest correct fix.
5. The regression test passes.
6. The full relevant suite passes.
7. Data/database files remain unchanged unless the change is intentional and reviewed.
8. A non-author reviews the fix.
9. The integrated or deployed application is rechecked.
10. The Issue is closed with evidence.

## 10. Documentation-task Definition of Done

A documentation task is Done only when:

- it is based on real repository or test evidence;
- planned, implemented, verified and Done work are distinguished;
- terminology matches the v3 implementation;
- outdated v2 statements are identified as historical rather than silently mixed with v3;
- owner-authored technical claims are preserved or reviewed by the responsible owner;
- links, file paths, commands and screenshots work;
- a non-author reviews technical accuracy.

## 11. Coordinator governance boundary

Junjie's governance work may update planning, project status, traceability, Definition of Done, acceptance records and release records.

It must not directly change teammate-owned:

- backend or recommendation implementation;
- authentication implementation;
- frontend implementation;
- automated test implementation;
- datasets, catalogue importer or database files;
- teammate technical explanations.

A discovered technical problem is recorded and assigned to its owner. It is not silently fixed in a governance commit.

## 12. Release Definition of Done

The final release may be tagged only when:

- [ ] The final scope and deferred requirements are approved.
- [ ] All required stories have honest final statuses.
- [ ] All blocking defects are closed or formally accepted with impact.
- [ ] The authoritative v3 baseline is reviewed and merged into `main`.
- [ ] The intended complete automated suite passes in a clean environment or CI.
- [ ] GitHub Actions shows a successful run for the release commit.
- [ ] The release commit leaves tracked database/data files in the intended state.
- [ ] GitHub Pages → Render → PostgreSQL end-to-end flow is smoke-tested.
- [ ] Accounts, history and favorites persist across a production restart/redeploy check.
- [ ] No secrets are present in the repository.
- [ ] At least two non-team acceptance tests are recorded where available before submission.
- [ ] Architecture, ERD/database, API, testing, deployment, agile evidence and user guide are linked from README.
- [ ] A changelog and release tag are created.
- [ ] A final ZIP backup is created, opened and checked.
- [ ] Final known limitations are recorded.

## 13. Completion evidence template

```markdown
## Completion Evidence

- Requirement / Issue:
- Owner:
- Branch:
- Commit SHA:
- Pull Request:
- Reviewer:
- Acceptance criteria:
- Automated test command:
- Environment:
- Automated result and exit code:
- Manual acceptance steps/result:
- Deployment evidence:
- Data/database integrity result:
- Documentation updated:
- Known limitations:
- Final status:
```

## 14. Integrity rule

The team must not fabricate client feedback, test results, commit history, TDD history, deployment results, licence claims, security verification or iteration evidence. Retrospective evidence must be labelled retrospective. A missing check remains unchecked.
