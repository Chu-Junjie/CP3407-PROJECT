# Release Meeting Record and Action Plan

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation branch:** `feature/product-database`  
**Meeting record maintained by:** @Chu-Junjie  
**Document state:** Prepared for formal review and execution

## 1. Purpose

This record documents the release decisions, named responsibilities and remaining actions agreed in the team meeting notes. It defines how the V3 implementation moves from repository-ready status to a reviewed, verified and packaged release on `main`.

A meeting decision does not prove that a test, deployment, database, browser or acceptance activity passed. Every runtime result must identify the tested commit, environment, executor, steps and observed outcome.

## 2. Named responsibilities

| Work area | Named responsibility |
|---|---|
| Meeting notes, schedule, traceability, evidence review, defect assignment, acceptance coordination, reconciliation record and release decision | @Chu-Junjie |
| Flask API, authentication, recommendation, pagination, backend defects, automated tests and CI interpretation | @ZhengZaikun |
| Schema, catalogue, importer, provenance, PostgreSQL, persistence, backup and database defects | @tiantian09091 |
| Interface, GitHub Pages, desktop/mobile flows, accessibility, browser evidence and frontend defects | @Guanyu-Lu |
| External acceptance | Two non-team participants coordinated by @Chu-Junjie |

## 3. Operating rules recorded in the meeting notes

- Formal GitHub Approval must apply to the current PR head before merge.
- @Chu-Junjie does not modify implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu without explicit approval.
- Runtime claims require actual execution for a named commit and environment.
- US-09 Budget Alternatives is Deferred and is not a current release gate.
- The catalogue importer must run against a disposable build copy and must not run against production user data.
- Passwords, JWTs, cookies, database URLs and secrets must not appear in evidence.
- `feature/product-database` remains the implementation baseline for reconciliation.
- A changed release candidate receives a new SHA and the affected checks are rerun.

## 4. Phase A — Formal review of the project record package

Review these Pull Requests:

1. #35 — CI workflow and canonical test scope;
2. #47 — US-09 scope decision;
3. #48 — database verification record;
4. #52 — design and architecture;
5. #54 — Agile and retrospective evidence;
6. #58 — development toolchain and dependencies;
7. #44 — V3/`main` reconciliation plan;
8. #60 — status, traceability and release controls;
9. #46 — release evidence index;
10. #50 — project closeout review record.

### Required formal reviews

- @ZhengZaikun reviews backend, API, authentication, recommendation, automated tests, CI and runtime-dependency statements.
- @tiantian09091 reviews schema, catalogue, importer, provenance, PostgreSQL, persistence and recovery statements.
- @Guanyu-Lu reviews frontend, GitHub Pages, responsive behaviour, accessibility and browser-flow statements.
- @Chu-Junjie checks meeting-note consistency, status vocabulary, evidence boundaries, merge order and release controls.

### Completion conditions

- [ ] Required GitHub Approvals are recorded for each current PR head.
- [ ] Requested changes are completed by the named person responsible for the affected area.
- [ ] Each approved PR is mergeable against the latest V3 base.
- [ ] No runtime result is inferred from a meeting decision or documentation approval.

## 5. Phase B — Merge approved records into the release branch

Recommended order:

```text
#35 → #47 → #48 → #52 → #54 → #58 → #44 → #60 → #46 → #50
```

Before each merge, @Chu-Junjie checks:

- the approved head SHA has not changed;
- the formal Approval applies to that head;
- the changed-file list matches the PR purpose;
- no implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu is changed outside the approved scope;
- the squash-merge title accurately describes the record.

### Completion conditions

- [ ] All approved record PRs are merged into `feature/product-database`.
- [ ] Merge commits and PR numbers are retained in the meeting record and evidence index.
- [ ] The V3 branch contains the complete reviewed project record set.

## 6. Phase C — Freeze the release candidate

@Chu-Junjie records:

| Field | Value |
|---|---|
| Candidate branch | Pending |
| Candidate SHA | Pending |
| Freeze date/timezone | Pending |
| Included PRs | Pending |
| Formal approvals | Pending |
| Known limitations | Pending |

After freeze:

- no feature changes enter the candidate;
- @ZhengZaikun, @tiantian09091 or @Guanyu-Lu may submit a release-blocking fix only for their stated area;
- each fix requires a separate Issue, branch, PR, review and retest;
- @Chu-Junjie records the new candidate SHA and affected reruns.

## 7. Phase D — Canonical CI

@ZhengZaikun verifies the frozen candidate with:

```bash
python -m pytest --collect-only -q test_server.py
python -m pytest -q test_server.py
git diff --exit-code
```

Required evidence:

- workflow run ID;
- tested candidate SHA or merge ref;
- runner, Python and pytest versions;
- collected, passed and failed counts;
- execution time and exit result;
- tracked-file integrity result.

Expected result:

```text
12 tests collected
12 tests passed
tracked-file integrity passed
```

The historical `test_mock.py` audit remains visible and non-blocking.

### Completion conditions

- [ ] @ZhengZaikun confirms the canonical suite passed for the frozen candidate.
- [ ] Tracked-file integrity passed.
- [ ] @Chu-Junjie links the evidence from the release index and checklist.

## 8. Phase E — Catalogue and local database verification

@tiantian09091 runs the importer against a disposable database copy and retains:

- products: 11,000;
- product specifications: 2,000;
- joined recommendation candidates: 2,000;
- category distribution: 800/833/300/61/6;
- duplicate product IDs: 0;
- duplicate specification IDs: 0;
- orphan specifications: 0;
- source metadata present;
- private tables empty in the generated catalogue artifact;
- repeated-generation behaviour.

The evidence must include candidate SHA, Python version, commands, source/output paths, timestamp and complete non-sensitive output.

### Completion conditions

- [ ] @tiantian09091 confirms all counts and integrity checks.
- [ ] No tracked source database is unintentionally modified.
- [ ] Any failure has an Issue explicitly assigned to @tiantian09091 or @ZhengZaikun when backend integration is involved.

## 9. Phase F — Deployment identity and PostgreSQL

- @Guanyu-Lu records the GitHub Pages source branch/folder and visible frontend commit.
- @ZhengZaikun records the Render API commit, build/start commands and `/api/health` behaviour.
- @tiantian09091 confirms `DATABASE_URL` is configured without exposing its value, the active dialect is PostgreSQL, expected tables exist and catalogue counts are correct.
- @Chu-Junjie records the evidence IDs and status.

### Completion conditions

- [ ] Frontend and API commit identities are recorded.
- [ ] @tiantian09091 confirms PostgreSQL for the deployed API.
- [ ] @ZhengZaikun confirms API/database integration.
- [ ] No credential or secret is retained.

## 10. Phase G — Persistence and privacy

Using non-sensitive demonstration accounts:

1. @ZhengZaikun creates or verifies the API flow for Account A, favorite, history snapshot and feedback.
2. @tiantian09091 records the rows before restart or redeployment.
3. The service is restarted or redeployed.
4. @tiantian09091 confirms the records persist.
5. @ZhengZaikun verifies Account B cannot access Account A history or favorites.
6. @Guanyu-Lu verifies the corresponding signed-in and signed-out browser behaviour.
7. @Chu-Junjie records statuses without passwords or tokens.

### Completion conditions

- [ ] Account, favorite, history, snapshot and feedback persist.
- [ ] Cross-user access is rejected.
- [ ] Failed checks are assigned explicitly to @ZhengZaikun, @tiantian09091 or @Guanyu-Lu according to the observed area.

## 11. Phase H — Browser E2E

@Guanyu-Lu executes the deployed browser matrix:

- frontend load, console, Network/API destination, loading, empty and error states;
- register, login, current identity, protected-route rejection and logout;
- recommendation, category/budget compliance, Top 5 and pagination;
- compare two and three products and invalid comparison handling;
- add/remove favorite and same-category favorite comparison;
- create, restore and delete history;
- feedback;
- share-state restoration in an isolated session;
- desktop and mobile completion;
- keyboard access, visible focus, labels, readable errors and zoom/reflow.

@ZhengZaikun confirms API/authentication observations. @tiantian09091 confirms database/persistence observations. @Chu-Junjie maintains the evidence matrix and retest record.

### Completion conditions

- [ ] Every critical scenario has an evidence ID and status.
- [ ] Frontend failures are assigned to @Guanyu-Lu.
- [ ] Backend/API/test failures are assigned to @ZhengZaikun.
- [ ] Database/PostgreSQL failures are assigned to @tiantian09091.
- [ ] Critical failures are fixed and retested.

## 12. Phase I — External acceptance

@Chu-Junjie coordinates two non-team participants. Each participant attempts:

1. register and log in;
2. find a product within a selected budget;
3. browse another result page;
4. compare two products;
5. save a favorite;
6. reopen search history;
7. submit feedback;
8. share and reopen recommendation state.

Record participant ID, date, device/browser, independent completion, prompts, observations, defects and retest outcome. Do not retain unnecessary personal information.

### Completion conditions

- [ ] Two non-team participants complete the agreed scope.
- [ ] Blocking usability defects are resolved or explicitly accepted.
- [ ] Actual outcomes are retained in `docs/v3-external-uat-record.md`.

## 13. Phase J — Release decision

@Chu-Junjie completes the decision record only after receiving the named confirmations:

| Gate | Confirmation |
|---|---|
| Formal reviews | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| Canonical CI | @ZhengZaikun |
| Catalogue integrity | @tiantian09091 |
| PostgreSQL identity/counts | @tiantian09091 and @ZhengZaikun |
| Persistence/privacy | @tiantian09091, @ZhengZaikun and @Guanyu-Lu |
| Desktop/mobile E2E | @Guanyu-Lu, with API/data confirmation from @ZhengZaikun and @tiantian09091 |
| External acceptance | @Chu-Junjie |
| Accepted limitations | Recorded in team meeting notes by @Chu-Junjie and confirmed by the affected named person |

Decision values:

- **Go:** all mandatory gates pass;
- **Conditional Go:** only explicitly accepted non-critical limitations remain;
- **No-Go:** a mandatory gate fails or evidence is incomplete.

## 14. Phase K — Reconciliation to `main`

After Go or Conditional Go:

1. @Chu-Junjie creates the approved reconciliation branch from the verified V3 candidate.
2. @Chu-Junjie refreshes the `main` comparison and file inventory.
3. @ZhengZaikun decides backend/test/dependency conflicts.
4. @tiantian09091 decides database/catalogue/importer conflicts.
5. @Guanyu-Lu decides frontend conflicts.
6. @Chu-Junjie consolidates meeting notes, status, traceability, README and release records.
7. Affected tests and smoke checks are rerun.
8. The final PR to `main` requires formal Approvals from @ZhengZaikun, @tiantian09091 and @Guanyu-Lu.
9. Merge occurs only after required checks pass.

## 15. Phase L — Tag and package

After merge to `main`, @Chu-Junjie records:

- final `main` SHA;
- release tag;
- release notes and known limitations;
- final archive path;
- checksum;
- database backup/recovery reference from @tiantian09091;
- final CI reference from @ZhengZaikun;
- deployed frontend reference from @Guanyu-Lu;
- closed Issues and deferred backlog entries.

## 16. Current action status

| Phase | Status |
|---|---|
| Formal review | Ready to begin |
| Merge approved records | Pending formal reviews |
| Release-candidate freeze | Pending |
| Final CI | Pending |
| Catalogue verification | Pending |
| Deployment/PostgreSQL | Pending |
| Persistence/privacy | Pending |
| Browser E2E | Pending |
| External acceptance | Pending |
| Reconciliation | Pending |
| Release packaging | Pending |

Execution results are added only after the corresponding activity is completed.