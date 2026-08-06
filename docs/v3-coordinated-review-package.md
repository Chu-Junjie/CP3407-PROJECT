# V3 Coordinated Review and Closeout Package

**Tracking Issue:** #49  
**Coordinator:** Chu Junjie  
**Target base branch:** `feature/product-database`  
**Review status:** Deferred — no approval is recorded by this document  
**Package status:** Prepared for a later coordinated review and conditional closeout

## 1. Purpose

This document provides one controlled path from the current Draft Pull Requests to a release candidate. It keeps each Pull Request independent, preserves component ownership and prevents prepared documentation from being treated as executed technical evidence.

The team review is intentionally deferred. The closeout sequence below assumes that the required reviewers later approve the relevant Pull Requests, but this planning assumption must never be recorded as an actual GitHub approval.

## 2. Operating rules

1. Every Pull Request remains independently reviewable and mergeable.
2. No reviewer approval is fabricated or inferred from silence.
3. A template or plan may be merged as a prepared engineering record when its status remains explicit.
4. A technical result may be marked `Verified` only after a named test, environment and retained result exist.
5. Teammate-owned backend, frontend, tests, datasets, databases, importers and deployment configuration remain under their owners.
6. All package Pull Requests target `feature/product-database`; no package item authorizes a direct merge to `main`.
7. Review-dependent work is held while coordinator-owned preparation and consistency checks continue.

## 3. Package inventory

| PR | Scope | Current state | Required before merge |
|---|---|---|---|
| #35 | GitHub Actions V3 test-evidence workflow | Draft / Blocked | Zaikun confirms the final suite and `test_mock.py` disposition; non-author approval. |
| #44 | Safe `main`/V3 reconciliation plan | Draft / Prepared | Affected owners confirm file treatment; non-author approval. |
| #46 | V3 release evidence index | Draft / Prepared | References and statuses are current; non-author approval. |
| #47 | US-09 scope decision record | Draft / Decision pending | Issue #40 owner input and a recorded A/B/C decision; non-author approval. |
| #48 | Database release-verification record | Draft / Template prepared | Yuyang confirms wording; non-author approval. Executed results may remain pending. |
| #50 | This coordinated review and closeout package | Draft / Prepared | Package inventory and closeout rules are accurate; non-author approval. |
| #52 | V3 design and architecture reference | Draft / Prepared | Zaikun, Yuyang and Guanyu confirm their component descriptions; non-author approval. |
| #54 | Agile delivery, demo, feedback and retrospective record | Draft / Prepared | Owners confirm component history; non-author approval. |
| #58 | Development toolchain and dependency reference | Draft / Prepared | Owners confirm their toolchain sections; non-author approval. |

## 4. Technical gates kept separate from documentation review

| Gate | Tracking | Current state | Owner action |
|---|---|---|---|
| Canonical full test scope | Issue #34 / PR #35 | Blocked | Zaikun decides how V3 handles legacy `test_mock.py`, then the agreed suite is run. |
| US-09 release scope | Issue #40 / PR #47 | Pending decision | Zaikun and Guanyu provide impact; the team records Option A, B or C. |
| Catalogue and PostgreSQL verification | Issue #41 / PR #48 | Implementation exists; release verification pending | Yuyang records queries, importer checks, environment and persistence evidence. |
| Deployed V3 identity and E2E | Issue #42 | Not Run / Unverified | Confirm frontend/API/database identities, then execute the E2E matrix. |
| Safe branch reconciliation | Issue #43 / PR #44 | Planned only | Create an integration branch only after owner-confirmed file treatment and explicit approval. |
| External acceptance | PR #37 templates | Not Run | Execute stable-candidate participant sessions and retain outcomes. |

A successful documentation review does not close these technical gates.

## 5. Reviewer scope for the later coordinated review

### Guanyu (`Guanyu-Lu`)

- PR #44: protection of current V3 frontend work and `index.html` ownership.
- PR #46: frontend implementation, deployment identity, E2E and accessibility statements.
- PR #47: US-09 presentation and browser-E2E impact.
- PR #52: interface structure, responsive behaviour and accessibility wording.
- PR #54: frontend iteration, demonstration and feedback history.
- PR #58: browser, GitHub Pages and interface-design tooling.
- PR #50: practicality of the coordinated review and closeout rules.

### Zaikun (`ZhengZaikun`)

- PR #35: final test scope, commands, dependencies and legacy-test disposition.
- PR #44: backend/test/dependency conflict ownership.
- PR #46: API, authentication, privacy and test-evidence statements.
- PR #47: US-09 algorithm, API and automated-test impact.
- PR #48: API-related persistence and privacy verification wording.
- PR #52: backend, API, authentication and recommendation architecture.
- PR #54: backend/test iteration outcomes and blockers.
- PR #58: runtime dependencies, pytest, CI and Render API tooling.
- PR #50: practicality of the coordinated review and closeout rules.

### Yuyang (`tiantian09091`)

- PR #44: preservation of completed V3 database, catalogue and importer work.
- PR #46: catalogue, provenance, PostgreSQL, persistence and recovery statements.
- PR #47: data/source/price implications of the selected option.
- PR #48: schema, query, importer, provenance and PostgreSQL verification method.
- PR #52: ERD, relationships, importer and database architecture.
- PR #54: database/catalogue/importer delivery history.
- PR #58: database, importer, PostgreSQL and provenance tooling.
- PR #50: practicality of the coordinated review and closeout rules.

## 6. Coordinator work completed before review

- The V3 implementation baseline is identified as `feature/product-database`.
- Yuyang's completed database, catalogue and importer work is protected from overwrite in the reconciliation plan.
- CI evidence separates the passing 12-test V3 API subset from the failing complete repository audit.
- US-09 remains a recorded scope decision rather than an implied completed feature.
- Database, E2E and external-acceptance templates are separated from executed results.
- Architecture, Agile delivery and toolchain references have dedicated Draft Pull Requests.
- No package Pull Request modifies teammate-owned implementation.
- No package document records a review, deployment, persistence check or acceptance session that did not occur.

## 7. Review-deferred state

While team review is paused:

- keep PRs #35, #44, #46, #47, #48, #50, #52, #54 and #58 as Draft;
- do not request additional reviewers or repeat pings;
- do not record approvals in the outcome table;
- continue only read-only inspection and coordinator-owned consistency fixes;
- keep Issues #34, #40, #41, #42 and #43 open;
- do not create the reconciliation branch or merge to `main`.

## 8. Conditional closeout sequence after real approvals

The following sequence begins only after the required GitHub reviews are actually submitted.

1. Resolve review comments on each independent branch.
2. Re-run reference and terminology checks across all coordinator-owned documents.
3. Merge approved prepared-document PRs into `feature/product-database` in a controlled order:
   - PR #44 — reconciliation plan;
   - PR #52 — design and architecture;
   - PR #54 — Agile delivery record;
   - PR #58 — development toolchain;
   - PR #46 — release evidence index updated to the merged state;
   - PR #50 — coordinated review and closeout package.
4. Merge PR #48 only as an explicitly unexecuted verification record unless actual results have been populated and reviewed.
5. Merge PR #47 only after Issue #40 contains the final supported US-09 decision.
6. Merge PR #35 only after the canonical suite decision is recorded and the workflow accurately represents it.
7. Close documentation Issues only after their associated PR is merged and completion criteria are satisfied.
8. Freeze a release-candidate commit on `feature/product-database`.
9. Execute the canonical CI suite for that frozen commit.
10. Execute Issue #41 database/PostgreSQL verification against the frozen candidate.
11. Confirm deployed frontend/API/database identity and execute Issue #42 E2E.
12. Execute the external-acceptance sessions and record defects or accepted limitations.
13. Update README, project status, requirements traceability and final acceptance records to match the verified candidate.
14. Create the reconciliation branch only under Issue #43 after explicit approval.
15. Preserve V3 implementation and selectively integrate useful `main` evidence.
16. Run the final suite and deployment smoke checks on the reconciliation commit.
17. Obtain final team sign-off, merge to `main`, create the release tag and retain the final submission package.

## 9. Conditional merge outcome table

This table records actual GitHub state only. The word `Pending` must not be replaced by `Approved` until a real review exists.

| PR | Review | Merge readiness | Current note |
|---|---|---|---|
| #35 | Pending | Blocked | Canonical test scope unresolved. |
| #44 | Pending | Not ready | Owner confirmation required. |
| #46 | Pending | Prepared | Requires final reference refresh after package changes. |
| #47 | Pending | Blocked | US-09 decision unresolved. |
| #48 | Pending | Prepared as template | Execution results remain separate. |
| #50 | Pending | Prepared | Review intentionally deferred. |
| #52 | Pending | Prepared | Component-owner confirmation required. |
| #54 | Pending | Prepared | Component-history confirmation required. |
| #58 | Pending | Prepared | Toolchain-owner confirmation required. |

## 10. Project completion definition

The coordinator's responsibility is complete only when:

- the required reviews are actually recorded;
- approved coordinator-owned PRs are merged;
- technical blockers have owner-supported outcomes;
- the final test suite passes or has a formally approved and documented scope;
- database, deployment, E2E and acceptance evidence is retained;
- branch reconciliation preserves current V3 work;
- README, traceability, status and acceptance records agree;
- the release is merged to `main`, tagged and packaged;
- open Issues accurately represent any accepted post-release limitations.

## 11. Non-authorization statement

This package does not authorize fabricated approvals, edits to teammate-owned implementation, hidden test failures, unexecuted verification claims, automatic batch merge, creation of the reconciliation branch or merge to `main`.