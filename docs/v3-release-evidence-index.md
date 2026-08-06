# V3 Release Evidence Index

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Document owner:** Chu Junjie — Project Manager and Release Coordinator  
**Status:** Prepared for formal review and release-candidate evidence updates

## 1. Purpose

This index provides a single traceable entry point for the evidence used to evaluate the V3 release. It separates implementation evidence, repository verification, automated testing, runtime verification, acceptance and final release records.

The index does not replace the detailed source documents. Each item must be read together with its linked Issue, Pull Request, commit and execution record.

## 2. Evidence status vocabulary

| Status | Meaning |
|---|---|
| Historical | Retained evidence from an earlier iteration or removed contract. |
| Implemented | Code, data or documentation exists in the repository. |
| Repository verified | A claim is supported by inspection of named repository files or commits. |
| Runtime verified | A named check passed in a named environment for a named commit. |
| Accepted limitation | A limitation is explicitly documented and approved for the current release. |
| Deferred | The item is outside the current release scope and retained in the backlog. |
| Blocked | Execution cannot continue until a dependency or defect is resolved. |
| Not Run | The required execution has not occurred. |
| Failed | The check was executed and did not meet the acceptance condition. |
| Release complete | All applicable release gates have passed and the release artifact exists. |

## 3. Authoritative baseline

| Item | Value |
|---|---|
| Repository | `Chu-Junjie/CP3407-PROJECT` |
| V3 implementation branch | `feature/product-database` |
| Recorded baseline commit | `7c406515bd4b657372fe519869596825cdf91d56` |
| Default branch | `main` |
| Current relationship | Branches diverged; controlled reconciliation required |

The V3 branch is the implementation baseline. Completed V3 backend, frontend, database, catalogue and importer work must not be replaced by older `main` versions during reconciliation.

## 4. Submission documentation package

| Evidence ID | Record | Pull Request | Current status |
|---|---|---:|---|
| DOC-01 | Safe `main`/V3 reconciliation plan | #44 | Prepared for review |
| DOC-02 | V3 release evidence index | #46 | Prepared for review |
| DOC-03 | US-09 scope decision | #47 | Deferred / Unscheduled |
| DOC-04 | Database release verification record | #48 | Repository verified; runtime checks open |
| DOC-05 | Submission and release review package | #50 | Prepared for review |
| DOC-06 | V3 design and architecture | #52 | Prepared for component review |
| DOC-07 | Agile iteration, demonstration and feedback evidence | #54 | Prepared for review |
| DOC-08 | Development toolchain and dependencies | #58 | Prepared for review |
| DOC-09 | Scope, CI and release-gate alignment | #60 | Prepared for review |
| CI-01 | V3 GitHub Actions test workflow | #35 | CI verified for recorded PR ref |

## 5. Automated test evidence

### Canonical V3 suite

```bash
python -m pytest -q test_server.py
```

### Recorded GitHub Actions execution

| Field | Value |
|---|---|
| Workflow | `V3 Test Evidence` |
| Run | `31096706920` |
| Workflow source commit | `4e698826dbeac719b56f1ff5cea060109d0bdd60` |
| Tested PR merge ref | `8ecdb5fea8829a85521825b864a9bfe6e630a4ff` |
| Runner | Ubuntu 24.04.4 |
| Python | 3.11.15 |
| pytest | 9.1.1 |
| Result | 12 collected, 12 passed in 1.23 seconds |
| Tracked-file integrity | Passed |
| Overall conclusion | Success |

Status: **Runtime verified for the recorded PR ref.**

The canonical suite must be rerun for the final frozen release candidate.

### Historical compatibility audit

`test_mock.py` is retained as Practical 8 evidence for removed V2 Pandas and raw-SQLite interfaces. It is executed in a visible non-release audit job.

Recorded audit result:

```text
6 tests collected
6 tests failed
```

Status: **Historical compatibility evidence.** These failures are not classified as V3 release regressions and the historical file remains unchanged.

## 6. Scope evidence

### US-09 Budget Alternatives

Decision: **Deferred from the current V3 release**  
Backlog milestone: **Unscheduled**

Repository basis:

- the current API contract does not define a budget-alternative response field;
- `/api/recommend` does not return a separately selected alternative product;
- the canonical automated suite has no US-09 acceptance case;
- frontend display scaffolding is not treated as end-to-end implementation evidence.

Current-release behaviour: budget filtering is supported; a separately selected cheaper equivalent alternative is not promised.

Status: **Deferred / accepted release limitation pending formal review.**

## 7. Database and catalogue evidence

### Repository-verified implementation

- SQLAlchemy selects PostgreSQL through `DATABASE_URL` and otherwise uses SQLite.
- Seven application tables are defined: products, product specifications, users, favorites, search history, saved results and feedback.
- The importer defines 2,000 recommendation-ready public catalogue records:
  - 800 laptops;
  - 833 smartphones;
  - 300 smart watches;
  - 61 headphones;
  - 6 tablets.
- Imported product IDs begin at `10,000,001`.
- The implementation target is 11,000 total products and 2,000 product specifications.
- Public source, licence and fixed currency-conversion rules are retained.
- The importer verifies catalogue counts, category quotas and absence of private rows in its generated output.

Status: **Repository verified.**

### Operational restriction

The importer is a catalogue-build tool. It must run against a disposable input/output database and must not run directly against a live database containing user accounts, favorites, history or feedback.

### Runtime database gates

| Check | Status |
|---|---|
| Actual release database counts | Not Run |
| Join and orphan verification | Not Run |
| Deployed database dialect | Unverified |
| PostgreSQL initialization | Not Run |
| Persistence after restart/redeploy | Not Run |
| Cross-user deployed isolation | Not Run |
| Backup and restore | Not Run |
| Final secret review | Not Run |

## 8. Design and architecture evidence

The design record covers:

- system context and logical architecture;
- GitHub Pages frontend and Render API deployment model;
- Flask, SQLAlchemy and catalogue importer responsibilities;
- API and authentication boundaries;
- recommendation and pagination flow;
- database entities and relationships;
- account privacy, favorites and history boundaries;
- desktop/mobile information architecture;
- accessibility considerations;
- design alternatives and known limitations.

Status: **Prepared for component-owner review.** Runtime deployment and persistence claims remain outside source-derived design evidence.

## 9. Agile and project-management evidence

The Agile evidence record includes:

- planned and delivered scope by iteration or reconstructed evidence phase;
- task ownership and dependencies;
- delivery evidence through Issues, Pull Requests and commits;
- blockers, scope changes and corrective actions;
- demonstration and feedback status;
- retrospective improvements;
- a reusable iteration close-out template.

Historical dates, effort, demonstrations or client feedback that are not supported by retained evidence remain explicitly identified as unavailable or not run.

Status: **Prepared for review.**

## 10. Toolchain and dependency evidence

The toolchain record documents:

- Git and GitHub workflow;
- Python environment and runtime dependencies;
- Flask, Flask-Cors, Gunicorn, PyJWT, SQLAlchemy and psycopg;
- SQLite, PostgreSQL and catalogue-import tooling;
- pytest and GitHub Actions;
- GitHub Pages and Render deployment roles;
- environment variables and secret-handling rules;
- dependency-governance procedures.

Status: **Prepared for review.** Commands are procedures and do not imply successful execution unless linked evidence exists.

## 11. Deployment and acceptance evidence

| Evidence area | Required record | Current status |
|---|---|---|
| GitHub Pages frontend commit | URL, commit SHA, date | Unverified |
| Render API commit | URL, commit SHA, date | Unverified |
| Production database | PostgreSQL identity without secrets | Unverified |
| API health | Response and timestamp | Not Run for final candidate |
| Desktop E2E | Scenario records and Network evidence | Not Run |
| Mobile E2E | Scenario records and screenshots | Not Run |
| Authentication and privacy | Two-account evidence | Not Run |
| Favorites/history persistence | Before/after restart evidence | Not Run |
| Feedback persistence | Before/after restart evidence | Not Run |
| Share restoration | Isolated-session evidence | Not Run |
| External acceptance | Two non-team participants | Not Run |

Prepared templates are retained in:

- `docs/v3-e2e-acceptance-evidence.md`;
- `docs/v3-external-uat-record.md`.

A prepared template is not an executed result.

## 12. Review and merge evidence

Formal review must be recorded in GitHub by the relevant technical owners:

- Zaikun: backend, API, algorithm, automated tests and runtime dependencies;
- Yuyang: database, catalogue, importer, provenance and PostgreSQL;
- Guanyu: frontend, responsive behaviour, accessibility and browser flows;
- Junjie: project status, traceability, evidence integrity and release coordination.

| Gate | Status |
|---|---|
| Component-owner review | Pending formal GitHub record |
| Documentation PR merge to V3 | Pending |
| Release-candidate freeze | Pending |
| Final CI rerun | Pending |
| Runtime verification | Pending |
| Acceptance | Pending |
| Reconciliation approval | Pending |
| Merge to `main` | Pending |
| Release tag | Pending |
| Final package/checksum | Pending |

## 13. Release sequence

1. complete formal component review;
2. merge approved documentation and CI records into `feature/product-database`;
3. freeze the V3 release-candidate commit;
4. execute database, deployment, persistence, privacy, E2E and acceptance checks;
5. update the evidence index from actual results;
6. create a controlled reconciliation branch;
7. preserve the V3 implementation and selectively integrate useful `main` evidence;
8. rerun the canonical suite and release smoke test;
9. update README and final status records;
10. merge the approved reconciliation Pull Request to `main`;
11. create the release tag and final submission package.

## 14. Evidence integrity controls

- Do not mark a source-derived target as an observed runtime result.
- Do not report approval without a GitHub review record.
- Do not report deployment identity without a commit or service record.
- Do not report persistence without restart or redeploy evidence.
- Do not retain passwords, JWTs, connection strings or personal data.
- Do not modify teammate-owned implementation through documentation closeout work.

## 15. Current release position

The repository has a defined V3 baseline, current scope decision, passing canonical CI evidence for a recorded PR ref and a complete submission-document structure.

The project is **not yet release complete** because final runtime verification, formal reviews, release-candidate testing, reconciliation, `main` integration and release packaging remain outstanding.
