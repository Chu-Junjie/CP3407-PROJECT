# V3 Release Execution Plan

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation branch:** `feature/product-database`  
**Plan owner:** Chu Junjie — Project Manager and Release Coordinator  
**Document state:** Prepared for formal review and execution

## 1. Objective

This plan defines the remaining work required to move the V3 implementation from repository-ready status to a reviewed, verified and packaged release on `main`.

The plan preserves technical ownership, requires evidence for each release gate and prevents older branch content from replacing the V3 implementation during integration.

## 2. Operating principles

- Formal review must occur before documentation and workflow PRs are merged.
- Runtime claims require actual execution for a named commit and environment.
- Technical defects are fixed by the relevant component owner.
- The release coordinator manages scope, evidence, retesting and Go/No-Go decisions.
- The V3 branch is the implementation baseline for reconciliation.
- US-09 Budget Alternatives is deferred and is not a current release gate.
- The catalogue importer must never run directly against production user data.
- Credentials, tokens and connection strings must not be retained in evidence.

## 3. Roles and responsibilities

| Role | Owner | Responsibilities |
|---|---|---|
| Project and release coordination | Chu Junjie | Schedule, traceability, evidence review, defect assignment, acceptance, reconciliation and release decision |
| Backend, API and automated tests | Zaikun Zheng | Flask API, authentication, recommendation logic, test scope, backend defects and CI interpretation |
| Database, catalogue and persistence | Yuyang Zhou | Schema, importer, catalogue integrity, PostgreSQL, persistence, backup and database defects |
| Frontend, responsive interface and browser verification | Guanyu Lu | Interface, GitHub Pages, desktop/mobile flows, accessibility and frontend defects |
| External acceptance participants | Two non-team users | Complete assigned tasks and provide independent observations |

## 4. Workstream overview

| Workstream | Current status | Completion condition |
|---|---|---|
| WS-1 Documentation and scope review | Prepared | Formal approvals and approved PRs merged into V3 |
| WS-2 Canonical CI | Verified for recorded PR ref | Passed again for frozen release candidate |
| WS-3 Catalogue integrity | Repository verified | Disposable build and integrity checks pass |
| WS-4 PostgreSQL deployment | Unverified | Deployed API commit, dialect and counts confirmed |
| WS-5 Persistence and privacy | Not Run | Restart/redeploy and cross-user checks pass |
| WS-6 Browser E2E | Not Run | Critical desktop/mobile scenarios completed |
| WS-7 External acceptance | Not Run | Two non-team participants complete required tasks |
| WS-8 Reconciliation to `main` | Not started | Approved reconciliation PR merged |
| WS-9 Release packaging | Not started | Tag, archive, checksum and final record created |

## 5. Phase 1 — Formal package review

### Scope

Review the following Pull Requests:

- #35 — CI workflow and canonical test scope;
- #44 — V3/`main` reconciliation plan;
- #46 — release evidence index;
- #47 — US-09 decision;
- #48 — database release verification;
- #50 — submission and release review package;
- #52 — design and architecture;
- #54 — Agile iteration and feedback evidence;
- #58 — development toolchain and dependencies;
- #60 — project status, traceability and release-gate alignment.

### Review assignments

#### Zaikun

Confirm:

- API and authentication descriptions;
- recommendation and pagination behaviour;
- canonical V3 test scope;
- historical mock-test classification;
- backend dependencies and Render service wording;
- US-09 backend/API impact.

#### Yuyang

Confirm:

- schema and relationships;
- catalogue quotas and provenance;
- importer safety boundary;
- SQLite/PostgreSQL roles;
- database verification and recovery requirements.

#### Guanyu

Confirm:

- frontend flows and interface descriptions;
- desktop/mobile behaviour;
- accessibility considerations;
- GitHub Pages and browser-E2E requirements;
- US-09 interface limitation.

### Completion criteria

- [ ] Formal GitHub reviews are recorded.
- [ ] Requested changes are resolved by the correct owner.
- [ ] Each approved PR is mergeable against the latest V3 base.
- [ ] No runtime result is inferred from review approval.

## 6. Phase 2 — Merge approved records into V3

Recommended sequence:

1. PR #35 — CI workflow;
2. PR #47 — US-09 scope;
3. PR #48 — database verification;
4. PR #52 — architecture;
5. PR #54 — Agile evidence;
6. PR #58 — toolchain;
7. PR #44 — reconciliation plan;
8. PR #60 — status and traceability;
9. PR #46 — evidence index;
10. PR #50 — final review package.

Before each merge:

- confirm the PR head has not changed unexpectedly;
- confirm review approval applies to the current head;
- inspect changed files;
- confirm the PR does not modify teammate-owned implementation outside its approved scope;
- use a clear squash-merge title where appropriate.

### Completion criteria

- [ ] All approved package PRs are merged into `feature/product-database`.
- [ ] The branch is clean and contains the complete submission record set.
- [ ] Merged PR numbers and commit SHAs are retained.

## 7. Phase 3 — Freeze the V3 release candidate

Record:

| Field | Value |
|---|---|
| Release-candidate branch | Pending |
| Release-candidate SHA | Pending |
| Freeze date/timezone | Pending |
| Included PRs | Pending |
| Known limitations | Pending |
| Review approvals | Pending |

Freeze rules:

- no feature changes after freeze;
- only release-blocking defect fixes may enter;
- every fix requires owner review and retesting;
- a changed candidate receives a new SHA and affected checks are rerun.

## 8. Phase 4 — Canonical CI verification

Run:

```bash
python -m pytest --collect-only -q test_server.py
python -m pytest -q test_server.py
git diff --exit-code
```

Required evidence:

- workflow run ID;
- candidate SHA or tested merge ref;
- runner and Python version;
- pytest version;
- collected/passed/failed counts;
- execution time and exit result;
- tracked-file integrity result.

Expected release result:

```text
12 tests collected
12 tests passed
tracked-file integrity passed
```

The historical `test_mock.py` audit remains visible and non-blocking.

### Completion criteria

- [ ] Canonical suite passes for the frozen candidate.
- [ ] Tracked-file integrity passes.
- [ ] Evidence is linked from the release index and checklist.

## 9. Phase 5 — Catalogue and local database verification

Use a disposable database copy.

Required checks:

- products: 11,000;
- product specifications: 2,000;
- joined recommendation candidates: 2,000;
- category distribution: 800/833/300/61/6;
- duplicate product IDs: 0;
- duplicate specification IDs: 0;
- orphan specifications: 0;
- source metadata present;
- private tables empty in the generated catalogue artifact;
- repeated generation behaviour documented.

Record:

- tester;
- candidate SHA;
- Python version;
- commands;
- source and output paths;
- timestamp;
- complete non-sensitive output;
- status and defect Issue if required.

### Completion criteria

- [ ] All required counts and integrity checks pass.
- [ ] No tracked source database is unintentionally modified.
- [ ] Yuyang approves the result.

## 10. Phase 6 — Deployment identity and PostgreSQL

Confirm:

- GitHub Pages frontend URL and deployed source/commit;
- Render API URL and deployed commit;
- build and start commands;
- presence of `DATABASE_URL` and `JWT_SECRET_KEY` without exposing values;
- `/api/health` response;
- database dialect reports PostgreSQL;
- expected tables and catalogue counts exist.

### Completion criteria

- [ ] Frontend and API identities are recorded.
- [ ] PostgreSQL is confirmed for the deployed API.
- [ ] No credential is retained in evidence.
- [ ] Deployment is tied to the candidate or approved release commit.

## 11. Phase 7 — Persistence and privacy

Using non-sensitive demonstration accounts:

1. register Account A;
2. save a favorite;
3. create a history entry and result snapshot;
4. submit feedback;
5. record the data before restart/redeploy;
6. restart or redeploy the service;
7. log in again and confirm data persists;
8. register Account B;
9. confirm Account B cannot access Account A history or favorites;
10. record results without tokens or passwords.

### Completion criteria

- [ ] Account persists.
- [ ] Favorites persist.
- [ ] History and snapshot persist.
- [ ] Feedback persists.
- [ ] Cross-user access is rejected.
- [ ] Yuyang and Zaikun approve relevant technical results.

## 12. Phase 8 — Browser E2E

Required deployed scenarios:

### Foundation

- frontend loads without blocking console errors;
- requests reach the intended Render API;
- loading, empty and error states are observed;
- source/price limitation wording is accurate.

### Authentication

- register;
- login;
- current-user identity;
- protected-route rejection when unauthenticated;
- logout.

### Recommendation

- valid request;
- category and budget compliance;
- separate Top 5;
- next/previous pagination;
- stable query across pages;
- invalid input and no-result behaviour.

### Compare, favorites and history

- compare two and three products;
- reject invalid comparison;
- add/remove favorite;
- compare same-category favorites;
- create, restore and delete history.

### Feedback and sharing

- submit positive or negative feedback;
- generate a share state;
- open it in an isolated session;
- confirm private account data is not exposed.

### Responsive and accessibility

- complete critical flow on desktop;
- complete critical flow on mobile viewport/device;
- keyboard navigation;
- visible focus;
- labels and readable errors;
- basic zoom/reflow observation.

### Completion criteria

- [ ] Every critical scenario has a status and evidence ID.
- [ ] Failed/blocked cases link to owner-assigned Issues.
- [ ] Critical defects are fixed and retested.
- [ ] Guanyu confirms frontend results; Zaikun/Yuyang confirm related API/data results.

## 13. Phase 9 — External acceptance

Use two non-team participants.

Required participant tasks:

1. register and log in;
2. find a product within a selected budget;
3. browse another result page;
4. compare two products;
5. save a favorite;
6. reopen search history;
7. submit feedback;
8. share and reopen the recommendation state.

Record:

- participant ID, not unnecessary personal data;
- date, device and browser;
- independent completion result;
- prompts required;
- observations and feedback;
- defects created;
- retest outcome.

### Completion criteria

- [ ] Two non-team participants complete the agreed scope.
- [ ] Blocking usability defects are resolved or explicitly accepted.
- [ ] Results are retained in `docs/v3-external-uat-record.md`.

## 14. Phase 10 — Release decision

Complete the release decision record:

| Gate | Result |
|---|---|
| Formal reviews | Pending |
| Canonical CI | Pending final candidate |
| Catalogue integrity | Pending |
| PostgreSQL identity/counts | Pending |
| Persistence/privacy | Pending |
| Desktop/mobile E2E | Pending |
| External acceptance | Pending |
| Critical defects | Pending |
| Accepted limitations | Pending |
| Release decision | Pending |

Decision values:

- **Go:** all mandatory gates pass and remaining limitations are accepted;
- **Conditional Go:** only explicitly accepted non-critical limitations remain;
- **No-Go:** a mandatory gate fails or evidence is incomplete.

The release coordinator records the decision, while technical owners confirm results in their areas.

## 15. Phase 11 — Controlled reconciliation to `main`

After a Go/Conditional Go decision:

1. create `release/v3-main-reconciliation` from the verified V3 candidate;
2. refresh the comparison with `main`;
3. classify every `main`-only file;
4. retain useful historical evidence;
5. preserve V3 technical implementation;
6. send technical conflicts to the relevant owner;
7. update README and final project records;
8. rerun affected tests and smoke checks;
9. open the final PR to `main`;
10. require formal approval and successful checks before merge.

### Completion criteria

- [ ] Reconciliation inventory is complete.
- [ ] Owner-controlled conflicts are resolved.
- [ ] V3 implementation is preserved.
- [ ] Final PR is approved and passes required checks.
- [ ] Merge to `main` is completed.

## 16. Phase 12 — Tag and package

After merge to `main`:

- record final `main` SHA;
- create the release tag;
- confirm deployed version where applicable;
- export the final project archive;
- exclude local secrets, virtual environments and temporary test data;
- retain a checksum;
- retain database backup/recovery information;
- close completed release Issues;
- keep deferred and accepted-limitation items traceable.

### Completion criteria

- [ ] Release tag exists.
- [ ] Final archive exists.
- [ ] Checksum is recorded.
- [ ] Final status and evidence index are current.
- [ ] Release record identifies remaining limitations.

## 17. Defect workflow

For each failed or blocked check:

1. create a separate Issue;
2. include candidate SHA, environment, steps, expected and observed result;
3. assign the correct owner;
4. apply severity and release-blocking classification;
5. fix on an owner-controlled branch;
6. review and merge the fix;
7. rerun the failed scenario and affected regression checks;
8. update the evidence record.

## 18. Evidence naming

Recommended evidence IDs:

- `CI-###` — automated tests;
- `DB-###` — database/catalogue checks;
- `DEP-###` — deployment identity;
- `PERS-###` — persistence;
- `PRIV-###` — privacy;
- `E2E-###` — browser scenarios;
- `UAT-###` — external acceptance;
- `REL-###` — release/reconciliation/package.

## 19. Current execution state

| Phase | Status |
|---|---|
| Formal package review | Ready to begin |
| Merge approved records | Pending review |
| Release-candidate freeze | Pending |
| Final CI | Pending |
| Catalogue verification | Pending |
| Deployment/PostgreSQL | Pending |
| Persistence/privacy | Pending |
| Browser E2E | Pending |
| External acceptance | Pending |
| Reconciliation | Pending |
| Release packaging | Pending |

This plan is ready for formal review. Execution results must be added only after the corresponding activity is completed.
