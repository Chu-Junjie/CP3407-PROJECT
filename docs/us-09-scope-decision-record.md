# US-09 Scope Decision Record

**Project:** Smart Digital Product Recommendation Platform  
**User story:** US-09 — Budget Alternatives  
**Record owner:** Chu Junjie — Project Manager and Release Coordinator  
**Decision:** Deferred from the current V3 release  
**Backlog milestone:** `Unscheduled`

## 1. Decision

US-09 is deferred from the current V3 release.

The current release supports maximum-budget filtering and ranks eligible products within the selected constraints. It does not promise a separately selected cheaper alternative that preserves equivalent specifications or user experience.

## 2. Repository basis

- `api-contract.md` does not define a budget-alternative response object.
- `/api/recommend` returns filters, counts, pagination, Top 5 recommendations, page data and an optional history ID.
- The backend does not return a separately selected cheaper-equivalent product.
- `test_server.py` contains no US-09 acceptance case.
- `index.html` contains optional display scaffolding, but it remains hidden when the backend does not provide an alternative.
- Interface scaffolding alone is not end-to-end implementation evidence.

## 3. Current-release impact

- No budget-alternative algorithm is added.
- No additional API field is promised.
- No US-09 scenario belongs to the canonical release suite.
- E2E verifies maximum-budget filtering only.
- User-facing documentation must not imply that a cheaper equivalent product is automatically generated.
- US-09 remains visible in the future backlog rather than being reported as completed.

The normal ranked result set may contain lower-priced products that satisfy the selected filters. This is standard recommendation behaviour and is not a dedicated budget-alternative feature.

## 4. Future implementation requirements

A future implementation requires:

- same-category eligibility;
- a defined saving threshold;
- category-specific core specifications;
- deterministic selection;
- visible price savings and trade-offs;
- an explicit API contract;
- desktop and mobile interface states;
- unit, API, E2E and user-acceptance tests;
- no-result behaviour when no suitable alternative exists.

## 5. Risk rationale

Implementing US-09 without a precise equivalence rule could mislead users by presenting a cheaper product as comparable despite missing or inferior core specifications. Deferral avoids an ambiguous release claim and protects recommendation reliability.

## 6. Traceability

| Field | Value |
|---|---|
| Current release status | Deferred |
| Backlog status | Unscheduled |
| Dedicated API support | Not implemented |
| Dedicated frontend behaviour | Not active |
| Automated acceptance | Not included in current release |
| E2E scope | Budget filtering only |
| Release documentation | Limitation must be stated clearly |

## 7. Review checklist

### Backend and algorithm

- [ ] Confirm the current API has no dedicated alternative response.
- [ ] Confirm no current algorithm is represented as satisfying US-09.
- [ ] Confirm deferral introduces no backend regression.

### Frontend

- [ ] Confirm inactive scaffolding does not mislead users.
- [ ] Confirm no interface text promises the deferred feature.
- [ ] Confirm E2E verifies budget filtering only.

### Project and release

- [x] Decision and backlog status recorded.
- [x] Current-release limitation defined.
- [x] Future implementation requirements retained.
- [ ] Formal GitHub approvals recorded.
- [ ] Traceability and final release documentation aligned after merge.

This record is prepared for formal review and merge after the relevant component owners confirm the current API and interface scope.
