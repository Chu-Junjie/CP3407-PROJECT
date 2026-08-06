# V3 to Main Reconciliation Plan

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative V3 baseline:** `feature/product-database`  
**Target branch:** `main`  
**Document owner:** Chu Junjie — Project Manager and Release Coordinator  
**Status:** Prepared for formal review; execution begins only after approval and release-candidate verification

## 1. Purpose

This plan defines how the completed V3 implementation will be integrated into `main` without overwriting current backend, frontend, database, catalogue, importer or testing work with older branch content.

The plan separates technical implementation ownership from release coordination. It authorizes no automatic conflict resolution and no direct modification of teammate-owned implementation.

## 2. Branch relationship

Recorded comparison:

| Item | Value |
|---|---|
| `main` commit | `d8f2d3a3f4d0ff6df1be4a1e813f0451c50073b0` |
| V3 baseline commit | `7c406515bd4b657372fe519869596825cdf91d56` |
| Merge base | `1c5696fe36a0d6ee4ca875267fa02e0278a51831` |
| V3 ahead of `main` | 13 commits |
| V3 behind `main` | 22 commits |
| Relationship | Diverged |

The final reconciliation must be based on the then-current reviewed V3 release candidate rather than the recorded baseline commit above.

## 3. Reconciliation principles

1. `feature/product-database` is the authoritative V3 implementation baseline.
2. V3 technical implementation must not be replaced by older `main` versions.
3. Useful `main`-only project evidence may be retained when it does not conflict with V3.
4. Conflicts in teammate-owned files must be resolved by the relevant component owner.
5. Documentation-only changes must not be used to alter technical behaviour.
6. The reconciliation branch must be reviewed and tested before merge to `main`.
7. No release status may be marked complete before actual verification.

## 4. V3 implementation to preserve

The following V3 areas must be retained as the implementation source of truth unless the relevant owner approves a newer technical change.

### Backend and API

- `server.py` V3 Flask and SQLAlchemy implementation;
- JWT registration and login;
- recommendation, pagination and Top 5 response flow;
- private search history and saved result snapshots;
- favorites and favorite comparison;
- product comparison and feedback endpoints;
- database selection through `DATABASE_URL`.

Owner: Zaikun Zheng.

### Database, catalogue and importer

- V3 SQLAlchemy schema and relationships;
- `import_real_catalog.py`;
- `real_product_catalog.csv`;
- `product_specs.csv`;
- public-data provenance and conversion rules;
- SQLite/PostgreSQL integration;
- bundled database only when the database owner confirms the intended release treatment.

Owner: Yuyang Zhou.

### Frontend

- V3 `index.html` interface;
- structured recommendation filters;
- pagination and comparison;
- registration/login interface;
- favorites and account centre;
- history restoration and deletion;
- feedback and sharing;
- responsive and accessibility behaviour;
- production API configuration.

Owner: Guanyu Lu.

### Automated tests and CI

- current `test_server.py` V3 contract;
- historical `test_mock.py` retained without misclassifying V2 incompatibilities as V3 regressions;
- approved V3 GitHub Actions workflow.

Owner: Zaikun Zheng for technical test content; Chu Junjie for workflow evidence and release coordination.

## 5. `main` content eligible for selective retention

The following `main`-only content may be retained when it is accurate, non-conflicting and useful for project traceability:

- historical practical evidence;
- coordinator command logs;
- earlier compilation and dependency-check evidence;
- frontend field-confirmation records;
- database evidence records;
- backend CI evidence records;
- historical Issue drafts clearly labelled as historical;
- non-conflicting improvements to project status and traceability.

Retention does not mean that every `main` file must be copied. The reconciliation Pull Request must identify each retained file and its purpose.

## 6. Files requiring owner-controlled comparison

| File or area | Risk | Required owner |
|---|---|---|
| `server.py` | Older compatibility additions may conflict with V3 API/schema | Zaikun |
| `index.html` | Later deployment or interface changes may affect V3 behaviour | Guanyu |
| `requirements.txt` | Duplicate or different dependency strategy | Zaikun, with Yuyang for PostgreSQL driver |
| `product_specs.csv` | Duplicate or conflicting catalogue specification content | Yuyang |
| `digital_products.db` | Binary conflict and unclear release treatment | Yuyang |
| `docs/project-status.md` | Different status snapshots may conflict | Junjie, with owner confirmation for technical claims |
| `docs/requirements-traceability.md` | User-story status and evidence may conflict | Junjie, with relevant component owners |
| `docs/definition-of-done.md` | Governance changes may overlap | Junjie |
| `README.md` | Current V3 and historical claims require final consolidation | All component owners |

No conflict in these areas should be resolved solely by the release coordinator where the result changes technical meaning.

## 7. Pre-reconciliation gates

The reconciliation branch should not be created until the following records are available:

- formal GitHub review of the V3 documentation package;
- approved CI workflow and canonical test scope;
- approved US-09 scope decision;
- approved database verification record;
- reviewed V3 architecture and toolchain records;
- final V3 release-candidate commit identified;
- canonical test suite passed for the release candidate;
- deployed frontend/API/database identity recorded;
- blocking database, persistence, E2E and acceptance defects resolved or explicitly accepted.

## 8. Reconciliation workflow

### Step 1 — Freeze the V3 release candidate

Record:

- branch;
- commit SHA;
- date and timezone;
- included Pull Requests;
- known limitations;
- current test and runtime evidence.

No new feature work should enter the candidate without reopening the relevant release gates.

### Step 2 — Create a controlled reconciliation branch

Create the branch from the reviewed V3 release candidate, not from `main`.

Recommended naming:

```text
release/v3-main-reconciliation
```

### Step 3 — Inventory `main`-only changes

For every `main`-only file, classify it as:

- retain unchanged;
- adapt as documentation only;
- superseded by V3;
- conflict requiring owner decision;
- exclude from the final release.

Record the classification and rationale in the reconciliation Pull Request.

### Step 4 — Integrate approved non-conflicting evidence

Bring in only records that improve traceability without changing the V3 technical implementation.

### Step 5 — Resolve owner-controlled conflicts

- Zaikun resolves backend, API, algorithm and test conflicts;
- Yuyang resolves database, catalogue, importer and binary-database conflicts;
- Guanyu resolves frontend and deployment-interface conflicts;
- Junjie resolves coordinator-owned status, traceability and release-document conflicts.

Every technical resolution should have a clear commit and review trail.

### Step 6 — Update final project documentation

After the technical candidate is stable:

- update README to clearly distinguish the current release from historical iterations;
- align project status and traceability with actual results;
- record the final test command and evidence;
- record deployment URLs and commit identities;
- record accepted limitations;
- complete only those release checklist items supported by evidence.

### Step 7 — Run final verification

Required checks include:

- canonical V3 test suite;
- tracked-file integrity;
- catalogue and schema integrity;
- deployed health and database identity;
- authentication and privacy;
- recommendation, pagination and comparison;
- favorites, history, feedback and sharing;
- desktop and mobile smoke tests;
- accepted E2E and external acceptance scope;
- secret and packaging review.

### Step 8 — Open the final Pull Request to `main`

The Pull Request must include:

- release-candidate SHA;
- reconciliation branch SHA;
- file-classification summary;
- owner-controlled conflict decisions;
- test and runtime evidence;
- accepted limitations;
- reviewer approvals;
- rollback instructions.

### Step 9 — Merge, tag and package

After approval and successful required checks:

- merge the reconciliation Pull Request to `main`;
- confirm the final `main` SHA;
- create the release tag;
- produce the final project archive;
- record checksum and backup location;
- confirm the deployed version corresponds to the intended release.

## 9. Rollback approach

Before integration:

- retain the V3 release-candidate SHA;
- retain the pre-merge `main` SHA;
- retain database backup or restoration instructions;
- ensure the release can be redeployed from the V3 candidate if reconciliation introduces a defect.

A rollback must not use the catalogue importer against a live database containing user data.

## 10. Reconciliation record template

| Field | Value |
|---|---|
| V3 release-candidate SHA | Pending |
| Reconciliation branch | Pending |
| Pre-merge `main` SHA | Pending |
| Final reconciliation SHA | Pending |
| Canonical CI result | Pending |
| Database verification | Pending |
| Deployed E2E result | Pending |
| External acceptance | Pending |
| Accepted limitations | Pending |
| Reviewer approvals | Pending |
| Final `main` SHA | Pending |
| Release tag | Pending |
| Package/checksum | Pending |

## 11. Approval criteria

The reconciliation plan is ready for execution when:

- component owners approve the preservation and conflict boundaries;
- the V3 submission documentation is merged;
- the release candidate is frozen and verified;
- no unresolved critical defect remains;
- the project team agrees that the recorded limitations are acceptable.

This document prepares the integration process. It does not itself merge branches, resolve technical conflicts or establish release completion.
