# US-09 Scope Decision Record

**Project:** Smart Digital Product Recommendation Platform  
**User story:** US-09 — Budget Alternatives  
**Meeting record maintained by:** @Chu-Junjie  
**Decision:** Deferred from the current V3 release  
**Backlog status:** `Unscheduled`

## 1. Meeting decision

The team meeting notes record Option C — Defer. Formal GitHub Reviews are still required from @ZhengZaikun for backend/API/test scope and @Guanyu-Lu for frontend/E2E scope.

The current release supports maximum-budget filtering. It does not promise a separately selected cheaper product that preserves equivalent specifications.

## 2. Repository evidence

### Backend and API

The current API contract and `/api/recommend` response include filters, counts, Top 5, pagination, result data and optional history information. They do not define or return a `budget_alternative` object.

No deterministic rule currently defines:

- how much cheaper an alternative must be;
- whether it must use the same category;
- which specifications may not be reduced;
- how it interacts with ranking, Top 5 or pagination.

### Automated tests

`test_server.py` verifies budget parsing and filtering. It does not contain an acceptance case for selecting a cheaper equivalent product.

### Frontend

`index.html` contains optional rendering compatibility for a budget-alternative field. Because the current API does not produce that field, the display region is not end-to-end implementation evidence.

## 3. Named responsibilities

- @ZhengZaikun confirms that the current backend, API, recommendation and canonical tests do not promise US-09.
- @Guanyu-Lu confirms that the optional interface region does not establish a completed feature and that demonstrations must not imply otherwise.
- @Chu-Junjie maintains the meeting decision, traceability status, known limitation and backlog record.

## 4. Current release wording

> The current release filters recommendations by a user's maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

## 5. Current release impact

| Area | Treatment |
|---|---|
| Backend and recommendation | No alternative-selection algorithm is added. |
| API | No budget-alternative response field is promised. |
| Frontend | Optional rendering compatibility may remain, but it must not be presented as an active feature. |
| Automated tests | No US-09 case is part of the current canonical suite. |
| Deployed E2E | Verify maximum-budget filtering only. |
| Schedule | No additional US-09 implementation enters the current candidate. |

## 6. Future backlog definition

Before US-09 re-enters a release, @ZhengZaikun and @Guanyu-Lu must define and review:

- cheaper-by percentage or absolute threshold;
- same-category requirement;
- protected use-case and specification rules;
- relationship to Top 5 and pagination;
- API fields;
- card, price-difference and empty-state behaviour;
- historical-price limitations;
- automated boundary tests;
- desktop/mobile browser acceptance.

@Chu-Junjie records the future decision and schedules a new Issue, branch and Pull Request.

## 7. Required record updates

- [ ] @Chu-Junjie updates final README wording during reconciliation.
- [x] @Chu-Junjie records `Deferred` in project status and traceability on PR #60.
- [x] @Chu-Junjie removes US-09 from current mandatory release gates.
- [x] @Chu-Junjie records the known limitation in the release package.
- [ ] @ZhengZaikun formally approves PR #47.
- [ ] @Guanyu-Lu formally approves PR #47.

## 8. Responsibility boundary

This record does not modify backend/API/test implementation maintained by @ZhengZaikun or frontend implementation maintained by @Guanyu-Lu. Any future implementation requires a new technical Issue, branch, tests and Pull Request.