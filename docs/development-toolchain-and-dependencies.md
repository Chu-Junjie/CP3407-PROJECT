# Development Toolchain and Dependency Governance

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Record owner:** Chu Junjie — Project Manager and Release Coordinator  
**Status:** Prepared for formal component review

This document records the tools, libraries, environments and governance controls used to develop, test, review, deploy and release the project. Commands are operating procedures and do not imply successful execution unless linked evidence exists for a named commit and environment.

## Toolchain overview

| Area | Tool or service | Project use |
|---|---|---|
| Version control | Git | Branching, commits, comparison and release history |
| Collaboration | GitHub Issues and Pull Requests | Task assignment, review, decisions and evidence links |
| Automation | GitHub Actions | Canonical test execution and tracked-file integrity checks |
| Runtime language | Python 3.11 | Backend, importer, tests and database verification |
| Backend framework | Flask | REST API and request handling |
| Cross-origin support | Flask-Cors | Browser-to-API access control |
| Production server | Gunicorn | Render production process |
| Authentication | PyJWT and Werkzeug password hashing | Token issue/validation and password security |
| Data access | SQLAlchemy | SQLite/PostgreSQL schema and queries |
| PostgreSQL driver | psycopg | SQLAlchemy PostgreSQL connectivity |
| Local database | SQLite | Bundled demonstration and disposable verification |
| Production database | PostgreSQL | Persistent catalogue and user-owned records |
| Testing | pytest | Canonical V3 API tests |
| Frontend | HTML, CSS and JavaScript | Responsive single-page user interface |
| Static hosting | GitHub Pages | Frontend deployment |
| API hosting | Render | Flask/Gunicorn service deployment |
| Design records | Mermaid and external modelling/prototype tools | Architecture, ERD, sequence and interface design |

## Version-control workflow

- `main`: final integrated release branch;
- `feature/product-database`: authoritative V3 implementation baseline during release preparation;
- `feature/*` and `fix/*`: owner-controlled technical work;
- `docs/*`: documentation, governance and evidence records;
- `ci/*`: CI workflow and test-evidence changes;
- `release/*`: controlled release-candidate or reconciliation work.

Commits should contain one logical change, use meaningful prefixes, avoid mixing unrelated technical and documentation work, identify generated/binary artifacts and preserve ownership boundaries.

Pull Requests should include purpose, scope, changed files, linked Issue, test/evidence summary, known limitations, reviewers and merge conditions.

## Python environment

Recommended setup:

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
```

Record:

```bash
python --version
python -m pip --version
python -m pip freeze
```

A clean environment should be used for final verification.

## Runtime dependencies

| Dependency | Version range | Responsibility |
|---|---|---|
| Flask | `>=3.0,<4.0` | REST API and application lifecycle |
| Flask-Cors | `>=4.0,<7.0` | Allowed browser origins and CORS headers |
| gunicorn | `>=22,<24` | Production WSGI server |
| PyJWT | `>=2.8,<3.0` | JWT token encoding and decoding |
| SQLAlchemy | `>=2.0,<3.0` | Schema, SQL generation, transactions and portability |
| psycopg[binary] | `>=3.1,<4.0` | PostgreSQL driver |

pytest is installed separately in CI. Any dependency-policy change requires backend/database-owner review.

## Backend and deployment tools

Flask provides routing, JSON handling, error handlers and application lifecycle. Production uses:

```bash
gunicorn server:app
```

Flask-Cors supports the separately hosted frontend. Production controls include intended origins, HTTPS, consistent JSON errors, `Cache-Control: no-store` and `X-Content-Type-Options: nosniff`.

PyJWT and Werkzeug password hashing support authentication. `JWT_SECRET_KEY` must be environment-configured and never committed or retained in evidence.

## Database tools

SQLAlchemy provides one data-access layer for SQLite and PostgreSQL.

SQLite is used for local demonstration, isolated tests and disposable catalogue verification. PostgreSQL is the persistent production target through `DATABASE_URL`.

The catalogue importer transforms public datasets, retains provenance, normalizes historical prices, keeps missing values as `Not specified`, inserts deterministic IDs and validates counts. It must run only against disposable build copies.

## Automated testing

Canonical command:

```bash
python -m pytest -q test_server.py
```

The suite covers setup/health, filtering, pagination, authentication, history, feedback, comparison and favorites.

`test_mock.py` is retained as a non-release historical V2 compatibility audit.

Test controls:

- isolated temporary databases;
- no tracked-file modification;
- recorded collection/result counts;
- recorded Python/pytest versions;
- exact tested commit;
- rerun for the frozen release candidate.

## GitHub Actions

The `V3 Test Evidence` workflow contains a required V3 suite and visible non-blocking historical audit. It records environment, commit, collection, result and tracked-file integrity.

Recorded successful run `31096706920` produced 12/12 passes in 1.23 seconds. This applies to the recorded PR ref; final-candidate verification remains required.

## Frontend and hosting

The frontend uses HTML, CSS and JavaScript for GitHub Pages. It includes authentication, structured filters, loading/error/empty states, Top 5, pagination, comparison, favorites, history, feedback, sharing, responsive layout and accessibility attributes.

GitHub Pages evidence must record the deployed URL, source/commit, date, console state and API destination.

Render evidence must record the deployed commit, health state, database dialect and redacted configuration metadata. Expected commands:

```text
Build command: pip install -r requirements.txt
Start command: gunicorn server:app
```

Required environment keys:

```text
DATABASE_URL
JWT_SECRET_KEY
```

Values must never be retained.

## Secret and evidence handling

Never commit or retain database passwords, full connection strings, JWT secrets, bearer tokens, real passwords or unnecessary personal information.

Before release, inspect tracked files/history, redact screenshots/logs, use non-sensitive demonstration accounts and record only safe metadata.

## Dependency-change governance

A dependency change requires:

1. rationale;
2. technical owner;
3. version range;
4. compatibility/security review;
5. local installation result;
6. automated test result;
7. production impact;
8. rollback approach;
9. reviewed documentation update.

## Review responsibilities

- Zaikun: Flask, authentication, recommendation, tests, CI, Gunicorn and Render API wording.
- Yuyang: SQLAlchemy, psycopg, SQLite/PostgreSQL, importer, provenance and database recovery controls.
- Guanyu: frontend, GitHub Pages, browser tools, responsive/accessibility verification and prototype tooling.
- Junjie: Git/GitHub process, evidence integrity, release sequencing and approval tracking.

## Submission checklist

- [x] Runtime dependencies documented.
- [x] Development and deployment tools documented.
- [x] Canonical test command documented.
- [x] Database/importer safety boundaries documented.
- [x] Secret-handling rules documented.
- [x] Dependency-governance procedure documented.
- [ ] Formal component reviews recorded.
- [ ] Final clean-environment execution recorded.
- [ ] Final deployed environment verified.

This document is ready for formal component review.
