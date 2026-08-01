# CP3407 Project Status — Yuyang Unified Baseline

**Evidence date:** 1 August 2026  
**Purpose:** Shared factual baseline for the team and AI assistants

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
| `feedback` | Still to implement | US-08 persisted up/down feedback |

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
| US-08 | Planned | Add feedback schema, route, UI and tests |
| US-09 | Planned | Add same-category cheaper spec-complete alternative |
| US-10 | Planned | URL sharing/restoration |

## Known integration blockers

1. Old tests assume `setup_database()` returns an integer; Yuyang candidate returns a count dictionary.
2. Old temporary DB fixtures do not create a temporary `product_specs.csv`.
3. Old mocks refer to `TABLE_NAME`; the candidate uses `PRODUCTS_TABLE` and `SPECS_TABLE`.
4. Invalid `max_price` currently falls back silently instead of returning 400.
5. Explicit `excluded_brands` is not fully merged with text exclusions.
6. Feedback and budget alternative are not implemented in the candidate.
7. Final HTML still needs real API and comparison integration.
8. Test execution has not been verified in the current packaging environment because Flask is unavailable there.

## Verification rule

The Yuyang package is the adopted integration direction, but implementation status changes to Done only after code is merged, tests are actually run, a non-author review is completed, and the integrated system is demonstrated.
