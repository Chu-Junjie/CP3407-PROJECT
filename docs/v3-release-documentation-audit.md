# Release Record Consistency Audit

**Project:** Smart Digital Product Recommendation Platform  
**Audit date:** 6 August 2026  
**Audited baseline:** `feature/product-database`  
**Meeting and audit record maintained by:** @Chu-Junjie  
**Related tracking:** Issue #38 / PR #39

## 1. Purpose

This historical audit records stale, conflicting or unsupported project statements and links each correction to @ZhengZaikun, @tiantian09091, @Guanyu-Lu or @Chu-Junjie.

The audit does not prove runtime behaviour and does not authorise @Chu-Junjie to change implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu.

## 2. Evidence levels

| Level | Meaning |
|---|---|
| Historical | Earlier iteration evidence retained with a clear time/scope boundary. |
| Implemented | Code, data or documentation exists, but applicable gates remain open. |
| Verified | A named check passed for a named commit and environment. |
| Done | Every applicable implementation, review, verification and release gate passed. |

## 3. Named correction responsibilities

- @ZhengZaikun confirms backend/API descriptions, canonical tests, CI interpretation and runtime dependencies.
- @tiantian09091 confirms schema, catalogue, importer, provenance, PostgreSQL and recovery descriptions.
- @Guanyu-Lu confirms frontend, GitHub Pages, responsive, accessibility and deployed-interface descriptions.
- @Chu-Junjie maintains team meeting notes, status, traceability, README structure, evidence links and release wording.

## 4. Audit findings and current correction path

| ID | Finding | Risk | Correction path | Status |
|---|---|---|---|---|
| AUD-01 | README mixes historical iteration statements with current V3 statements | Readers may treat older completion claims as current release evidence | @Chu-Junjie restructures README during final reconciliation; @ZhengZaikun, @tiantian09091 and @Guanyu-Lu confirm their sections | Open until reconciliation |
| AUD-02 | Historical user-story statuses conflict with V3 traceability | Requirements may appear completed without current verification | PR #60 aligns status and traceability; @ZhengZaikun, @tiantian09091 and @Guanyu-Lu review technical mappings | In review |
| AUD-03 | Earlier documents did not identify the canonical V3 suite | Partial or historical tests could be misreported | Issue #34 / PR #35 records `python -m pytest -q test_server.py`; @ZhengZaikun reviews | In review |
| AUD-04 | Historical `test_mock.py` failures were mixed with current release status | Expected V2 incompatibility could block or misrepresent V3 | PR #35 separates the historical audit from the release job | In review |
| AUD-05 | Deployment links did not identify the exact frontend/API commit | An older deployment could be described as V3 | @Guanyu-Lu records frontend identity; @ZhengZaikun records API identity under Issue #42 | Not Run |
| AUD-06 | PostgreSQL configuration was described without deployed proof | Persistence could be overstated | @tiantian09091 records engine, tables, counts and restart persistence; @ZhengZaikun confirms API integration | Not Run |
| AUD-07 | Architecture descriptions mixed older CSV/raw-SQLite design with current SQLAlchemy/account features | Readers could not identify the current design | PR #52 provides the V3 design; named technical reviews are pending | In review |
| AUD-08 | US-09 scope was unclear | Budget filtering could be confused with cheaper-alternative selection | Issue #40 / PR #47 records Deferred / `Unscheduled`; @ZhengZaikun and @Guanyu-Lu review | In review |
| AUD-09 | Acceptance templates could be mistaken for executed tests | Project completion could be overstated | PR #37 templates remain `Not Run`; Issue #42 tracks execution | Corrected preparation; execution pending |
| AUD-10 | Database targets were not separated from observed counts | 11,000/2,000 targets could be presented as actual output | PR #48 records repository targets and assigns runtime checks to @tiantian09091 | In review |
| AUD-11 | Generic responsibility wording obscured who must review or fix work | Review and defect routing could be ambiguous | Current Issues, PRs and records use explicit mentions of @ZhengZaikun, @tiantian09091, @Guanyu-Lu and @Chu-Junjie | Corrected on active branches |
| AUD-12 | Historical `main` status used outdated role wording | Default-branch historical records could conflict with current meeting records | PR #61 rewrites the historical status and requests all three named reviews | In review |

## 5. Current verified evidence

- PR #33 merged the V3 governance baseline.
- PR #37 merged E2E and external-acceptance preparation only.
- PR #39 merged this audit record.
- Workflow run `31096706920` recorded 12/12 passes and tracked-file integrity for the recorded PR ref.
- US-09 is recorded as Deferred / `Unscheduled`.
- Database/schema/catalogue/importer facts are repository verified.

## 6. Evidence still required

- formal Approvals for the current open PR heads;
- final release-candidate CI from @ZhengZaikun;
- disposable catalogue output and PostgreSQL evidence from @tiantian09091;
- deployed frontend identity and browser E2E from @Guanyu-Lu;
- two non-team external-acceptance records coordinated by @Chu-Junjie;
- final reconciliation and README update;
- final tag, archive and checksum.

## 7. Integrity rules

- Team decisions are recorded as team meeting notes maintained by @Chu-Junjie.
- Responsibilities use explicit GitHub mentions.
- A meeting decision is not a formal Approval.
- A template is not an executed result.
- A source target is not an observed database count.
- Historical evidence is not current release evidence.
- Passwords, tokens and connection strings are not retained.

## 8. Completion criteria

- [x] Findings and risks are recorded.
- [x] Every correction is assigned explicitly.
- [x] Current V3 and historical records are separated.
- [x] Canonical CI, US-09 and database-status corrections are represented in active PRs.
- [ ] Open correction PRs receive formal Approvals and merge.
- [ ] Runtime and acceptance evidence is executed.
- [ ] README and historical `main` wording are finalised through reviewed reconciliation.

The audit closes only as a documentation activity. It does not mark the V3 release Done.