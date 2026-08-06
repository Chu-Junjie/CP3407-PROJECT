# V3 Coordinated Review and Closeout Package

**Tracking Issue:** #49  
**Coordinator:** Chu Junjie  
**Review status:** Deferred  
**Target base branch:** `feature/product-database`

## 1. Purpose

Coordinate the V3 Draft Pull Requests and define the remaining closeout sequence. Repository-supported decisions have been completed without waiting for verbal confirmation; actual GitHub approvals, runtime verification and final integration remain separate gates.

No approval is inferred from silence. Every Pull Request remains independent.

## 2. Repository-derived decisions completed

### Canonical V3 testing

```bash
python -m pytest -q test_server.py
```

Workflow run `31096706920` succeeded:

- Ubuntu 24.04.4;
- Python 3.11.15;
- pytest 9.1.1;
- 12 tests collected;
- 12 passed in 1.23s;
- tracked-file integrity passed.

`test_mock.py` remains a visible non-release Practical 8 compatibility audit. Its six V2 failures do not belong to the canonical release gate. Issue #34 is completed.

### US-09

US-09 Budget Alternatives is Deferred from the current V3 release and retained in the backlog as `Unscheduled`.

The release supports maximum-budget filtering but does not promise a separately selected cheaper equivalent alternative.

### Database and importer

Repository inspection confirms the schema, PostgreSQL/SQLite selection, catalogue quotas, source/licence metadata, currency rules and built-in validation. Runtime database counts, deployed PostgreSQL identity, persistence and recovery remain open.

The catalogue importer must not run directly against a live production database containing private user data.

## 3. Package inventory

| PR | Purpose | Current closeout status |
|---|---|---|
| #35 | CI workflow | Canonical job successful; Draft review deferred |
| #44 | Safe branch reconciliation plan | Prepared; no reconciliation branch created |
| #46 | Release evidence index | Updated through current decisions |
| #47 | US-09 decision record | Option C — Deferred |
| #48 | Database verification record | Repository findings complete; runtime blocked |
| #50 | This closeout package | Updated; review deferred |
| #52 | Design and architecture | Prepared |
| #54 | Agile delivery/evidence record | Prepared |
| #58 | Development toolchain | Prepared |
| #60 | Scope, CI and release-gate status alignment | Four coordinator documents updated |

## 4. Review-deferred rules

1. Keep all package PRs Draft.
2. Do not record or imply approval without an actual GitHub review.
3. Do not send repeated review pings while review is deferred.
4. Do not merge one PR because another PR was approved.
5. Do not modify teammate-owned implementation from coordinator branches.
6. Do not treat source inspection as deployed or acceptance evidence.
7. Do not create a reconciliation branch or merge to `main` without separate explicit approval.

## 5. Component review scope when review resumes

### Guanyu — frontend

Review:

- deployed frontend and interface statements;
- responsive/accessibility wording;
- US-09 frontend limitation;
- browser E2E procedure;
- branch protection for `index.html`.

### Zaikun — backend and tests

Review:

- API/auth/recommendation statements;
- canonical test workflow and historical audit boundary;
- backend privacy and persistence expectations;
- US-09 backend/API limitation;
- branch protection for backend/test files.

### Yuyang — database and catalogue

Review:

- schema, quotas, importer and provenance statements;
- PostgreSQL and persistence procedure;
- importer production-data warning;
- preservation of V3 database/data/importer files during reconciliation.

### Junjie — coordination

Maintain:

- Issue/PR/commit references;
- evidence status consistency;
- schedule and release gates;
- review outcome records;
- final reconciliation/release sequence.

## 6. Work completed before review

- [x] V3 baseline recorded.
- [x] Canonical test suite selected.
- [x] Successful canonical CI retained.
- [x] Historical mock audit classified.
- [x] US-09 deferred with limitation wording.
- [x] Database source-level verification recorded.
- [x] Release Evidence Index refreshed.
- [x] Coordinator status documents aligned in PR #60.
- [ ] Local catalogue command output retained.
- [ ] Deployed environment identity confirmed.
- [ ] Release-candidate CI executed.
- [ ] PostgreSQL persistence/privacy executed.
- [ ] Browser E2E executed.
- [ ] External acceptance executed.

## 7. Runtime gates that remain open

### Database and deployment

- actual local and PostgreSQL counts;
- active PostgreSQL dialect;
- deployed API commit;
- restart/redeploy persistence;
- backup/restore;
- final secret scan.

### Browser

- GitHub Pages deployed commit;
- frontend-to-API integration;
- auth, recommendation, pagination, comparison, favorites, history, feedback and share;
- mobile, keyboard, focus, error and empty-state evidence.

### Acceptance

- two non-team participant sessions;
- task outcomes, observations and ratings;
- defect and retest decisions.

## 8. Closeout sequence

### Phase A — Runtime verification

1. Run catalogue verification against a disposable copy.
2. Confirm deployed frontend/API/PostgreSQL identity.
3. Freeze the release candidate.
4. Rerun canonical CI for that commit.
5. Execute PostgreSQL persistence and privacy tests.
6. Execute browser E2E.
7. Execute external acceptance.

### Phase B — Review and documentation integration

1. Resume real GitHub review.
2. Resolve comments on each independent PR.
3. Merge actually approved coordinator-owned PRs into `feature/product-database`.
4. Update README and final records from actual evidence.
5. Close Issues only when their own criteria are satisfied.

### Phase C — Branch reconciliation and release

1. Obtain explicit approval to create the Issue #43 reconciliation branch.
2. Preserve V3 backend, frontend, database, catalogue and importer work.
3. Bring across only useful `main` historical evidence.
4. Resolve overlaps under component ownership.
5. Rerun canonical CI and runtime checks.
6. Merge to `main` through a reviewed PR.
7. Confirm deployed release identity.
8. Create release tag, changelog and final package.

## 9. Coordinator completion criteria

The coordinator role is complete when:

- all references and statuses are consistent;
- repository-derived decisions are retained;
- real reviews are recorded;
- approved coordinator records are merged;
- runtime, E2E and acceptance evidence is retained;
- final documents match the release;
- reconciliation is reviewed and complete;
- release tag and package are created;
- no unsupported result is presented as passed.

## 10. Non-authorization statement

This package does not authorize:

- edits to teammate-owned backend, frontend, tests, datasets, databases, importers or deployment configuration;
- invented review, deployment, persistence, E2E or acceptance results;
- direct execution of the importer against production user data;
- automatic batch approval or merge;
- creation of the reconciliation branch or merge to `main` without separate approval.
