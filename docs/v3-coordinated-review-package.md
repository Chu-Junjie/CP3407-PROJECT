# V3 Coordinated Review and Closeout Package

**Tracking Issue:** #49  
**Coordinator:** Chu Junjie  
**Review request status:** Deferred  
**Target base branch:** `feature/product-database`

## 1. Purpose

This document defines the closeout path for the current V3 Draft Pull Requests. Technical review is deferred, but repository-supported questions are resolved now so the project does not remain blocked on information already present in source control.

No GitHub approval is inferred from silence. Every PR remains Draft until actual review resumes.

## 2. Repository-derived decisions

### 2.1 Automated-test scope

**Canonical V3 release suite:**

```bash
python -m pytest -q test_server.py
```

`test_mock.py` is historical Practical 8, Task 7 evidence. It targets removed V2 Pandas/raw-SQLite interfaces and is retained as a non-release compatibility audit rather than a V3 release gate.

PR #35 now separates:

- a required V3 release-suite job;
- a visible, non-blocking historical mock audit.

### 2.2 US-09 Budget Alternatives

**Decision:** Option C — Deferred from the current V3 release  
**Future milestone:** Unscheduled

The API contract, backend response and V3 tests do not implement a cheaper-alternative object. The frontend contains optional display scaffolding only. Current release material must state that budget filtering exists but separate cheaper-alternative selection does not.

### 2.3 Database and importer position

Repository inspection confirms:

- SQLAlchemy SQLite/PostgreSQL selection;
- seven application tables;
- a deterministic 2,000-row catalogue target;
- a total implementation target of 11,000 products and 2,000 specifications;
- documented dataset sources, licences and fixed currency conversion rules;
- built-in catalogue validation.

Runtime counts, PostgreSQL identity, persistence, backup and deployed isolation remain open.

The catalogue importer is a build-artifact tool. It deletes private rows from the generated output copy and must not run directly against a live production database containing user data.

## 3. Draft package inventory

| PR | Purpose | Current treatment |
|---|---|---|
| #35 | CI workflow | Canonical V3 suite defined; new workflow run required. |
| #44 | Safe `main`/V3 reconciliation | Prepared; no reconciliation branch created. |
| #46 | Release evidence index | Updated with repository-derived decisions. |
| #47 | US-09 scope record | Option C — Deferred. |
| #48 | Database/PostgreSQL verification | Static findings complete; runtime evidence pending. |
| #50 | This closeout package | Updated; actual review deferred. |
| #52 | V3 design and architecture | Prepared. |
| #54 | Agile delivery and retrospective record | Prepared. |
| #58 | Development toolchain and dependencies | Prepared. |

## 4. Current operating rules

1. Keep all package PRs Draft while review is deferred.
2. Do not record an approval that is not present in GitHub.
3. Do not modify teammate-owned implementation.
4. Use repository evidence to resolve scope and documentation questions.
5. Keep runtime verification separate from source inspection.
6. Do not merge to `main` or create the reconciliation branch without separate approval.
7. Do not run the catalogue importer against production user data.

## 5. Work that can be completed before review resumes

- [x] Define the canonical V3 test suite.
- [x] Classify `test_mock.py` as a historical non-release audit.
- [x] Record US-09 as deferred.
- [x] Record repository-derived schema, importer, provenance and operational findings.
- [x] Refresh Release Evidence Index.
- [ ] Obtain a successful new PR #35 canonical workflow result.
- [ ] Prepare coordinator-owned status corrections for US-09 and test scope.
- [ ] Run local catalogue verification against a disposable database copy.
- [ ] Confirm deployed frontend/API/PostgreSQL identity.
- [ ] Execute deployed E2E and external acceptance.

## 6. Technical gates that source inspection cannot close

### 6.1 PostgreSQL

Still required:

- actual Render API commit;
- active database dialect;
- schema and catalogue counts;
- persistence after restart/redeploy;
- cross-user isolation;
- backup and restore.

### 6.2 Deployed browser behaviour

Still required:

- GitHub Pages commit;
- frontend-to-API Network evidence;
- authentication, pagination, comparison, favorites, history, feedback and share flows;
- mobile, keyboard, error and empty-state evidence.

### 6.3 External acceptance

Still required:

- two non-team participant sessions;
- retained task outcomes, observations and ratings;
- defect/limitation decisions.

## 7. Conditional closeout sequence

### Phase A — Current repository closeout

1. Wait for the updated PR #35 workflow run.
2. Record the canonical CI result.
3. Update the US-09 decision Issue and coordinator-owned status files.
4. Update test-scope wording in coordinator-owned documents.
5. Keep all technical runtime gates visible.

### Phase B — Release-candidate verification

1. Confirm the deployed frontend and API commit identities.
2. Confirm PostgreSQL is active.
3. Freeze one release-candidate commit.
4. Run the canonical V3 suite.
5. Run local catalogue integrity commands.
6. Run PostgreSQL persistence and privacy checks.
7. Execute browser E2E.
8. Execute external acceptance.
9. Record defects and retests.

### Phase C — Review and integration

1. Resume real GitHub review.
2. Resolve review comments on each independent PR.
3. Merge independently approved coordinator-owned PRs into `feature/product-database`.
4. Update README, project status, traceability, execution plan and acceptance checklist from actual evidence.
5. Request explicit approval to create the Issue #43 reconciliation branch.
6. Preserve the V3 implementation while integrating useful `main` evidence.
7. Run final CI and release checks.
8. Merge to `main` only after all critical gates pass or are formally accepted limitations.
9. Create a release tag and final package.

## 8. Completion of the coordinator role

Junjie's role is complete only when:

- the package references are consistent;
- repository-derived decisions are recorded;
- real review outcomes are retained;
- approved coordinator documents are merged;
- CI, database, deployment, E2E and acceptance results are recorded;
- release status documents reflect actual evidence;
- reconciliation is reviewed and completed;
- the final release is tagged and packaged;
- no unverified result is represented as passed.

## 9. Ownership boundary

This package does not authorize changes to teammate-owned backend, frontend, tests, datasets, databases, importers or deployment configuration. It also does not authorize an approval, merge, deployment or runtime result that has not actually occurred.
