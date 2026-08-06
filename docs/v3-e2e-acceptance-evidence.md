# V3 End-to-End Acceptance Evidence

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative baseline:** `feature/product-database`  
**Meeting and evidence record maintained by:** @Chu-Junjie  
**Execution tracking:** Issue #42  
**Document status:** Preparation template — all scenarios remain `Not Run`

## 1. Record basis

The E2E scope and responsibilities are documented in the team meeting notes maintained by @Chu-Junjie. This template does not claim that any browser, deployment, persistence or privacy scenario has passed.

## 2. Named responsibilities

- @Guanyu-Lu executes frontend, GitHub Pages, desktop/mobile, accessibility and browser-Network scenarios.
- @ZhengZaikun confirms API, authentication, recommendation, comparison, favorites, history and feedback behaviour.
- @tiantian09091 confirms PostgreSQL identity, catalogue counts, persistence and database observations.
- @Chu-Junjie maintains meeting notes, evidence IDs, statuses, defect assignments and retest records.

Defect routing:

- frontend/browser/accessibility → @Guanyu-Lu;
- backend/API/authentication/test → @ZhengZaikun;
- database/catalogue/PostgreSQL/persistence → @tiantian09091;
- meeting/status/evidence record → @Chu-Junjie.

## 3. Test baseline

```text
Evidence ID:
Tester:
Named confirmation:
Date/timezone:
Candidate branch:
Candidate SHA:
Frontend URL:
Frontend visible commit:
API URL:
API deployed commit:
Database dialect:
Device/viewport:
Browser/version:
Status: Not Run / Passed / Failed / Blocked / Accepted Limitation
```

Evidence from different commits or environments must be recorded separately.

## 4. Foundation and Network

- [ ] @Guanyu-Lu confirms the frontend loads without blocking console errors.
- [ ] @Guanyu-Lu confirms browser requests reach the intended Render API.
- [ ] @ZhengZaikun confirms request methods, status codes and central API response fields.
- [ ] @tiantian09091 confirms source and historical-price wording is accurate.
- [ ] @Guanyu-Lu records loading, empty, timeout and backend-error states.
- [ ] @Chu-Junjie confirms evidence contains no password, JWT, cookie, authorization header or connection string.

## 5. Authentication and privacy

- [ ] @Guanyu-Lu completes registration, login, current-profile and logout flows.
- [ ] @ZhengZaikun confirms protected endpoints reject unauthenticated access.
- [ ] @ZhengZaikun verifies Account B cannot access Account A history or favorites.
- [ ] @tiantian09091 confirms the private records are stored in the intended PostgreSQL environment.
- [ ] @Guanyu-Lu confirms private browser views are unavailable after logout.

## 6. Recommendation, Top 5 and pagination

- [ ] @Guanyu-Lu submits a valid recommendation request.
- [ ] @ZhengZaikun confirms category, budget, use-case and brand rules.
- [ ] @Guanyu-Lu confirms the separate Top 5 is identifiable.
- [ ] @Guanyu-Lu confirms next/previous navigation preserves the query.
- [ ] @ZhengZaikun confirms page and page-size boundaries.
- [ ] @tiantian09091 confirms returned products have joined specification/source data.
- [ ] @Guanyu-Lu records empty and out-of-range behaviour.

US-09 Budget Alternatives is Deferred. This E2E record verifies maximum-budget filtering only.

## 7. Comparison

- [ ] @Guanyu-Lu compares two valid products.
- [ ] @Guanyu-Lu compares three valid products.
- [ ] @ZhengZaikun confirms invalid, duplicate, missing and unsupported IDs are rejected.
- [ ] @tiantian09091 confirms compared products have valid joined catalogue records.

## 8. Favorites and history

- [ ] @Guanyu-Lu adds and removes a favorite.
- [ ] @Guanyu-Lu compares supported same-category favorites.
- [ ] @ZhengZaikun confirms favorite authorization and validation.
- [ ] @Guanyu-Lu creates, restores and deletes a history record.
- [ ] @ZhengZaikun confirms history authorization and snapshot behaviour.
- [ ] @tiantian09091 confirms favorites/history persist after restart or redeployment.

## 9. Feedback and sharing

- [ ] @Guanyu-Lu submits feedback and records the visible response.
- [ ] @ZhengZaikun confirms feedback validation and API response.
- [ ] @tiantian09091 confirms feedback persistence.
- [ ] @Guanyu-Lu creates a shareable recommendation state.
- [ ] @Guanyu-Lu opens it in an isolated browser session.
- [ ] @ZhengZaikun confirms private account data is not exposed.

## 10. Responsive and accessibility observations

- [ ] @Guanyu-Lu completes the critical flow on desktop.
- [ ] @Guanyu-Lu completes the critical flow on mobile.
- [ ] @Guanyu-Lu checks keyboard access and focus order.
- [ ] @Guanyu-Lu checks visible focus, labels and readable error text.
- [ ] @Guanyu-Lu checks zoom/reflow and records any limitation.

## 11. Persistence scenario

1. @ZhengZaikun verifies creation of Account A and private records.
2. @tiantian09091 records the database state before restart or redeployment.
3. The service is restarted or redeployed.
4. @tiantian09091 confirms the same records remain.
5. @ZhengZaikun verifies cross-user isolation.
6. @Guanyu-Lu verifies the corresponding browser state.
7. @Chu-Junjie records evidence IDs without private values.

## 12. Scenario evidence template

```text
Scenario ID:
Executed by:
Confirmed by:
Candidate SHA:
Environment:
Preconditions:
Steps:
Expected result:
Observed result:
Evidence location:
Status:
Defect Issue and explicit assignee:
Retest result:
```

## 13. Completion criteria

- [ ] @Guanyu-Lu records desktop/mobile browser evidence and accessibility observations.
- [ ] @ZhengZaikun confirms API, authentication, recommendation and privacy observations.
- [ ] @tiantian09091 confirms PostgreSQL, catalogue and persistence observations.
- [ ] @Chu-Junjie confirms every scenario has an honest status and evidence link.
- [ ] Every Failed or Blocked scenario is explicitly assigned to @Guanyu-Lu, @ZhengZaikun or @tiantian09091.
- [ ] Critical defects are fixed through separate reviewed Pull Requests and retested.

A prepared checkbox is not a passed scenario. A missing check remains unchecked.