# Teacher Feedback Change Request — 4 August 2026

## Status

Implemented and tested in this local working copy. Team review, merge and production deployment are still required. This document records a deliberate scope change and supersedes the earlier frozen decision that excluded login and database migration.

## Feedback and response

| Teacher feedback | Implemented response | Verification |
|---|---|---|
| The dataset/database is too small and appears CSV-based | SQLAlchemy database layer; PostgreSQL via `DATABASE_URL`; bundled SQLite for local use; 9,000 product rows and 2,000 joined recommendation-ready specification rows | `/api/health` reports the database backend and table counts |
| No login and searches disappear | Password-hashed accounts, JWT login, private search history and result snapshots, history open/delete UI | Register, login, `/api/auth/me`, `/api/history` integration tests |
| Only five recommendations are displayed | 20 results per page, up to 100 per API request, with previous/next controls covering all matching candidates; the best five remain separately identified as `top_recommendations` | Pagination tests confirm two pages of 20 in the isolated dataset |

## Data provenance and limitation

The existing source contained 9,000 behavioural product observations but only 33 joined product specification rows. To create a demonstrable 2,000-row catalogue without inventing claims about external sources, this revision deterministically generates additional educational demonstration specifications from the existing product rows. Every generated row has `DataSource = educational-synthetic`; original specification rows have `DataSource = educational-prototype`.

These records and prices are not live. For a stronger final submission, replace synthetic catalogue rows with a properly licensed product dataset and record its source, licence, retrieval date and cleaning method. Live updates are possible through a scheduled, licensed vendor/API import, but scraping or claiming real-time prices is outside this implementation.

## Database tables

- `products`: 9,000 original behavioural product observations.
- `product_specs`: 2,000 recommendation-ready catalogue/specification rows.
- `users`: account identifiers and password hashes; plaintext passwords are never stored.
- `favorites`: user-owned saved products used for persistent same-category comparison.
- `search_history`: user-owned query, parsed filters, match count and timestamp.
- `search_results`: saved ranked result snapshots linked to a history record.
- `feedback`: helpful/not-helpful votes optionally linked to a user and search.

## Deployment notes

Render must receive `DATABASE_URL` from a managed PostgreSQL database and a random `JWT_SECRET_KEY` of at least 32 characters. The GitHub Pages frontend continues to call the Render Flask API. SQLite is suitable for local demonstration, but Render's ephemeral web-service disk is not suitable for persistent accounts and history.

## Evidence produced locally

- Database initialization: 9,000 `products`, 2,000 `product_specs`.
- Manual integration flow: registration → recommendation → history list/detail → feedback summary.
- Automated test command: `.venv/bin/pytest -q`.
- Automated result on 4 August 2026 after favorites/account-center expansion: `12 passed`.

Do not mark this change as reviewed, merged or deployed until those events actually occur.
