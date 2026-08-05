# CP3407 Project Status — Yuyang Unified Baseline

**Evidence date:** 5 August 2026
**Purpose:** Shared factual baseline for the team and AI assistants

## Task 1 governance status

| Item | Final status |
|---|---|
| Coordinator | Chu Junjie |
| Tracking Issue | `#16` — Closed |
| Foundation Pull Request | `#17` — Merged |
| Foundation branch | `docs/project-foundation` |
| Closeout branch | `docs/task1-closeout` |
| Target branch | `main` |
| Non-author reviewer | `@Chu Junjie` |
| Review result | `Approved` |
| Merge commit | `ae9366d` |
| Project Board status | `Done` |
| Project baseline | `Merged` |
| Implementation verification | `Not verified in Task 1` |
| Automated PR checks | `Not run` |

The documentation branch records the adopted direction only. It does not prove that the Yuyang candidate implementation works or that its tests pass.


## Task 2 database integration status

| Item | Final status |
|---|---|
| Coordinator | Chu Junjie |
| Database Pull Request | `#19` — Merged |
| Non-author reviewer | `@Chu Junjie` |
| Review result | `Approved` |
| Merge commit | `f798bd7` |
| Record-count evidence | `products=9000; product_specs=33` |
| ProductID integrity | `Passed — 0 unmatched IDs` |
| Feedback persistence | `Passed` |
| Invalid vote rejection | `Passed` |
| Database tests | `Passed` |
| Project Board status | `Done` |
| Task 2 status | `Completed` |

Task 2 is recorded as completed by the retained database, review, and merge evidence above. The Task 3 update below does not re-run or revalidate Task 2 acceptance checks.

## Task 3 backend CI and compatibility status

| Item | Actual current status |
|---|---|
| Coordinator branch | `feature/share-ci-evidence` |
| Main synchronization | `fbd733c` merged by `e907354`; `server.py`, `index.html`, and `product_specs.csv` inherited from main without coordinator manual edits |
| Dependency manifest | **Candidate for clean-environment use** - reconciled with `origin/main` to six direct project, test, and deployment dependencies; approved ranges and Gunicorn preserved; pytest and requests retained |
| Existing-environment installation | **Passed** - `python -m pip install -r requirements.txt`; exit code `0` |
| Installed dependency consistency | **Passed** - post-`fbd733c` `python -m pip check` reported no broken requirements; exit code `0` |
| Python compilation | **Passed** - post-`fbd733c` `python -m compileall -q .`; exit code `0` |
| Test collection | **Passed** - post-`fbd733c` collection found 21 tests; exit code `0` |
| Historical full test baseline | **Failed, preserved** - 5 failed, 1 passed, 15 errors in 3.03s; exit code `1` |
| Dependency-reconciliation full test baseline | **Failed** - 5 failed, 1 passed, 15 errors in 2.98s; exit code `1` |
| Post-`fbd733c` full test baseline | **Failed** - 4 failed, 2 passed, 15 errors in 3.30s; exit code `1` |
| Legacy fixture compatibility | **Blocked** - obsolete `server.CSV_PATH` patch causes all 15 `test_server.py` setup errors |
| Mock compatibility | **Failed** - 4 failed and 2 passed in `test_mock.py`; one recommend mock improved to pass |
| Database-state isolation | **Failed** - tests modified tracked `digital_products.db`; the side effect was recorded and the committed 401408-byte database restored |
| Coordinator evidence Pull Request | `#25` |
| Backend implementation Pull Request | **Not confirmed** |
| Task 3 | **In Progress** |

The successful installation, consistency, compilation, and collection results do not override the failed full-suite result. The historical, dependency-reconciliation, and post-`fbd733c` baselines are retained as separate evidence. The additional passing mock does not complete a user story. The database side effect also shows that test isolation is incomplete; the generated SQLite change was recorded, restored, and not committed.

## Current repository before Yuyang integration

The original source snapshot contains Flask, SQLite, a 9,000-row `products` table, a Streamlit prototype, a static HTML page with mock recommendations, and existing pytest/mock tests.

## New supplied Yuyang candidate baseline

`yuyang_database_us05_update_v2.zip` provides:

- updated `server.py`;
- `product_specs.csv` with 33 records;
- `test_database_us05.py`;
- dependency baseline;
- `database_us05_update.md`.

The updated backend candidate adds:

- import of `products` and `product_specs`;
- unique indexes on ProductID;
- category inference;
- use-case keyword matching;
- joined recommendation payloads with specifications;
- `/api/compare` for exactly 2 or 3 IDs;
- CORS configuration and safer debug configuration.

## Unified final database direction

| Table | Status | Purpose |
|---|---|---|
| `products` | Existing, 9,000 rows | Category, brand, price and behavioural scoring |
| `product_specs` | Supplied candidate, 33 rows | Real display names, specs, use cases and PurchaseURL for US-05/07 |
| `feedback` | Backend candidate; Task 3 acceptance not evidenced | US-08 persisted up/down feedback |

`brand_links` is removed from the final plan.

## Important limitations

- The 33 specification records form a small educational demonstration set.
- Product prices are inherited from the behavioural dataset and must not be described as current retail prices.
- Specification provenance and licences are not fully verified by the supplied materials.
- Recommendation uses `INNER JOIN`, so the demo recommendation space is limited to products with spec records.
- PurchaseURL may be a manufacturer homepage, not a checkout link.

## Current User Story status after adopting the candidate direction

| Story | Status | Required next action |
|---|---|---|
| US-01 | Improved candidate | Verify category, brand, budget, exclusions and use-case parsing; validate bad inputs |
| US-02 | Existing + improved candidate | Verify both tables, indexes, import safety and deployment initialization |
| US-03 | Backend candidate / frontend pending | Preserve Top 5 and integrate real HTML frontend |
| US-04 | Backend candidate | Verify reasons and display in final HTML |
| US-05 | Database/backend candidate | Merge product_specs and `/api/compare`; integrate 2–3 product comparison UI |
| US-06 | Partial | Support query and explicit excluded_brands consistently |
| US-07 | Data candidate | Use PurchaseURL and safe frontend fallback; document URL limitation |
| US-08 | Backend candidate / Task 3 not evidenced | Verify valid and invalid votes, HTTP response, persistence, and integrated UI |
| US-09 | Backend candidate / Task 3 not evidenced | Verify same-category, cheaper, different-ID, specification-complete alternative and null behavior |
| US-10 | Planned | URL sharing/restoration |

## Known integration blockers

1. All 15 legacy `test_server.py` items stop in fixture setup because the fixture patches obsolete `server.CSV_PATH`.
2. The legacy fixture does not provide separate current-schema products and `product_specs` inputs with matching ProductIDs and a temporary SQLite database.
3. The old mocks do not fully model the current `setup_database()` count-dictionary contract, two-table imports, schema checks, `PRAGMA` responses, or joined queries.
4. The recommend mock now passes, but the health, setup, query, and leaderboard mocks remain incompatible with current behavior.
5. One leaderboard mock asserts an obsolete internal `setup_database()` call.
6. The post-`fbd733c` full test baseline remains failed: 4 failed, 2 passed, and 15 errors; exit code 1.
7. Test execution modifies tracked `digital_products.db`, so complete database-state isolation is not established.
8. Current acceptance evidence is missing for comparison, exclusion merging, product links, feedback, and the budget-alternative rules.
9. The backend implementation Pull Request, review, and merge are not confirmed.

## Task 1 risk register

| ID | Risk | Impact | Responsible technical owner | Tracking owner | Status |
|---|---|---|---|---|---|
| R-01 | Old documents or prompts still describe `brand_links` as part of the final design | Database, API and frontend may follow conflicting contracts | Relevant document owner | Junjie | Closed |
| R-02 | The supplied candidate modifies `server.py` before backend ownership is formally transferred | Conflicting backend changes and difficult merge review | Yuyang and Zaikun | Junjie | Closed |
| R-03 | Existing tests and mocks are incompatible with the two-table setup | Tests collect, but the latest run reports 4 failures and 15 setup errors | Yuyang and Zaikun | Junjie | Open |
| R-04 | The 9,000 behavioural records may be incorrectly described as 9,000 fully specified products | Misleading technical documentation and demonstration claims | All members | Junjie | Closed |
| R-05 | The static HTML mock may be mistaken for completed frontend integration | User Stories may be marked Done without real API evidence | Guanyu | Junjie | Closed |
| R-06 | Candidate or unexecuted work may be reported as Passed, Verified or Done | Invalid project evidence and unreliable traceability | All members | Junjie | Closed |
| R-07 | Database record counts are reported without actual evidence | ... | Closed |
| R-08 | Specification ProductIDs do not match products | ... | Closed |
| R-09 | Feedback reports success without persistence | ... | Closed |
| R-10 | Tests modify shared database | Validation changed tracked `digital_products.db`; the side effect was recorded and restored, but isolation remains incomplete | Backend and test owners | Junjie | Open |
| R-11 | Database PR merged without non-author review | ... | Closed |

## Verification rule

The Yuyang package is the adopted integration direction, but implementation status changes to Done only after code is merged, tests are actually run, a non-author review is completed, and the integrated system is demonstrated.
