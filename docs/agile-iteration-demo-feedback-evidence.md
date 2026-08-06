# Agile Iteration, Demonstration, Feedback and Retrospective Evidence

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Recorded:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation baseline:** `feature/product-database`  
**Related tracking:** Issue #53

## 1. Purpose

This page consolidates the evidence that the project was planned, reviewed and adapted incrementally. It is written to support the CP3407 Agile software engineering and iteration-delivery criteria.

It does not reconstruct missing meetings, estimates, demonstrations or client feedback as if they had occurred. Where the repository does not retain sufficient evidence, the status is stated as `Not retained`, `Not Run`, `Unknown` or `Pending confirmation`.

## 2. Evidence boundary

The repository contains strong evidence for Issue-driven work, separate branches, Pull Requests, non-author review, governance updates, test audits and release-gate management. It contains less complete evidence for the following historical items:

- official iteration start and end dates;
- planned story-point or hour estimates for every story;
- actual hours spent by every owner;
- deployed demonstration after every iteration;
- client or external-user feedback after every iteration;
- formal team retrospective minutes for every iteration.

A merged Pull Request proves that a reviewed repository change was delivered to its target branch. It does not, by itself, prove that the change was deployed, demonstrated to a client or accepted by an external user.

## 3. Status vocabulary

| Status | Meaning |
|---|---|
| `Planned` | Scope or evidence work is defined but not yet completed. |
| `Prepared` | A template, plan or review record exists; execution has not occurred. |
| `Implemented` | Code, data or documentation exists on the named branch. |
| `Verified` | A named check passed for a named commit and environment. |
| `Blocked` | Completion depends on an unresolved technical or decision gate. |
| `Not Run` | The required test, demonstration or acceptance session has not occurred. |
| `Not retained` | The activity may have occurred, but no reliable repository evidence is currently retained. |
| `Pending confirmation` | An owner must confirm the accuracy or provide the missing evidence. |
| `Done` | All applicable Definition of Done and release gates have passed. |

## 4. Iteration naming rule

The phases below are a coordinator reconstruction from retained GitHub evidence. They must not be presented as the official teaching-week or sprint numbering unless the team confirms the original iteration dates and goals.

| Evidence phase | Coordinator label | Official iteration label |
|---|---|---|
| Phase 0 | Foundation and governance | `Pending confirmation` |
| Phase 1 | Database integration and evidence | `Pending confirmation` |
| Phase 2 | Backend compatibility and test audit | `Pending confirmation` |
| Phase 3 | V3 baseline adoption and release preparation | `Pending confirmation` |
| Phase 4 | Release verification, reconciliation and coordinated review | Current work |

## 5. Evidence source map

| Evidence | What it supports | What it does not prove |
|---|---|---|
| PR #17 | Initial project foundation, contracts, responsibilities and governance baseline | Complete implementation or deployment |
| PR #20 | Foundation close-out evidence | Completion of later technical work |
| PR #22 | Task 2 database evidence and status updates | Current V3 PostgreSQL release verification |
| PR #25 | Task 3 dependency, compilation, collection and failure evidence | A passing backend suite |
| PR #33 | Adoption of the current V3 governance and release baseline | Technical verification or release readiness |
| PR #35 | Reproducible CI workflow and partial V3 test evidence | A passing complete suite |
| PR #37 | E2E and external-UAT evidence templates | Executed E2E or client feedback |
| PR #39 | Release-documentation consistency audit | Correction of every finding |
| Issue #40 / PR #47 | Controlled US-09 scope-decision process | A selected option or implemented feature |
| Issue #41 / PR #48 | Database/PostgreSQL release-verification process | Executed persistence verification |
| Issue #42 | Deployed E2E execution tracker | A deployed V3 acceptance pass |
| Issue #43 / PR #44 | Safe `main` and V3 reconciliation planning | Completed branch reconciliation |
| Issue #45 / PR #46 | Release evidence index | Closure of the linked blockers |
| Issue #49 / PR #50 | Coordinated team-review package | Owner approval or merge permission |
| Issue #51 / PR #52 | V3 design and architecture explanation | External editable UML/ERD/prototype completion |

## 6. Phase 0 — Foundation and governance

### 6.1 Goal

Establish a documented project foundation before database, backend and frontend integration continued.

### 6.2 Planned scope retained in GitHub

- project baseline and frozen decisions;
- database and API contracts;
- team task and branch responsibilities;
- requirements traceability;
- Definition of Done;
- project status and risks;
- Issue and Pull Request templates.

### 6.3 Owners

| Area | Owner status |
|---|---|
| Coordination and governance | Junjie |
| Backend/API technical confirmation | Zaikun — review required |
| Database technical confirmation | Yuyang — review required |
| Frontend/UI technical confirmation | Guanyu — review required |

### 6.4 Estimate and schedule evidence

| Field | Evidence status |
|---|---|
| Planned start/end | `Not retained` in this page |
| Planned effort | `Not retained` |
| Actual effort | `Not retained` |
| Delivery evidence | PR #17 and PR #20 |
| Schedule variance | `Unknown` without the original plan |

### 6.5 Delivered outcome

PR #17 established the documented project foundation. PR #20 later recorded the foundation close-out. The evidence supports a reviewed governance deliverable, not completion of the full product.

### 6.6 Demonstration and feedback

| Item | Status |
|---|---|
| Deployed demonstration | `Not retained` |
| Client feedback | `Not retained` |
| Teacher feedback | Some later teacher-feedback revision is represented in the repository, but phase-specific evidence is `Pending confirmation` |
| Formal retrospective | `Not retained` |

### 6.7 Coordinator retrospective observation

The initial governance baseline later became stale when the project moved from the earlier 9,000-row/33-specification description to the V3 11,000-product/2,000-specification implementation. This shows that governance documents need an explicit baseline commit and scheduled consistency review.

### 6.8 Process adjustment linked to evidence

- PR #33 adopted the V3 governance baseline.
- PR #39 audited stale and conflicting release documentation.
- PR #46 created a central release-evidence index.

This is a coordinator observation and corrective-action record, not evidence that the team held a formal retrospective at the end of Phase 0.

## 7. Phase 1 — Database integration and evidence

### 7.1 Goal

Integrate the selected database design and retain evidence for records, ProductID integrity, feedback and database-related acceptance status.

### 7.2 Planned scope inferred from retained evidence

- `products`, `product_specs` and `feedback` database work;
- ProductID relationship checks;
- feedback persistence and validation;
- status, traceability and Definition of Done updates.

The exact original iteration backlog and estimate remain `Pending confirmation` from the team.

### 7.3 Delivery evidence

PR #22 records Task 2 database integration evidence and refers to the technical database Pull Request used at that stage.

Yuyang's later V3 catalogue, database and importer work is already implemented on `feature/product-database`. It must not be confused with missing development merely because it has not yet been integrated into `main`.

### 7.4 Estimate and variance

| Field | Status |
|---|---|
| Planned estimate | `Not retained` |
| Actual effort | `Pending confirmation` from Yuyang |
| Planned records/specifications | Historical baseline differed from V3 |
| Current V3 implementation | 11,000 products and 2,000 recommendation-ready specification records are represented by the adopted baseline, pending release verification |
| Main variance | The project data scope and implementation architecture expanded after the earlier baseline |

### 7.5 Demonstration and feedback

| Item | Status |
|---|---|
| Database demonstration after the phase | `Not retained` |
| Client/user feedback | `Not retained` |
| Database owner review | Historical review evidence exists through earlier PRs; current V3 release verification remains open |
| PostgreSQL persistence test | `Not Run` or `Unverified` until Issue #41 is completed |

### 7.6 Blockers and corrective action

The current release still requires:

- exact tested commit and environment;
- row-count and integrity output;
- importer repeatability;
- provenance and licence evidence;
- Render PostgreSQL identity;
- restart/redeploy persistence;
- backup, restore and rollback evidence.

Issue #41 and PR #48 were created to prevent implemented database work from being incorrectly described as release-verified.

### 7.7 Coordinator retrospective observation

Implementation, evidence and release verification should be separate statuses. A technically completed data/importer contribution can be `Implemented` while production persistence remains `Unverified`.

## 8. Phase 2 — Backend compatibility and test audit

### 8.1 Goal

Reconcile dependencies, collect the complete tests, identify compatibility failures and retain reproducible evidence without modifying the backend/test owner's files.

### 8.2 Planned scope retained in PR #25

- dependency installation and validation;
- compilation;
- pytest collection;
- backend and mock-test execution;
- database side-effect recording;
- restoration of the tracked SQLite database;
- requirements and status updates;
- backend compatibility issue drafts.

### 8.3 Delivered evidence

PR #25 recorded multiple failing baselines and preserved the distinction between installation, compilation, test collection and test success. It also recorded that test execution modified the tracked SQLite database and that the file was restored rather than committed.

### 8.4 Estimate and schedule evidence

| Field | Status |
|---|---|
| Planned effort | `Not retained` |
| Actual effort | `Not retained` |
| Original completion expectation | Backend completion was expected but the retained evidence showed the suite remained failed |
| Variance reason | Legacy fixtures, old API contracts and incomplete database isolation |

### 8.5 Testing outcome evolution

| Evidence point | Result | Interpretation |
|---|---|---|
| Historical Task 3 baseline | Failed tests and setup errors | Backend compatibility blocked |
| Later V3 CI subset | `test_server.py` 12/12 passed | Verified only for the tested PR ref |
| Complete V3 repository audit | 18 collected, 12 passed, 6 failed | Complete suite remains Blocked |

### 8.6 Demonstration and feedback

| Item | Status |
|---|---|
| Deployed backend demo | `Not retained` for the historical phase |
| Client feedback | `Not retained` |
| Test-owner decision on legacy mocks | `Pending confirmation` in Issue #34 |
| Formal retrospective | `Not retained` |

### 8.7 Corrective action

Issue #34 and PR #35 establish a clean CI workflow that:

- runs the current V3 API suite separately;
- runs the complete repository suite without silently excluding legacy failures;
- reports tracked-file integrity;
- keeps the PR Draft until the test owner decides the correct disposition of `test_mock.py`.

### 8.8 Coordinator retrospective observation

A green subset must never be reported as a green release suite. Test ownership and the canonical release command must be agreed before documentation is corrected or the workflow is merged.

## 9. Phase 3 — V3 baseline adoption and release preparation

### 9.1 Goal

Adopt the current V3 implementation as the authoritative branch, update governance, prepare acceptance evidence and audit release-document consistency.

### 9.2 Delivered outcomes

| Work | Evidence status |
|---|---|
| V3 governance baseline | PR #33 merged |
| E2E evidence template | PR #37 merged; execution `Not Run` |
| External-UAT template | PR #37 merged; participant sessions `Not Run` |
| Documentation consistency audit | PR #39 merged |
| CI workflow | PR #35 remains Draft and Blocked by test-owner decision |

### 9.3 Scope and schedule variance

The V3 branch introduced a materially broader architecture than the historical baseline, including:

- SQLAlchemy;
- PostgreSQL through `DATABASE_URL`;
- accounts and JWT authentication;
- favorites;
- private history and saved result snapshots;
- pagination and separate Top 5 results;
- a larger product catalogue and specifications dataset.

The exact planned-versus-actual effort for each owner is `Pending confirmation`. The increased technical scope explains why old status statements and test contracts could not be treated as current release evidence.

### 9.4 Demonstration and feedback

| Item | Status |
|---|---|
| GitHub Pages URL exists in documentation | Candidate endpoint only |
| Render API URL exists in frontend configuration | Candidate endpoint only |
| Exact deployed frontend commit | `Unverified` |
| Exact deployed API commit | `Unverified` |
| Production database engine | `Unverified` |
| Deployed V3 E2E | `Not Run` |
| Two external UAT participants | `Not Run` |
| Client feedback after this phase | `Not retained` or `Not Run` |

### 9.5 Corrective action

- Issue #42 tracks deployment identity and deployed E2E execution.
- PR #37 provides repeatable test and UAT records.
- Issue #41/PR #48 separates database implementation from release verification.
- Issue #40/PR #47 prevents US-09 from being marked Done before the team chooses retain, revise or defer.

### 9.6 Coordinator retrospective observation

Acceptance preparation must start before release, but templates must remain visibly different from executed evidence. The project now uses `Prepared`, `Implemented`, `Verified`, `Blocked`, `Not Run` and `Unverified` to avoid false completion claims.

## 10. Phase 4 — Release verification, reconciliation and coordinated review

### 10.1 Goal

Prepare an internally consistent review package, resolve branch divergence safely and collect the missing technical-owner evidence before any final merge to `main`.

### 10.2 Current planned work

| Workstream | Tracking | Current state |
|---|---|---|
| Canonical CI/test scope | Issue #34 / PR #35 | Blocked |
| US-09 scope | Issue #40 / PR #47 | Pending owner input |
| Database/PostgreSQL verification | Issue #41 / PR #48 | Not Run / Unverified |
| Deployed E2E | Issue #42 | Not Run |
| `main`/V3 reconciliation | Issue #43 / PR #44 | Draft plan |
| Release evidence index | Issue #45 / PR #46 | Draft |
| Coordinated team review | Issue #49 / PR #50 | Draft |
| V3 design page | Issue #51 / PR #52 | Draft |
| Agile iteration evidence | Issue #53 / this document | Draft preparation |

### 10.3 Branch and release variance

`main` and `feature/product-database` have diverged. This invalidates a simple direct merge assumption. The response is to use the V3 branch as the implementation baseline, retain valuable `main`-only historical evidence selectively and require owner decisions for overlapping technical files.

### 10.4 Demonstration and feedback plan

Before final release consideration:

1. confirm the exact deployed frontend, API and database environment;
2. execute the E2E matrix on desktop and mobile;
3. record API/Network evidence for authentication, privacy and persistence claims;
4. run two independent external-user acceptance sessions;
5. create owner-specific defect Issues for failures;
6. retest fixes;
7. record client/user feedback and the resulting action;
8. obtain non-author review and all affected-owner approvals.

All items remain `Not Run`, `Unverified`, `Blocked` or `Pending` until evidence exists.

### 10.5 Coordinator retrospective observation

The current package demonstrates a move from document-by-document updates to an evidence-gated release process. The remaining risk is creating too many independent Draft PRs without a clear review order. Issue #49 and PR #50 address that risk by defining one coordinated review package while keeping every PR independently reviewable and mergeable.

## 11. Cross-phase scope-change log

| Change | Evidence | Impact | Current response |
|---|---|---|---|
| Earlier database/specification baseline replaced by V3 | PR #33 | Historical documents and tests became stale | V3 governance adoption and documentation audit |
| SQLAlchemy/PostgreSQL/account/history/favorites/pagination added | V3 branch | Larger technical and acceptance scope | New traceability, CI, E2E and database verification records |
| Legacy test contracts no longer match V3 | Issue #34 / PR #35 | Complete suite blocked | Test owner must decide update/archive/exclusion |
| US-09 status unclear | Issue #40 / PR #47 | Requirements and demo risk | Formal retain/revise/defer decision |
| Deployed identity not confirmed | Issue #42 | Cannot claim V3 deployment | Record exact frontend/API/database identity before E2E |
| `main` and V3 diverged | Issue #43 / PR #44 | Direct merge could overwrite completed work | Owner-controlled reconciliation plan |
| HD design evidence incomplete | Issue #51 / PR #52 | Design rubric risk | Consolidated architecture page plus pending external diagrams |
| Iteration/demo/feedback evidence fragmented | Issue #53 | Agile rubric risk | This consolidated evidence page |

## 12. Schedule and budget evidence gap

The HD requirement includes delivery on time and within budget. The repository currently supports schedule control through Issues, branches, Pull Requests, blocker records and review gates, but it does not yet retain a complete planned-versus-actual effort ledger.

The following must be completed from real team records rather than estimated retrospectively:

| Required field | Current status | Required source |
|---|---|---|
| Planned effort per user story | `Pending confirmation` | Original backlog, planning sheet or meeting record |
| Actual effort per user story | `Pending confirmation` | Owner work log or accepted reconstruction |
| Planned iteration | Partial | Backlog/Issue evidence |
| Actual delivery iteration | Partial | PR merge history |
| Time variance | `Unknown` for many stories | Planned and actual values |
| Financial/tool budget | `Not retained` | Approved budget/tool-cost record |
| Variance reason | Partial | Issue, review or retrospective evidence |
| Scope adjustment | Stronger evidence | Issues #34, #40, #41, #42 and #43 |

No hours, story points or dollar values should be inserted without a source accepted by the team.

## 13. Demonstration and feedback ledger

| Phase | Demo commit/environment | Demonstrator | Audience/client | Feedback evidence | Status |
|---|---|---|---|---|---|
| Foundation | — | — | — | — | `Not retained` |
| Database integration | — | — | — | — | `Not retained` |
| Backend compatibility | — | — | — | — | `Not retained` |
| V3 release preparation | Candidate URLs only | — | — | — | `Not Run` / `Unverified` |
| Final release candidate | Pending frozen SHA | Pending | Two external participants plus assessor/client where applicable | PR #37 records to be populated | `Planned` |

When an actual session occurs, record:

- date and timezone;
- deployed commit and environment;
- demonstrator;
- participant/client role;
- tasks shown;
- observed result;
- exact feedback;
- action accepted, rejected or deferred;
- related Issue and retest evidence.

## 14. Retrospective improvement register

These entries are coordinator observations supported by repository changes. They are not represented as formal team-retrospective minutes unless the team confirms them.

| Observation | Evidence | Improvement action | Follow-up status |
|---|---|---|---|
| Governance became stale when the implementation baseline changed | PR #33, PR #39 | Adopt a named authoritative branch and audit documentation consistency | Implemented in documentation |
| Local or partial test evidence could be overgeneralised | Issue #34, PR #35 | Separate V3 subset and complete-suite jobs; retain red blockers | Draft / Blocked |
| Templates could be mistaken for acceptance results | PR #37 | Initialise every scenario as `Not Run` and require environment evidence | Prepared |
| Implemented database work could be mistaken for production verification | Issue #41, PR #48 | Separate implementation and PostgreSQL persistence evidence | Draft / Not Run |
| Deployment URLs did not prove deployed commit identity | Issue #42 | Record exact frontend/API/database identity before E2E | Open |
| Diverged branches created overwrite risk | Issue #43, PR #44 | Use a file-level, owner-approved reconciliation plan | Draft |
| Multiple Draft PRs could overwhelm reviewers | Issue #49, PR #50 | Use one coordinated review order and owner-specific checklists | Draft |
| Design evidence was spread across implementation files | Issue #51, PR #52 | Create one V3 architecture/database/UI page | Draft |
| Agile evidence was fragmented | Issue #53 | Consolidate iteration, demo, feedback and retrospective evidence | In progress |

## 15. Reusable iteration close-out template

Copy this section for every future iteration or release-candidate cycle.

### Iteration identity

- Iteration name/number:
- Start date/timezone:
- End date/timezone:
- Iteration goal:
- Frozen baseline commit:
- Coordinator:
- Participants:

### Planned scope

| Story/task | Priority | Reason | Owner | Planned effort | Dependency | Acceptance criteria |
|---|---|---|---|---:|---|---|
|  |  |  |  |  |  |  |

### Actual outcome

| Story/task | Delivered? | Actual effort | PR/commit | Test evidence | Deployment/demo evidence | Variance reason |
|---|---|---:|---|---|---|---|
|  |  |  |  |  |  |  |

### Demonstration

- Deployment URL/environment:
- Exact deployed commit:
- Demonstration date/timezone:
- Demonstrator:
- Audience/client:
- Features demonstrated:
- Failed or blocked flows:
- Evidence location:

### Feedback

| Participant/client | Feedback | Evidence | Decision | Owner | Due date | Retest evidence |
|---|---|---|---|---|---|---|
|  |  |  | Accept / Reject / Defer |  |  |  |

### Retrospective

- What was planned well:
- What was delivered well:
- What was delayed or blocked:
- Root cause:
- What should stop:
- What should continue:
- What should start:
- One measurable process improvement for the next iteration:
- Owner and due date:

### Close-out decision

- Planned scope completed: Yes / No / Partial
- Accepted limitations:
- Deferred work and target iteration:
- Client/user acceptance status:
- Review status:
- Final iteration status:

## 16. Owner review checklist

### Zaikun — backend, API and testing

- [ ] Confirm Phase 2 and current CI/test descriptions.
- [ ] Confirm that no passing subset is described as a passing complete suite.
- [ ] Add or correct backend iteration dates, estimates and actual effort only where evidence exists.
- [ ] Confirm the technical blocker and next action for `test_mock.py`.
- [ ] Confirm backend demo/client-feedback evidence, or leave it `Not retained`.

### Yuyang — data, database and importer

- [ ] Confirm Phase 1 and current V3 database descriptions.
- [ ] Confirm that completed implementation is not described as missing development.
- [ ] Add or correct database iteration dates, estimates and actual effort only where evidence exists.
- [ ] Confirm database demo/client-feedback evidence, or leave it `Not retained`.
- [ ] Confirm Issue #41/PR #48 as the correct release-verification path.

### Guanyu — frontend, UX and demonstrations

- [ ] Confirm frontend iteration and delivery descriptions.
- [ ] Add or correct demo dates, deployed commits and feedback only where evidence exists.
- [ ] Confirm whether any earlier user/client session can be supported by retained evidence.
- [ ] Confirm the current GitHub Pages deployment identity status.
- [ ] Review the final demo and external-UAT plan.

### Junjie — coordination and evidence integrity

- [ ] Ensure planned and actual values remain separate.
- [ ] Link every completion statement to Issue, PR, commit, test or acceptance evidence.
- [ ] Keep missing historical evidence explicit.
- [ ] Record schedule/scope changes and corrective actions.
- [ ] Do not mark the project Done while release gates remain open.

## 17. Completion conditions for this Agile evidence page

This page may be merged as an evidence framework after owner review, but the project cannot claim exemplary completed iteration evidence until:

- official iteration labels and dates are confirmed;
- available planned and actual effort values are entered from real sources;
- the deployed V3 release candidate is identified;
- deployed demonstrations are executed and retained;
- external-user feedback is collected and acted upon;
- formal retrospective outcomes are recorded for the remaining cycles;
- the final release gates are completed or accurately accepted as limitations.

Until then, this page is a transparent record of strong repository process evidence and the remaining HD evidence gaps.
