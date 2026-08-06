# V3 Database and PostgreSQL Release Verification Record

**Tracking Issue:** #41  
**Database/data owner:** Yuyang Zhou (`tiantian09091`)  
**Coordinator:** Chu Junjie  
**Current implementation branch:** `feature/product-database`  
**Verification status:** `Not Run` / `Unverified` unless an executed result is entered below

## 1. Purpose

This document is the version-controlled execution record for V3 catalogue, database, importer, provenance and PostgreSQL release verification.

Yuyang's V3 database, catalogue and importer work is already implemented on `feature/product-database`. This record does not ask her to rebuild completed work. It defines the evidence required before those implementation statements can be promoted to release verification.

## 2. Evidence rules

Every executed check must record:

- evidence ID;
- exact branch and full commit SHA;
- date, time and timezone;
- executor;
- environment;
- command or query;
- relevant non-sensitive output;
- evidence location;
- result status;
- related defect or blocker Issue where applicable.

Allowed result values:

- `Not Run`
- `Passed`
- `Failed`
- `Blocked`
- `Unverified`
- `Accepted Limitation`

Do not use `Passed` merely because code, CSV files, SQLAlchemy models or importer logic exist.

## 3. Tested baseline

| Field | Value |
|---|---|
| Branch | Pending |
| Full commit SHA | Pending |
| Verification date/timezone | Pending |
| Executor | Pending |
| Python version | Pending |
| SQLAlchemy version | Pending |
| Local database engine | Pending |
| Render database engine | Pending |
| Render service commit | Pending |
| Evidence folder or Issue comment | Pending |

Results from different commits or database engines must be recorded separately.

## 4. Environment separation

### 4.1 Local SQLite verification

| Field | Value |
|---|---|
| Database path | Pending |
| Fresh database or existing database | Pending |
| Setup/import command | Pending |
| Status | `Not Run` |
| Evidence | Pending |

### 4.2 Render PostgreSQL verification

| Field | Value |
|---|---|
| Render service | Pending |
| Deployed commit SHA | Pending |
| `DATABASE_URL` configured | `Unverified` |
| Database engine confirmed safely | `Unverified` |
| Table initialization method | Pending |
| Catalogue import method | Pending |
| Status | `Not Run` |
| Evidence | Pending |

Do not store or paste the connection string, password, JWT secret or any private credential in this record.

## 5. Table and row-count verification

### DB-COUNT-01 — Required table inventory

**Status:** `Not Run`

Record the actual table-list query and output for the tested environment.

| Expected area | Observed table | Status |
|---|---|---|
| Product catalogue | Pending | `Not Run` |
| Product specifications | Pending | `Not Run` |
| Users | Pending | `Not Run` |
| Favorites | Pending | `Not Run` |
| Search history | Pending | `Not Run` |
| Saved result snapshots | Pending | `Not Run` |
| Feedback | Pending | `Not Run` |

**Command/query:** Pending  
**Output:** Pending  
**Evidence:** Pending

### DB-COUNT-02 — Product count

**Expected implementation statement:** 11,000 products  
**Status:** `Not Run`

**Command/query:** Pending  
**Observed count:** Pending  
**Evidence:** Pending

### DB-COUNT-03 — Specification count

**Expected implementation statement:** 2,000 product specifications  
**Status:** `Not Run`

**Command/query:** Pending  
**Observed count:** Pending  
**Evidence:** Pending

### DB-COUNT-04 — Category distribution

**Status:** `Not Run`

Record category names and actual counts used by the recommendation system.

| Category | Product rows | Specification rows | Recommendation-ready joined rows | Status |
|---|---:|---:|---:|---|
| Pending | Pending | Pending | Pending | `Not Run` |

## 6. ProductID integrity and joins

### DB-INT-01 — ProductID uniqueness in products

**Status:** `Not Run`

- Query: Pending
- Duplicate count: Pending
- Expected: `0`
- Evidence: Pending

### DB-INT-02 — ProductID uniqueness in product specifications

**Status:** `Not Run`

- Query: Pending
- Duplicate count: Pending
- Expected: `0`
- Evidence: Pending

### DB-INT-03 — Specification rows without a product

**Status:** `Not Run`

- Query: Pending
- Orphan count: Pending
- Expected: `0`, unless an approved limitation is documented
- Evidence: Pending

### DB-INT-04 — Products without specifications

**Status:** `Not Run`

- Query: Pending
- Missing-specification count: Pending
- Interpretation: Pending
- Evidence: Pending

This count may be non-zero if only a subset is recommendation-ready. The result must be explained rather than automatically treated as a defect.

### DB-INT-05 — Recommendation-ready joined count

**Status:** `Not Run`

- Query matching the actual recommendation join: Pending
- Joined row count: Pending
- Expected implementation statement: 2,000, subject to actual query evidence
- Evidence: Pending

## 7. Required field completeness

Record null, empty and invalid-value checks for fields used by the API or frontend.

| Field | Table | Check | Observed invalid rows | Status | Evidence |
|---|---|---|---:|---|---|
| ProductID | Pending | Null/empty/type | Pending | `Not Run` | Pending |
| Product name/title | Pending | Null/empty | Pending | `Not Run` | Pending |
| Category | Pending | Null/empty/known values | Pending | `Not Run` | Pending |
| Price | Pending | Null/non-numeric/negative | Pending | `Not Run` | Pending |
| DataSource | Pending | Null/empty | Pending | `Not Run` | Pending |
| PurchaseURL or source URL | Pending | Required/optional contract | Pending | `Not Run` | Pending |
| Specification fields used in ranking | Pending | Null/type/range | Pending | `Not Run` | Pending |

## 8. Importer execution and repeatability

### DB-IMP-01 — First clean import

**Status:** `Not Run`

| Field | Value |
|---|---|
| Importer | `import_real_catalog.py` |
| Command | Pending |
| Starting database state | Pending |
| Products before | Pending |
| Product specifications before | Pending |
| Products after | Pending |
| Product specifications after | Pending |
| Users/favorites/history/feedback affected | Pending |
| Exit code | Pending |
| Evidence | Pending |

### DB-IMP-02 — Immediate second import

**Status:** `Not Run`

| Field | Value |
|---|---|
| Command | Pending |
| Products before | Pending |
| Product specifications before | Pending |
| Products after | Pending |
| Product specifications after | Pending |
| Duplicate ProductIDs introduced | Pending |
| Duplicate specification rows introduced | Pending |
| Unrelated user data changed | Pending |
| Exit code | Pending |
| Evidence | Pending |

### DB-IMP-03 — Failure and rollback behaviour

**Status:** `Not Run`

Record one safe failure-path test or an owner-approved explanation where destructive testing is inappropriate.

- Failure condition: Pending
- Transaction behaviour: Pending
- Partial rows left behind: Pending
- Recovery command or process: Pending
- Evidence: Pending

## 9. Provenance, licence and price limitations

### DB-PROV-01 — Dataset identity

**Status:** `Unverified`

| Field | Value |
|---|---|
| Dataset/source name | Pending |
| Source owner/publisher | Pending |
| Source location | Pending |
| Licence or usage permission | Pending |
| Retrieval date | Pending |
| Retained source file | Pending |
| Evidence | Pending |

### DB-PROV-02 — DataSource retention

**Status:** `Not Run`

- Query: Pending
- Distinct `DataSource` values: Pending
- Missing DataSource rows: Pending
- Evidence: Pending

### DB-PROV-03 — Currency conversion

**Status:** `Unverified`

| Field | Value |
|---|---|
| Original currencies present | Pending |
| Display/storage currency | Pending |
| EUR conversion rule | Pending |
| INR conversion rule | Pending |
| USD conversion rule | Pending |
| Rate date/source | Pending |
| Rounding rule | Pending |
| Evidence | Pending |

### DB-PROV-04 — Historical price wording

**Status:** `Not Run`

Confirm that database fields, API responses, frontend labels and documentation do not imply live inventory, live retailer availability or real-time pricing where only historical/sourced catalogue values exist.

- Checked locations: Pending
- Observed wording: Pending
- Limitation wording approved: Pending
- Evidence: Pending

## 10. PostgreSQL deployment verification

### DB-PG-01 — Deployment identity

**Status:** `Unverified`

| Field | Value |
|---|---|
| Render service name | Pending |
| Deployed branch | Pending |
| Deployed commit SHA | Pending |
| Deployment date/timezone | Pending |
| Evidence | Pending |

### DB-PG-02 — Engine confirmation

**Status:** `Unverified`

Use a safe method that reveals only the engine/dialect or a redacted startup log.

- `DATABASE_URL` present: Pending
- Dialect/engine observed: Pending
- No connection string exposed: Pending
- Evidence: Pending

### DB-PG-03 — Schema initialization

**Status:** `Not Run`

- Initialization command/process: Pending
- Tables created: Pending
- Migration/version method: Pending
- Exit result: Pending
- Evidence: Pending

### DB-PG-04 — Catalogue initialization

**Status:** `Not Run`

- Import command/process: Pending
- Products observed: Pending
- Specifications observed: Pending
- Import duration: Pending
- Errors/warnings: Pending
- Evidence: Pending

## 11. Persistence across restart or redeploy

Use non-sensitive demonstration accounts and data.

### DB-PERSIST-01 — User account

**Status:** `Not Run`

- Test account identifier: Redacted/non-sensitive
- Created before restart: Pending
- Available after restart/redeploy: Pending
- Evidence: Pending

### DB-PERSIST-02 — Favorite

**Status:** `Not Run`

- ProductID: Pending
- Favorite created before restart: Pending
- Favorite present after restart/redeploy: Pending
- Evidence: Pending

### DB-PERSIST-03 — Search history and saved result snapshot

**Status:** `Not Run`

- History entry created before restart: Pending
- Snapshot restored before restart: Pending
- History entry present after restart/redeploy: Pending
- Snapshot restored after restart/redeploy: Pending
- Evidence: Pending

### DB-PERSIST-04 — Feedback

**Status:** `Not Run`

- Non-sensitive feedback record created: Pending
- Record present after restart/redeploy: Pending
- Evidence: Pending

### DB-PERSIST-05 — Cross-user isolation

**Status:** `Not Run`

Where safe, verify that one account cannot read or mutate another account's favorites or history.

- Test method: Pending
- Result: Pending
- Evidence: Pending

If this cannot be tested safely, record `Blocked` or `Accepted Limitation`; do not infer privacy from schema design alone.

## 12. Backup, recovery and free-tier limitations

### DB-OPS-01 — Backup method

**Status:** `Unverified`

- Current backup mechanism: Pending
- Frequency/retention: Pending
- Manual export command or provider method: Pending
- Evidence: Pending

### DB-OPS-02 — Restore procedure

**Status:** `Not Run`

- Restore target/environment: Pending
- Procedure: Pending
- Validation query after restore: Pending
- Result: Pending
- Evidence: Pending

### DB-OPS-03 — Rollback plan

**Status:** `Unverified`

- Application rollback method: Pending
- Database rollback method: Pending
- Catalogue re-import method: Pending
- Responsible owner: Pending
- Evidence: Pending

### DB-OPS-04 — Hosting limitations

**Status:** `Unverified`

Record relevant Render/PostgreSQL plan limitations without exposing billing or private account data.

- Sleep/spin-down behaviour: Pending
- Storage limit: Pending
- Backup limitation: Pending
- Expiry/retention risk: Pending
- Mitigation: Pending

## 13. Secret and repository-safety check

### DB-SEC-01 — Repository scan

**Status:** `Not Run`

Check tracked files and relevant history for:

- full PostgreSQL connection strings;
- database passwords;
- JWT production secrets;
- private API keys;
- personal test data;
- exported database backups containing private data.

| Check | Result | Evidence |
|---|---|---|
| Current tracked files | Pending | Pending |
| Relevant recent history | Pending | Pending |
| GitHub Actions/workflow values | Pending | Pending |
| Documentation and screenshots | Pending | Pending |

Any discovered credential must be treated as compromised and rotated by the responsible owner. Do not copy it into an Issue or PR.

## 14. Defect and blocker log

| Evidence ID | Status | Problem | Owner | Related Issue | Retest required |
|---|---|---|---|---|---|
| Pending | Pending | Pending | Pending | Pending | Pending |

Component ownership:

- data/catalogue/importer/PostgreSQL: Yuyang;
- backend/API/auth/history/favorites: Zaikun;
- frontend display or source wording: Guanyu;
- coordination/evidence/release status: Junjie.

## 15. Release decision summary

Complete only after the required checks are executed.

| Area | Final status | Evidence |
|---|---|---|
| Catalogue counts | Pending | Pending |
| ProductID integrity and joins | Pending | Pending |
| Importer repeatability | Pending | Pending |
| Provenance and licence | Pending | Pending |
| Currency and historical-price limitations | Pending | Pending |
| PostgreSQL deployment identity | Pending | Pending |
| Persistence | Pending | Pending |
| Backup and recovery | Pending | Pending |
| Secret scan | Pending | Pending |
| Database release gate | Pending | Pending |

Allowed final database release-gate values:

- `Passed`
- `Blocked`
- `Accepted Limitation`

Do not use `Passed` while any required critical check remains `Not Run`, `Failed` or `Unverified`.

## 16. Reviewer checklist

### Yuyang

- [ ] The document accurately separates implemented work from release verification.
- [ ] Queries and commands match the actual V3 schema and importer.
- [ ] Provenance, price and PostgreSQL wording is technically accurate.
- [ ] No secret or private data is included.
- [ ] Entered results match retained evidence.

### Zaikun

- [ ] User-owned tables and API persistence expectations match the backend contract.
- [ ] Cross-user isolation checks match authentication and authorization behaviour.
- [ ] No backend result is inferred from database structure alone.

### Guanyu

- [ ] Product source and historical-price wording matches the frontend presentation.
- [ ] Any database-related frontend limitation is represented accurately.

### Junjie

- [ ] Every status is evidence-based.
- [ ] Failed and blocked checks link to owner-controlled Issues.
- [ ] The database release gate is not closed prematurely.
- [ ] No teammate-owned data, importer, database or deployment file is modified.

## 17. Non-authorization statement

This verification record does not authorize Junjie to:

- edit datasets, CSV files, SQLite/PostgreSQL data, importers or schema;
- access or publish secrets;
- change Render configuration;
- restart or redeploy a service;
- create test accounts without the agreed execution process;
- mark any check passed without actual evidence;
- merge database work to `main`.
