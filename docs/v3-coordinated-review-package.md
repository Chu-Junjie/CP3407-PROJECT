# V3 Coordinated Team Review Package

**Tracking Issue:** #49  
**Coordinator:** Chu Junjie  
**Review request status:** Not sent  
**Target reviewers:** Guanyu Lu, Zaikun Zheng and Yuyang Zhou  
**Target base branch:** `feature/product-database`

## 1. Purpose

This document coordinates one review period for the current V3 Draft Pull Requests while keeping each Pull Request independent.

The goal is to reduce repeated review requests, give every technical owner a clear review scope and avoid merging any package merely because another package was approved.

## 2. Review principles

1. Every Pull Request remains independently reviewable, approvable and mergeable.
2. A reviewer approves only statements and changes they are qualified to verify.
3. No reviewer is asked to approve another owner's technical implementation on that owner's behalf.
4. A documentation template is not an executed result.
5. A passing test subset is not a passing complete suite.
6. A Draft PR remains Draft while its prerequisite decision or evidence is unresolved.
7. All package PRs target `feature/product-database`, not `main`.
8. Merge to `main` remains governed separately by Issue #43 and final release evidence.

## 3. Package inventory

| PR | Title | Changed area | Current status | Main prerequisite |
|---|---|---|---|---|
| #35 | `ci: add V3 test evidence workflow` | `.github/workflows/tests.yml` | Draft / Blocked | Issue #34 owner decision on `test_mock.py` and canonical final suite. |
| #44 | `docs: plan safe reconciliation of main and V3` | Reconciliation plan only | Draft | Owner confirmation for file-level choices before any integration branch. |
| #46 | `docs: add V3 release evidence index` | Release evidence index only | Draft | Accuracy review across all component statements. |
| #47 | `docs: add US-09 V3 scope decision record` | US-09 decision template only | Draft / Pending | Issue #40 backend and frontend owner input and final team decision. |
| #48 | `docs: add V3 database release verification record` | Database verification template only | Draft / Pending execution | Issue #41 owner review and later executed evidence. |
| #50 | This coordinated review package | Review coordination only | Draft | Package inventory and reviewer scopes must be accurate. |

PR #50 is expected to be the Pull Request containing this document. If GitHub assigns a different number, update this row before the final review request.

## 4. Evidence references already merged

The review package should be read together with:

- PR #33 — V3 governance and release baseline;
- PR #37 — E2E and external UAT evidence templates;
- PR #39 — release-documentation consistency audit;
- Issue #42 — deployed V3 E2E execution tracking.

These merged records provide governance and preparation evidence. They do not prove final deployment or acceptance.

## 5. Prerequisites before reviewer requests are sent

### 5.1 Issue #34 / PR #35

- [ ] Zaikun records whether `test_mock.py` is updated, archived or formally excluded.
- [ ] Zaikun records the canonical complete test command and expected collected files.
- [ ] PR #35 wording is updated if the owner decision changes the intended workflow.
- [ ] The current 12-pass subset and 6-failure complete-suite evidence remains accurately separated.

### 5.2 Issue #40 / PR #47

- [ ] Zaikun records the backend, recommendation, API and automated-test impact.
- [ ] Guanyu records the frontend, interaction, empty-state and browser-E2E impact.
- [ ] The team selects Option A, B or C.
- [ ] PR #47 final-decision fields remain Pending until the team decision exists.

### 5.3 Issue #41 / PR #48

- [ ] Yuyang confirms the record matches the actual V3 schema, catalogue and importer.
- [ ] No execution result is populated without a command/query and retained output.
- [ ] PostgreSQL and credential wording does not expose private data.
- [ ] The record continues to acknowledge that Yuyang's implementation is completed on the V3 branch.

### 5.4 Issue #42

- [ ] Guanyu confirms the deployed GitHub Pages identity or records it as blocked.
- [ ] API/database owners confirm the deployed API and database environment or record them as blocked.
- [ ] No E2E result is marked Passed before execution.

### 5.5 Issue #43 / PR #44

- [ ] The team agrees that `feature/product-database` is the V3 implementation baseline.
- [ ] Yuyang's completed V3 database, catalogue and importer work is protected from overwrite.
- [ ] Main-only historical evidence is separated from obsolete implementation.
- [ ] No reconciliation branch has been created before explicit approval.

### 5.6 Issue #45 / PR #46

- [ ] Issue and PR references are current.
- [ ] Evidence statuses are accurate.
- [ ] No unresolved gate is marked Done.

Reviewer requests may still be sent when an item is genuinely Blocked, but the relevant PR must remain Draft and the request must clearly ask for review of the documented blocker rather than approval to merge.

## 6. Reviewer scope — Guanyu

**GitHub:** `Guanyu-Lu`  
**Primary ownership:** frontend, UI/UX, deployed frontend behaviour

### Required PR review

| PR | Required Guanyu review |
|---|---|
| #35 | Confirm the workflow does not make unsupported frontend claims; no workflow ownership approval is required beyond shared integration impact. |
| #44 | Confirm the plan does not allow `main` to overwrite current V3 frontend work and that `index.html` conflict choices remain under frontend ownership. |
| #46 | Review frontend implementation status, deployed GitHub Pages identity wording, E2E status and accessibility statements. |
| #47 | Record and confirm the US-09 frontend/UI/E2E impact and recommendation. |
| #48 | Review product-source and historical-price wording where it affects frontend presentation. |
| #50 | Confirm this reviewer scope is accurate and practical. |

### Guanyu approval checklist

- [ ] V3 frontend work is not described as missing merely because it is not in `main`.
- [ ] No deployed frontend commit is claimed without confirmation.
- [ ] All Issue #42 scenarios remain evidence-based.
- [ ] US-09 UI, empty-state, responsive and E2E impact is accurately represented.
- [ ] No coordinator document authorizes edits to frontend-owned files.

## 7. Reviewer scope — Zaikun

**GitHub:** `ZhengZaikun`  
**Primary ownership:** backend, API, recommendation logic, automated tests

### Required PR review

| PR | Required Zaikun review |
|---|---|
| #35 | Confirm final test scope, `test_mock.py` disposition, dependency strategy and workflow commands. |
| #44 | Confirm backend/test/dependency overlap remains under backend ownership and that the plan does not choose `server.py` or test versions on his behalf. |
| #46 | Review backend/API/auth/privacy and automated-test evidence wording. |
| #47 | Record and confirm US-09 algorithm, API and automated-test impact and recommendation. |
| #48 | Review user-owned table persistence expectations, authentication/privacy checks and API-related database wording. |
| #50 | Confirm this reviewer scope is accurate and practical. |

### Zaikun approval checklist

- [ ] The 12-pass V3 subset is not presented as a passing complete suite.
- [ ] The 6 legacy mock failures remain visible until an owner decision is made.
- [ ] The canonical release test command is explicit before PR #35 leaves Draft.
- [ ] US-09 backend, algorithm, API and test requirements are unambiguous or the feature is explicitly deferred.
- [ ] No coordinator document authorizes edits to backend or automated-test files.

## 8. Reviewer scope — Yuyang

**GitHub:** `tiantian09091`  
**Primary ownership:** datasets, database, importer, provenance, PostgreSQL verification

### Required PR review

| PR | Required Yuyang review |
|---|---|
| #35 | Confirm the workflow does not misstate database verification; no test-owner approval is required for backend test disposition. |
| #44 | Confirm her completed V3 database, catalogue and importer work is authoritative and protected from overwrite. |
| #46 | Review catalogue counts, provenance, PostgreSQL, persistence, backup and limitation wording. |
| #47 | Review only data/price/source implications of the selected US-09 option where applicable. |
| #48 | Confirm schema/query/importer/provenance/PostgreSQL wording and later validate populated results. |
| #50 | Confirm this reviewer scope is accurate and practical. |

### Yuyang approval checklist

- [ ] The package states that her V3 implementation is completed on `feature/product-database`.
- [ ] Verification remains separate from implementation presence.
- [ ] Count, uniqueness, join and importer checks match the actual schema and scripts.
- [ ] PostgreSQL verification avoids exposing credentials.
- [ ] Historical price and source limitations are accurate.
- [ ] No coordinator document authorizes edits to data, database or importer files.

## 9. Coordinator scope — Junjie

### Coordinator responsibilities

- maintain accurate Issue, PR and commit references;
- distinguish Prepared, Implemented, Verified, Blocked, Not Run and Unverified;
- update coordinator-owned documents after owner evidence exists;
- keep every PR Draft until its prerequisites are satisfied;
- request all three reviewers during the same coordinated review period;
- avoid duplicate pings while review is pending;
- record review results and unresolved comments;
- merge only independently approved PRs;
- keep technical release, deployment and acceptance gates open until evidence exists.

### Coordinator checklist

- [ ] No teammate-owned implementation file is modified.
- [ ] No unexecuted result is marked Passed.
- [ ] Each PR contains one coherent concern.
- [ ] Every PR targets `feature/product-database`.
- [ ] Review requests are sent only after the package is internally consistent.
- [ ] A non-author approval is obtained for every PR that is merged.
- [ ] Closing an Issue occurs only after its completion criteria are satisfied.

## 10. Coordinated review order

The reviewers may open the PRs in any order, but the recommended reasoning order is:

1. **PR #46 — Evidence index:** understand the complete current state.
2. **PR #44 — Reconciliation plan:** confirm branch and ownership protections.
3. **PR #35 — CI workflow:** confirm test evidence and unresolved test scope.
4. **PR #47 — US-09 decision record:** complete the scope decision.
5. **PR #48 — Database verification record:** confirm the later execution method.
6. **PR #50 — Review package:** confirm shared review and merge rules.

This order does not authorize merging in the same order.

## 11. Approval and merge rules

### 11.1 PR #35

May leave Draft only when:

- Zaikun has recorded the final test scope;
- the workflow matches that scope;
- the complete suite evidence is not hidden;
- a non-author reviewer approves.

A red complete-suite job may be retained as audit evidence but does not satisfy the final release test gate.

### 11.2 PR #44

May leave Draft only when:

- all affected owners confirm file-level treatment;
- no technical version is selected on an owner's behalf;
- the plan still prohibits immediate integration to `main`;
- a non-author reviewer approves.

### 11.3 PR #46

May leave Draft when:

- current references and statuses are accurate;
- each technical owner confirms the statements affecting their component;
- a non-author reviewer approves.

### 11.4 PR #47

May leave Draft only when:

- Issue #40 has a complete owner-supported decision;
- the selected option and impacts are entered accurately;
- required implementation work is tracked separately;
- a non-author reviewer approves.

If Issue #40 is still pending, PR #47 may remain a useful Draft template but must not merge as a completed decision.

### 11.5 PR #48

The template may be approved and merged before execution only if it remains clearly labelled as an unexecuted record. Populated release results require later review of the actual evidence.

### 11.6 PR #50

May leave Draft when:

- all listed PR numbers and scopes are correct;
- reviewers agree that the coordinated process is understandable;
- it does not imply automatic batch approval or merge;
- a non-author reviewer approves.

## 12. Request message to use later

Do not send this message until the coordinator confirms the package is ready.

> @Guanyu-Lu @ZhengZaikun @tiantian09091 The V3 coordinator-owned Draft review package is ready. Please review the PRs within your component scope using `docs/v3-coordinated-review-package.md`. Each PR remains independent; approval of one does not approve the others, and unresolved technical results remain Draft or Blocked. Please leave component-specific corrections on the relevant PR rather than approving another owner's implementation on their behalf.

## 13. Review outcome record

Complete after reviewer requests are sent.

| PR | Guanyu | Zaikun | Yuyang | Non-author approval | Draft removed | Merged | Notes |
|---|---|---|---|---|---|---|---|
| #35 | Not requested | Not requested | Not requested | No | No | No | Test scope pending. |
| #44 | Not requested | Not requested | Not requested | No | No | No | Owner confirmations pending. |
| #46 | Not requested | Not requested | Not requested | No | No | No | Evidence index Draft. |
| #47 | Not requested | Not requested | Not requested | No | No | No | US-09 decision pending. |
| #48 | Not requested | Not requested | Not requested | No | No | No | Verification template; results not run. |
| #50 | Not requested | Not requested | Not requested | No | No | No | Review package Draft. |

## 14. Post-review sequence

1. Address requested changes on the relevant independent branches.
2. Re-request only the reviewers whose requested changes were addressed.
3. Mark a PR ready only when its own merge rules are satisfied.
4. Merge approved coordinator-owned documentation/workflow PRs into `feature/product-database`.
5. Update Issue states individually; do not close all package Issues as one action.
6. Freeze a release candidate only after test scope and US-09 scope are resolved.
7. Execute database verification, deployed E2E and external UAT for the frozen commit.
8. Create any reconciliation branch only under Issue #43 after explicit approval.
9. Merge to `main` only after the final release checklist has actual retained evidence.

## 15. Non-authorization statement

This coordinated review package does not authorize:

- changing teammate-owned implementation;
- requesting approval for results that have not been executed;
- automatic batch approval or batch merge;
- marking a PR ready solely because another PR was approved;
- closing Issues #34, #40, #41, #42 or #43 without their own completion evidence;
- creating the reconciliation branch;
- merging to `main`.
