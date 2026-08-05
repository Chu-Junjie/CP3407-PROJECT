# Issue Draft: Update Backend Mocks for the Current Two-Table Contract

## Status

Draft only. Do not create this Issue on GitHub until the coordinator and backend/test owner review the scope.

## Problem

The preserved `test_mock.py` baseline has five failures and one pass. The old mocks model a single products source and older internal call structure, while the current backend initializes products, `product_specs`, and feedback data and performs additional schema, integrity, joined-query, and budget-alternative work.

## Actual evidence

- Full-suite evidence: `docs/evidence/task3-pytest-baseline.txt`.
- Focused mock evidence: `docs/evidence/task3-test-mock.txt`.
- Mock result: 5 failed and 1 passed; exit code `1`.
- The only passing item is `test_mock_missing_csv_error_response`.

## Required mock work

### Separate products and `product_specs` mocks

- Provide distinct current-schema dataframes for `PRODUCTS_CSV_PATH` and `SPECS_CSV_PATH`.
- Route `pandas.read_csv` responses by the requested path instead of returning the same products-only dataframe twice.
- Model writes to `PRODUCTS_TABLE` and `SPECS_TABLE` separately.
- Use unique, matching ProductIDs across both mock datasets.

### Current `setup_database()` contract

- Model the return value as a count dictionary with `products`, `product_specs`, and `feedback`, not a single integer.
- Model query-specific SQLite behavior rather than one catch-all cursor result.
- Include current table-existence checks, per-table counts, index/setup operations, duplicate-spec checks, orphan-spec join checks, and feedback count behavior as applicable.
- Do not retain obsolete one-commit or one-read assumptions when the current contract performs separate setup steps.

### Health endpoint query isolation

- Patch `setup_database()` with the current count dictionary.
- Isolate the current connection/query boundary used by the health endpoint.
- Patch or accurately model `_table_columns` for products and specifications.
- Patch or accurately model `_joined_candidate_count`.
- Assert the current nested table response and joined candidate count rather than old top-level table/count fields.

### Recommend endpoint initialization isolation

- Keep request parsing and `build_leaderboard` controlled.
- Also isolate the current budget-alternative path, including `find_budget_alternative`, so the mock does not reach real database initialization.
- Assert observable response behavior and the current external contract without requiring repository CSV or SQLite data.

### Current schema and `PRAGMA` responses

- Provide realistic `sqlite_master` table-existence responses.
- Provide separate `PRAGMA table_info(products)` and `PRAGMA table_info(product_specs)` rows with accessible `name` fields.
- Provide complete current-schema results for joined candidate queries and integrity checks.
- For the exclusion query, model the current joined SQL aliases and normalized brand comparison rather than the old single-table statement.

### Obsolete internal-call assertion

Remove the expectation that `build_leaderboard()` directly calls `setup_database()`. The current function delegates candidate retrieval; tests should verify controlled candidates, ranking, limits, and returned payloads rather than an obsolete internal call count.

## Acceptance criteria

- Products and `product_specs` use separate complete mock datasets with matching ProductIDs.
- Database setup mocks follow the current three-count dictionary contract.
- Health tests isolate all current table-column and joined-count queries.
- Recommend tests isolate leaderboard and budget-alternative/database initialization paths.
- SQLite mocks return current schema and `PRAGMA` responses for both tables.
- The obsolete `build_leaderboard()` internal-call assertion is removed or replaced with an observable-behavior assertion.
- `python -m pytest -q test_mock.py` reports 6 passed and exits `0`.
- Complete pytest output and the exit code are saved to a new evidence file, such as `docs/evidence/task3-test-mock-after-compatibility.txt`.
- The preserved failed baseline is not overwritten or deleted.
- No production compatibility shim is added to `server.py` solely for the mocks.

## Validation commands

```text
python -m pytest -q test_mock.py
git diff --check
git diff -- server.py
```

After both compatibility issues are resolved, run the full pytest suite and save new evidence without replacing the preserved failed baseline.

## Out of scope

- Creating this Issue on GitHub from the draft.
- Changing current backend behavior solely to satisfy obsolete internal mock expectations.
- Editing frontend, CSV, or SQLite project data.
