# Agile Iteration, Demonstration, Feedback and Retrospective Record

**Project:** Smart Digital Product Recommendation Platform  
**Record owner:** Chu Junjie — Project Manager and Release Coordinator  
**Authoritative implementation baseline:** `feature/product-database`  
**Status:** Prepared for formal team review

## 1. Purpose

This record consolidates the project's iterative planning, delivery evidence, demonstrations, feedback, scope changes and retrospective actions. It distinguishes retained historical iteration records from later repository-based evidence phases.

No date, effort value, meeting, demonstration, user test or stakeholder feedback is reported unless it is supported by retained project evidence. Missing evidence is identified explicitly.

## 2. Evidence principles

- A merged Pull Request is repository delivery evidence, not automatically a deployed demonstration.
- A prepared acceptance template is not an executed acceptance result.
- Estimated effort is not actual elapsed time.
- An implementation may be recorded as delivered while runtime verification remains open.
- Historical iteration statements must be labelled as historical when they no longer describe the current release.
- Defects and scope changes must link to an Issue, Pull Request or decision record where available.

## 3. Team roles

| Team member | Project role | Primary responsibilities |
|---|---|---|
| Chu Junjie | Project Manager and Release Coordinator | Scheduling, task allocation, Agile records, traceability, acceptance coordination and release management |
| Guanyu Lu | UI/UX Designer and Frontend Developer | Interface design, responsive frontend, interaction implementation and browser verification |
| Zaikun Zheng | Backend and Algorithm Engineer | Flask API, authentication, recommendation logic and automated tests |
| Yuyang Zhou | Database Administrator | Dataset preparation, schema, importer, SQLite/PostgreSQL integration, provenance and database verification |

## 4. Historical iteration plan

The repository README records three planned iterations. These entries are retained as planning history and must not be interpreted as the final release status without current traceability evidence.

| Iteration | Goal | Planned stories | Planned effort |
|---|---|---|---:|
| Iteration 1 | Core input-to-recommendation pipeline | US-01, US-02, US-03 | 36 ideal days |
| Iteration 2 | Explanation, comparison and exclusion controls | US-04, US-05, US-06 | 36 ideal days |
| Iteration 3 | Purchase links, feedback, budget alternatives and sharing | US-07, US-08, US-09, US-10 | 36 ideal days |

The historical README reports full planned velocity for Iterations 1 and 2. Actual time-sheet evidence is not retained in the current repository, so the values remain planning/velocity records rather than independently verified labour hours.

## 5. Iteration 1 — Core pipeline

### Planned objective

Create the first working path from user input to stored product data and a recommendation leaderboard.

### Planned stories

- US-01 — Natural-language needs description;
- US-02 — Database setup and import;
- US-03 — Customized Top 5 leaderboard.

### Repository delivery evidence

The project history contains early frontend, backend and integration branches and Pull Requests for the recommendation pipeline. The current V3 implementation has since replaced or extended significant parts of this baseline.

### Demonstration status

A GitHub Pages link is retained in the README, but the historical label does not by itself establish which commit or API environment was demonstrated. The deployed baseline must be identified before the link is used as current release evidence.

Status: **Historical demonstration reference; current deployed identity unverified.**

### Feedback status

No structured Iteration 1 client-feedback record is retained in the current repository.

Status: **Not retained.**

### Retrospective

Strengths:

- a complete user journey was decomposed into input, data and result-display stories;
- ownership was divided across frontend, backend and database work;
- early integration produced a usable foundation.

Improvements carried forward:

- identify the exact deployed commit for each demonstration;
- retain acceptance notes instead of relying on a live-link label;
- distinguish current release status from historical sprint completion claims.

## 6. Iteration 2 — Decision support

### Planned objective

Improve recommendation transparency and enable comparison and exclusion preferences.

### Planned stories

- US-04 — Personalized explanation;
- US-05 — Product specification comparison;
- US-06 — Exclude unwanted features.

### Repository delivery evidence

The current V3 interface and API include recommendation reasons, product comparison and structured preference filters. Exact mapping between the historical story wording and the current structured implementation is maintained in the requirements traceability record.

### Demonstration status

No retained demonstration record identifies a tested Iteration 2 commit, environment and observer feedback.

Status: **Not retained.**

### Feedback status

No structured client-feedback record is retained for Iteration 2.

Status: **Not retained.**

### Retrospective

Strengths:

- the project progressed from a simple leaderboard to explainable decision support;
- comparison and filtering increased practical usefulness;
- component separation made later V3 migration possible.

Improvements carried forward:

- define acceptance criteria at story level before implementation;
- retain screenshots and Network evidence for demonstrations;
- record differences between planned natural-language behaviour and delivered structured controls.

## 7. Iteration 3 and V3 scope adjustment

### Planned objective

Add purchase redirection, feedback, budget alternatives and sharing.

### Scope outcome

| Story | Current V3 treatment |
|---|---|
| US-07 — Direct purchase links | Implemented as available product/reference URLs; live checkout is not guaranteed |
| US-08 — Feedback mechanism | Implemented through the feedback API and interface controls; runtime persistence still requires verification |
| US-09 — Budget alternatives | Deferred; backlog milestone `Unscheduled` |
| US-10 — Share leaderboard | Implemented as share-state restoration; deployed isolated-session verification remains required |

US-09 was removed from the current release scope because the backend contract, selection rule and automated acceptance criteria were not implemented. The decision is retained in `docs/us-09-scope-decision-record.md`.

### Retrospective

Strengths:

- incomplete scope was explicitly deferred rather than reported as completed;
- feedback, sharing, accounts and history were integrated into the V3 design;
- known limitations were separated from implemented behaviour.

Improvements carried forward:

- make scope decisions before release preparation;
- require API, UI and test acceptance definitions for cross-component stories;
- avoid dormant frontend scaffolding being mistaken for completed functionality.

## 8. Repository evidence phase — Governance baseline

### Objective

Replace inconsistent project records with shared V3 status, traceability, Definition of Done and release controls.

### Delivery evidence

PR #33 merged the governance documentation into `feature/product-database`.

Delivered records include:

- `docs/project-status.md`;
- `docs/requirements-traceability.md`;
- `docs/definition-of-done.md`;
- `docs/v3-execution-plan.md`;
- `docs/final-acceptance-and-release-checklist.md`.

### Outcome

- V3 status vocabulary defined;
- implementation and verification separated;
- release gates documented;
- ownership boundaries recorded.

### Retrospective

The governance baseline reduced ambiguity, but later repository changes still required a documentation consistency audit and status-alignment work.

Improvement: review project status after each significant merge rather than only at final release preparation.

## 9. Repository evidence phase — Database and catalogue integration

### Objective

Integrate the public product catalogue, recommendation-ready specifications and SQLAlchemy/PostgreSQL design.

### Delivery evidence

The V3 branch contains:

- `import_real_catalog.py`;
- `real_product_catalog.csv`;
- `product_specs.csv`;
- SQLAlchemy schema and database selection;
- bundled SQLite catalogue data;
- provenance and fixed conversion rules.

### Outcome

Repository inspection supports a 2,000-record imported catalogue target and 11,000 total product target. Runtime counts, PostgreSQL persistence and recovery remain separate verification gates.

### Demonstration and feedback

No retained external demonstration or client-feedback record specifically validates the final catalogue and PostgreSQL behaviour.

Status: **Runtime verification and external feedback pending.**

### Retrospective

Strengths:

- provenance and missing-value handling were retained;
- PostgreSQL support was incorporated through a portable data layer;
- importer validation logic was added.

Improvement:

- execute catalogue generation only against disposable copies;
- retain command output and database integrity results;
- separate catalogue reconstruction from production user-data backup.

## 10. Repository evidence phase — Backend and CI verification

### Objective

Define the current V3 automated test scope and retain historical compatibility evidence.

### Delivery evidence

PR #35 introduces the `V3 Test Evidence` GitHub Actions workflow.

Canonical command:

```bash
python -m pytest -q test_server.py
```

Recorded workflow run `31096706920`:

- 12 tests collected;
- 12 tests passed in 1.23 seconds;
- tracked-file integrity passed;
- overall conclusion: success.

The historical `test_mock.py` suite remains visible as a non-release V2 compatibility audit.

### Retrospective

Strengths:

- current release tests and historical tests are clearly separated;
- failing historical evidence is retained rather than hidden;
- tracked-file side effects are checked.

Improvement:

- rerun the canonical suite for the frozen release candidate;
- document test dependencies consistently for local and CI use;
- link every final test result to the exact tested commit.

## 11. Repository evidence phase — Acceptance preparation

### Objective

Prepare repeatable deployed E2E and external user-acceptance records.

### Delivery evidence

The V3 branch contains:

- `docs/v3-e2e-acceptance-evidence.md`;
- `docs/v3-external-uat-record.md`.

### Outcome

Critical authentication, recommendation, pagination, comparison, favorites, history, feedback, sharing, responsive and privacy scenarios are defined.

### Current status

The templates are prepared, but execution evidence is not retained.

Status: **Not Run.**

### Retrospective

A prepared scenario matrix improves consistency, but acceptance must be scheduled early enough to allow defect correction and retesting before the release deadline.

## 12. Repository evidence phase — Release documentation and review package

### Objective

Consolidate architecture, toolchain, scope, database, release evidence and reconciliation records for formal team review.

### Delivery package

- PR #44 — reconciliation plan;
- PR #46 — release evidence index;
- PR #47 — US-09 decision;
- PR #48 — database verification record;
- PR #50 — submission and release review package;
- PR #52 — architecture and design;
- PR #54 — Agile evidence;
- PR #58 — development toolchain;
- PR #60 — scope, CI and release-gate alignment.

### Current status

The records are prepared for formal GitHub review. Runtime verification and final release work remain separate gates.

## 13. Scope-change register

| Change | Reason | Impact | Evidence |
|---|---|---|---|
| CSV/raw-SQLite backend replaced by SQLAlchemy design | Support current schema and PostgreSQL | API/tests/documentation updated | V3 implementation branch |
| Product catalogue expanded | Improve recommendation-ready data | Importer, provenance and database checks added | Database branch evidence |
| Accounts, favorites and history added | Support persistent private user workflows | JWT, user tables and privacy testing required | `server.py`, `index.html` |
| Pagination added | Support all matching results | API/UI contract and navigation tests required | V3 implementation |
| US-09 deferred | No implemented deterministic alternative contract | Removed from current release acceptance | PR #47 |
| Historical mocks classified as non-release | Removed V2 interfaces no longer match V3 | CI separates current suite and historical audit | PR #35 |
| `main` reconciliation delayed | Branches diverged and contain owner-controlled conflicts | Controlled integration required | PR #44 |

## 14. Demonstration and feedback ledger

| Evidence ID | Activity | Commit/environment | Participants | Result | Status |
|---|---|---|---|---|---|
| DEMO-H1 | Historical GitHub Pages demonstration reference | Not identified | Not retained | Link exists; baseline unclear | Historical |
| DEMO-V3 | Final V3 deployed demonstration | Pending | Pending | Pending | Not Run |
| UAT-01 | External participant 1 | Pending | Non-team participant | Pending | Not Run |
| UAT-02 | External participant 2 | Pending | Non-team participant | Pending | Not Run |
| FB-01 | Technical-owner review | Current package PRs | Zaikun, Yuyang, Guanyu | Pending formal GitHub record | Pending |

## 15. Planned-versus-actual evidence gaps

| Area | Planned evidence | Available evidence | Gap |
|---|---|---|---|
| Effort | Story estimates and actual effort | Estimates retained; actual hours not retained | Do not invent actual hours |
| Demonstrations | Demonstration after each iteration | Historical live link only | Commit, environment and observations absent |
| Client feedback | Feedback after each iteration | No structured historical records | Final external acceptance still required |
| Burndown | Planned and actual remaining effort | README graphs retained | Underlying daily source data not retained |
| Release validation | CI, database, E2E and UAT | CI prepared and partially verified | Runtime database, E2E and UAT pending |

## 16. Retrospective improvement register

| Improvement | Owner | Application |
|---|---|---|
| Record exact commit and environment for every demonstration | Junjie | Final V3 demonstration and UAT |
| Separate repository implementation from runtime verification | Junjie and technical owners | Status and release records |
| Require owner-controlled technical conflict resolution | All component owners | `main` reconciliation |
| Use disposable databases for catalogue builds and tests | Yuyang | Database verification |
| Retain current and historical test results separately | Zaikun and Junjie | CI workflow |
| Define cross-component acceptance before implementation | Product team | Future US-09 and similar stories |
| Schedule acceptance before final merge | Junjie | Release plan |
| Update status documents after major merges | Junjie | Project governance |

## 17. Iteration close-out template

For future iteration records, capture:

### Identification

- iteration name;
- start/end dates;
- baseline and final commit;
- participants and responsibilities.

### Planning

- objective;
- planned stories/tasks;
- priority and estimate;
- dependencies and risks.

### Delivery

- completed items;
- incomplete or deferred items;
- Pull Requests and commits;
- actual effort where recorded;
- variance and explanation.

### Demonstration

- deployed URL and commit;
- environment;
- participants;
- demonstrated scenarios;
- observed result;
- screenshots or Network evidence.

### Feedback

- feedback source;
- exact feedback summary;
- resulting decision;
- linked defect/change Issue;
- retest result.

### Retrospective

- what worked;
- what did not work;
- root causes;
- one or more assigned improvement actions.

## 18. Review checklist

### Backend/test review

- [ ] Confirm backend and CI evidence descriptions.
- [ ] Confirm historical test classification.
- [ ] Confirm no unsupported backend completion claim exists.

### Database review

- [ ] Confirm catalogue, importer and PostgreSQL descriptions.
- [ ] Confirm runtime checks remain open where evidence is absent.
- [ ] Confirm no production-data operation is implied.

### Frontend review

- [ ] Confirm current frontend and historical demonstration wording.
- [ ] Confirm responsive/accessibility acceptance remains runtime evidence.
- [ ] Confirm US-09 interface limitation is accurate.

### Project/release review

- [x] Historical and current evidence are separated.
- [x] Missing effort, demonstration and feedback records are not invented.
- [x] Scope changes and retrospective actions are traceable.
- [ ] Formal GitHub reviews recorded.
- [ ] Final demonstration and external acceptance completed.

This record is ready for formal team review. It should be updated only from new retained evidence.
