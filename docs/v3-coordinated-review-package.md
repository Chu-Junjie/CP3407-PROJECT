# V3 Submission and Release Review Package

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Document owner:** Chu Junjie — Project Manager and Release Coordinator  
**Document status:** Prepared for formal team review

## 1. Purpose

This document consolidates the records required to review the V3 release candidate in a controlled and traceable manner. It links the project scope, architecture, implementation evidence, testing evidence, database verification, deployment checks, acceptance records and release controls without replacing the detailed source documents.

The package supports a professional review process in which each component owner confirms the accuracy of the records related to their work before final integration into `main`.

## 2. Submission package

| Pull Request | Record | Primary review scope |
|---|---|---|
| #35 | V3 CI workflow and canonical automated test scope | Backend, API and automated testing |
| #44 | Safe reconciliation plan for `main` and V3 | Integration boundaries and file preservation |
| #46 | V3 release evidence index | Evidence completeness and status consistency |
| #47 | US-09 scope decision record | Product scope, API and UI implications |
| #48 | Database release verification record | Schema, catalogue, importer and PostgreSQL controls |
| #50 | Submission and release review package | Cross-document consistency and release sequence |
| #52 | V3 design and architecture | Architecture, database and interface design |
| #54 | Agile iteration, demonstration and feedback evidence | Planning, delivery, variance and retrospective records |
| #58 | Development toolchain and dependency reference | Tools, dependencies, environments and governance |
| #60 | Scope, CI and release-gate status alignment | Project status, traceability and final acceptance controls |

Each Pull Request remains independently reviewable and should be merged only after its affected component owners confirm the relevant technical statements.

## 3. Confirmed repository decisions

### 3.1 Authoritative V3 baseline

`feature/product-database` is the authoritative V3 implementation baseline. It contains the current Flask and SQLAlchemy backend, recommendation flow, authentication, private favorites and history, catalogue importer, database schema, responsive frontend and release documentation.

Completed V3 implementation must not be replaced by older `main` versions during reconciliation.

### 3.2 Canonical automated test scope

The canonical V3 release test command is:

```bash
python -m pytest -q test_server.py
```

GitHub Actions workflow run `31096706920` recorded:

- Ubuntu 24.04.4;
- Python 3.11.15;
- pytest 9.1.1;
- 12 tests collected;
- 12 tests passed in 1.23 seconds;
- tracked-file integrity passed;
- overall workflow conclusion: `success`.

`test_mock.py` is retained as historical Practical 8 evidence for the removed V2 contract. It is executed as a visible non-release compatibility audit and is not used as the V3 release gate.

The canonical suite must be run again for the final frozen release candidate.

### 3.3 US-09 scope

US-09 Budget Alternatives is deferred from the current V3 release and retained in the backlog with an `Unscheduled` milestone.

The current release supports maximum-budget filtering but does not promise a separately selected cheaper equivalent alternative. A future implementation requires an agreed selection rule, API field, interface treatment, automated tests and deployed acceptance criteria.

### 3.4 Database implementation status

Repository inspection confirms:

- SQLAlchemy supports SQLite locally and PostgreSQL through `DATABASE_URL`;
- the application defines products, product specifications, users, favorites, search history, saved results and feedback tables;
- the importer defines a 2,000-record public catalogue comprising 800 laptops, 833 smartphones, 300 smart watches, 61 headphones and 6 tablets;
- the implementation target is 11,000 product rows and 2,000 joined product-specification rows;
- source, licence and fixed currency-conversion rules are retained;
- catalogue generation must use a disposable output database and must not run directly against production user data.

Actual deployed PostgreSQL identity, persistence, backup and recovery remain runtime verification requirements.

## 4. Review responsibilities

### Zaikun Zheng — Backend and Algorithm Engineer

Review and confirm:

- Flask API and authentication descriptions;
- recommendation and pagination behaviour;
- canonical automated test scope;
- historical mock-test classification;
- backend dependencies and deployment wording;
- API impact of deferred US-09 scope.

### Yuyang Zhou — Database Administrator

Review and confirm:

- schema and relationship descriptions;
- catalogue counts and category quotas;
- public-data provenance and conversion rules;
- importer behaviour and production-data restriction;
- SQLite/PostgreSQL configuration wording;
- persistence, backup and recovery verification requirements.

### Guanyu Lu — UI/UX and Frontend Developer

Review and confirm:

- interface information architecture;
- recommendation, comparison, favorites, history, feedback and sharing flows;
- desktop and mobile behaviour;
- accessibility observations and interface limitations;
- GitHub Pages and deployed-browser verification requirements;
- UI impact of deferred US-09 scope.

### Chu Junjie — Project Manager and Release Coordinator

Responsible for:

- maintaining consistent project status and scope records;
- linking Issues, Pull Requests, commits and test evidence;
- coordinating component reviews and recording outcomes;
- assigning defects to the appropriate technical owner;
- coordinating retesting and acceptance;
- applying the release checklist and Go/No-Go decision;
- ensuring no unverified activity is reported as completed.

## 5. Required review outcome

For each Pull Request, the reviewer should record one of the following outcomes:

- **Approved:** the record accurately represents the reviewed component;
- **Approved with accepted limitation:** the record is accurate and the limitation is explicitly retained;
- **Changes requested:** specific corrections are required before merge.

An approval confirms the accuracy of the documentation within the reviewer's component scope. It does not by itself prove deployed runtime behaviour.

## 6. Merge sequence after approval

The recommended merge sequence into `feature/product-database` is:

1. PR #35 — CI workflow and test scope;
2. PR #47 — US-09 scope decision;
3. PR #48 — database verification record;
4. PR #52 — design and architecture;
5. PR #54 — Agile delivery evidence;
6. PR #58 — development toolchain;
7. PR #44 — reconciliation plan;
8. PR #60 — project status and release-gate alignment;
9. PR #46 — release evidence index;
10. PR #50 — final package index.

Each Pull Request should be checked against the latest base before merge. Squash merge may be used to keep one clear commit per documentation deliverable.

## 7. Runtime verification required before `main`

The following activities require actual execution and cannot be replaced by source inspection or team approval:

- catalogue generation and integrity verification on a disposable database copy;
- deployed frontend and API commit identification;
- confirmation that the deployed API uses PostgreSQL;
- account, favorites, history and feedback persistence after restart or redeploy;
- cross-user privacy checks;
- desktop and mobile browser E2E;
- sharing and history-restoration checks;
- external user acceptance;
- final release-candidate CI rerun;
- final secret and release-package review.

Every executed item must record the tested commit, environment, date, steps, expected result, observed result and evidence location.

## 8. Reconciliation and final release

After the documentation package is approved and runtime gates are complete:

1. freeze the V3 release-candidate commit;
2. create a controlled reconciliation branch;
3. preserve V3 implementation files as authoritative;
4. integrate only useful non-conflicting historical evidence from `main`;
5. resolve owner-controlled conflicts through the relevant technical owner;
6. rerun the canonical test suite and release smoke test;
7. update README and final status records from actual evidence;
8. open the final reconciliation Pull Request to `main`;
9. merge only after approval and successful required checks;
10. create the release tag and final project package.

## 9. Evidence integrity rules

- Implementation presence is not runtime verification.
- A prepared test record is not an executed test.
- An approval is not deployment evidence.
- A passing PR ref is not automatically the final release-candidate result.
- Missing evidence must remain `Not Run`, `Blocked`, `Failed` or `Unverified` as applicable.
- Credentials, tokens, connection strings and personal data must not be retained in project evidence.
- Teammate-owned implementation must not be modified by the release coordinator without an owner-approved technical change.

## 10. Submission readiness checklist

- [x] V3 implementation baseline identified.
- [x] Documentation package indexed.
- [x] Canonical automated test scope recorded.
- [x] US-09 scope decision recorded.
- [x] Database implementation and operational boundaries recorded.
- [x] Component review responsibilities defined.
- [x] Merge and reconciliation sequence defined.
- [x] Runtime evidence requirements defined.
- [ ] Formal GitHub reviews recorded.
- [ ] Approved package Pull Requests merged into `feature/product-database`.
- [ ] Runtime verification completed.
- [ ] Final release candidate frozen and tested.
- [ ] Reconciliation Pull Request approved and merged into `main`.
- [ ] Release tag and final project package created.

This record is ready for formal component review. It must be updated only when new review, runtime or release evidence exists.
