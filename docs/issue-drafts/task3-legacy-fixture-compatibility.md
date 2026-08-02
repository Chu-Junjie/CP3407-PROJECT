# Issue Draft: Update Legacy Server Fixtures for the Current Database Contract

## Status

Draft only. Do not create this Issue on GitHub until the coordinator and backend/test owner review the scope.

## Problem

All 15 collected tests in `test_server.py` error during autouse fixture setup before their test bodies execute. The fixture currently patches:

```python
monkeypatch.setattr(server, "CSV_PATH", csv_path)
```

The current backend no longer exposes `server.CSV_PATH`. It uses separate products and specification sources, so restoring the obsolete alias in production code solely to satisfy the old fixture would hide the real compatibility work.

## Actual evidence

- Preserved full-suite evidence: `docs/evidence/task3-pytest-baseline.txt`.
- Preserved result: `5 failed, 1 passed, 15 errors in 3.03s`.
- Preserved exit code: `1`.
- Every `test_server.py` item is one of the 15 setup errors caused by the obsolete fixture patch.
- Dedicated collection still succeeds: 21 tests collected, exit code `0`.

## Current contract to use

Patch the current path constants to files inside each test's `tmp_path`:

- `server.PRODUCTS_CSV_PATH`
- `server.SPECS_CSV_PATH`
- `server.DB_PATH`

Use the current table and setup contracts:

- products input must contain every field required by `PRODUCT_REQUIRED_COLUMNS`;
- specifications input must contain every field required by `SPECS_REQUIRED_COLUMNS`;
- `setup_database()` returns a dictionary containing `products`, `product_specs`, and `feedback` counts;
- current health output describes those tables separately and includes the joined recommendation-candidate count.

## Required fixture work

1. Create a temporary products CSV and a separate temporary `product_specs` CSV under `tmp_path`.
2. Give both datasets complete current schemas; do not reuse a products-only dataframe for specifications.
3. Use unique, matching `ProductID` values across the two datasets so join behavior is deterministic. Every specification ProductID must exist in products.
4. Patch `PRODUCTS_CSV_PATH`, `SPECS_CSV_PATH`, and `DB_PATH` to the temporary paths.
5. Ensure every test uses the temporary SQLite file and never reads from or writes to the repository's `digital_products.db`.
6. Remove the obsolete `server.CSV_PATH` fixture assumption.
7. Update later legacy assertions only where they conflict with the agreed current external contract. Do not add production compatibility variables merely to preserve old internal names.
8. Review the setup return value, nested health response, invalid `max_price` behavior, request-filter defaults, and current explanation text after the fixture begins reaching the test bodies.

## Acceptance criteria

- All 15 `test_server.py` test bodies execute without fixture setup errors.
- Temporary products and `product_specs` data use matching ProductIDs and complete current schemas.
- Tests use a temporary SQLite database and leave repository data unchanged.
- No obsolete `CSV_PATH` compatibility alias is added to `server.py`.
- Assertions describe the agreed current API/database behavior rather than obsolete implementation details.
- `python -m pytest -q test_server.py` completes with exit code `0`.
- Complete pytest output and the exit code are saved to a new evidence file, such as `docs/evidence/task3-test-server-after-fixture-compatibility.txt`.
- The preserved failed baseline is not overwritten or deleted.
- `git diff -- server.py` is empty for this test-compatibility issue unless a separately reviewed production change is explicitly approved.

## Validation commands

```text
python -m pytest -q test_server.py
git diff --check
git diff -- server.py
```

The full suite should be run only after this fixture issue and the separate mock-compatibility issue are resolved. A green `test_server.py` run alone does not prove Task 3 completion.

## Out of scope

- Restoring obsolete production APIs or variables only to make legacy tests pass.
- Changing recommendation behavior without an approved backend requirement.
- Modifying frontend, CSV, or SQLite project data.
