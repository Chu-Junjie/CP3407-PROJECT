# V3 Release Documentation Consistency Audit

**Project:** Smart Digital Product Recommendation Platform  
**Audit date:** 6 August 2026  
**Coordinator:** Chu Junjie  
**Audited baseline:** `feature/product-database`  
**Audit branch:** `docs/junjie-v3-release-audit`  
**Related tracking:** Issue #38

## 1. Purpose

This document records inconsistencies, stale statements and missing evidence links across the current release documentation. It is an audit record only.

It does not rewrite the README, change technical implementation, alter test scope, change datasets or claim that any unresolved release gate has passed. Each correction must be made by the appropriate document or component owner through a reviewed Pull Request.

## 2. Evidence boundary

The audit distinguishes four evidence levels:

| Evidence level | Meaning |
|---|---|
| Historical | Earlier iteration or v2 information retained for project history and clearly labelled as historical. |
| Implemented | Code, data or documentation exists on the authoritative branch, but applicable review or verification remains open. |
| Verified | A named check passed for a named commit and environment. |
| Done | Every applicable Definition of Done and release gate has passed. |

A passing subset of tests is not a passing complete suite. A prepared acceptance template is not an executed acceptance result. A deployment instruction is not deployment or persistence evidence.

## 3. Current evidence snapshot

The following facts are supported by retained GitHub evidence at the time of this audit:

- PR #33 was reviewed and merged into `feature/product-database` as merge commit `07f3672a12722b9038c6d1b64a72ab68e696b091`.
- PR #35 adds the proposed GitHub Actions workflow and remains Draft pending backend/test-owner review.
- PR #35 workflow run `31082762154` collected 12 V3 API tests from `test_server.py`; all 12 passed on Python 3.11.15 and the tracked-file integrity check passed.
- The same workflow collected 18 repository tests; 12 passed and 6 legacy `test_mock.py` tests failed. The complete repository suite is therefore Blocked, not Verified.
- PR #37 prepares E2E and external-UAT templates and remains Draft. No browser, deployment, PostgreSQL persistence or external-participant result is claimed.
- US-09 Budget Alternatives remains `Scope confirmation required` in the v3 traceability baseline.

## 4. Audit summary

| Severity | Count | Meaning |
|---|---:|---|
| High | 5 | Could cause an incorrect completion, testing, scope or release claim. |
| Medium | 6 | Could confuse reviewers or make current and historical information difficult to distinguish. |
| Low | 2 | Administrative metadata or navigation should be refreshed. |

No finding in this audit authorizes Junjie to modify teammate-owned implementation or technical explanations.

## 5. Detailed findings

### DOC-A01 — README test command implies a complete runnable suite

**Severity:** High  
**Affected file:** `README.md`  
**Current statement:** The local-run section directs readers to install `requirements.txt` and run `.venv/bin/pytest -q`.  
**Observed conflict:** `requirements.txt` does not currently include pytest, and the first complete CI audit collected 18 tests with 12 passed and 6 failed. Only `test_server.py` has current green CI evidence.

**Risk:** A reader may reasonably interpret the documented command as an expected green release check.

**Required correction:**

- document the test dependency installation path;
- distinguish the V3 API subset command from the complete repository audit command;
- state the current legacy-test blocker until the owner resolves, archives or formally excludes `test_mock.py`;
- do not describe the complete suite as passing before a successful run exists.

**Owner:** Zaikun confirms final test scope; Junjie coordinates documentation wording; README change requires review.  
**Status:** Open — blocked by Issue #34 and PR #35 review.

### DOC-A02 — README mixes current V3 content with unlabeled historical iteration claims

**Severity:** High  
**Affected file:** `README.md`  
**Observed conflict:** The README begins with the V3 SQLAlchemy/PostgreSQL/11,000-product baseline, then continues into early iteration sections that state all planned work was completed, merged into `main`, and carried no technical debt.

**Risk:** Assessors may interpret historical sprint claims as the current release state, even though the authoritative baseline remains `feature/product-database` and current verification, deployment and acceptance blockers are recorded.

**Required correction:**

- add a clear historical-record boundary before the older iteration narrative;
- identify which statements describe Iteration 1/2 evidence rather than the current V3 release;
- remove or qualify absolute current-sounding claims such as no unfinished work or no technical debt;
- link readers to `docs/project-status.md` and `docs/requirements-traceability.md` for current status.

**Owner:** Junjie coordinates structure; each component owner reviews technical statements about their work.  
**Status:** Open.

### DOC-A03 — README User Story statuses conflict with V3 traceability

**Severity:** High  
**Affected file:** `README.md`  
**Observed conflict:** Older README tables mark US-01 through US-06 as Done and US-07 through US-10 as In-Progress. The V3 traceability matrix instead distinguishes Implemented, Candidate and Scope confirmation required. In particular, US-09 is not confirmed as retained scope.

**Risk:** Two public status sources report different project states and use incompatible status vocabularies.

**Required correction:**

- use the V3 status vocabulary for any current status table;
- retain older sprint statuses only inside a clearly labelled historical section;
- record US-09 as awaiting a retain/revise/defer decision until the team confirms scope;
- avoid equating implementation presence with Done.

**Owner:** Junjie coordinates status consistency; Zaikun and Guanyu confirm US-09 scope/implementation impact.  
**Status:** Open — US-09 decision pending.

### DOC-A04 — Governance documents still say PR #33 review and merge are pending

**Severity:** Medium  
**Affected files:** `docs/project-status.md`, `docs/requirements-traceability.md`, `docs/v3-execution-plan.md`  
**Observed conflict:** These documents were authored before PR #33 completed and retain statements such as governance review/merge not yet evidenced and tasks to create/merge the governance PR.

**Risk:** Current coordination progress is understated and reviewers cannot tell which governance gate has already passed.

**Required correction:**

- record PR #33 and merge commit `07f3672a12722b9038c6d1b64a72ab68e696b091`;
- mark only the governance-document review/merge tasks complete;
- do not imply that merging governance documents verified the technical baseline or merged V3 into `main`;
- keep final integration, deployment, CI and acceptance gates open.

**Owner:** Junjie.  
**Status:** Open.

### DOC-A05 — Project status says no GitHub Actions evidence exists

**Severity:** High  
**Affected files:** `docs/project-status.md`, `docs/requirements-traceability.md`, `docs/v3-execution-plan.md`  
**Observed conflict:** The documents state that no successful GitHub Actions workflow is retained and that the recorded 12 passes are local-only. PR #35 now provides partial CI evidence: the V3 API subset passed, while the full repository audit failed because of six legacy mock tests.

**Risk:** Documentation may either omit useful verified evidence or later be over-corrected into a false full-suite success claim.

**Required correction:**

- record the successful `test_server.py` CI job as Verified for the tested PR merge ref only;
- record the full repository audit as Blocked with 18 collected, 12 passed and 6 failed;
- retain the distinction between workflow existence, subset success and release-commit full-suite success;
- do not check the V3-4 exit gate until the intended complete suite passes for the release commit.

**Owner:** Junjie records evidence; Zaikun decides legacy test disposition.  
**Status:** Open — awaiting PR #35 review and owner decision.

### DOC-A06 — README live-demo label does not identify the demonstrated baseline

**Severity:** Medium  
**Affected file:** `README.md`  
**Current label:** `Live Demo: ... Iteration 1 Platform`  
**Observed gap:** The README also describes V3 capabilities, but the link label does not state whether the deployed page and API currently demonstrate Iteration 1 or the V3 baseline.

**Risk:** Reviewers may test the link expecting V3 features and treat an older deployment as current release evidence.

**Required correction:**

- identify the exact frontend and API environment represented by the link;
- state the deployed commit or release candidate where available;
- label an older deployment as historical;
- do not describe the link as V3 deployment evidence until the E2E matrix is executed.

**Owner:** Guanyu confirms frontend deployment; Zaikun/Yuyang confirm API/database environment; Junjie records evidence.  
**Status:** Open — deployed E2E not yet run.

### DOC-A07 — README technology and feature descriptions are newer than the later architecture narrative

**Severity:** Medium  
**Affected file:** `README.md`  
**Observed conflict:** The current-version section names SQLAlchemy, JWT accounts, favorites, private history, pagination and PostgreSQL, while later historical architecture and narrative sections describe the earlier CSV/Top-5-oriented design.

**Risk:** Readers cannot determine which architecture is current and which diagrams or descriptions are historical.

**Required correction:**

- label older architecture diagrams and explanations as historical or replace them through an owner-reviewed architecture update;
- ensure current architecture shows GitHub Pages, Render Flask/SQLAlchemy, SQLite demonstration and PostgreSQL production persistence;
- include current user-owned tables and authentication/privacy boundaries;
- require technical owners to review their components.

**Owner:** All technical owners; Junjie coordinates consolidation.  
**Status:** Open.

### DOC-A08 — Current status documents omit pending acceptance-template PR #37

**Severity:** Low  
**Affected files:** `docs/project-status.md`, `docs/v3-execution-plan.md`  
**Observed gap:** V3-3/V3-5 work has progressed from no prepared record to a Draft PR containing E2E and two-participant UAT templates.

**Required correction:**

- record PR #37 as prepared evidence design, not executed acceptance;
- keep V3-3 verification and V3-5 external acceptance incomplete;
- after review/merge, link the templates from the execution plan and release checklist.

**Owner:** Junjie.  
**Status:** Open — PR #37 awaiting review.

### DOC-A09 — Status metadata still points to completed temporary governance work

**Severity:** Low  
**Affected files:** V3 governance documents  
**Observed gap:** Headers continue to identify `docs/junjie-v3-governance` as the active governance working branch after its contents were merged through PR #33.

**Required correction:**

- replace active-working-branch wording with a historical merge reference where appropriate;
- keep `feature/product-database` as the authoritative current baseline;
- identify new evidence branches only in their specific records.

**Owner:** Junjie.  
**Status:** Open.

### DOC-A10 — Release checklist is correct as a template but has no populated release-candidate record

**Severity:** Medium  
**Affected file:** `docs/final-acceptance-and-release-checklist.md`  
**Observed state:** The checklist correctly leaves release branch, SHA, URLs, counts, reviewers and test results blank.

**Risk:** Blank fields could later be mistaken for completed checks if the document is presented without a release status statement.

**Required correction:**

- keep unchecked items unchanged until evidence exists;
- add a release-candidate execution record only after a candidate SHA is frozen;
- link CI, E2E, UAT, deployment, database and review evidence to the completed fields;
- never pre-check items based on implementation presence.

**Owner:** Junjie coordinates; all owners supply evidence.  
**Status:** Correctly pending; no immediate checklist rewrite required.

### DOC-A11 — Current status overstates the age of some blockers after governance merge

**Severity:** Medium  
**Affected file:** `docs/project-status.md`  
**Observed conflict:** The blocker list includes replacement of outdated project-status, traceability and Definition of Done documents, although those replacement documents were merged in PR #33. Other blockers—full-suite CI, deployment, E2E, UAT and release artifacts—remain valid.

**Required correction:**

- close the completed replacement-documents blocker;
- replace it with this cross-document consistency audit and subsequent owner-reviewed corrections;
- keep technical verification blockers open.

**Owner:** Junjie.  
**Status:** Open.

### DOC-A12 — Current test documentation does not yet name the final intended suite

**Severity:** High  
**Affected files:** `README.md`, `docs/requirements-traceability.md`, `docs/v3-execution-plan.md`, `docs/final-acceptance-and-release-checklist.md`  
**Observed gap:** Documents correctly require an owner decision on `test_mock.py`, but no final decision exists. Therefore no document can yet state the final collected test count or final passing command.

**Required correction:**

- retain `Blocked` until Zaikun records update/archive/exclusion reasoning;
- after the decision, define one canonical release test command and expected collected files;
- preserve legacy tests as historical evidence if archived rather than silently deleting their history;
- require a successful clean-environment/CI run for the chosen release suite.

**Owner:** Zaikun; Junjie tracks evidence.  
**Status:** Blocked by Issue #34.

### DOC-A13 — Documentation does not yet distinguish release-ready dependency files

**Severity:** Medium  
**Affected files:** `README.md`, dependency documentation  
**Observed gap:** Runtime dependencies are listed in `requirements.txt`, while pytest was installed separately in PR #35. The repository does not yet document whether test dependencies belong in `requirements.txt`, a separate development requirements file or a documented CI-only command.

**Required correction:**

- technical owner selects and documents the dependency strategy;
- local and CI instructions use the same supported strategy;
- production runtime installation should not be changed by the coordinator without owner review.

**Owner:** Zaikun/test owner.  
**Status:** Open.

## 6. Correction order

Corrections should be applied in this order to avoid rewriting documents against unresolved decisions:

1. Zaikun decides the final `test_mock.py` disposition and canonical test command in Issue #34.
2. Team confirms whether US-09 is retained, revised or deferred.
3. PR #35 is reviewed; CI evidence wording is finalized without hiding the full-suite failure.
4. PR #37 is reviewed; templates are merged as preparation only.
5. Component owners confirm deployed frontend/API/database identity and architecture wording.
6. Junjie creates a separate documentation-correction branch from the then-latest baseline.
7. README and governance documents are updated through owner-reviewed commits.
8. Release checklist fields are populated only for a frozen release candidate with actual evidence.

## 7. Proposed correction ownership matrix

| Document area | Coordinator action | Required owner confirmation |
|---|---|---|
| README current/historical structure | Propose structure and status links | All owners confirm technical sections |
| Test commands and dependencies | Record approved command/evidence | Zaikun |
| US-09 status | Record team decision | Zaikun + Guanyu; team approval |
| Deployment/live-demo identity | Record URLs, commit and environment | Guanyu + Zaikun + Yuyang |
| PostgreSQL/persistence wording | Record retained evidence | Yuyang + Zaikun |
| Architecture and API narrative | Coordinate consistency | Relevant technical owner |
| E2E/UAT links and status | Record preparation/execution separately | Guanyu/Yuyang/Zaikun review applicable fields |
| Release checklist completion | Populate evidence fields | All relevant owners/reviewers |

## 8. Exit criteria for this audit

This audit may be closed only when:

- [ ] findings are acknowledged or corrected through reviewed Pull Requests;
- [ ] README clearly separates current V3 information from historical iteration records;
- [ ] US-09 has an approved scope decision;
- [ ] the canonical release test command and intended suite are documented;
- [ ] partial CI evidence and the full-suite blocker are reported accurately;
- [ ] governance documents record PR #33 as merged without implying technical verification;
- [ ] pending PR #37 is described as evidence preparation until actual tests run;
- [ ] current deployment links identify the demonstrated environment;
- [ ] no technical-owner explanation is changed without that owner's review;
- [ ] the final release checklist remains evidence-based and unprechecked.

## 9. Current audit conclusion

The V3 direction is documented, and governance PR #33 is merged. However, the public README and several governance status sections do not yet reflect the latest governance merge and partial CI evidence. The largest release-documentation risks are the implied complete pytest command, mixed historical/current status claims, unresolved US-09 scope, and the absence of a final test-suite decision.

The documentation set is therefore **In Progress**, not release-ready. The next correction PR must wait for owner decisions where the wording depends on test scope, US-09 or deployed-environment identity. This audit itself changes no teammate-owned implementation or technical explanation.