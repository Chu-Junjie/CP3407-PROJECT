# V3 Release Evidence Index

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Recorded:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Known implementation baseline:** `7c406515bd4b657372fe519869596825cdf91d56`  
**Tracking Issue:** #45  
**Current stage:** Documentation package prepared; coordinated review deferred; execution and release gates remain open

## 1. Purpose

This index maps current project statements to their authoritative Issue, Pull Request, commit, test or execution record. It distinguishes implementation, prepared engineering records and executed verification.

The index does not treat a planned or deferred review as an actual approval. It also does not convert a prepared test, database, E2E or acceptance record into a passed result.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| `Prepared` | A reviewable plan, template, checklist, design or operating record exists. |
| `Implemented` | The code, data or document exists on the named branch. |
| `Verified` | A named check passed for a named commit or PR ref in a named environment. |
| `Blocked` | A known decision, failure or dependency prevents completion. |
| `Not Run` | The required execution activity has not occurred. |
| `Unverified` | Repository configuration or implementation suggests a value, but the target environment has not been confirmed. |
| `Pending review` | A real GitHub review has not yet been submitted. |
| `Done` | Every applicable completion and release gate has actual retained evidence. |

## 3. Current project baseline

| Area | Current state | Evidence boundary |
|---|---|---|
| V3 implementation | `Implemented` on `feature/product-database` | The known branch baseline is not proof that the same commit is deployed. |
| `main` relationship | Diverged | Issue #43 / PR #44 plans safe reconciliation; no integration branch exists. |
| Product catalogue and importer | `Implemented` | Yuyang's V3 work exists; release queries, importer repeatability and PostgreSQL persistence remain pending. |
| API and account services | `Implemented` | The 12-test V3 API subset passed on the PR #35 CI ref; the complete suite remains blocked. |
| Frontend V3 flows | `Implemented` on the V3 branch | GitHub Pages identity and deployed E2E remain unverified. |
| Review package | `Prepared`, `Pending review` | PR #50 coordinates later review and conditional closeout; it records no approval. |

## 4. Merged governance and preparation evidence

| Area | Source | Status | Supports | Does not support |
|---|---|---|---|---|
| Governance baseline | PR #33, merge commit `07f3672a12722b9038c6d1b64a72ab68e696b091` | `Prepared` and merged | Status, traceability, Definition of Done, execution and release controls. | Final technical verification or release readiness. |
| E2E and external acceptance templates | PR #37, merge commit `183d50bb254059cda0709b6d648e1a7910d38167` | `Prepared` and merged | Repeatable execution records and evidence rules. | Any browser or participant task passing. |
| Release-documentation audit | PR #39, merge commit `7c406515bd4b657372fe519869596825cdf91d56` | `Prepared` and merged | Known consistency findings and correction priorities. | Completion of all corrections. |

## 5. Current Draft engineering package

| PR | Engineering record | Current state | Main remaining dependency |
|---|---|---|---|
| #35 | CI workflow and test evidence | Draft / Blocked | Final V3 test scope and legacy-test decision. |
| #44 | Safe branch reconciliation plan | Draft / Prepared | Component-owner file-treatment confirmation. |
| #46 | This release evidence index | Draft / Prepared | Final consistency review and later status refresh. |
| #47 | US-09 scope decision record | Draft / Blocked | Owner-supported A/B/C decision. |
| #48 | Database/PostgreSQL verification record | Draft / Prepared template | Owner review, then executed evidence. |
| #50 | Coordinated review and closeout package | Draft / Prepared | Actual later reviews; no approval is currently recorded. |
| #52 | V3 design and architecture reference | Draft / Prepared | Component-owner confirmation and external-artifact links where available. |
| #54 | Agile delivery, demo, feedback and retrospective record | Draft / Prepared | Component-history confirmation and retained evidence. |
| #58 | Development toolchain and dependency reference | Draft / Prepared | Component-owner toolchain confirmation. |

## 6. Automated tests and CI

| Check | Source | Result | Status | Next evidence |
|---|---|---:|---|---|
| V3 API suite | Issue #34 / PR #35, run `31082762154` | `12 collected`, `12 passed` | `Verified` for that PR merge ref | Repeat on the frozen release candidate. |
| Complete repository suite | Same run | `18 collected`, `12 passed`, `6 failed` | `Blocked` | Zaikun records the V3 disposition of `test_mock.py` and canonical command. |
| Tracked-file integrity | Same run | `git diff --exit-code` passed | `Verified` for that PR ref | Repeat for the release candidate. |
| CI workflow adoption | PR #35 | Workflow exists on Draft branch | `Prepared` | Owner decision and actual review before merge. |
| Release-candidate CI | No result | Not executed | `Not Run` | Run the agreed full suite on the frozen candidate. |

The passing subset must not be described as a passing complete repository suite.

## 7. Requirements and scope decisions

| Area | Source | Current state | Completion requirement |
|---|---|---|---|
| US-09 Budget Alternatives | Issue #40 / PR #47 | `Blocked` / scope confirmation required | Zaikun and Guanyu provide component impact; the team records Option A, B or C. |
| Requirements traceability | Merged governance document | Current baseline exists | Refresh after final scope, verification and release outcomes are known. |
| Schedule and iteration evidence | Issue #53 / PR #54 | `Prepared` | Confirm component history; add only retained evidence. |

## 8. Database, catalogue and PostgreSQL

| Area | Current state | Tracking | Required next evidence |
|---|---|---|---|
| Yuyang's V3 database/catalogue/importer | `Implemented` | Issue #41 / PR #48 | Exact tested commit, environment and actual query output. |
| `products = 11,000` | Pending release verification | Issue #41 | Actual query and retained result. |
| `product_specs = 2,000` | Pending release verification | Issue #41 | Actual query, joins, missing-link and orphan checks. |
| ProductID integrity | `Unverified` for release | Issue #41 | Uniqueness and referential-integrity outputs. |
| Importer repeatability | `Not Run` for release | Issue #41 | Consecutive runs, before/after counts and duplicate checks. |
| Provenance and price limitations | Evidence requested | Issue #41 | Dataset, licence, retrieval date, DataSource and historical-price statement. |
| Render PostgreSQL identity | `Unverified` | Issue #41 / #42 | Deployed commit, safe engine evidence and configuration confirmation without secrets. |
| Persistence after restart/redeploy | `Not Run` | Issue #41 | User, Favorite, History and Feedback before/after evidence. |
| Backup, recovery and rollback | `Unverified` | Issue #41 | Current procedure and safe retained evidence. |

Implementation presence is not the same as release verification, and Yuyang is not being asked to rebuild completed V3 work.

## 9. Deployment and E2E

| Item | Candidate value/state | Status | Next action |
|---|---|---|---|
| GitHub Pages | `https://chu-junjie.github.io/CP3407-PROJECT/` | `Unverified` as V3 | Confirm source branch/folder and exact deployed commit. |
| Render API | `https://cp3407-api.onrender.com` | Candidate endpoint only | Confirm deployed commit and environment. |
| Production database | PostgreSQL support exists in code | `Unverified` | Confirm deployed engine safely. |
| Frontend-to-API integration | Repository configuration exists | `Not Run` as release E2E | Execute the Issue #42 matrix. |
| Authentication/privacy | Implemented in V3 | `Not Run` as deployed E2E | Test register/login/logout, rejection and cross-user isolation. |
| Recommendation, Top 5, pagination | Implemented in V3 | `Not Run` as deployed E2E | Execute on the confirmed candidate. |
| Compare, favorites, history | Implemented in V3 | `Not Run` as deployed E2E | Execute create/read/restore/delete flows. |
| Feedback and share | Implemented/candidate | `Not Run` | Execute in isolated browser state and check privacy. |
| Responsive/accessibility | Design and CSS evidence prepared | `Not Run` as acceptance | Record desktop, mobile, keyboard, focus, labels and zoom observations. |

## 10. Design, delivery and toolchain references

| Reference | Source | Current state | Main boundary |
|---|---|---|---|
| Architecture, database and interface design | Issue #51 / PR #52 | `Prepared`, pending review | Describes current implementation; does not verify deployment or PostgreSQL persistence. |
| Agile delivery and retrospective history | Issue #53 / PR #54 | `Prepared`, pending review | Missing historical dates, effort, demonstrations or feedback remain explicitly missing. |
| Development toolchain and dependencies | Issue #55 / PR #58 | `Prepared`, pending review | Commands are operating procedures, not automatic pass claims. |
| Coordinated closeout process | Issue #49 / PR #50 | `Prepared`, pending review | Defines later sequence; records no actual review or merge. |

## 11. External acceptance

| Requirement | Current state | Required evidence |
|---|---|---|
| Stable deployed candidate | Not confirmed | Exact frontend, API and database identities. |
| Non-team participant sessions | `Not Run` | Separate participant records using the same task script. |
| Independent/prompted completion | `Not Run` | Outcome for each task and participant. |
| Confusion, ratings and limitations | `Not Run` | Retained observations and defect/limitation decisions. |
| Acceptance decision | Open | Explicit accept, block or accepted-limitation outcome. |

## 12. Branch reconciliation and release integration

| Gate | Current state | Source | Completion condition |
|---|---|---|---|
| File-level reconciliation plan | `Prepared` Draft | Issue #43 / PR #44 | Owners confirm overlapping-file treatment. |
| Preserve completed V3 data work | Required | PR #44 | Do not replace Yuyang's current V3 database/catalogue/importer with obsolete `main` versions. |
| Preserve useful historical evidence | Planned | PR #44 | Select evidence without restoring obsolete implementation. |
| Reconciliation branch | Not created | Issue #43 | Explicit approval after plan review and technical gates. |
| Reconciliation PR | Not created | Issue #43 | Controlled conflict resolution, tests and verification. |
| Merge to `main` | `Blocked` | Issue #43 and release checklist | Actual review, test, database, deployment, E2E and acceptance evidence. |

## 13. Remaining blocker register

| Blocker | Owner(s) | Coordinator responsibility |
|---|---|---|
| Final suite and legacy `test_mock.py` | Zaikun | Keep evidence accurate and do not hide failures. |
| US-09 release scope | Zaikun, Guanyu and team | Maintain pending status until a supported decision exists. |
| Database/PostgreSQL release verification | Yuyang | Track evidence without editing data, importer or deployment configuration. |
| Deployed V3 identity and E2E | Guanyu plus API/database owners | Keep scenarios `Not Run` until execution. |
| External acceptance | Junjie coordinates | Run only after the candidate is stable. |
| Safe reconciliation | All affected owners; Junjie coordinates | Do not create or merge the branch prematurely. |
| Actual PR reviews | Relevant non-author teammates | Do not infer approval from the user's planning assumption or reviewer silence. |

## 14. Conditional closeout after actual reviews

1. Resolve actual review comments and merge independently approved prepared documents into `feature/product-database`.
2. Resolve Issue #40 before merging the completed US-09 decision record.
3. Resolve Issue #34 before adopting the final CI workflow as release evidence.
4. Freeze a V3 release-candidate commit.
5. Execute the canonical suite, database/PostgreSQL verification, deployed E2E and external acceptance.
6. Update README, project status, requirements traceability and final acceptance records from actual results.
7. Create the Issue #43 reconciliation branch only after explicit approval.
8. Preserve V3 implementation, selectively retain useful `main` evidence and re-run final checks.
9. Obtain final sign-off, merge to `main`, create a release tag and retain the submission package.

## 15. Current completion assessment

| Area | State |
|---|---|
| Coordinator-owned planning and engineering references | Substantially prepared |
| Actual team reviews | Deferred / pending |
| Technical owner decisions | Several pending |
| Release verification | Incomplete |
| Integration to `main` | Not started |
| Project release | Not complete |

## 16. Non-authorization statement

This index does not authorize fabricated approvals, edits to teammate-owned implementation, hidden test failures, unexecuted verification claims, automatic batch merge, creation of the reconciliation branch or merge to `main`.