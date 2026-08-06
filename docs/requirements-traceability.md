# V3 Requirements Traceability

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Evidence date:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Inspected baseline:** `7c406515bd4b657372fe519869596825cdf91d56`

## 1. Status definitions

| Status | Meaning |
|---|---|
| `Candidate` | Partial code or data exists, but the complete requirement is not established. |
| `Implemented` | The feature exists on the authoritative branch. |
| `Repository verified` | Source, contract or test files directly support the statement. |
| `CI verified` | A named automated check passed for a named ref and environment. |
| `Deferred` | The requirement is not part of the current release and remains in the backlog. |
| `Blocked` | A specific missing runtime result prevents completion. |
| `Done` | All applicable implementation, review, test, deployment and acceptance gates passed. |

`Implemented`, `CI verified` and `Done` are different states.

## 2. Baseline evidence

| Evidence item | Current record |
|---|---|
| Authoritative V3 branch | `feature/product-database` |
| Inspected V3 commit | `7c406515bd4b657372fe519869596825cdf91d56` |
| API contract | `api-contract.md` |
| Backend and schema | `server.py` |
| Frontend | `index.html` |
| Catalogue importer | `import_real_catalog.py` |
| Current V3 tests | `test_server.py` |
| Historical compatibility tests | `test_mock.py` — Practical 8, Task 7, non-release audit |
| Canonical CI workflow branch | PR #35, commit `4e698826dbeac719b56f1ff5cea060109d0bdd60` |
| Successful workflow run | `31096706920` |
| US-09 decision | Issue #40 / PR #47 — Deferred |
| Database repository record | Issue #41 / PR #48 |
| Deployment/E2E tracking | Issue #42 |
| Reconciliation tracking | Issue #43 / PR #44 |

## 3. User Story matrix

| ID | Requirement | Repository implementation/evidence | Remaining evidence | Current status |
|---|---|---|---|---|
| US-01 | Parse product needs including category and budget | Parsing functions and `test_budget_and_category_are_parsed` | Invalid/boundary cases and deployed request evidence | Implemented; CI subset verified |
| US-02 | Create and populate product database | SQLAlchemy setup, SQLite seed, PostgreSQL selection, importer quotas | Actual release counts, repeatability, PostgreSQL initialization and persistence | Implemented; runtime blocked |
| US-03 | Return ranked personalised recommendations | `/api/recommend`, pagination and separate Top 5; pagination tests | Ranking boundary and deployed browser evidence | Implemented; CI subset verified |
| US-04 | Explain recommendation reasons and scores | Result construction and frontend display | Direct reason/score assertions and UI readability evidence | Implemented |
| US-05 | Compare exactly 2 or 3 products | `/api/compare`; automated 1-ID rejection and 2-ID success | Three, duplicate, invalid and missing-ID cases; deployed UI | Implemented; partial CI verified |
| US-06 | Exclude unwanted brands | Query and explicit exclusion support in contract/implementation | Combined exclusions and deployed request evidence | Candidate |
| US-07 | Provide safe product/source links | `PurchaseURL`, `DataSource`, importer metadata and frontend link handling | Protocol validation, fallback and deployed limitation wording | Candidate |
| US-08 | Store helpful/not-helpful feedback | Feedback POST/GET and aggregate automated test | Invalid vote, linkage and production persistence | Implemented; partial CI verified |
| US-09 | Show a cheaper budget alternative | Backend/API/test evidence does not implement it; frontend renderer is optional scaffolding | Future deterministic rules, API/UI contract, tests and E2E | **Deferred — Unscheduled** |
| US-10 | Share and restore recommendation results | Frontend share/restore implementation candidate | Special characters, exclusions and isolated-browser E2E | Candidate |
| V3-US-11 | Register and log in securely | Password hashes, JWT endpoints and auth test | Duplicates, invalid credentials, token expiry/configuration and deployed evidence | Implemented; partial CI verified |
| V3-US-12 | Preserve private history and result snapshots | History list/detail/delete and private-history tests | Cross-user denial, boundaries and redeploy persistence | Implemented; partial CI verified |
| V3-US-13 | Save and compare favorites | Favorite endpoints, private persistence and same-category tests | Duplicate/unowned/cross-user and deployed UI evidence | Implemented; partial CI verified |
| V3-US-14 | Browse matches through pagination | Page metadata, controls and page-one/page-two tests | Empty/out-of-range/maximum boundaries and deployed browser evidence | Implemented; partial CI verified |
| V3-US-15 | Use persistent production storage | SQLAlchemy PostgreSQL selection through `DATABASE_URL` | Deployed dialect, initialization, restart persistence and recovery | Candidate; blocked |

## 4. US-09 release decision

**Status:** Deferred  
**Backlog milestone:** Unscheduled

Repository basis:

- the API contract contains no budget-alternative response field;
- the backend recommendation response contains no alternative object;
- the canonical V3 tests contain no alternative-selection acceptance case;
- the frontend only renders an optional field when supplied.

Release limitation:

> The current release filters recommendations by a user's maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

## 5. Non-functional requirements

| ID | Requirement | Current evidence | Remaining gate | Status |
|---|---|---|---|---|
| NFR-01 | Responsive and usable interface | Responsive CSS and accessibility-oriented markup | Desktop/mobile/keyboard deployed evidence | Not verified |
| NFR-02 | Authentication and privacy | Hashing/JWT design and private route tests | Cross-user negative tests and deployed configuration | Partially verified |
| NFR-03 | Data provenance and honest pricing | Source/licence constants, DataSource and historical-price wording | Independent source review and final UI/docs check | Repository verified |
| NFR-04 | Reproducible database setup | Deterministic importer, quotas and `verify_database()` | Retained command output and PostgreSQL initialization | Implemented; runtime blocked |
| NFR-05 | Automated regression protection | Successful canonical GitHub Actions job | Release-candidate rerun and remaining critical coverage | CI verified for PR ref |
| NFR-06 | Production availability and persistence | Hosting/database configuration in source | Deployed identity, smoke test and restart persistence | Not verified |
| NFR-07 | Evidence integrity | Issues, Draft PRs and explicit evidence vocabulary | Final review and release evidence | In progress |
| NFR-08 | No repository secrets | Environment-variable design | Final tracked/history scan and hosting confirmation | Not verified |

## 6. Canonical automated evidence

### Required V3 release suite

```bash
python -m pytest -q test_server.py
```

| Field | Evidence |
|---|---|
| Workflow run | `31096706920` |
| Workflow source commit | `4e698826dbeac719b56f1ff5cea060109d0bdd60` |
| Tested PR merge ref | `8ecdb5fea8829a85521825b864a9bfe6e630a4ff` |
| Environment | Ubuntu 24.04.4, Python 3.11.15, pytest 9.1.1 |
| Collection | 12 |
| Result | 12 passed in 1.23s |
| Integrity | `git diff --exit-code` passed |
| Conclusion | Success |

### Historical compatibility audit

`test_mock.py` collected six and recorded six expected V2 compatibility failures. It remains visible as historical evidence but is excluded from the V3 release suite because it patches interfaces removed by the SQLAlchemy/API revision.

## 7. Database traceability

Repository-derived targets:

| Item | Target/source basis | Runtime state |
|---|---|---|
| Total products | 9,000 retained rows + 2,000 imported rows | Expected 11,000; not run for release DB |
| Product specifications | Importer quotas | Expected 2,000; not run for release DB |
| Laptops | Importer quota | 800 target |
| Smartphones | Importer quota | 833 target |
| Smart watches | Importer quota | 300 target |
| Headphones | Importer quota | 61 target |
| Tablets | Importer quota | 6 target |
| PostgreSQL | `DATABASE_URL` selection in source | Deployed dialect unverified |
| Persistence | User/favorite/history/feedback schema | Restart/redeploy not run |

The importer is intended to build a clean catalogue artifact and must not run against a live production database containing private user data.

## 8. Evidence required for `Done`

Each story marked `Done` must identify:

| Field | Required record |
|---|---|
| Final wording | Unambiguous requirement and acceptance criteria |
| Scope status | Included, revised or deferred |
| Owner | Responsible component owner(s) |
| Branch/commit | Exact tested ref and SHA |
| Pull Request | Number and target branch |
| Review | Actual non-author GitHub result |
| Automated evidence | Command, environment, counts, exit result |
| Manual evidence | Tester, date, steps and observations |
| Deployment evidence | URL, environment and deployed commit where applicable |
| Limitations | Known constraints and accepted risks |
| Final status | `Done` only after all applicable gates pass |

## 9. Ownership rule

The coordinator updates traceability and evidence status. This document does not modify teammate-owned backend, frontend, tests, datasets, database files, importers or deployment settings.
