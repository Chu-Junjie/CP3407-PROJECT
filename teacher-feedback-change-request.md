# Teacher Feedback Change Request — 4 August 2026

## Status

Implemented and tested in this local working copy. Team review, merge and production deployment are still required. This document records a deliberate scope change and supersedes the earlier frozen decision that excluded login and database migration.

## Feedback and response

| Teacher feedback | Implemented response | Verification |
|---|---|---|
| The dataset/database is too small and appears CSV-based | SQLAlchemy database layer; PostgreSQL via `DATABASE_URL`; bundled SQLite for local use; 11,000 product rows and 2,000 joined recommendation-ready public-dataset records | `/api/health` reports the database backend and table counts |
| No login and searches disappear | Password-hashed accounts, JWT login, private search history and result snapshots, history open/delete UI | Register, login, `/api/auth/me`, `/api/history` integration tests |
| Only five recommendations are displayed | 20 results per page, up to 100 per API request, with previous/next controls covering all matching candidates; the best five remain separately identified as `top_recommendations` | Pagination tests confirm two pages of 20 in the isolated dataset |

## Data provenance and limitation

The earlier 2,000 synthetic specifications have been replaced. The active catalogue now contains 800 laptops, 833 smartphones, 300 smart watches, 61 headphones and 6 tablets imported from four attributed public datasets. Their licences are Apache 2.0, CC BY-SA 4.0 and CC0; exact links and transformations are recorded in the README and every row stores a `DataSource` value.

These records and prices are historical dataset snapshots, not live inventory. EUR and INR prices are normalized to USD with fixed documented rates, and repeated Datafiniti merchant observations use the median recorded price. Missing technical attributes are stored as `Not specified`; the importer does not fabricate them. `import_real_catalog.py` provides a reproducible import and validation path.

## Database tables

- `products`: 11,000 rows (9,000 historical behavioural observations plus 2,000 imported catalogue products).
- `product_specs`: 2,000 public-dataset catalogue/specification rows used by recommendations.
- `users`: account identifiers and password hashes; plaintext passwords are never stored.
- `favorites`: user-owned saved products used for persistent same-category comparison.
- `search_history`: user-owned query, parsed filters, match count and timestamp.
- `search_results`: saved ranked result snapshots linked to a history record.
- `feedback`: helpful/not-helpful votes optionally linked to a user and search.

## Deployment notes

Render must receive `DATABASE_URL` from a managed PostgreSQL database and a random `JWT_SECRET_KEY` of at least 32 characters. The GitHub Pages frontend continues to call the Render Flask API. SQLite is suitable for local demonstration, but Render's ephemeral web-service disk is not suitable for persistent accounts and history.

## Evidence produced locally

- Database initialization: 11,000 `products`, 2,000 `product_specs`, and zero submitted user/history/favorite rows.
- Manual integration flow: registration → recommendation → history list/detail → feedback summary.
- Automated test command: `.venv/bin/pytest -q`.
- Automated result on 5 August 2026 after real-catalogue import: `12 passed`.

Do not mark this change as reviewed, merged or deployed until those events actually occur.
