# Agile Iteration, Demonstration, Feedback and Retrospective Record

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Team meeting record maintained by:** @Chu-Junjie  
**Status:** Prepared for formal review

## 1. Purpose

This record links iteration planning, repository delivery, scope decisions, demonstrations, feedback gaps and retrospective actions. Decisions and responsibilities are recorded in the team meeting notes maintained by @Chu-Junjie.

No date, effort, meeting, demonstration, user response or feedback result is invented. Missing evidence remains explicitly missing.

## 2. Named responsibilities

- @ZhengZaikun confirms backend, API, recommendation, automated-test and CI iteration records.
- @tiantian09091 confirms catalogue, database, importer, provenance and PostgreSQL iteration records.
- @Guanyu-Lu confirms frontend, interface, deployment and demonstration records.
- @Chu-Junjie maintains meeting notes, planning, scope changes, evidence links, retrospective actions and release follow-up.

## 3. Historical iteration overview

| Iteration | Planned outcome | Repository evidence boundary | Current interpretation |
|---|---|---|---|
| Iteration 1 | Basic input, product data and recommendation presentation | Historical README and early implementation records | Historical baseline; not final V3 release evidence |
| Iteration 2 | Explanation, comparison and preference filtering | Historical Issues, PRs and implementation records | Historical delivery; final deployed behaviour requires V3 E2E |
| Iteration 3 | Links, feedback, budget alternatives and sharing | Mixed historical and current implementation evidence | US-07, US-08 and US-10 are represented in V3; US-09 is Deferred |

Historical estimates and completion statements are retained only as historical records. They do not prove the current V3 release status.

## 4. Current release-preparation phases

| Phase | Main result | Evidence | Status |
|---|---|---|---|
| Governance baseline | V3 status vocabulary, traceability, release gates | PR #33 | Merged historical foundation |
| Acceptance preparation | E2E and two-participant templates | PR #37 | Merged preparation; scenarios `Not Run` |
| Documentation audit | Stale/conflicting statement inventory | PR #39 | Merged audit |
| Canonical CI decision | `test_server.py` as current release suite | Issue #34 / PR #35 | 12/12 passed for recorded PR ref; final candidate pending |
| Scope decision | US-09 Deferred / `Unscheduled` | Issue #40 / PR #47 | Recorded; formal reviews pending |
| Database inspection | Schema, catalogue and importer facts | Issue #41 / PR #48 | Repository verified; runtime pending |
| Architecture | Current system, API, data and interface design | Issue #51 / PR #52 | Prepared for named reviews |
| Toolchain | Development, test and deployment tools | Issue #55 / PR #58 | Prepared for named reviews |
| Release controls | Status, traceability, meeting action plan and checklist | Issue #59 / PR #60 | Prepared for named reviews |
| Reconciliation | Controlled V3-to-`main` plan | Issue #43 / PR #44 | Planned; not started |

## 5. Meeting decisions recorded for the release

- `feature/product-database` remains the implementation baseline.
- @ZhengZaikun reviews backend/API/test/CI records.
- @tiantian09091 reviews database/catalogue/importer/PostgreSQL records.
- @Guanyu-Lu reviews frontend/GitHub Pages/browser records.
- @Chu-Junjie maintains meeting notes, status, evidence and release coordination.
- Canonical release command: `python -m pytest -q test_server.py`.
- Historical `test_mock.py` remains visible but non-blocking.
- US-09 Budget Alternatives is Deferred.
- The importer must not run against production user data.
- Runtime gates remain open until actual execution.
- Integration into `main` begins only from a verified candidate.

## 6. Demonstration and feedback ledger

| ID | Activity | Evidence available | Status | Follow-up |
|---|---|---|---|---|
| DEMO-H1 | Historical iteration demonstrations referenced in project records | Repository text may describe earlier demonstrations; complete independent evidence is not retained here | Historical only | Do not use as final V3 acceptance |
| DEMO-V3 | Final V3 deployed demonstration | No executed record yet | Not Run | @Guanyu-Lu executes browser flow; @ZhengZaikun and @tiantian09091 confirm API/data observations |
| UAT-01 | External participant 1 | Template prepared | Not Run | @Chu-Junjie coordinates and records actual outcome |
| UAT-02 | External participant 2 | Template prepared | Not Run | @Chu-Junjie coordinates and records actual outcome |
| FEED-TEAM | Team review comments | Meeting agreement recorded; formal GitHub Reviews pending | In progress | Named reviewers submit formal Approvals or requested changes |

## 7. Scope-change register

| Change | Decision | Reason | Named confirmation |
|---|---|---|---|
| V3 baseline supersedes earlier 9,000/33-specification governance statements | Adopted | Current branch contains SQLAlchemy, accounts, pagination and expanded catalogue work | @ZhengZaikun, @tiantian09091, @Guanyu-Lu formally review affected records |
| Canonical release suite is `test_server.py` | Adopted | It exercises the current SQLAlchemy/API contract with isolated temporary databases | @ZhengZaikun |
| `test_mock.py` treated as historical audit | Adopted | It targets removed V2 contracts | @ZhengZaikun |
| US-09 Budget Alternatives | Deferred | Current backend contract and canonical tests do not implement the feature | @ZhengZaikun and @Guanyu-Lu |
| Importer restricted to disposable catalogue builds | Adopted | Generated artifacts clear private rows | @tiantian09091 |
| Reconciliation begins from V3 | Adopted | Prevent older `main` content from replacing current implementation | @ZhengZaikun, @tiantian09091 and @Guanyu-Lu |

## 8. Planned-versus-actual evidence gaps

| Gap | Current status | Required action |
|---|---|---|
| Formal GitHub Approvals | Pending | @ZhengZaikun, @tiantian09091 and @Guanyu-Lu review the applicable current PR heads |
| Final candidate CI | Pending | @ZhengZaikun reruns the canonical suite after freeze |
| Actual catalogue integrity output | Pending | @tiantian09091 runs disposable verification |
| Deployed frontend/API identity | Pending | @Guanyu-Lu and @ZhengZaikun record exact commits |
| PostgreSQL identity and persistence | Pending | @tiantian09091 records engine, counts and restart result; @ZhengZaikun confirms API integration |
| Desktop/mobile E2E | Not Run | @Guanyu-Lu executes Issue #42 |
| External acceptance | Not Run | @Chu-Junjie coordinates two non-team participants |
| Reconciliation to `main` | Not started | Follow Issue #43 and PR #44 after Go/Conditional Go |

## 9. Retrospective observations

### What worked

- Issue/branch/PR separation made responsibilities traceable.
- Status vocabulary prevented implementation from being confused with verification.
- Canonical CI isolated current V3 tests from historical compatibility evidence.
- Team meeting notes recorded scope decisions before final integration.

### What needs improvement

- Technical review should occur earlier, before a large closeout package forms.
- Runtime evidence should be captured at the time of execution.
- Deployed commit identity should be recorded with each deployment.
- Test databases should always be disposable and isolated.
- Historical and current release statements should be separated from the beginning.

### Actions

- @ZhengZaikun records final test evidence with the tested SHA.
- @tiantian09091 records database/PostgreSQL evidence with commands and outputs.
- @Guanyu-Lu records browser evidence with frontend/API identities and Network details.
- @Chu-Junjie maintains one meeting record, one evidence index and one release checklist.

## 10. Iteration closeout template

```text
Iteration/phase:
Meeting date/timezone:
Meeting notes maintained by: @Chu-Junjie
Planned outcomes:
Completed repository work:
Formal reviews:
Executed tests and environments:
Demonstration evidence:
Feedback received:
Scope changes:
Open defects assigned to:
- @ZhengZaikun:
- @tiantian09091:
- @Guanyu-Lu:
Retrospective actions:
Release impact:
```

## 11. Completion criteria

- [x] Historical and current records are separated.
- [x] V3 scope changes are traceable.
- [x] Named responsibilities are explicit.
- [x] Missing evidence is stated honestly.
- [ ] @ZhengZaikun formally approves backend/test/CI sections.
- [ ] @tiantian09091 formally approves database/catalogue/importer sections.
- [ ] @Guanyu-Lu formally approves frontend/demonstration sections.
- [ ] Final V3 demonstration and external acceptance are added after execution.

Formal review of this record does not replace final runtime verification.