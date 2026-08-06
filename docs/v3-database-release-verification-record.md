# V3 Database and PostgreSQL Release Verification Record

**Tracking Issue:** #41  
**Database/data owner:** Yuyang Zhou (`tiantian09091`)  
**Coordinator:** Chu Junjie  
**Authoritative implementation branch:** `feature/product-database`  
**Repository baseline:** `7c406515bd4b657372fe519869596825cdf91d56`  
**Current status:** Repository verification completed; deployed PostgreSQL verification pending

## 1. Purpose

This record separates facts that can be verified directly from the repository from checks that require a running SQLite or PostgreSQL environment.

Yuyang's catalogue, importer and database implementation is already present on the V3 branch. No reimplementation is requested by this document.

## 2. Repository-derived findings

### 2.1 Database selection and initialization

`server.py`:

- uses PostgreSQL when `DATABASE_URL` is configured;
- converts `postgres://` and `postgresql://` values to the SQLAlchemy psycopg dialect;
- falls back to `digital_products.db` for local use;
- creates tables through SQLAlchemy metadata;
- seeds `products` and `product_specs` only when the target tables are empty;
- returns row counts for products, specifications, users, favorites, history and feedback.

**Repository result:** Implemented  
**Deployed engine result:** Unverified

### 2.2 Schema inventory

The V3 schema defines:

1. `products`
2. `product_specs`
3. `users`
4. `favorites`
5. `search_history`
6. `search_results`
7. `feedback`

The repository defines primary keys, foreign keys and the user/product uniqueness constraint for favorites.

**Repository result:** Verified from source  
**Actual deployed schema:** Not Run

### 2.3 Catalogue construction target

`import_real_catalog.py` defines a 2,000-row recommendation catalogue using these quotas:

| Category | Target rows |
|---|---:|
| Laptops | 800 |
| Smartphones | 833 |
| Smart Watches | 300 |
| Headphones | 61 |
| Tablets | 6 |
| **Total** | **2,000** |

Imported catalogue IDs begin at `10,000,001`. The importer retains the original behavioural product rows below that range, replaces the imported catalogue range and rebuilds `product_specs`.

The implementation therefore targets:

- 9,000 retained behavioural rows;
- 2,000 imported catalogue rows;
- 11,000 total product rows;
- 2,000 recommendation-ready specification rows.

**Repository result:** Deterministic implementation target  
**Observed database counts:** Not Run

### 2.4 Built-in importer validation

The importer contains `verify_database()` and checks:

- `product_specs` count equals the total quota of 2,000;
- joined category counts exactly match the quota table;
- `users`, `search_history`, `favorites` and `feedback` are empty in the generated catalogue artifact;
- distinct `DataSource` values are reported.

This is executable validation logic, but the repository does not retain a current command output for the release commit.

**Repository result:** Validation implemented  
**Release execution result:** Not Run

### 2.5 Repeatability and destructive-operation boundary

The importer:

- copies the source database to `digital_products_real.db` by default;
- deletes prior imported product rows with IDs at or above `10,000,001`;
- deletes and rebuilds all specification rows;
- deletes private users, favorites, saved results, history and feedback from the generated catalogue artifact;
- inserts deterministic IDs and writes `real_product_catalog.csv`.

This design makes repeated catalogue builds structurally repeatable when run against a build copy. It must not be used directly against a live production database containing user data.

**Operational decision:**

- use the importer to build or refresh a clean catalogue artifact;
- use `server.py` initialization to seed an empty PostgreSQL database from the reviewed bundled SQLite artifact;
- do not point the importer at the production PostgreSQL database;
- back up any target file before a manual catalogue rebuild.

### 2.6 Provenance and price treatment

The importer records four public dataset sources:

| Catalogue area | Recorded source | Licence recorded in code |
|---|---|---|
| Laptops | Kaggle laptop-price-dataset | Apache-2.0 |
| Smartphones | Kaggle smartphone-dataset | Apache-2.0 |
| Smart watches | Flipkart fitness trackers | CC BY-SA 4.0 |
| Headphones/tablets | Datafiniti electronics pricing | CC0 |

Recorded price rules:

- EUR to USD: `1.08`;
- INR per USD: `83.0`;
- USD source prices remain USD;
- final imported prices are rounded to two decimal places;
- prices are historical dataset snapshots, not live prices or inventory.

**Repository result:** Source and transformation rules documented in executable code  
**Independent licence/source-page review:** Pending

### 2.7 Data completeness behaviour

The importer keeps missing descriptive fields as `Not specified` rather than inventing values. It filters invalid or non-positive prices and removes obvious accessory records for headphone/tablet selection.

`product_specs` fields are declared non-null in the SQLAlchemy schema, so importer fallbacks are necessary for seed compatibility.

## 3. Integrity expectations derived from the schema

| Check | Repository expectation | Runtime evidence |
|---|---|---|
| Product ID uniqueness | `products.ProductID` primary key | Not Run |
| Specification ID uniqueness | `product_specs.ProductID` primary key | Not Run |
| Specification orphan prevention | Foreign key to `products.ProductID` | Not Run for deployed engine |
| Recommendation-ready joined rows | 2,000 target | Not Run |
| Duplicate favorites | Prevented by unique user/product constraint | Not Run for deployed engine |
| User-owned history | Foreign key to users with cascade delete | Not Run for deployed engine |
| Saved result cleanup | Cascade from history to results | Not Run for deployed engine |
| Feedback reference cleanup | Nullable references with `SET NULL` | Not Run for deployed engine |

SQLite and PostgreSQL can differ in foreign-key enforcement and delete behaviour. Actual PostgreSQL checks remain required.

## 4. Commands for final local verification

Run against a disposable copy, not the only working database:

```bash
python import_real_catalog.py \
  --source digital_products.db \
  --output digital_products_real.db \
  --csv-output real_product_catalog.csv
```

Then record non-sensitive output from:

```sql
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM product_specs;
SELECT ProductCategory, COUNT(*)
FROM products
WHERE ProductID >= 10000001
GROUP BY ProductCategory
ORDER BY ProductCategory;

SELECT COUNT(*) - COUNT(DISTINCT ProductID) FROM products;
SELECT COUNT(*) - COUNT(DISTINCT ProductID) FROM product_specs;

SELECT COUNT(*)
FROM product_specs s
LEFT JOIN products p ON p.ProductID = s.ProductID
WHERE p.ProductID IS NULL;

SELECT COUNT(*)
FROM products p
JOIN product_specs s ON s.ProductID = p.ProductID;
```

Expected catalogue-build results:

- products: 11,000;
- product specifications: 2,000;
- imported category distribution: 800 / 833 / 300 / 61 / 6;
- duplicate IDs: 0;
- orphan specifications: 0;
- joined recommendation-ready rows: 2,000.

These remain expected values until actual command output is retained.

## 5. PostgreSQL release checks still required

GitHub source cannot establish the following runtime facts:

- whether the Render service currently has `DATABASE_URL` configured;
- the exact deployed API commit;
- whether the active database dialect is PostgreSQL;
- whether all seven tables were initialized in the deployed database;
- actual deployed counts and joins;
- persistence after restart or redeployment;
- cross-user authorization behaviour in the deployed environment;
- provider backup availability and restore success.

These items remain `Not Run` or `Unverified`; they must not be converted to `Passed` from repository inspection alone.

## 6. Required deployed persistence scenario

For a frozen release candidate:

1. confirm the deployed API commit without exposing credentials;
2. confirm the database dialect through `/api/health` or a redacted log;
3. create one non-sensitive test account;
4. save one favorite, one history record and one feedback record;
5. record the entries before restart/redeploy;
6. restart or redeploy the service;
7. confirm the same account data remains;
8. confirm a second account cannot access the first account's history or favorites;
9. delete the demonstration data where appropriate.

## 7. Backup and recovery position

Repository-supported recovery assets are:

- the authoritative importer;
- the retained public-catalogue source mapping;
- the bundled SQLite seed artifact;
- deterministic imported ProductIDs;
- SQLAlchemy table creation and empty-database seeding.

These assets support catalogue reconstruction. They do not constitute a backup of production user data.

Before production use, the team must retain a provider export or documented `pg_dump`/restore process for user-owned data. Until then, production backup and restore remain `Unverified`.

## 8. Secret-safety position

The code reads `DATABASE_URL` and `JWT_SECRET_KEY` from environment configuration. No connection string or production secret should be copied into Issues, Pull Requests, screenshots or test logs.

A final repository/history secret scan remains required before release.

## 9. Current release-gate summary

| Area | Current status | Basis |
|---|---|---|
| Schema and database-selection implementation | Implemented | `server.py` |
| Catalogue quotas and deterministic build | Implemented | `import_real_catalog.py` |
| Provenance and conversion rules | Implemented in code | Importer constants and source metadata |
| Built-in catalogue validation | Implemented | `verify_database()` |
| Actual SQLite release counts | Not Run | No retained release-command output |
| Actual PostgreSQL identity and counts | Unverified | Requires deployed environment |
| Restart/redeploy persistence | Not Run | Requires deployed environment |
| Cross-user deployed isolation | Not Run | Requires deployed E2E |
| Production backup and restore | Unverified | Provider/process evidence absent |
| **Database release gate** | **Blocked on runtime verification** | Repository inspection cannot replace execution |

## 10. Ownership boundary

This record changes no dataset, CSV, database, importer, schema, backend or deployment configuration. It documents repository-derived facts and the exact remaining runtime checks.
