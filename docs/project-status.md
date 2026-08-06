# V3 Project Status

**Project:** Smart Digital Product Recommendation Platform  
**Coordinator:** Chu Junjie  
**Status date:** 6 August 2026, Singapore time (UTC+8)  
**Authoritative implementation branch:** `feature/product-database`  
**Inspected implementation baseline:** `7c406515bd4b657372fe519869596825cdf91d56`

## 1. Executive status

The V3 implementation is present on `feature/product-database`. The project is in release verification and integration preparation, not final release.

Current position:

- core V3 backend, frontend, account, catalogue and persistence structures are implemented;
- the canonical V3 automated suite is defined and has passed in GitHub Actions;
- US-09 Budget Alternatives is deferred from the current release;
- catalogue, schema and importer design have been verified from repository source;
- deployed PostgreSQL identity, persistence, browser end-to-end testing and external acceptance remain open;
- team review is deferred and no approval is inferred;
- reconciliation with `main` has not started.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| `Implemented` | Code, data or documentation exists on the authoritative branch. |
| `Repository verified` | The statement is directly supported by version-controlled source, tests or contracts. |
| `CI verified` | A named workflow check passed for a named ref and environment. |
| `Prepared` | A plan, template or procedure exists but has not been executed. |
| `Deferred` | The item is outside the current release and remains in the backlog. |
| `Blocked` | A missing runtime result or dependency prevents release completion. |
| `Not Run` | The required verification has not been executed. |
| `Unverified` | The target environment or result is not confirmed. |
| `Done` | All applicable review, test, deployment and acceptance gates have passed. |

## 3. Technical baseline

| Area | Current V3 direction | Status |
|---|---|---|
| Backend | Python, Flask and SQLAlchemy | Implemented |
| Local persistence | Bundled SQLite seed/demo database | Implemented; release-file integrity still required |
| Production persistence | PostgreSQL selected through `DATABASE_URL` | Implemented in code; deployed runtime unverified |
| Catalogue | 11,000 target product rows, including 2,000 imported catalogue rows | Repository verified target; runtime count not run |
| Specifications | 2,000 recommendation-ready `product_specs` rows | Repository verified target; runtime count not run |
| Accounts | Password hashing and JWT authentication | Implemented; deployed security checks open |
| Private features | Favorites, history, result snapshots and feedback | Implemented; deployed persistence/privacy checks open |
| Recommendations | Budget/category filtering, ranking, pagination and separate Top 5 | Implemented; deployed browser verification open |
| Frontend | Responsive HTML/CSS/JavaScript client | Implemented on V3 branch; deployed identity unverified |
| Hosting | GitHub Pages frontend and Render API candidate endpoints | Configuration exists; deployed commits unverified |

## 4. Database structure

The V3 source defines seven application tables:

| Table | Purpose | Repository status |
|---|---|---|
| `products` | Behavioural and imported product records | Implemented |
| `product_specs` | Recommendation-ready specifications and source metadata | Implemented |
| `users` | Account identity and password hashes | Implemented |
| `favorites` | User-owned saved products | Implemented |
| `search_history` | User-owned searches and filters | Implemented |
| `search_results` | Saved ranked result snapshots | Implemented |
| `feedback` | Helpful/not-helpful records | Implemented |

Actual PostgreSQL table creation, row counts and delete behaviour remain runtime verification items.

## 5. Automated test and CI status

### Canonical V3 suite

```bash
python -m pytest -q test_server.py
```

GitHub Actions evidence:

| Field | Result |
|---|---|
| Workflow | `V3 Test Evidence` |
| Run | `31096706920` |
| Workflow source commit | `4e698826dbeac719b56f1ff5cea060109d0bdd60` |
| Tested PR merge ref | `8ecdb5fea8829a85521825b864a9bfe6e630a4ff` |
| Runner | Ubuntu 24.04.4 |
| Python | 3.11.15 |
| pytest | 9.1.1 |
| Collection | 12 tests |
| Result | 12 passed in 1.23s |
| Tracked-file integrity | Passed |
| Workflow conclusion | Success |

### Historical mock audit

`test_mock.py` is retained as Practical 8, Task 7 evidence and targets removed V2 Pandas/raw-SQLite contracts. It is not part of the V3 release suite.

The non-release audit collected six tests and recorded six expected compatibility failures. The failures remain visible, but do not block the canonical V3 job.

The canonical suite must be rerun for the eventual frozen release candidate.

## 6. User Story status

| Story | Current release status | Remaining release evidence |
|---|---|---|
| US-01 Natural-language input | Implemented | Invalid/boundary and deployed request evidence |
| US-02 Database setup/import | Implemented | Actual counts, local repeatability and PostgreSQL evidence |
| US-03 Recommendations | Implemented | Deployed pagination and Top 5 evidence |
| US-04 Explanations | Implemented | Ranking/reason assertions and UI readability evidence |
| US-05 Comparison | Implemented | Invalid/duplicate/missing-ID and deployed UI evidence |
| US-06 Excluded brands | Candidate | Combined text/explicit exclusion regression evidence |
| US-07 Product/source links | Candidate | URL safety, fallback and deployed wording evidence |
| US-08 Feedback | Implemented | Invalid vote, linkage and deployed persistence evidence |
| US-09 Budget alternatives | **Deferred** | Backlog item, milestone `Unscheduled` |
| US-10 Share/restore | Candidate | Special-character and isolated-browser evidence |
| V3-US-11 Accounts | Implemented | Negative auth, token and deployed security evidence |
| V3-US-12 Private history | Implemented | Cross-user denial and redeploy persistence evidence |
| V3-US-13 Favorites | Implemented | Duplicate/unowned/cross-user and deployed evidence |
| V3-US-14 Pagination | Implemented | Boundary and deployed browser evidence |
| V3-US-15 Production storage | Candidate | PostgreSQL identity, initialization and persistence evidence |

US-09 limitation statement:

> The current release filters recommendations by a user's maximum budget. It does not separately identify a cheaper alternative that preserves equivalent specifications.

## 7. Catalogue and importer findings

Repository inspection confirms:

- imported IDs begin at `10,000,001`;
- the importer defines 800 laptops, 833 smartphones, 300 smart watches, 61 headphones and 6 tablets;
- the target is 11,000 total products and 2,000 specification rows;
- source and licence metadata are retained;
- EUR→USD uses `1.08` and INR per USD uses `83.0`;
- prices are historical dataset snapshots, not live inventory or live retailer prices;
- built-in validation checks specification count, category quotas and absence of private rows in the generated catalogue artifact.

Operational restriction:

> The importer is a catalogue-build tool and must not be executed directly against a live production database containing user data.

## 8. Programme stage status

| Stage | Lead | Status | Exit condition |
|---|---|---|---|
| Scope and change control | Junjie | Repository decisions complete; review deferred | Actual review and approved merge of coordinator records |
| Catalogue/database verification | Yuyang; Junjie tracks | Repository verification complete; runtime blocked | Counts, PostgreSQL identity, persistence and recovery evidence |
| Backend/API verification | Zaikun; Junjie tracks | Canonical CI verified | Release-candidate rerun and remaining negative/boundary coverage |
| Frontend/deployed E2E | Guanyu; Junjie tracks | Not Run | Confirmed deployed commits and completed browser matrix |
| External acceptance | Junjie | Not Run | Two non-team participant records and defect decisions |
| Documentation consolidation | Junjie coordinates | In Progress | Current documents agree with final verified release |
| Branch reconciliation | All affected owners; Junjie coordinates | Not started | Explicit approval, reviewed integration branch and final checks |
| Final release | Junjie coordinates | Not started | Release checklist, tag and package complete |

## 9. Open blockers

1. Actual review and merge of Draft PRs are deferred.
2. Local catalogue verification output has not been retained for the release candidate.
3. Render API commit and active PostgreSQL dialect are unverified.
4. PostgreSQL initialization and persistence after restart/redeploy are not tested.
5. GitHub Pages deployed commit is unverified.
6. Browser E2E and accessibility checks are not run.
7. External acceptance is not run.
8. `main` reconciliation requires separate explicit approval.
9. Final README, release tag and package do not yet exist.

## 10. Risk register

| ID | Risk | Control | Status |
|---|---|---|---|
| V3-R01 | Older V2 evidence is mistaken for current behaviour | V3 baseline and historical test classification are explicit | Controlled |
| V3-R02 | Historical mock failures are presented as V3 regressions | Separate non-release audit job | Controlled |
| V3-R03 | Catalogue targets are reported as observed production counts | Repository targets and runtime results are separated | Open |
| V3-R04 | Importer removes live private data | Prohibit direct execution against production user DB | Controlled by process |
| V3-R05 | PostgreSQL secrets or user data are exposed | Environment variables, redaction and secret scan | Open |
| V3-R06 | Deployed auth/history permits cross-user access | Negative deployed tests required | Open |
| V3-R07 | Frontend and API deployments serve different commits | Deployment identity gate before E2E | Open |
| V3-R08 | Historical prices are described as live | Limitation wording and source metadata | Controlled; final UI/docs check open |
| V3-R09 | Release occurs without UAT or backup evidence | Final checklist blocks release | Open |

## 11. Ownership boundary

Junjie may update governance, planning, traceability, acceptance and release documents. This status update does not modify teammate-owned backend, frontend, automated tests, data, importer, database or deployment configuration.

Repository presence is not deployment evidence. No item is marked `Done` until its applicable gates have actual retained evidence.
