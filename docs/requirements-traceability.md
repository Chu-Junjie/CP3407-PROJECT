# Requirements Traceability — Yuyang Unified Baseline

This is a live matrix. `Candidate` means code was supplied but is not verified until merged and tested.

## Foundation evidence

| Evidence item | Final record |
|---|---|
| Coordinator | Chu Junjie |
| Tracking Issue | `#16` — Closed |
| Foundation Pull Request | `#17` — Merged |
| Foundation branch | `docs/project-foundation` |
| Closeout branch | `docs/task1-closeout` |
| Source branch | `main` |
| Baseline decision | `docs/project-baseline-decision.md` |
| Definition of Done | `docs/definition-of-done.md` |
| Team ownership | `docs/team-task-allocation.md` |
| Project status | `docs/project-status.md` |
| Closeout record | `docs/task1-closeout.md` |
| Non-author reviewer | `@Chu Junjie` |
| Review result | `Approved` |
| Merge commit | `ae9366d` |
| Project Board status | `Done` |
| Project baseline status | `Merged` |
| Implementation tests | `Not executed as part of Task 1` |
| Task 1 status | `Completed` |

| US | Requirement | Implementation / target | Tests / evidence | Owner | Current status |
|---|---|---|---|---|---|
| US-01 | Natural-language requirement extraction | Yuyang server candidate: category, brand, budget, exclusions, use cases | parser, validation and invalid input tests | Zaikun | Candidate / needs validation fixes |
| US-02 | Database setup/import | products + product_specs import, indexes, health counts | import, 9000/33 counts, join integrity, schema output | Yuyang | Candidate |
| US-03 | Top-5 leaderboard | joined spec-complete recommendation API + real HTML | recommend API tests and frontend Network evidence | Zaikun + Guanyu | Backend candidate / frontend pending |
| US-04 | Recommendation explanations | score reasons and use-case matches | score/reason tests and UI evidence | Zaikun + Guanyu | Candidate |
| US-05 | Compare 2–3 products | product_specs + `/api/compare` + comparison UI | exact count, invalid/missing IDs, field completeness | Yuyang + Zaikun + Guanyu | DB/backend candidate / UI pending |
| US-06 | Exclusions | merge text and explicit excluded_brands | exclusion API and regression tests | Zaikun | Partial |
| US-07 | Product link | `PurchaseURL` from product_specs and safe UI | URL validation and button/manual test | Yuyang + Guanyu | Data candidate / UI pending |
| US-08 | Feedback | feedback table, persistence, API and UI | valid up/down, invalid vote, DB insert | Yuyang + Zaikun + Guanyu | Planned |
| US-09 | Budget alternative | same category, cheaper, different ID, spec-complete | same category, cheaper, different, null case | Zaikun + Guanyu | Planned |
| US-10 | Share leaderboard | URL encode/restore and rerun recommend | special chars, exclusions, second-browser test | Junjie + Guanyu | Planned |

## Database evidence

| Evidence item | Current record |
|---|---|
| Coordinator | Chu Junjie |
| Tracking Issue | `#21` |
| Database Pull Request | `#19` — Merged |
| Non-author reviewer | `@Chu Junjie` |
| Review result | `Approved` |
| Merge commit | `f798bd7` |
| Evidence tracker | `docs/task2-database-evidence.md` |
| Project Board status | `Done` |
| Database tests | `Passed` |
| Task 2 status | `Completed` |

### Traceability targets

| User Story | Task 2 evidence requirement | Current status |
|---|---|---|
| US-02 | Database setup, schema, 9,000/33 counts and safe initialization | Verified |
| US-05 | Specification data, ProductID integrity and comparison support | Verified |
| US-07 | `PurchaseURL` source and missing-link limitation | Verified |
| US-08 | Joined database recommendation scope and data limitations | Verified |

## Backend verification evidence

This section records the original Task 3 evidence, the separate post-requirements-reconciliation validation, and the later validation after synchronizing main commit `fbd733c`. It does not replace the earlier implementation-candidate or Task 2 records.

| User Story | Actual Task 3 tests or evidence | Actual result | Task 3 status |
|---|---|---|---|
| US-01 | `test_us01_parse_explicit_budget`; `test_us01_parse_no_budget`; `test_us01_parse_budget_with_comma` | All three are prevented from executing by the autouse fixture's obsolete `server.CSV_PATH` patch | **Blocked by fixture setup** |
| US-02 | `test_us02_database_setup_imports_rows`; `test_us02_database_setup_does_not_duplicate_rows`; `test_us02_health_endpoint_reports_database` | All three are prevented from executing by the same fixture error | **Blocked by fixture setup** |
| US-03 | `test_us03_process_post_filters`; `test_us03_accept_intent_as_query`; `test_us03_invalid_max_price_falls_back_to_query` | All three are prevented from executing; the last test name also encodes an obsolete fallback expectation rather than the current HTTP 400 gate | **Blocked by fixture setup** |
| US-04 | `test_us04_match_score_is_between_zero_and_one_hundred`; `test_us04_matching_preferences_receive_higher_score`; `test_us04_reasons_describe_matching_preferences` | All three are prevented from executing by the fixture error | **Blocked by fixture setup** |
| US-05 | `test_us05_candidates_never_exceed_maximum_budget`; `test_us05_leaderboard_contains_at_most_five_sorted_items`; `test_us05_recommendation_api_returns_required_fields` | All three are prevented from executing; despite their legacy prefixes, none verifies the current `/api/compare` requirement | **Blocked by fixture setup** |
| US-06 | No complete collected test proves text-exclusion and explicit `excluded_brands` merging | No successful applicable evidence | **Not evidenced** |
| US-07 | No collected test verifies `PurchaseURL` or product-link behavior | No successful applicable evidence | **Not evidenced** |
| US-08 | No collected test verifies feedback validation or persistence; the preserved mock/API baseline is incomplete and failed overall | Feedback completion cannot be claimed | **Incomplete / not evidenced** |
| US-09 | No complete test covers same-category, cheaper, different-ProductID, specification-complete budget alternatives and the null case | No successful applicable evidence | **Not evidenced** |

The three current Task 3 full-suite records remain distinct:

| Evidence stage | Full-suite result | Duration | Exit code | Conclusion |
|---|---|---:|---:|---|
| Historical baseline | `5 failed, 1 passed, 15 errors` | `3.03s` | `1` | **Failed; preserved** |
| After dependency-manifest reconciliation | `5 failed, 1 passed, 15 errors` | `2.98s` | `1` | **Failed** |
| After synchronizing main commit `fbd733c` | `4 failed, 2 passed, 15 errors` | `3.30s` | `1` | **Failed** |

After `requirements.txt` was reconciled with `origin/main`, the final manifest contained six direct project, test, and deployment dependencies. The existing environment installed the manifest successfully, `pip check` and compilation passed, and collection found 21 tests with exit code `0`. The restricted-shell launch attempts remain recorded separately from the later real Python executions in that evidence stage.

Main commit `fbd733c` was later synchronized through merge commit `e907354`. The resulting `server.py`, `index.html`, and `product_specs.csv` changes were inherited from main and were not manually authored by the Task 3 coordinator. The post-synchronization checks again recorded successful installation, dependency consistency, compilation, and collection of 21 tests. `test_server.py` still produced 15 fixture-setup errors. `test_mock.py` improved from `5 failed, 1 passed` to `4 failed, 2 passed` because `test_mock_recommend_endpoint_without_running_real_engine` now passes, but the full suite still fails.

The tests modified tracked `digital_products.db` as a side effect. That change was recorded in `docs/evidence/task3-database-side-effect-after-main-fbd733c.txt`, and the database was restored to its committed 401408-byte blob `cbb53aa8c096a974fa02fe010d422f630bb14c92`. The generated database was not retained or committed. Complete database-state isolation is therefore **Failed**, and no US-01 through US-09 status is promoted by the additional mock pass, collection success, or any failed full-suite baseline.

## Required evidence columns before final release

For every Story add:

- priority and justification;
- estimate and dependency;
- Acceptance Criteria;
- Issue;
- branch/commit;
- PR and reviewer;
- automated test command/result;
- manual acceptance result;
- deployment/demo link;
- final status.
