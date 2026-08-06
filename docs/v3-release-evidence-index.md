# V3 Release Evidence Index

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Recorded:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Known branch head at preparation time:** `7c406515bd4b657372fe519869596825cdf91d56`  
**Tracking Issue:** #45

## 1. Purpose

This document provides one review index for the current V3 release evidence. It points to the Issue, Pull Request, commit, test or execution record that supports each project statement.

It does not replace the detailed evidence records and does not convert prepared work into executed verification.

## 2. Evidence vocabulary

| Status | Meaning |
|---|---|
| `Prepared` | A reviewed or reviewable template, plan, checklist or audit exists, but the associated technical activity may not have been executed. |
| `Implemented` | The relevant code, data or document exists on the V3 branch, but applicable verification remains incomplete. |
| `Verified` | A named check passed for a named commit or Pull Request ref in a named environment, with retained evidence. |
| `Blocked` | A known unresolved decision, failure or missing dependency prevents completion. |
| `Not Run` | The required test or acceptance scenario has not been executed. |
| `Unverified` | A value or environment is inferred from repository configuration or implementation but has not been confirmed in the target environment. |
| `Done` | Every applicable Definition of Done and release gate has passed. No V3 release item should use this status merely because implementation exists. |

## 3. Current baseline

| Item | Recorded state | Evidence boundary |
|---|---|---|
| V3 implementation baseline | `feature/product-database` at known head `7c406515bd4b657372fe519869596825cdf91d56` | This is the current working baseline, not evidence that the same commit is deployed. |
| `main` relationship | Diverged from V3 at the recorded comparison | Issue #43 and Draft PR #44 plan reconciliation. No branch merge is authorized by this index. |
| V3 product catalogue | `Implemented` | The V3 branch contains the catalogue/importer direction, but release counts, provenance and PostgreSQL persistence require Issue #41 evidence. |
| V3 API and account functionality | `Implemented` with a verified test subset | The current `test_server.py` subset passed in PR #35 CI evidence; the complete repository suite remains blocked. |
| V3 frontend flows | `Implemented` on the V3 branch | The deployed frontend identity and browser E2E remain unverified under Issue #42. |

## 4. Governance and preparation evidence

| Area | Source | Status | What the evidence supports | What it does not support |
|---|---|---|---|---|
| V3 governance baseline | PR #33, merged as `07f3672a12722b9038c6d1b64a72ab68e696b091` | `Prepared` and merged | Current project status structure, traceability vocabulary, Definition of Done, execution plan and release checklist. | Technical verification, deployment, final acceptance or merge to `main`. |
| E2E and external UAT design | PR #37, merged as `183d50bb254059cda0709b6d648e1a7910d38167` | `Prepared` and merged | Repeatable E2E and two-participant UAT templates with evidence rules. | Any browser scenario, participant task or persistence check passing. |
| Release-documentation audit | PR #39, merged as `7c406515bd4b657372fe519869596825cdf91d56` | `Prepared` and merged | Thirteen documented consistency findings and correction order. | Correction of every finding or release readiness. |
| Branch reconciliation plan | Issue #43 / Draft PR #44 | `Prepared`, pending review | File-level integration principles and owner boundaries. | Selection of teammate-owned conflict resolutions or merge to `main`. |
| Release evidence index | Issue #45 / this Draft PR | `Prepared`, pending review | One coordinated map of evidence, blockers and reviewer responsibilities. | Changing any existing technical status or closing any blocker. |

## 5. Automated test and CI evidence

| Check | Source | Result | Status | Required next evidence |
|---|---|---:|---|---|
| V3 API test collection and execution | Issue #34 / PR #35, workflow run `31082762154` | `12 collected`, `12 passed` on Python 3.11.15 | `Verified` for the tested PR merge ref only | Re-run the agreed final suite for the eventual release commit. |
| Complete repository audit | Same workflow | `18 collected`, `12 passed`, `6 failed` | `Blocked` | Zaikun decides whether `test_mock.py` is updated, archived or formally excluded, and records the canonical command. |
| Tracked-file integrity after CI tests | Same workflow | `git diff --exit-code` passed | `Verified` for the tested PR ref | Repeat for the final release test run. |
| CI workflow adoption | Draft PR #35 | Workflow exists on a Draft branch | `Prepared` | Backend/test-owner review, final suite decision and non-author approval before merge. |
| Final release-commit CI | No retained result | Not executed | `Not Run` | Successful clean-environment run for the frozen release candidate. |

### Test evidence restriction

The passing `test_server.py` subset must not be described as a passing complete repository suite. PR #35 must remain Draft while the final test scope is unresolved.

## 6. User Story scope evidence

| Area | Source | Current status | Owner input required |
|---|---|---|---|
| US-09 Budget Alternatives | Issue #40 | `Scope confirmation required` / `Blocked` | Zaikun records algorithm/API/test impact; Guanyu records UI/E2E impact; the team selects retain, revise or defer. |
| Other V3 stories | `docs/requirements-traceability.md` | Use the current traceability status, not historical README labels | Each technical owner confirms implementation and verification statements affecting their component. |

Until Issue #40 is resolved, US-09 must not be marked `Done`, `Verified` or a confirmed V3 release requirement.

## 7. Database, catalogue and PostgreSQL evidence

| Area | Current state | Source | Required next evidence |
|---|---|---|---|
| Yuyang's V3 database, catalogue and importer work | `Implemented` on `feature/product-database` | Issue #41 and Issue #43 ownership record | Exact tested commit, environment and retained query outputs. |
| `products = 11,000` | Release verification pending | Issue #41 | Actual database query and output for the tested environment. |
| `product_specs = 2,000` | Release verification pending | Issue #41 | Actual query plus join, missing-link and orphan checks. |
| ProductID uniqueness and referential integrity | `Unverified` for release | Issue #41 | Actual queries and outputs. |
| Importer repeatability | `Not Run` for release evidence | Issue #41 | Two consecutive executions with before/after counts and duplicate checks. |
| Data source, licence and retrieval record | Evidence requested | Issue #41 | Dataset name, licence, retrieval date, `DataSource` retention and limitations. |
| Render PostgreSQL engine | `Unverified` | Issue #41 / Issue #42 | Deployed commit, confirmation that `DATABASE_URL` is configured without exposing secrets, and safe engine evidence. |
| Persistence across restart/redeploy | `Not Run` | Issue #41 | User, Favorite, History and Feedback checks before and after restart or redeploy. |
| Backup and recovery | `Unverified` | Issue #41 | Current backup method, tested or documented recovery steps and rollback plan. |

### Database ownership restriction

This index records that Yuyang's work is already implemented on the V3 branch. It does not ask her to rebuild it. Verification evidence and any data, importer or deployment changes remain under Yuyang's ownership.

## 8. Deployed frontend, API and E2E evidence

| Item | Candidate value | Status | Source / next step |
|---|---|---|---|
| GitHub Pages URL | `https://chu-junjie.github.io/CP3407-PROJECT/` | `Unverified` as V3 identity | Issue #42 requires Guanyu to confirm source branch, folder and deployed commit. |
| Render API URL | `https://cp3407-api.onrender.com` | Candidate endpoint only | Issue #42 and Issue #41 require deployed commit and environment confirmation. |
| Frontend-to-API integration | Repository configuration exists | `Not Run` as deployed E2E | Execute the merged E2E template and retain Network evidence. |
| Authentication and privacy flows | Implemented in V3 | `Not Run` as deployed E2E | Register/login/logout, unauthenticated rejection and safe cross-user isolation checks. |
| Recommendation, Top 5 and pagination | Implemented in V3 | `Not Run` as deployed E2E | Execute against the confirmed deployed commit and API. |
| Compare, favorites and history | Implemented in V3 | `Not Run` as deployed E2E | Execute create/read/restore/delete and privacy scenarios. |
| Feedback and share restoration | Implemented/candidate | `Not Run` as deployed E2E | Execute in a second browser or isolated session without leaking private data. |
| Desktop/mobile/accessibility observations | Template prepared | `Not Run` | Record desktop, mobile, keyboard, focus, labels and zoom observations. |

Repository URLs and API configuration are not deployment verification by themselves. Every Issue #42 scenario remains `Not Run` until executed.

## 9. External acceptance evidence

| Requirement | Current state | Required evidence |
|---|---|---|
| Two non-team participant sessions | Template merged in PR #37 | Two separately identified, non-sensitive participant records using identical task scripts. |
| Independent completion and prompted completion | `Not Run` | Recorded outcome for each task and participant. |
| Confusion, ratings and observed limitations | `Not Run` | Retained notes and limitation/defect decisions. |
| UAT release gate | Open | Explicit accept, block or accepted-limitation decision based on actual sessions. |

The existence of `docs/v3-external-uat-record.md` is preparation evidence only.

## 10. Branch reconciliation and release integration

| Gate | Current status | Source | Completion condition |
|---|---|---|---|
| File-level reconciliation plan | Draft | Issue #43 / PR #44 | All affected owners confirm the proposed source and treatment of overlapping files. |
| Preserve Yuyang V3 work | Required | Issue #43 / PR #44 | V3 database, catalogue and importer remain authoritative unless Yuyang approves otherwise. |
| Preserve useful `main` evidence | Planned | Issue #43 / PR #44 | Historical evidence is selected without restoring obsolete implementation or status claims. |
| Reconciliation branch | Not created | Issue #43 | Explicit approval after the plan is reviewed. |
| Reconciliation PR | Not created | Issue #43 | Owner-controlled conflict resolution, complete tests and required verification. |
| Merge to `main` | Blocked | Issue #43 and release checklist | All technical, deployment, acceptance and review gates have actual evidence. |

## 11. Current blocker register

| Blocker | Owner(s) | Current next action |
|---|---|---|
| Final test scope and legacy `test_mock.py` | Zaikun; Junjie tracks | Record the owner decision in Issue #34 and review PR #35. |
| US-09 release scope | Zaikun, Guanyu and Junjie | Select Option A, B or C in Issue #40 with impact and estimate. |
| Database/PostgreSQL release verification | Yuyang; Junjie tracks | Add commands, outputs, environment and persistence evidence to Issue #41. |
| Deployed V3 identity and E2E | Guanyu plus relevant API/database owners | Confirm deployed commits/environments, then execute Issue #42. |
| Safe `main`/V3 reconciliation | All affected owners; Junjie coordinates | Review Issue #43 / PR #44 before any integration branch is created. |
| External UAT | Junjie coordinates; two non-team participants | Execute the merged participant template after the deployed candidate is stable. |

## 12. Final coordinated reviewer matrix

| Reviewer | Required review scope |
|---|---|
| Guanyu (`Guanyu-Lu`) | Frontend ownership, deployed GitHub Pages identity, current/historical UI wording, US-09 presentation, responsive/accessibility and E2E scenarios. |
| Zaikun (`ZhengZaikun`) | Backend/API/authentication/privacy wording, CI workflow, final test scope, `test_mock.py`, dependencies and US-09 algorithm/API impact. |
| Yuyang (`tiantian09091`) | V3 catalogue/database/importer preservation, counts and joins, provenance, PostgreSQL identity, persistence, backup and recovery wording. |
| Junjie (`Chu-Junjie`) | Governance consistency, Issue/PR links, evidence status, schedule, review completion and release-gate decisions. |

A reviewer should not be asked to approve another owner's technical implementation on that owner's behalf. Final review should confirm both the shared release package and each reviewer's own component statements.

## 13. Planned review-package sequence

1. Keep PR #35 and PR #44 as Draft.
2. Prepare the remaining coordinator-owned evidence and decision-record Draft PRs.
3. Record owner responses in Issues #34, #40, #41 and #42 without fabricating missing results.
4. Update Draft documents only where owner evidence supports the change.
5. Request Guanyu, Zaikun and Yuyang together for the coordinated review package.
6. Resolve comments and obtain at least one non-author approval for each PR.
7. Merge approved documentation and workflow PRs into `feature/product-database`, not directly into `main`.
8. Freeze a release-candidate commit only after the final test scope and US-09 scope are resolved.
9. Execute release-commit CI, deployed E2E, database persistence and external UAT.
10. Create the integration branch and PR only after Issue #43 prerequisites are satisfied.
11. Merge to `main` only when the final acceptance and release checklist is supported by retained evidence.

## 14. Non-authorization statement

This index does not authorize:

- modifying teammate-owned backend, frontend, tests, datasets, database files, importers or deployment settings;
- selecting a conflict resolution for a component owner;
- changing README or User Story statuses before the associated decision;
- marking a test, deployment, persistence or acceptance scenario as passed without execution;
- merging a Draft PR;
- creating the reconciliation branch;
- merging `feature/product-database` into `main`.
