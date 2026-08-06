# US-09 Budget Alternatives — V3 Scope Decision Record

**Tracking Issue:** #40  
**Current status:** `Deferred from V3 release`  
**Coordinator:** Chu Junjie  
**Decision date:** 6 August 2026, Singapore time (UTC+8)  
**Selected option:** Option C — Defer

## 1. Decision

US-09 Budget Alternatives is not part of the current V3 release commitment. It remains in the product backlog with an `Unscheduled` milestone.

The current V3 release may provide recommendation filtering by budget, ranked results, a separate Top 5 and pagination. It must not claim that the API selects or returns a cheaper qualifying alternative.

## 2. Repository-derived basis

The decision is based on the authoritative `feature/product-database` implementation rather than an unrecorded verbal assumption.

### Backend and API evidence

- `api-contract.md` documents recommendation filters, pagination, Top 5, history, comparison, favorites and feedback, but does not define a budget-alternative response field.
- `/api/recommend` in `server.py` returns `filters`, `count`, `total_candidates`, pagination fields, `top_recommendations`, `data` and optional `history_id`.
- The response does not calculate or return `budget_alternative`.
- No deterministic eligibility rule exists for percentage/amount cheaper, same-category qualification or protected specifications.

### Automated-test evidence

- `test_server.py` verifies budget parsing and filtering.
- It does not contain an acceptance test for selecting a cheaper alternative.
- The retained V3 API suite therefore does not support a claim that US-09 is implemented or verified.

### Frontend evidence

- `index.html` contains a `budgetAlternative` display region and accepts an optional `budget_alternative` or `budgetAlternative` field.
- The display code is compatibility/presentation scaffolding only.
- Because the current backend contract does not produce the field, the frontend element does not establish an end-to-end feature.

## 3. Final requirement wording

> US-09 is deferred from the current V3 release. The release supports budget-constrained recommendation filtering but does not promise a separately selected cheaper alternative. A future implementation must define deterministic eligibility, API fields, presentation, automated tests and deployed acceptance before the story can re-enter a release scope.

## 4. Reason for deferral

Keeping US-09 in the current release would require new backend ranking rules, a revised API contract, automated tests, frontend states and deployed browser acceptance. Those requirements are not present in the current implementation baseline.

Deferral avoids:

- presenting dormant frontend scaffolding as a completed feature;
- adding unplanned algorithm and API changes during release preparation;
- weakening the distinction between budget filtering and alternative selection;
- delaying verification of the implemented V3 account, catalogue, pagination and persistence work.

## 5. Component impact

| Area | V3 release treatment |
|---|---|
| Backend/recommendation | No new alternative-selection algorithm is required for the current release. |
| API | No `budget_alternative` field is part of the current V3 contract. |
| Frontend | Existing optional rendering scaffolding may remain, but release documentation and demonstrations must not imply the field is produced. |
| Automated tests | No US-09 acceptance test is required in the current canonical V3 suite. |
| Deployed E2E | E2E verifies budget filtering only; it must not record US-09 as passed. |
| Schedule | No additional implementation is added to the current release candidate. |

## 6. Known limitation wording

Use the following statement in current release material:

> The current release filters recommendations by a user's maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

## 7. Backlog definition

**Backlog status:** Deferred  
**Milestone:** Unscheduled

Before future implementation begins, the backlog item must define:

- cheaper-by percentage or absolute threshold;
- same-category requirement;
- protected use-case and core-specification rules;
- relationship to Top 5 and pagination;
- response fields and empty-state behaviour;
- source and historical-price limitations;
- automated boundary tests;
- deployed desktop/mobile acceptance.

## 8. Required documentation corrections

The following coordinator-owned records should be updated during final closeout:

- `README.md` — remove historical V3 `In-Progress` wording for US-09;
- `docs/project-status.md` — record `Deferred`;
- `docs/requirements-traceability.md` — replace `Scope confirmation required` with `Deferred`;
- `docs/v3-execution-plan.md` — remove US-09 from current release gates;
- `docs/final-acceptance-and-release-checklist.md` — record it as non-applicable for this release;
- `docs/v3-release-evidence-index.md` — record this repository-derived decision;
- demonstration and final-report wording — include the known limitation.

## 9. Completion checklist

- [x] Option C is selected.
- [x] Deferral reason is supported by current repository evidence.
- [x] Current V3 scope explicitly excludes US-09.
- [x] Backend, API, frontend and test impacts are recorded.
- [x] Known limitation wording is defined.
- [x] Future backlog status is `Unscheduled`.
- [ ] Coordinator-owned status documents are corrected in the final closeout PR.
- [ ] This decision record receives actual GitHub review before merge.

## 10. Ownership boundary

This decision does not remove or modify teammate-owned backend, frontend or test code. The optional frontend renderer remains untouched. Any future US-09 implementation requires a new technical Issue, owner-controlled branch, tests and Pull Request.
