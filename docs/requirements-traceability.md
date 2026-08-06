# V3 Requirements Traceability Matrix

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation branch:** `feature/product-database`  
**Record owner:** Chu Junjie — Project Manager and Release Coordinator  
**Document state:** Prepared for formal review and final acceptance updates

## 1. Purpose

This matrix links the project's user stories and cross-cutting release requirements to implementation files, automated tests, runtime acceptance and current release status.

Implementation evidence and runtime verification are recorded separately. A story is not classified as release complete solely because related code exists.

## 2. Status definitions

| Status | Meaning |
|---|---|
| Implemented | Required behaviour is present in the V3 repository. |
| Implemented with scope clarification | The release provides a narrower or structured form of the original story. |
| Repository verified | The implementation statement is supported by named repository evidence. |
| Runtime verification pending | Browser, deployment, persistence or acceptance evidence is still required. |
| Deferred | Excluded from the current release and retained in the backlog. |
| Accepted limitation | The limitation is documented and approved for release. |
| Release complete | All implementation, verification, review and acceptance criteria have passed. |

## 3. User-story traceability

### US-01 — Describe product needs

**Original intent:** Allow a user with limited technical knowledge to describe needs without researching detailed specifications.

**Current V3 delivery:** Structured product type, maximum budget, main use, preferred brand and excluded brand controls.

| Field | Record |
|---|---|
| Priority | 10 |
| Planned estimate | 12 ideal days |
| Current status | Implemented with scope clarification |
| Frontend evidence | `index.html` recommendation form |
| Backend evidence | Request-filter parsing and `/api/recommend` in `server.py` |
| Automated evidence | Filter parsing and recommendation tests in `test_server.py` |
| Runtime acceptance | Submit valid and invalid combinations on desktop/mobile |
| Known limitation | Current V3 uses structured controls rather than unrestricted natural-language interpretation |
| Owner review | Guanyu and Zaikun |

### US-02 — Database setup and product import

| Field | Record |
|---|---|
| Priority | 10 |
| Planned estimate | 10 ideal days |
| Current status | Implemented; runtime verification pending |
| Implementation evidence | SQLAlchemy schema, `import_real_catalog.py`, `digital_products.db`, `real_product_catalog.csv`, `product_specs.csv` |
| Repository target | 11,000 products and 2,000 product specifications |
| Automated/repository evidence | Importer validation logic and database setup tests |
| Runtime acceptance | Disposable catalogue build, counts, duplicates, joins, orphans and PostgreSQL verification |
| Operational limitation | Importer must not run directly against production user data |
| Owner review | Yuyang, with Zaikun for API/database integration |

### US-03 — Customized recommendation leaderboard

| Field | Record |
|---|---|
| Priority | 10 |
| Planned estimate | 14 ideal days |
| Current status | Implemented; deployed verification pending |
| Frontend evidence | Results list, match scores, reasons, Top Recommendations and pagination in `index.html` |
| Backend evidence | Scoring, sorting and `/api/recommend` response in `server.py` |
| Automated evidence | Recommendation and pagination cases in `test_server.py` |
| Runtime acceptance | Correct category/budget results, separate Top 5, pagination and stable query state |
| Owner review | Zaikun and Guanyu |

### US-04 — Personalized recommendation explanation

| Field | Record |
|---|---|
| Priority | 20 |
| Planned estimate | 13 ideal days |
| Current status | Implemented; runtime verification pending |
| Frontend evidence | Recommendation reason displayed on product cards |
| Backend evidence | Human-readable reason generated with ranked product payload |
| Automated evidence | Covered indirectly through recommendation payload tests; dedicated wording acceptance may be added |
| Runtime acceptance | Explanations are visible, understandable and consistent with selected preferences |
| Owner review | Zaikun and Guanyu |

### US-05 — Product specification comparison

| Field | Record |
|---|---|
| Priority | 20 |
| Planned estimate | 10 ideal days |
| Current status | Implemented; runtime verification pending |
| Frontend evidence | Product selection and comparison table in `index.html` |
| Backend evidence | `/api/compare` and `/api/favorites/compare` |
| Automated evidence | Comparison validation in `test_server.py` |
| Runtime acceptance | Compare exactly 2 or 3 valid products and reject invalid selections |
| Limitation | Favorite comparison requires products from the same category |
| Owner review | Zaikun and Guanyu |

### US-06 — Exclude unwanted products or features

**Current V3 delivery:** Structured excluded-brand filtering and other category/budget/use-case constraints.

| Field | Record |
|---|---|
| Priority | 30 |
| Planned estimate | 13 ideal days |
| Current status | Implemented with scope clarification |
| Frontend evidence | Excluded-brand control in `index.html` |
| Backend evidence | Exclusion filter handling in recommendation logic |
| Automated evidence | Filter behaviour within `test_server.py` |
| Runtime acceptance | Excluded brand does not appear in returned results |
| Known limitation | Arbitrary free-text deal-breaker extraction is not the current V3 contract |
| Owner review | Zaikun and Guanyu |

### US-07 — Direct product or purchase links

| Field | Record |
|---|---|
| Priority | 40 |
| Planned estimate | 7 ideal days |
| Current status | Implemented with accepted limitation pending review |
| Frontend evidence | Product action URLs rendered from catalogue data |
| Database evidence | `PurchaseURL` retained in product specifications |
| Runtime acceptance | Link opens a valid manufacturer, reference or product page |
| Known limitation | Links may not be live checkout links and catalogue prices are historical snapshots |
| Owner review | Yuyang and Guanyu |

### US-08 — Recommendation feedback

| Field | Record |
|---|---|
| Priority | 40 |
| Planned estimate | 7 ideal days |
| Current status | Implemented; persistence verification pending |
| Frontend evidence | Helpful and Not Helpful controls |
| Backend evidence | `/api/feedback` GET/POST |
| Database evidence | Feedback table and optional user/history/product references |
| Automated evidence | Feedback API test in `test_server.py` |
| Runtime acceptance | Submit feedback and confirm persistence after restart/redeploy |
| Owner review | Zaikun, Yuyang and Guanyu |

### US-09 — Budget alternatives

| Field | Record |
|---|---|
| Priority | 50 |
| Planned estimate | 12 ideal days |
| Current status | Deferred |
| Backlog milestone | `Unscheduled` |
| Decision record | `docs/us-09-scope-decision-record.md` |
| Current supported behaviour | Maximum-budget filtering |
| Excluded release claim | No separately selected cheaper equivalent alternative |
| Current E2E scope | Verify budget filtering only |
| Future requirements | Deterministic eligibility, API field, UI states and complete tests |
| Owner review | Zaikun and Guanyu |

### US-10 — Share recommendation results

| Field | Record |
|---|---|
| Priority | 50 |
| Planned estimate | 10 ideal days |
| Current status | Implemented; deployed verification pending |
| Frontend evidence | Share Results action and state restoration logic |
| Backend dependency | Recommendation request and result reconstruction |
| Runtime acceptance | Open shared state in an isolated browser session without exposing private account data |
| Owner review | Guanyu and Zaikun |

## 4. Cross-cutting V3 requirements

### CR-01 — Registration and authentication

| Field | Record |
|---|---|
| Status | Implemented; deployed verification pending |
| Backend evidence | Register, login and current-user endpoints |
| Security evidence | Password hashing and JWT issue/validation |
| Frontend evidence | Register/login/logout and account controls |
| Automated evidence | Registration/login tests |
| Runtime acceptance | Valid and invalid login, logout and protected-endpoint rejection |

### CR-02 — Private favorites

| Field | Record |
|---|---|
| Status | Implemented; persistence/privacy verification pending |
| Backend evidence | Favorites GET/POST/DELETE and favorite comparison |
| Database evidence | User/product favorite relationship and uniqueness constraint |
| Runtime acceptance | Add/remove, same-category comparison, restart persistence and cross-user isolation |

### CR-03 — Private search history and snapshots

| Field | Record |
|---|---|
| Status | Implemented; persistence/privacy verification pending |
| Backend evidence | History list/detail/delete and saved result snapshots |
| Database evidence | `search_history` and `search_results` |
| Runtime acceptance | Create, restore and delete history; reject access from another account; persist after restart |

### CR-04 — Pagination and complete result access

| Field | Record |
|---|---|
| Status | Implemented; deployed verification pending |
| Backend evidence | `page`, `per_page`, `total_pages` and total candidate fields |
| Frontend evidence | Previous/Next controls and page status |
| Automated evidence | Pagination tests |
| Runtime acceptance | Navigate pages without changing filters and handle invalid pages correctly |

### CR-05 — Public-data provenance and price limitations

| Field | Record |
|---|---|
| Status | Repository verified; final presentation review pending |
| Evidence | `DataSource`, `LastUpdated`, importer source/licence constants and README catalogue disclosure |
| Acceptance | Source wording is visible and no live price/inventory claim is made |

### CR-06 — PostgreSQL production persistence

| Field | Record |
|---|---|
| Status | Supported by implementation; runtime verification pending |
| Evidence | SQLAlchemy engine selection and psycopg dependency |
| Runtime acceptance | `/api/health` reports PostgreSQL; user-owned data persists after restart/redeploy |

### CR-07 — Responsive and accessible interface

| Field | Record |
|---|---|
| Status | Implemented considerations; browser verification pending |
| Evidence | Responsive CSS, labels, status roles, live regions and keyboard-operable controls |
| Runtime acceptance | Critical flow on desktop/mobile, keyboard navigation, focus visibility and zoom/reflow observations |

## 5. Release evidence mapping

| Evidence area | Record |
|---|---|
| Current project status | `docs/project-status.md` |
| Definition of Done | `docs/definition-of-done.md` |
| Execution plan | `docs/v3-execution-plan.md` |
| Final acceptance | `docs/final-acceptance-and-release-checklist.md` |
| Architecture | `docs/v3-design-and-architecture.md` |
| Test workflow | PR #35 |
| Database verification | `docs/v3-database-release-verification-record.md` |
| E2E template | `docs/v3-e2e-acceptance-evidence.md` |
| External acceptance template | `docs/v3-external-uat-record.md` |
| Release evidence index | `docs/v3-release-evidence-index.md` |
| Reconciliation plan | `docs/v3-main-reconciliation-plan.md` |

## 6. Current acceptance summary

| Category | Status |
|---|---|
| Repository implementation | Substantially implemented for current scope |
| Canonical CI for recorded PR ref | 12/12 passed |
| Formal component review | Pending GitHub record |
| Database runtime verification | Not Run |
| Deployed frontend/API identity | Unverified |
| PostgreSQL persistence/privacy | Not Run |
| Desktop/mobile E2E | Not Run |
| External acceptance | Not Run |
| Reconciliation to `main` | Not started |
| Release tag/package | Not created |

## 7. Approval checklist

- [ ] Zaikun confirms backend/API/test mappings.
- [ ] Yuyang confirms database/catalogue/provenance mappings.
- [ ] Guanyu confirms frontend/interaction/accessibility mappings.
- [ ] Junjie records formal review outcomes.
- [ ] Runtime results are linked to the affected requirements.
- [ ] Accepted limitations are approved.
- [ ] Final release-candidate evidence is recorded.

This traceability matrix is ready for formal review. Status values must be updated only from retained review or execution evidence.
