# V3 Release Evidence Index

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Meeting and evidence index maintained by:** @Chu-Junjie  
**Status:** Prepared for formal review and release-candidate updates

## 1. Evidence rule

This index links repository evidence and team meeting notes. Meeting decisions identify scope and responsibilities but do not replace formal GitHub Reviews, executed tests, deployed-environment checks or acceptance outcomes.

## 2. Named responsibilities

| Evidence area | Named confirmation |
|---|---|
| Backend, API, authentication, recommendation, automated tests and CI | @ZhengZaikun |
| Database, catalogue, importer, provenance, PostgreSQL, persistence and recovery | @tiantian09091 |
| Frontend, GitHub Pages, responsive behaviour, accessibility and browser flows | @Guanyu-Lu |
| Meeting notes, status, traceability, evidence links, acceptance coordination and release record | @Chu-Junjie |

## 3. Current indexed records

| ID | Record | Current status | Formal review |
|---|---|---|---|
| GOV-01 | V3 governance baseline, PR #33 | Merged into V3 | Historical approval retained |
| ACC-01 | E2E and external-acceptance templates, PR #37 | Merged preparation; scenarios remain `Not Run` | Historical approval retained |
| DOC-01 | Release documentation audit, PR #39 | Merged audit | Historical approval retained |
| CI-01 | Canonical workflow, Issue #34 / PR #35 | Workflow run `31096706920`: 12/12 passed; final-candidate rerun pending | @ZhengZaikun |
| INT-01 | Reconciliation plan, Issue #43 / PR #44 | Prepared; no reconciliation branch created | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| REL-INDEX | This evidence index, Issue #45 / PR #46 | Prepared | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| SCOPE-09 | US-09 decision, Issue #40 / PR #47 | Deferred / `Unscheduled` | @ZhengZaikun, @Guanyu-Lu |
| DB-PLAN | Database verification record, Issue #41 / PR #48 | Repository verified; runtime gate open | @tiantian09091, @ZhengZaikun |
| CLOSE-01 | Project closeout review record, Issue #49 / PR #50 | Prepared | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| ARCH-01 | V3 design and architecture, Issue #51 / PR #52 | Prepared | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| AGILE-01 | Iteration and retrospective record, Issue #53 / PR #54 | Prepared | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| TOOL-01 | Toolchain and dependencies, Issue #55 / PR #58 | Prepared | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| STATUS-01 | Status, traceability, meeting action plan and release checklist, Issue #59 / PR #60 | Prepared | @ZhengZaikun, @tiantian09091, @Guanyu-Lu |
| E2E-RUN | Deployed E2E execution, Issue #42 | Not Run | @Guanyu-Lu with API/data confirmation from @ZhengZaikun and @tiantian09091 |
| UAT-RUN | Two-participant external acceptance | Not Run | Coordinated by @Chu-Junjie |

## 4. Verified evidence currently available

### Canonical CI

- command: `python -m pytest -q test_server.py`;
- workflow run: `31096706920`;
- Python: 3.11.15;
- pytest: 9.1.1;
- result: 12 collected, 12 passed in 1.23 seconds;
- tracked-file integrity: passed;
- scope: recorded PR merge ref only.

@ZhengZaikun must review PR #35 and rerun the canonical suite for the frozen release candidate.

### Historical test audit

`test_mock.py` remains unchanged as historical V2 compatibility evidence. Its expected failures are visible in a non-blocking job and are not V3 release regressions.

### US-09

The team meeting notes and repository contract record US-09 Budget Alternatives as Deferred with backlog status `Unscheduled`. Current acceptance verifies maximum-budget filtering only. @ZhengZaikun and @Guanyu-Lu must formally review PR #47.

### Database repository inspection

The repository defines:

- SQLAlchemy with SQLite fallback and PostgreSQL through `DATABASE_URL`;
- seven application tables;
- a target of 11,000 products and 2,000 recommendation-ready specifications;
- importer quotas of 800/833/300/61/6;
- provenance and fixed conversion rules;
- importer validation and the restriction against running it on production user data.

@tiantian09091 must provide actual disposable-build and deployed PostgreSQL evidence. @ZhengZaikun must confirm API integration.

## 5. Evidence still required

| Evidence ID | Required result | Named responsibility |
|---|---|---|
| CI-FINAL | Canonical suite and tracked-file integrity for the frozen candidate | @ZhengZaikun |
| DB-LOCAL | Actual counts, distribution, duplicates, joins, orphans and repeatability on a disposable copy | @tiantian09091 |
| DEP-FE | GitHub Pages source and visible frontend commit | @Guanyu-Lu |
| DEP-API | Render API commit, build/start commands and health response | @ZhengZaikun |
| DB-PG | PostgreSQL dialect, tables and deployed counts | @tiantian09091 with API confirmation from @ZhengZaikun |
| PERS-01 | Account, favorite, history, snapshot and feedback persist after restart/redeployment | @tiantian09091 and @ZhengZaikun |
| PRIV-01 | Account B cannot access Account A private records | @ZhengZaikun, with browser confirmation from @Guanyu-Lu |
| E2E-DESK | Critical deployed flow on desktop | @Guanyu-Lu |
| E2E-MOB | Critical deployed flow on mobile | @Guanyu-Lu |
| E2E-A11Y | Keyboard, focus, labels, readable errors and zoom/reflow observations | @Guanyu-Lu |
| UAT-01/02 | Two non-team participant records | @Chu-Junjie |
| INT-FINAL | Approved reconciliation PR to `main` | @Chu-Junjie, with Approvals from @ZhengZaikun, @tiantian09091 and @Guanyu-Lu |
| REL-FINAL | Final `main` SHA, tag, notes, archive and checksum | @Chu-Junjie |

## 6. Status rules

- Do not describe a source-code target as an observed runtime result.
- Do not describe a prepared template as an executed test.
- Do not describe a meeting decision as a formal GitHub Approval.
- Do not combine evidence from different commits or environments without separate records.
- Do not retain passwords, JWTs, cookies, connection strings or unnecessary participant data.
- Every failed or blocked frontend case is assigned to @Guanyu-Lu, backend/API/test case to @ZhengZaikun, and database/PostgreSQL case to @tiantian09091.

## 7. Final release record

The index is complete only when it links:

```text
Final main commit:
Release tag:
Canonical CI:
Catalogue verification:
PostgreSQL identity and counts:
Persistence and privacy:
Desktop/mobile E2E:
External acceptance:
Known limitations:
Release decision:
Final archive:
Checksum:
```

No missing field may be inferred from implementation presence or meeting agreement.