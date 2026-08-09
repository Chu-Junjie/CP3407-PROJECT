# Requirements Traceability — Teacher Feedback Revision v3.0

**Evidence date:** 6 August 2026  
**Coordinator:** Chu Junjie  
**Authoritative implementation baseline:** `feature/product-database`  
**Governance branch:** `docs/junjie-v3-governance`

## 1. Status vocabulary

| Status | Meaning |
|---|---|
| `Planned` | Approved requirement exists, but implementation evidence is absent. |
| `Candidate` | Code or data exists but has not completed the applicable verification gates. |
| `Implemented` | The feature exists on the authoritative branch; review, deployment or acceptance may remain incomplete. |
| `Verified` | Named automated or manual evidence has passed for a named commit/environment. |
| `Blocked` | A specific unresolved dependency prevents verification or completion. |
| `Done` | All applicable Definition of Done gates are satisfied. |
| `Scope confirmation required` | The teacher-feedback revision may have changed or removed the original requirement. |

`Implemented`, `Verified` and `Done` are deliberately different. Repository presence alone is not pass evidence.

## 2. Baseline and change-control evidence

| Evidence item | Current record |
|---|---|
| Historical foundation tracking | Issue `#16`, PR `#17`, closeout PR `#20` |
| Historical v2 baseline | 9,000 `products` and 33 `product_specs`; retained as historical only |
| Adopted v3 implementation branch | `feature/product-database` |
| V3 governance branch | `docs/junjie-v3-governance` |
| Teacher-feedback record | `teacher-feedback-change-request.md` |
| V3 API contract | `api-contract.md` |
| V3 project status | `docs/project-status.md` |
| V3 execution plan | `docs/v3-execution-plan.md` |
| Final acceptance checklist | `docs/final-acceptance-and-release-checklist.md` |
| Review/merge status | Not yet evidenced for the complete v3 baseline |
| Production deployment acceptance | Not yet evidenced |

## 3. User Story traceability matrix

| ID | Requirement | V3 implementation / target | Current repository evidence | Owner(s) | Remaining evidence | Current status |
|---|---|---|---|---|---|---|
| US-01 | Parse natural-language product needs, including category and budget | Revised request parsing in `server.py` | `test_server.py` includes budget/category parsing checks | Zaikun | Invalid values, boundaries, integrated request/response and deployed evidence | Implemented |
| US-02 | Create and populate the product database | SQLAlchemy setup; SQLite local seed; PostgreSQL through `DATABASE_URL`; 11,000 products and 2,000 specs | `digital_products.db`, `import_real_catalog.py`, `real_product_catalog.csv`, health/count tests | Yuyang | Clean initialization, exact release counts, repeat safety, PostgreSQL seed and persistence evidence | Implemented |
| US-03 | Return ranked personalised recommendations | Paginated recommendations, default 20 and maximum 100, with separate Top 5 | `/api/recommend` contract and pagination tests in `test_server.py` | Zaikun + Guanyu | Complete API assertions, browser Network evidence and deployed pagination acceptance | Implemented |
| US-04 | Explain recommendation reasons and scores | Result payload contains match score and reason | Backend and frontend implementation on the v3 branch | Zaikun + Guanyu | Unit assertions for ranking/reasons and manual UI readability evidence | Implemented |
| US-05 | Compare exactly 2 or 3 products | `/api/compare` plus frontend comparison | `test_compare_requires_two_or_three_products`; revised UI implementation | Yuyang + Zaikun + Guanyu | Duplicate/missing/invalid-ID cases, field completeness and deployed UI evidence | Implemented |
| US-06 | Exclude unwanted brands | Query and explicit `excluded_brands` accepted by revised recommendation contract | `api-contract.md` and backend candidate | Zaikun | Regression tests proving combined exclusions and frontend request evidence | Candidate |
| US-07 | Provide a safe product/source link | `PurchaseURL` and `DataSource` supplied with catalogue results | Public-catalogue import files and revised frontend labels | Yuyang + Guanyu | URL protocol validation, broken/missing fallback and limitation wording acceptance | Candidate |
| US-08 | Store helpful/not-helpful feedback | `POST /api/feedback`; aggregate `GET /api/feedback` | `test_feedback_is_stored_and_summarised` | Yuyang + Zaikun + Guanyu | Invalid vote, ownership/history linkage where applicable, production persistence and UI evidence | Implemented |
| US-09 | Show a cheaper budget alternative | Original v2 story; not clearly retained in the revised v3 API contract | No final v3 acceptance evidence identified | Zaikun + Guanyu | Team decision: retain with revised criteria or defer with reason and impact | Scope confirmation required |
| US-10 | Share and restore recommendation results | Revised frontend contains share/restore behaviour | `index.html` implementation candidate | Junjie + Guanyu | Special characters, filters/exclusions, second-browser restoration and deployed evidence | Candidate |
| V3-US-11 | Register and log in securely | Password hashes and JWT registration/login | `/api/auth/register`, `/api/auth/login`, `/api/auth/me`; auth test | Zaikun | Invalid/duplicate credentials, token expiry/configuration, clean-environment and deployed evidence | Implemented |
| V3-US-12 | Preserve private search history and result snapshots | Authenticated history list/detail/delete | History endpoints and privacy/persistence tests | Zaikun + Guanyu | Cross-user denial test, pagination/boundaries, redeploy persistence and frontend evidence | Implemented |
| V3-US-13 | Save and compare favorite products | User-owned favorites and same-category favorite comparison | Favorites endpoints and tests in `test_server.py` | Zaikun + Guanyu | Duplicate/idempotent behaviour, cross-user denial and deployed UI evidence | Implemented |
| V3-US-14 | Browse all matches through pagination | Page/per-page metadata and controls; Top 5 retained separately | Pagination contract, backend tests and frontend implementation | Zaikun + Guanyu | First/last/empty/out-of-range page tests and browser evidence | Implemented |
| V3-US-15 | Use persistent production storage | PostgreSQL selected by `DATABASE_URL` | SQLAlchemy implementation and deployment notes | Yuyang + Zaikun | Render PostgreSQL provisioning, migration/seed, restart/redeploy persistence and rollback evidence | Candidate |

## 4. Non-functional requirements

| ID | Requirement | Target evidence | Owner(s) | Current status |
|---|---|---|---|---|
| NFR-01 | Responsive and usable interface | Desktop/mobile screenshots, keyboard path and error-state evidence | Guanyu | Not verified |
| NFR-02 | Authentication and privacy | Password hashes, JWT secret configuration, authorization and cross-user denial tests | Zaikun | Partially evidenced |
| NFR-03 | Data provenance and honest pricing claims | Source, licence, transformation and historical-price statements | Yuyang | Implemented; review pending |
| NFR-04 | Reproducible database setup | Import command, exact counts, integrity checks and PostgreSQL setup | Yuyang | Implemented candidate |
| NFR-05 | Automated regression protection | Clean-environment full suite and successful GitHub Actions workflow | Technical owners; Junjie tracks | Not verified |
| NFR-06 | Production availability and persistence | Render API/GitHub Pages smoke test and PostgreSQL persistence evidence | Zaikun + Yuyang + Guanyu | Not verified |
| NFR-07 | Honest project evidence | Command, date, commit SHA, result, reviewer and limitations | All; Junjie coordinates | In Progress |
| NFR-08 | No secrets in repository | Repository review plus production environment-variable evidence | Zaikun + Junjie audit | Not verified |

## 5. Current automated-test evidence

The authoritative branch documentation records:

```text
.venv/bin/pytest -q
12 passed
```

This is retained as branch-reported local evidence, not yet as final CI evidence. Before release, the team must record:

- the tested commit SHA;
- Python and dependency environment;
- the complete collected test count;
- whether old `test_mock.py` is updated, archived or intentionally excluded;
- exit code and elapsed result;
- confirmation that tracked database/data files remain unchanged;
- a successful clean-environment or GitHub Actions run.

## 6. Required completion evidence per story

Each final `Done` story must identify:

| Field | Required record |
|---|---|
| Requirement | Final wording and acceptance criteria |
| Scope decision | Retained, revised or deferred after teacher feedback |
| Owner | Responsible member(s) |
| Branch and commit | Exact ref and SHA |
| Pull Request | Number and target branch |
| Reviewer | Non-author reviewer and result |
| Automated evidence | Command, environment, passed/failed counts and exit code |
| Manual evidence | Date, tester, steps and observed result |
| Deployment evidence | URL/environment and smoke-test result where applicable |
| Documentation | Updated file paths |
| Limitations | Honest known limitations |
| Final status | `Done` only when all applicable gates pass |

## 7. Ownership rule

The coordinator updates traceability and evidence status only. Technical implementation changes remain with the assigned database, backend and frontend owners. A missing result is recorded as missing; it is not repaired or marked passed by editing a teammate-owned file without approval.
