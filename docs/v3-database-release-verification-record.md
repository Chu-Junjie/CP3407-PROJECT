# V3 Database Release Verification Record

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative baseline:** `feature/product-database`  
**Technical owner:** Yuyang Zhou — Database Administrator  
**Record owner:** Chu Junjie — Project Manager and Release Coordinator  
**Status:** Repository verification recorded; runtime verification pending

## 1. Purpose

This record separates database implementation evidence that can be verified from the repository from runtime evidence that must be collected from an executed SQLite or PostgreSQL environment.

## 2. Repository-verified implementation

The V3 repository defines:

- SQLAlchemy database access;
- PostgreSQL selection through `DATABASE_URL`;
- SQLite fallback for local and bundled demonstration use;
- products, product specifications, users, favorites, search history, saved results and feedback tables;
- a public catalogue importer with source and licence metadata;
- fixed historical EUR/USD and INR/USD conversion rules;
- catalogue verification logic.

### Catalogue target

| Category | Imported rows |
|---|---:|
| Laptops | 800 |
| Smartphones | 833 |
| Smart Watches | 300 |
| Headphones | 61 |
| Tablets | 6 |
| **Total** | **2,000** |

Imported IDs begin at `10,000,001`. The implementation target is 11,000 total product rows and 2,000 joined product-specification rows.

## 3. Importer safety boundary

`import_real_catalog.py` is a catalogue-build tool. It replaces imported catalogue/specification rows in its output and clears private application tables in the generated catalogue artifact.

It must:

- run against a disposable input/output database;
- never run directly against a production database containing user accounts, favorites, history or feedback;
- retain its command output and verification result;
- be reviewed by the database owner before release use.

## 4. Required disposable-database verification

| Check | Expected result | Status |
|---|---|---|
| `products` count | 11,000 | Not Run |
| `product_specs` count | 2,000 | Not Run |
| Joined recommendation candidates | 2,000 | Not Run |
| Duplicate product IDs | 0 | Not Run |
| Duplicate specification IDs | 0 | Not Run |
| Orphan specifications | 0 | Not Run |
| Products without specification rows | 9,000 historical rows | Not Run |
| Missing data-source values | 0 | Not Run |
| Private rows in generated catalogue artifact | 0 | Not Run |
| Category distribution | Matches recorded quotas | Not Run |
| Repeated generation | Deterministic or documented | Not Run |

For each execution, record the tested commit, Python version, command, input path, output path, timestamp, result and evidence location.

## 5. PostgreSQL runtime verification

| Check | Required evidence | Status |
|---|---|---|
| Render API commit | Service deploy record and SHA | Unverified |
| Database dialect | `/api/health` reports PostgreSQL | Unverified |
| Schema initialization | Table counts and successful startup | Not Run |
| Catalogue population | 11,000/2,000 observed counts | Not Run |
| Account persistence | Login succeeds after restart/redeploy | Not Run |
| Favorites persistence | Saved item remains after restart/redeploy | Not Run |
| History persistence | History and snapshot remain accessible | Not Run |
| Feedback persistence | Stored feedback remains counted | Not Run |
| Cross-user isolation | Account B cannot access Account A data | Not Run |
| Backup procedure | Backup record or documented provider process | Not Run |
| Restore procedure | Restoration test or accepted limitation | Not Run |
| Secret handling | No credentials retained in repository/evidence | Not Run |

## 6. Verification evidence template

| Field | Value |
|---|---|
| Tester | Pending |
| Date/timezone | Pending |
| Tested commit | Pending |
| Environment | Pending |
| Database dialect | Pending |
| Command or procedure | Pending |
| Expected result | Pending |
| Observed result | Pending |
| Status | Not Run |
| Evidence location | Pending |
| Defect Issue | None |

## 7. Defect ownership

- schema, catalogue, importer, provenance or PostgreSQL defects: Yuyang;
- backend database-session or API defects: Zaikun;
- user-interface display defects caused by database responses: Guanyu;
- evidence coordination, status and retest scheduling: Junjie.

## 8. Release acceptance criteria

The database release gate can pass only when:

- the disposable catalogue verification meets all required counts and integrity checks;
- the deployed database is identified as PostgreSQL;
- account-owned data persists after restart or redeploy;
- cross-user isolation is demonstrated;
- backup and recovery are documented or explicitly accepted as a limitation;
- no secret or personal data is exposed in retained evidence;
- the database owner approves the technical result.

Repository implementation alone is insufficient to mark the runtime database gate as passed.

## 9. Current conclusion

The repository contains a defined V3 database schema, public catalogue, importer, provenance rules and PostgreSQL configuration path. These items are repository verified.

The final database release gate remains pending until actual catalogue, deployed PostgreSQL, persistence, privacy and recovery evidence is collected and reviewed.
