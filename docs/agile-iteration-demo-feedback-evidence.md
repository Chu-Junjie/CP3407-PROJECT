# Agile Iteration, Demonstration, Feedback and Retrospective Record

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Recorded:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation baseline:** `feature/product-database`  
**Related tracking:** Issue #53  
**Status:** Draft — owner confirmation and missing historical evidence pending

## 1. Purpose

This document consolidates the available evidence that the project was planned, delivered, reviewed and adapted incrementally.

It does not reconstruct missing meetings, estimates, demonstrations or stakeholder feedback as if they had occurred. Where the repository does not retain sufficient evidence, the status is stated as `Not retained`, `Not Run`, `Unknown` or `Pending confirmation`.

## 2. Evidence boundary

The repository contains strong evidence for:

- Issue-driven planning;
- separate branches and Pull Requests;
- non-author review;
- governance and traceability updates;
- test audits;
- release-gate management;
- owner boundaries and blocker escalation.

The repository contains incomplete historical evidence for:

- official iteration start and end dates;
- planned story-point or hour estimates for every story;
- actual effort for every owner;
- deployed demonstrations after every iteration;
- stakeholder feedback after every iteration;
- formal retrospective minutes after every iteration.

A merged Pull Request proves that a reviewed repository change reached its target branch. It does not prove that the change was deployed, demonstrated or externally accepted.

## 3. Status vocabulary

| Status | Meaning |
|---|---|
| Planned | Scope or evidence work is defined but not yet completed. |
| Prepared | A template, plan or review record exists; execution has not occurred. |
| Implemented | Code, data or documentation exists on the named branch. |
| Verified | A named check passed for a named commit and environment. |
| Blocked | Completion depends on an unresolved technical or decision gate. |
| Not Run | The required test, demonstration or acceptance activity has not occurred. |
| Not retained | The activity may have occurred, but no reliable evidence is currently retained. |
| Pending confirmation | An owner must confirm the record or provide missing evidence. |
| Done | All applicable Definition of Done and release gates have passed. |

## 4. Delivery phases

The following phases are reconstructed from repository evidence. They are not presented as official sprint dates unless a source explicitly confirms that status.

| Phase | Primary objective | Main evidence | Repository delivery status | Deployment/demo status | Feedback status |
|---|---|---|---|---|---|
| Foundation and governance | Establish contracts, ownership, traceability and working rules | PR #17, PR #20 | Merged to `main` | Not retained | Not retained |
| Database integration | Record initial database structure, counts, integrity and feedback persistence | PR #22 | Merged to `main` | Not retained | Pending confirmation |
| Backend compatibility audit | Reconcile dependencies and expose legacy test incompatibility | PR #25 | Merged to `main` | Not applicable as product demo | Technical review retained; stakeholder feedback not retained |
| V3 baseline adoption | Adopt SQLAlchemy, account/history/favorites, pagination, larger catalogue and release governance | PR #33, PR #37, PR #39 | Merged to `feature/product-database` | Deployed identity unverified | External UAT not run |
| Release preparation | Resolve CI scope, database verification, deployed E2E, US-09 and branch reconciliation | Issues #34, #40–#53 and Draft PRs | In progress | Not Run or Unverified | Pending |

## 5. Phase 1 — Foundation and governance

### Objective

Establish a controlled project baseline before deeper integration work continued.

### Planned scope supported by repository evidence

- project baseline decision;
- frozen technical decisions;
- database and API contracts;
- team ownership and branch responsibilities;
- requirements traceability;
- Definition of Done;
- project status and risk tracking;
- Issue and Pull Request templates.

### Delivered evidence

- PR #17 established the documented project foundation;
- PR #20 recorded the close-out evidence for that governance work;
- non-author review and merge records were retained.

### Variance and limitations

- later V3 implementation changed the practical database, API and release baseline;
- older statements about approximately 9,000 behavioural rows and 33 specification rows became historical rather than current;
- early iteration demonstration and stakeholder-feedback evidence is not retained in the current repository record.

### Corrective action

PR #33 later replaced obsolete governance statements with the V3 baseline and introduced stronger evidence vocabulary.

### Coordinator retrospective observation

Governance documents should be updated whenever the implementation baseline changes materially. A project should not continue using a historical requirements or architecture record as if it describes the current release.

## 6. Phase 2 — Database integration

### Objective

Integrate and record the initial database design and evidence for the then-current baseline.

### Delivered evidence

PR #22 recorded:

- database Pull Request and review details;
- record counts;
- ProductID integrity;
- feedback persistence and validation;
- database test results;
- updates to traceability, project status and Definition of Done.

### Evidence boundary

The PR proves the recorded checks for the named historical baseline. It does not prove the current V3 SQLAlchemy/PostgreSQL implementation or current catalogue counts.

### Variance and corrective action

The V3 branch later introduced a larger catalogue, additional account-owned tables, SQLAlchemy and PostgreSQL support. Historical evidence is retained as history, while current verification is tracked separately under Issue #41 and PR #48.

### Owner confirmation required

Yuyang should confirm which historical database statements remain technically relevant and which must remain labelled as superseded.

## 7. Phase 3 — Backend compatibility and test audit

### Objective

Reconcile dependencies, execute the available backend test suite and document compatibility blockers without rewriting teammate-owned implementation.

### Delivered evidence

PR #25 retained:

- dependency installation evidence;
- pip and compilation checks;
- test collection output;
- failing full-suite evidence;
- legacy fixture and mock incompatibilities;
- database side-effect evidence;
- restoration of the tracked SQLite file;
- updated traceability and blocker records.

### Observed result

The historical full suite did not pass. Successful installation, compilation or collection was not represented as a passing test suite.

### Variance

The original expectation of straightforward backend verification was blocked by obsolete test fixtures, changed API contracts and incomplete database isolation.

### Corrective actions

- protected backend and test ownership boundaries were retained;
- blockers were returned to the backend/test owner;
- PR #35 introduced a reproducible CI workflow with separate V3 API and full-repository jobs;
- current canonical test scope remains pending under Issue #34.

### Coordinator retrospective observation

A release process must distinguish collection success, subset success and complete-suite success. A failing compatibility test should remain visible until the owner updates, archives or formally excludes it with a recorded reason.

## 8. Phase 4 — V3 baseline adoption

### Objective

Adopt the current implementation branch as the authoritative V3 baseline and prepare repeatable release evidence.

### Delivered evidence

PR #33 documented the V3 baseline, including:

- 11,000 products and 2,000 recommendation-ready specifications as the expected implementation counts;
- Flask and SQLAlchemy;
- SQLite local use and PostgreSQL production support through `DATABASE_URL`;
- password-hashed accounts and JWT authentication;
- favorites, private history, result snapshots and feedback;
- paginated recommendations with a separate Top 5.

PR #37 added repeatable deployed E2E and external-UAT templates.

PR #39 audited stale and conflicting release documentation.

### Evidence boundary

The merged governance, audit and test templates prove that controlled documentation exists. They do not prove deployed identity, PostgreSQL persistence, browser E2E or external-user acceptance.

### Variance and corrective actions

- README and historical documents still require later reconciliation;
- the full repository suite remains blocked by legacy tests;
- US-09 requires a team scope decision;
- deployed frontend/API/database identity remains unverified;
- `main` and `feature/product-database` have diverged and require controlled reconciliation.

### Coordinator retrospective observation

Preparation records and execution records must remain separate. Templates improve repeatability, but release status changes only after actual evidence is retained.

## 9. Phase 5 — Release preparation and controlled integration

### Objective

Complete the remaining decision, verification, review and integration gates without overwriting completed teammate work.

### Current work package

| Work item | Purpose | Current status |
|---|---|---|
| Issue #34 / PR #35 | Canonical CI and legacy-test disposition | Blocked pending Zaikun decision |
| Issue #40 / PR #47 | US-09 scope decision | Pending team input |
| Issue #41 / PR #48 | Catalogue and PostgreSQL verification | Prepared; execution pending |
| Issue #42 | Deployed browser E2E | Candidate endpoints recorded; identity unverified |
| Issue #43 / PR #44 | Safe `main` and V3 reconciliation | Draft planning record |
| Issue #45 / PR #46 | Release evidence index | Draft |
| Issue #49 / PR #50 | Coordinated team review package | Draft |
| Issue #51 / PR #52 | Architecture and design reference | Draft |
| Issue #53 / PR #54 | Agile delivery record | Draft |

### Current release gates

- canonical complete test scope approved;
- selected test suite passes in CI;
- database counts and integrity verified for a named commit;
- importer repeatability verified;
- PostgreSQL engine and persistence verified;
- deployed frontend and API commits confirmed;
- browser E2E executed;
- external UAT executed;
- all owner-specific defects resolved or accepted;
- controlled branch reconciliation reviewed;
- final release candidate approved.

## 10. Scope-change register

| Change | Trigger | Decision status | Impact |
|---|---|---|---|
| Replace historical database baseline with V3 | Teacher feedback and newer implementation | Adopted through PR #33 | Governance and release evidence had to be rewritten |
| Add SQLAlchemy and PostgreSQL support | Production-persistence requirement | Implemented; verification pending | New database and deployment checks required |
| Add accounts, favorites and private history | V3 scope expansion | Implemented; E2E pending | Authentication, privacy and persistence checks required |
| Add pagination plus separate Top 5 | Larger catalogue and usability needs | Implemented; E2E pending | API and UI acceptance expanded |
| Confirm US-09 budget alternatives | Historical requirement no longer matched confirmed V3 scope | Pending Issue #40 | Release wording and possible implementation remain blocked |
| Reconcile `main` and V3 | Branch divergence | Planning under Issue #43 | Direct merge is prohibited until owner review |

## 11. Demonstration and feedback ledger

| Phase or feature | Demonstration evidence | Feedback evidence | Status |
|---|---|---|---|
| Foundation documentation | Pull Request review | Non-author review | Retained |
| Historical database work | Repository evidence retained | Owner confirmation incomplete | Partial |
| Backend compatibility audit | Test logs and PR review | Technical review retained | Retained for technical audit only |
| Current V3 frontend | Candidate GitHub Pages URL | Guanyu confirmation pending | Unverified |
| Current V3 API | Candidate Render URL | Zaikun confirmation pending | Unverified |
| PostgreSQL persistence | No executed persistence record | Yuyang evidence pending | Not Run or Unverified |
| End-to-end product flows | Template prepared | No executed browser evidence | Not Run |
| External user acceptance | Two-participant template prepared | No participant result retained | Not Run |

## 12. Planned versus actual effort record

The repository does not currently retain reliable planned and actual effort values for every story. Those values must not be estimated retrospectively without team confirmation.

| Work item | Planned estimate | Actual effort | Variance | Evidence status |
|---|---:|---:|---:|---|
| Foundation and governance | Unknown | Unknown | Unknown | Historical estimates not retained |
| Database integration | Pending owner confirmation | Pending owner confirmation | Pending | Incomplete |
| Backend compatibility work | Pending owner confirmation | Pending owner confirmation | Pending | Incomplete |
| V3 frontend integration | Pending owner confirmation | Pending owner confirmation | Pending | Incomplete |
| Current release verification | To be estimated before execution | To be recorded after execution | Pending | Planned |

For future work, the estimate must be recorded before implementation or verification starts.

## 13. Blocker and corrective-action register

| Blocker | Owner | Corrective action | Tracking |
|---|---|---|---|
| Legacy `test_mock.py` incompatible with V3 | Zaikun | Update, archive or formally exclude with canonical test command | Issue #34 / PR #35 |
| US-09 scope unclear | Zaikun, Guanyu and Junjie | Select retain, revise or defer with impact assessment | Issue #40 / PR #47 |
| PostgreSQL and persistence unverified | Yuyang | Execute database verification record | Issue #41 / PR #48 |
| Deployed identity and E2E unverified | Guanyu with coordinator | Confirm commits and execute browser matrix | Issue #42 |
| `main` and V3 diverged | All owners | Approve file-level reconciliation before integration | Issue #43 / PR #44 |
| Technical documentation requires owner confirmation | Zaikun, Yuyang and Guanyu | Complete coordinated review package | Issue #49 / PR #50 |

## 14. Process improvements already introduced

| Observation | Improvement | Evidence |
|---|---|---|
| Historical and current status became mixed | Adopt explicit evidence vocabulary and authoritative V3 baseline | PR #33 |
| Test subset success could be mistaken for complete success | Separate V3 API and full-repository CI jobs | PR #35 |
| Acceptance could be claimed without repeatable records | Add E2E and UAT templates with `Not Run` defaults | PR #37 |
| Documentation contained stale claims | Perform structured consistency audit | PR #39 |
| Branch integration could overwrite owner work | Add owner-controlled reconciliation plan | Issue #43 / PR #44 |
| Multiple Draft PRs could create fragmented review | Add coordinated but independent review package | Issue #49 / PR #50 |
| Design decisions were distributed across files | Add consolidated design and architecture reference | Issue #51 / PR #52 |
| Delivery history lacked one controlled record | Add this Agile delivery record | Issue #53 / PR #54 |

## 15. Future iteration close-out template

Use this structure before closing a future iteration or release phase.

### Identity

- Iteration or phase name:
- Planned start:
- Planned finish:
- Actual finish:
- Coordinator:
- Technical owners:
- Target branch and commit:

### Goal and scope

- Goal:
- Planned user stories:
- Excluded scope:
- Dependencies:
- Priority rationale:

### Estimates

| Item | Owner | Planned effort | Actual effort | Variance | Reason |
|---|---|---:|---:|---:|---|
|  |  |  |  |  |  |

### Delivery evidence

| Item | Issue | Branch | PR | Commit | Review | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### Verification

- Test command:
- Test result:
- Environment:
- Database evidence:
- Deployment evidence:
- Browser evidence:
- Security/privacy evidence:

### Demonstration and feedback

- Demo date:
- Demonstrated commit and environment:
- Participants:
- Tasks demonstrated:
- Feedback received:
- Evidence location:
- Follow-up Issues:

### Retrospective

- What worked:
- What did not work:
- What changed during the iteration:
- Root cause of variance:
- One process improvement for the next phase:
- Owner and due date for the improvement:

### Close-out decision

- Completed scope:
- Deferred scope:
- Accepted limitations:
- Remaining blockers:
- Release decision:
- Approvals:

## 16. Review responsibilities

### Zaikun

- confirm backend and test-phase descriptions;
- confirm blocker and corrective-action wording;
- provide planned and actual effort where retained;
- identify unsupported technical claims.

### Yuyang

- confirm database, catalogue and importer history;
- distinguish historical evidence from current V3 evidence;
- provide planned and actual effort where retained;
- identify unsupported persistence claims.

### Guanyu

- confirm frontend delivery, demo and user-feedback history;
- confirm deployed-identity limitations;
- provide planned and actual effort where retained;
- identify unsupported UI claims.

### Junjie

- preserve planned-versus-actual separation;
- keep missing evidence visible;
- link scope changes and corrective actions;
- coordinate review without modifying teammate-owned implementation.

## 17. Current conclusion

The project has a strong repository-based incremental delivery process, with clear Issue, branch, Pull Request, review and release-gate controls. The remaining work is to complete owner confirmation, retain reliable estimates, execute deployment and acceptance activities, and close the technical release gates with evidence tied to a named commit and environment.