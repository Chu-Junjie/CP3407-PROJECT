# Task 3 Backend CI and Test Evidence

## Document control

| Item | Current record |
|---|---|
| Evidence dates | 2-3 August 2026 |
| Coordinator | Chu Junjie |
| Repository | `C:\JCU\CP3407\CP3407-PROJECT` |
| Working branch | `feature/share-ci-evidence` |
| Coordinator scope | Dependency, test, CI-readiness, traceability, and handoff evidence only |
| Backend Pull Request | Not confirmed |
| Overall Task 3 status | **In Progress** |

No backend or test implementation changes are part of this coordinator evidence update. In particular, `server.py`, `test_server.py`, and `test_mock.py` must remain unchanged.

## Status vocabulary

| Status | Meaning |
|---|---|
| Passed | The check ran successfully and has saved output with exit code `0`. |
| Failed | The check ran and reported failures. |
| Blocked | A named incompatibility prevents the relevant test bodies or completion gate from being exercised. |
| Candidate | The artifact exists and has been audited, but its clean-environment use has not been verified. |
| Not evidenced | No applicable successful test or retained acceptance evidence was found. |
| Not confirmed | Repository evidence is insufficient to make the claim. |

## Dependency status

`requirements.txt` was reconciled with `origin/main` in merge commit `d412853`. The final manifest contains these six direct project, test, and deployment dependencies:

```text
Flask>=3.0,<4.0
Flask-Cors>=4.0,<7.0
gunicorn>=22,<24
pandas>=2.0,<3.0
pytest
requests
```

The reconciliation preserves the Flask, Flask-Cors, and pandas version ranges and Gunicorn introduced by `origin/main`. It retains pytest and requests for the Task 3 test work. The earlier package-freeze-style manifest remains superseded; `pip freeze` was not used to create this manifest.

| Check | Actual result | Status |
|---|---|---|
| Manifest reconciliation | All six approved dependencies are present once, with the approved version ranges and no unrelated package | Passed |
| Installation in the existing environment | `python -m pip install -r requirements.txt` completed with exit code `0` | Passed |
| Installed-environment consistency | The post-merge `python -m pip check` reported `No broken requirements found.`; exit code `0` | Passed |
| Clean installation from this manifest | Not executed in a newly created environment | Not evidenced |

The manifest remains a **Candidate for clean-environment use** until installation is verified in a newly created environment. The successful install and `pip check` validate the existing Python 3.14.6 environment.

## Original coordinator check results

The managed terminal did not expose `python` on `PATH`; the first literal `python -m pip check` attempt therefore exited `1` before Python ran. The requested checks were then executed with the existing interpreter at `C:\Users\29034\AppData\Local\Programs\Python\Python314\python.exe`, which reported Python `3.14.6`.

| Check | Requested command | Actual result | Exit code | Status | Evidence |
|---|---|---|---:|---|---|
| Dependency consistency | `python -m pip check` | `No broken requirements found.` | `0` | Passed | `docs/evidence/task3-pip-check.txt` |
| Python compilation | `python -m compileall -q .` | No output | `0` | Passed | `docs/evidence/task3-python-compileall.txt` |
| Dedicated pytest collection | `python -m pytest --collect-only -q` | `21 tests collected in 2.12s` | `0` | Passed | `docs/evidence/task3-pytest-collect-only.txt` |

Collection success proves discovery only. It does not show that the collected tests pass.

## Preserved historical full-suite baseline

The full suite was not rerun during the original 2 August evidence update because the existing result was verifiable in `docs/evidence/task3-pytest-baseline.txt`.

```text
Python: 3.14.6
pytest: 9.1.1
Full result: 5 failed, 1 passed, 15 errors in 3.03s
Exit code: 1
Overall result: Failed
```

The preserved baseline file had SHA-256 `F911205C15E8DCFCE539382414CA78B3C0204E8ADB88B09428D9A470F5430BA2` before this update. It was not overwritten or deleted.

## Post-requirements-merge validation

The reconciled manifest was installed and the checks were rerun separately on 3 August 2026. These new artifacts do not overwrite the historical baseline.

| Check | Command | Actual result | Exit code | Status | Evidence |
|---|---|---|---:|---|---|
| Manifest installation | `python -m pip install -r requirements.txt` | Installation completed; Gunicorn 23.0.0 and pandas 2.3.3 were installed | `0` | Passed | `docs/evidence/task3-pip-install-after-requirements-merge.txt` |
| Dependency consistency | `python -m pip check` | `No broken requirements found.` | `0` | Passed | `docs/evidence/task3-pip-check-after-requirements-merge.txt` |
| Python compilation | `python -m compileall -q .` | No output | `0` | Passed | `docs/evidence/task3-compile-after-requirements-merge.txt` |
| Pytest collection | `python -m pytest --collect-only -q` | `21 tests collected in 7.13s` | `0` | Passed | `docs/evidence/task3-pytest-collection-after-requirements-merge.txt` |
| Focused server tests | `python -m pytest test_server.py -v` | `15 errors in 2.89s` | `1` | Blocked | `docs/evidence/task3-test-server-after-requirements-merge.txt` |
| Focused mock tests | `python -m pytest test_mock.py -v` | `5 failed, 1 passed in 2.60s` | `1` | Failed | `docs/evidence/task3-test-mock-after-requirements-merge.txt` |
| Full pytest suite | `python -m pytest -q` | `5 failed, 1 passed, 15 errors in 2.98s` | `1` | Failed | `docs/evidence/task3-pytest-baseline-after-requirements-merge.txt` |

The new full-suite baseline has the same failure counts and classifications as the preserved historical baseline. Collection success is still not pass evidence.

## Failure classification

### Legacy `test_server.py` fixture incompatibility

All 15 collected `test_server.py` items error during the autouse fixture setup at:

```python
monkeypatch.setattr(server, "CSV_PATH", csv_path)
```

The current backend has no `CSV_PATH`. It uses `PRODUCTS_CSV_PATH`, `SPECS_CSV_PATH`, and `DB_PATH`. Because setup fails, none of the 15 legacy test bodies executes.

The fixture must use temporary products and `product_specs` inputs with complete current schemas, matching unique `ProductID` values, and a temporary SQLite database. Restoring an obsolete production alias solely to satisfy the fixture is not an acceptable fix.

**Status: Blocked by fixture setup.**

### `test_mock.py` compatibility failures

The preserved baseline records five failures and one pass in `test_mock.py`. The passing item is `test_mock_missing_csv_error_response`.

| Failure | Current incompatibility |
|---|---|
| `test_mock_database_setup_imports_csv_when_table_is_missing` | A products-only dataframe is reused when current setup separately imports `product_specs`; the setup return contract is now a count dictionary. |
| `test_mock_health_endpoint_without_real_database` | Patching only `setup_database` does not isolate current schema and joined-count queries; the test reaches a missing `product_specs` table. |
| `test_mock_recommend_endpoint_without_running_real_engine` | The mock does not isolate the current budget-alternative/data-initialization path and reaches real database initialization. |
| `test_mock_database_query_contains_exclusion_filter` | The mock lacks current per-table schema, `PRAGMA table_info`, and joined-query responses. |
| `test_mock_leaderboard_uses_controlled_candidate_products` | It expects the obsolete internal behavior that `build_leaderboard()` directly calls `setup_database()`. |

**Status: Failed.**

## US-01 through US-09 evidence mapping

The `test_usNN` prefixes reflect the legacy test numbering. They are listed exactly as collected; where the current story definition differs, the limitation is stated.

| User Story | Actual collected tests or evidence | Current Task 3 status |
|---|---|---|
| US-01 | `test_us01_parse_explicit_budget`; `test_us01_parse_no_budget`; `test_us01_parse_budget_with_comma` | Blocked by fixture setup |
| US-02 | `test_us02_database_setup_imports_rows`; `test_us02_database_setup_does_not_duplicate_rows`; `test_us02_health_endpoint_reports_database` | Blocked by fixture setup |
| US-03 | `test_us03_process_post_filters`; `test_us03_accept_intent_as_query`; `test_us03_invalid_max_price_falls_back_to_query` | Blocked by fixture setup; the last test name represents an obsolete fallback expectation |
| US-04 | `test_us04_match_score_is_between_zero_and_one_hundred`; `test_us04_matching_preferences_receive_higher_score`; `test_us04_reasons_describe_matching_preferences` | Blocked by fixture setup |
| US-05 | `test_us05_candidates_never_exceed_maximum_budget`; `test_us05_leaderboard_contains_at_most_five_sorted_items`; `test_us05_recommendation_api_returns_required_fields` | Blocked by fixture setup; these tests do not evidence the current `/api/compare` acceptance rules |
| US-06 | No complete test proves parsing and merging text exclusions with explicit `excluded_brands` | Not evidenced |
| US-07 | No collected test verifies `PurchaseURL` or the product-link behavior | Not evidenced |
| US-08 | No collected test verifies feedback API validation or persistence; the existing mock/API baseline is incomplete and failed overall | Incomplete / not evidenced |
| US-09 | No complete test verifies same-category, cheaper, different-ID, specification-complete budget alternatives or the null case | Not evidenced |

## Task 3 completion gates

| Completion gate | Current status | Evidence or blocker |
|---|---|---|
| Audited direct-dependency manifest | Candidate | Six approved dependencies reconciled and installed in the existing environment; clean-environment installation not executed |
| Installed dependencies are consistent | Passed | Post-merge `pip check`, exit `0` |
| Python sources compile | Passed | Post-merge `compileall`, exit `0` |
| Legacy and mock tests collect | Passed | Post-merge collection found 21 tests, exit `0` |
| Full backend suite passes | Failed | Post-merge result: `5 failed, 1 passed, 15 errors`, exit `1` |
| Legacy fixtures are compatible | Blocked | Obsolete `server.CSV_PATH` stops all 15 server test bodies |
| Mock tests are compatible | Failed | Five mock failures remain |
| `/api/recommend` complete contract is verified | Not evidenced | Current recommend mock is incompatible and fails |
| `/api/compare` accepts only 2 or 3 unique valid ProductIDs | Not evidenced | No collected compare acceptance tests |
| Invalid `max_price` returns HTTP 400 | Not evidenced | Legacy test is blocked and expects obsolete fallback behavior |
| Text and explicit exclusions are combined | Not evidenced | No complete current-contract regression test |
| `/api/feedback` returns HTTP 201 and persists | Not evidenced | No collected feedback acceptance test |
| US-09 budget-alternative rules are fully tested | Not evidenced | Complete rule and null-case tests are missing |
| Backend Pull Request reviewed and merged | Not confirmed | No actual backend PR evidence was established in this task |

## Current blockers

1. The legacy fixture patches obsolete `server.CSV_PATH`, producing 15 setup errors.
2. The fixture does not provide separate current-schema products and `product_specs` data or complete temporary SQLite isolation.
3. Mock setup reuses products-only data for `product_specs` and does not model the current count-dictionary contract.
4. Health and recommend endpoint mocks do not isolate all current database and initialization calls.
5. Current schema, `PRAGMA`, joined-query, and integrity-query responses are incomplete in the SQLite mocks.
6. One mock asserts an obsolete internal `setup_database()` call instead of observable leaderboard behavior.
7. US-05 compare, US-06 exclusion merging, US-07 product links, US-08 feedback, and US-09 budget-alternative completion gates lack successful acceptance evidence.
8. A backend Pull Request, non-author review, and merge are not confirmed.

## Compatibility handoff drafts

Markdown drafts were prepared locally only:

- `docs/issue-drafts/task3-legacy-fixture-compatibility.md`
- `docs/issue-drafts/task3-mock-compatibility.md`

No GitHub Issue was created.

## Conclusion

The reconciled six-dependency manifest installs successfully in the existing environment. Dependency consistency, Python compilation, and pytest collection pass. The historical baseline remains preserved, and the new post-merge full-suite run remains failed with `5 failed, 1 passed, 15 errors`, exit code `1`. Legacy fixture compatibility remains blocked, mock compatibility remains failed, and the backend Pull Request is not confirmed.

**Task 3 remains In Progress.**
