# V3 and `main` Reconciliation Plan

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Tracking:** Issue #43  
**Working branch:** `docs/junjie-v3-reconciliation-plan`  
**Target review base:** `feature/product-database`

## 1. Purpose

This document prepares a file-level plan for safely reconciling `main` with the current V3 baseline.

It is a coordination record only. It does not merge branches, resolve conflicts, select a teammate-owned implementation, change release status or claim that any test, deployment, database or acceptance gate has passed.

## 2. Recorded comparison snapshot

At the time this plan was prepared:

- V3 baseline: `feature/product-database`
- V3 head: `7c406515bd4b657372fe519869596825cdf91d56`
- `main` head: `d8f2d3a3f4d0ff6df1be4a1e813f0451c50073b0`
- merge base: `1c5696fe36a0d6ee4ca875267fa02e0278a51831`
- branch state: `diverged`
- V3 was 13 commits ahead of and 22 commits behind `main`

These values are a planning snapshot. They must be regenerated immediately before any reconciliation branch is created.

## 3. Reconciliation principle

Use `feature/product-database` as the V3 implementation baseline.

Selectively preserve valid records that exist only on `main`, especially historical Task 3 evidence, without restoring obsolete implementation or obsolete completion claims.

The following actions are prohibited until the corresponding owners approve them:

- choosing a backend or test version on behalf of Zaikun;
- choosing a frontend version on behalf of Guanyu;
- choosing a dataset, database, importer or PostgreSQL version on behalf of Yuyang;
- merging either full branch into the other;
- marking any unresolved release gate as Passed, Verified or Done.

## 4. Confirmed ownership boundaries

| Area | Owner | Coordinator boundary |
|---|---|---|
| Backend, API, recommendation logic and automated tests | Zaikun (`ZhengZaikun`) | Junjie inventories differences and records decisions; Zaikun selects or changes implementation. |
| Frontend and deployed UI behaviour | Guanyu (`Guanyu-Lu`) | Junjie inventories differences and records decisions; Guanyu selects or changes implementation. |
| Dataset, catalogue, database, importer, provenance and PostgreSQL verification | Yuyang (`tiantian09091`) | Junjie preserves the V3 baseline and records evidence; Yuyang confirms technical choices. |
| Governance, scheduling, evidence index and release coordination | Junjie (`Chu-Junjie`) | Junjie may prepare documentation changes, subject to team review. |

## 5. File-level reconciliation matrix

### 5.1 V3 implementation and data baseline

| Path or area | Proposed source | Owner confirmation | Current planning status | Reason |
|---|---|---|---|---|
| `import_real_catalog.py` | `feature/product-database` | Yuyang | Preserve V3 | Yuyang's completed V3 importer is already on the V3 branch and is not missing development work. |
| `real_product_catalog.csv` | `feature/product-database` | Yuyang | Preserve V3 | Current V3 catalogue source used for the expanded product baseline. |
| `product_specs.csv` | `feature/product-database` unless Yuyang identifies a later valid correction | Yuyang | Owner confirmation required before integration | Both branch histories contain related specification records; the V3 version must not be overwritten by an older copy. |
| Catalogue/database schema and SQLAlchemy/PostgreSQL integration | `feature/product-database` | Yuyang + Zaikun where backend code overlaps | Preserve V3 architecture; verification still open | The V3 branch is the authoritative technical baseline, while Issue #41 tracks release evidence. |
| `digital_products.db` | Do not select by automatic merge | Yuyang | Special handling required | It is a binary tracked database and may contain test-generated changes. Counts and provenance must be verified rather than inferred from the file timestamp. |
| `server.py` | No automatic choice | Zaikun | Technical-owner decision required | Both branches contain backend changes. The V3 SQLAlchemy/JWT/history/favorites/pagination contract must not be replaced by older implementation, but valid later fixes on `main` must be reviewed. |
| `test_server.py` | No automatic choice | Zaikun | Technical-owner decision required | V3 currently has 12 passing API tests in PR #35 evidence; `main` also retains historical Task 3 test work. |
| `test_mock.py` | Remains unresolved under Issue #34 | Zaikun | Blocked | The six legacy tests fail against the V3 contract. They must be updated, archived or formally excluded with recorded reasoning. |
| `requirements.txt` | No automatic choice | Zaikun | Technical-owner decision required | Runtime and test dependency strategy must be consistent across local instructions, CI and deployment. |
| `index.html` | No automatic choice | Guanyu | Technical-owner decision required | Both branches contain frontend changes. V3 account, favorites, history, pagination, comparison, feedback and share flows must be preserved where implemented. |
| `api-contract.md` | V3 baseline, subject to Zaikun review | Zaikun | Review required | Contract wording must match the final backend and deployed API. |

### 5.2 V3 governance and acceptance records

| Path | Proposed source | Owner/reviewer | Status | Reason |
|---|---|---|---|---|
| `docs/definition-of-done.md` | Reconcile from V3, then review valid `main`-only Task 3 evidence references | Junjie; technical owners review their sections | Documentation reconciliation required | V3 contains the current release vocabulary; `main` may contain later historical evidence additions. |
| `docs/project-status.md` | Reconcile from V3, then add only verified later events | Junjie; all owners review technical status | Documentation reconciliation required | Current status must distinguish Implemented, Verified, Blocked and Done. |
| `docs/requirements-traceability.md` | Reconcile from V3, then add only verified later evidence | Junjie; story owners review | Documentation reconciliation required | US-09 remains unresolved under Issue #40. |
| `docs/v3-execution-plan.md` | V3 | Junjie | Preserve V3 and refresh later | Current execution sequence and release gates are defined here. |
| `docs/final-acceptance-and-release-checklist.md` | V3 | Junjie + all evidence owners | Preserve unchecked template | Fields must not be populated before a frozen release candidate has actual evidence. |
| `docs/v3-e2e-acceptance-evidence.md` | V3 | Junjie + Guanyu | Preserve V3 | Template is merged preparation; execution remains under Issue #42. |
| `docs/v3-external-uat-record.md` | V3 | Junjie | Preserve V3 | Template is not an executed UAT result. |
| `docs/v3-release-documentation-audit.md` | V3 | Junjie | Preserve V3 | Records documentation inconsistencies and correction order. |

### 5.3 `main`-only historical evidence for selective preservation

The following categories should be retained as historical evidence where valid, without restoring obsolete implementation:

| `main`-only area | Proposed treatment | Owner/reviewer | Notes |
|---|---|---|---|
| `docs/evidence/task3-*` command, install, compile, collection and test logs | Preserve in an explicitly historical evidence area | Junjie coordinates; Zaikun validates technical interpretation | Keep exact commands/results and failure history. Do not present older results as V3 release evidence. |
| `docs/evidence/task3-database-side-effect-*` | Preserve as historical side-effect evidence | Junjie + Yuyang/Zaikun review | Useful for explaining why tracked SQLite files require careful restoration and isolation. |
| `docs/task3-backend-ci-evidence.md` | Preserve or adapt as historical Task 3 evidence | Junjie + Zaikun | Must remain clearly separated from current PR #35 CI evidence. |
| `docs/task2-database-evidence.md` | Preserve as historical evidence if Yuyang confirms accuracy | Yuyang | Do not use it as a substitute for Issue #41 V3/PostgreSQL verification. |
| `docs/frontend_task2_field_confirmation.md` | Preserve as historical frontend evidence if Guanyu confirms usefulness | Guanyu | Do not treat it as current deployed V3 acceptance. |
| `docs/issue-drafts/task3-*` | Retain only if still useful as historical drafts or convert to links to active Issues | Junjie + Zaikun | Avoid duplicating or contradicting active Issue #34. |
| Later status additions on `main` | Extract verified facts only | Junjie + affected owner | Do not copy obsolete status wording wholesale. |

## 6. Conflict classes

### Class A — Preserve V3 by default

Applies to completed V3 assets that do not have an owner-confirmed later correction:

- Yuyang's V3 importer and catalogue;
- V3 acceptance and release-governance documents;
- current V3 product/API/data architecture as a baseline.

### Class B — Preserve `main` evidence only

Applies to logs and records that document earlier work but should not replace current implementation:

- Task 3 command logs;
- historical dependency installation and compile evidence;
- historical failed-suite and database-side-effect evidence.

### Class C — Owner-controlled technical conflict

Requires the component owner to provide the final selection or owner-controlled commit:

- `server.py`;
- `test_server.py` and `test_mock.py`;
- `requirements.txt`;
- `index.html`;
- overlapping database/specification files or configuration.

### Class D — Coordinator-owned documentation reconciliation

Junjie may prepare changes on a documentation-only branch, but technical claims remain subject to owner review:

- project status;
- requirements traceability;
- Definition of Done;
- release evidence index;
- reconciliation and release plans.

## 7. Required owner decisions before implementation

### Yuyang

- confirm the V3 catalogue/specification/importer files that must be preserved;
- identify any valid `main`-only data or database evidence to retain;
- confirm handling of the tracked SQLite database;
- provide Issue #41 verification evidence when available.

### Zaikun

- decide the final `test_mock.py` disposition and canonical complete test command;
- identify valid `main`-only backend fixes, if any;
- confirm final `server.py`, `test_server.py` and dependency strategy;
- review CI workflow PR #35.

### Guanyu

- identify valid `main`-only frontend changes, if any;
- confirm the V3 frontend version and deployment identity;
- review the final `index.html` integration choice;
- participate in Issue #42 deployed E2E execution.

### Junjie

- keep all unresolved gates visible;
- prepare the evidence and documentation inventory;
- avoid selecting teammate-owned implementation;
- create the final review package only after owner inputs are recorded.

## 8. Proposed integration sequence

1. Keep PR #35 Draft until Zaikun records the final test-scope decision.
2. Resolve or formally defer US-09 through Issue #40.
3. Obtain Issue #41 database/PostgreSQL verification evidence.
4. Confirm the deployed frontend/API identity and execute Issue #42.
5. Refresh the two-branch comparison and file inventory.
6. Obtain written file-level decisions from all three technical owners.
7. Create one separately approved reconciliation branch from the latest V3 baseline.
8. Bring in `main`-only historical evidence without restoring obsolete implementation.
9. Apply owner-controlled technical resolutions.
10. Run the canonical complete test suite and database verification.
11. Open a reconciliation PR for all affected owners and at least one non-author reviewer.
12. Merge to `main` only after every applicable release gate has actual evidence.

## 9. Review package policy

Draft Issues and Draft PRs may be prepared before the final group review so that owners can review one coordinated package later.

Until the review package is ready:

- do not merge Draft PRs;
- do not request a false approval on incomplete evidence;
- do not mark unresolved scenarios Passed;
- record each PR's dependency on Issues #34, #40, #41, #42 and #43 where applicable;
- keep teammate-owned implementation unchanged unless the owner supplies or explicitly approves the change.

## 10. Current status

- File-level planning: **Prepared for review**
- Reconciliation branch implementation: **Not started**
- Technical conflict resolution: **Not started**
- Complete release test: **Blocked by Issue #34**
- US-09 scope: **Pending Issue #40**
- Database/PostgreSQL verification: **Pending Issue #41**
- Deployed E2E acceptance: **Pending Issue #42**
- Merge to `main`: **Not authorized**

## 11. Completion criteria for this planning document

- [ ] Yuyang confirms the data/database/importer entries.
- [ ] Zaikun confirms the backend/test/dependency entries.
- [ ] Guanyu confirms the frontend entries.
- [ ] Junjie updates the matrix using only recorded owner decisions.
- [ ] The team approves the integration direction.
- [ ] A separate implementation/reconciliation branch is explicitly authorized.

No unchecked item may be inferred as complete from the existence of code or documentation alone.
