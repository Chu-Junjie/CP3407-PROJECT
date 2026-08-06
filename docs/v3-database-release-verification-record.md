# Database Release Verification Record

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative baseline:** `feature/product-database`  
**Database verification:** @tiantian09091  
**Backend/API confirmation:** @ZhengZaikun  
**Meeting and evidence record:** @Chu-Junjie  
**Status:** Repository verification recorded; runtime verification pending

## 1. Record basis

The database verification scope and responsibility assignments are documented in the team meeting notes maintained by @Chu-Junjie. Repository inspection establishes implementation facts only; it does not establish deployed PostgreSQL, persistence, privacy or recovery results.

## 2. Repository-verified implementation

### Database selection

The V3 application:

- uses PostgreSQL when `DATABASE_URL` is configured;
- normalises supported PostgreSQL URLs for psycopg;
- falls back to bundled SQLite for local use;
- creates the SQLAlchemy schema;
- seeds empty product/specification tables from the reviewed local catalogue artifact.

### Schema

Seven application tables are represented:

1. `products`
2. `product_specs`
3. `users`
4. `favorites`
5. `search_history`
6. `search_results`
7. `feedback`

### Catalogue targets

`import_real_catalog.py` defines 2,000 imported recommendation-ready records:

| Category | Target |
|---|---:|
| Laptops | 800 |
| Smartphones | 833 |
| Smart Watches | 300 |
| Headphones | 61 |
| Tablets | 6 |
| **Total** | **2,000** |

With 9,000 retained behavioural rows, the target is:

- `products = 11,000`;
- `product_specs = 2,000`;
- joined recommendation-ready rows = 2,000.

These are source-defined targets until @tiantian09091 retains actual command output.

## 3. Importer safety decision

The importer creates or refreshes a clean catalogue artifact. It replaces imported catalogue/specification rows and clears private application rows in the generated artifact.

Therefore:

- @tiantian09091 runs it only against a disposable build copy;
- it must not run directly against production user data;
- @tiantian09091 backs up any target artifact before rebuilding;
- PostgreSQL production data requires a separate backup and recovery process.

## 4. Provenance and price treatment

The repository records public catalogue sources, licence labels and fixed conversion rules. Prices are historical dataset snapshots, not live inventory or live retail prices. Missing descriptive values remain explicitly unavailable rather than being invented.

@tiantian09091 confirms the final source, licence, retrieval-date and conversion wording before release.

## 5. Local verification assigned to @tiantian09091

Run against a disposable copy and retain complete non-sensitive output:

```bash
python import_real_catalog.py \
  --source digital_products.db \
  --output digital_products_real.db \
  --csv-output real_product_catalog.csv
```

Required checks:

- products = 11,000;
- product specifications = 2,000;
- joined rows = 2,000;
- category distribution = 800/833/300/61/6;
- duplicate product IDs = 0;
- duplicate specification IDs = 0;
- orphan specifications = 0;
- products without specifications = 9,000;
- source metadata present;
- generated users, favorites, history and feedback tables empty;
- two consecutive catalogue builds do not create duplicates;
- tracked source files remain unchanged.

Evidence fields:

```text
Tester: @tiantian09091
Candidate SHA:
Date/timezone:
Python version:
Source path:
Output path:
Commands:
Observed counts:
Integrity results:
Tracked-file status:
Result: Not Run / Passed / Failed / Blocked
```

## 6. Deployed PostgreSQL verification

### @tiantian09091 records

- Render PostgreSQL environment identity without secrets;
- confirmation that `DATABASE_URL` is set without displaying its value;
- active database dialect;
- expected table presence;
- actual deployed product/specification counts;
- restart or redeployment persistence;
- backup and recovery procedure.

### @ZhengZaikun confirms

- Render API commit;
- API startup and health behaviour;
- application connection to the recorded PostgreSQL environment;
- authentication and private-data API behaviour;
- cross-user access rejection.

### @Chu-Junjie maintains

- meeting notes;
- evidence IDs and status;
- defect routing and retest record;
- release-gate decision without exposing credentials.

## 7. Persistence and privacy scenario

1. @ZhengZaikun verifies creation of a non-sensitive Account A.
2. @ZhengZaikun verifies a favorite, history record, saved result snapshot and feedback record.
3. @tiantian09091 records the corresponding data before restart or redeployment.
4. The service is restarted or redeployed.
5. @tiantian09091 confirms the records persist.
6. @ZhengZaikun verifies Account B cannot access Account A private records.
7. @Chu-Junjie records the result without passwords, tokens or private values.

## 8. Current status

| Check | Status | Named confirmation |
|---|---|---|
| SQLAlchemy and database-selection code | Implemented | @ZhengZaikun and @tiantian09091 formally review PR #48 |
| Seven-table schema representation | Repository verified | @tiantian09091 |
| Catalogue quotas and deterministic build logic | Repository verified | @tiantian09091 |
| Provenance and conversion logic | Repository verified | @tiantian09091 confirms final wording |
| Actual disposable-build counts | Not Run | @tiantian09091 |
| Importer repeatability | Not Run | @tiantian09091 |
| Deployed PostgreSQL dialect and counts | Unverified | @tiantian09091 with API confirmation from @ZhengZaikun |
| Restart/redeployment persistence | Not Run | @tiantian09091 and @ZhengZaikun |
| Cross-user isolation | Not Run | @ZhengZaikun |
| Backup and recovery | Unverified | @tiantian09091 |
| Final secret-safety record | Not Run | @Chu-Junjie, with configuration confirmation from @ZhengZaikun and @tiantian09091 |
| Database release gate | Blocked | Runtime evidence is incomplete |

## 9. Defect routing

- catalogue, schema, importer, PostgreSQL or recovery defect → assign to @tiantian09091;
- API connection, authentication or authorization defect → assign to @ZhengZaikun;
- evidence-status or meeting-record correction → assign to @Chu-Junjie.

## 10. Completion criteria

- [ ] @tiantian09091 retains disposable-build output and integrity queries.
- [ ] @tiantian09091 confirms PostgreSQL identity, tables and deployed counts.
- [ ] @tiantian09091 and @ZhengZaikun confirm persistence after restart or redeployment.
- [ ] @ZhengZaikun confirms cross-user isolation.
- [ ] @tiantian09091 retains backup/recovery evidence.
- [ ] @ZhengZaikun and @tiantian09091 formally approve PR #48.
- [ ] @Chu-Junjie links the completed evidence from the release index and checklist.

No runtime result may be inferred from repository targets or meeting decisions.