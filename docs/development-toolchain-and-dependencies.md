# Development Toolchain and Dependency Governance

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Record owner:** Chu Junjie — Project Manager and Release Coordinator  
**Status:** Prepared for formal component review

## 1. Purpose

This document records the tools, libraries, environments and governance controls used to develop, test, review, deploy and release the project. It explains each tool's role and the controls required to keep local, CI and production environments consistent.

Commands in this document are operating procedures. They do not imply successful execution unless linked evidence is retained for a named commit and environment.

## 2. Toolchain overview

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

## 3. Version-control workflow

### Branch roles

- `main`: final integrated release branch;
- `feature/product-database`: authoritative V3 implementation baseline during release preparation;
- `feature/*` and `fix/*`: owner-controlled technical work;
- `docs/*`: documentation, governance and evidence records;
- `ci/*`: CI workflow and test-evidence changes;
- `release/*`: controlled release-candidate or reconciliation work.

### Commit expectations

Commits should:

- describe one logical change;
- use meaningful prefixes such as `feat`, `fix`, `test`, `docs`, `ci` or `refactor`;
- avoid mixing unrelated technical and documentation changes;
- identify generated or binary artifacts explicitly;
- preserve teammate ownership boundaries.

### Pull Request expectations

Each Pull Request should include:

- purpose and scope;
- changed files;
- linked Issue or decision;
- test/evidence summary;
- ownership boundary;
- known limitations;
- required reviewers;
- merge condition.

Technical changes require review by the relevant component owner. Documentation approval confirms technical wording but does not replace runtime verification.

## 4. Python environment

Recommended local setup:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
```

Record the following for release evidence:

```bash
python --version
python -m pip --version
python -m pip freeze
```

A clean environment should be used for final release verification.

## 5. Runtime dependencies

Current `requirements.txt`:

| Dependency | Version range | Responsibility |
|---|---|---|
| Flask | `>=3.0,<4.0` | REST API and application lifecycle |
| Flask-Cors | `>=4.0,<7.0` | Allowed browser origins and CORS headers |
| gunicorn | `>=22,<24` | Production WSGI server |
| PyJWT | `>=2.8,<3.0` | JWT token encoding and decoding |
| SQLAlchemy | `>=2.0,<3.0` | Schema, SQL generation, transactions and portability |
| psycopg[binary] | `>=3.1,<4.0` | PostgreSQL driver |

pytest is installed separately in the current CI workflow. A future dependency-policy change may place development/test tools in a separate manifest, but production dependencies must not be changed without backend/database-owner review.

## 6. Flask application

Flask provides:

- routing and HTTP method handling;
- JSON request and response support;
- application error handlers;
- startup and local development server;
- integration with authentication and SQLAlchemy services.

Production uses Gunicorn rather than Flask's development server.

Expected start command:

```bash
gunicorn server:app
```

## 7. CORS, headers and browser integration

Flask-Cors allows the separately hosted GitHub Pages frontend to call the Render API.

Required controls:

- allow only intended frontend origins where practical;
- use HTTPS in production;
- avoid wildcard credentials configurations;
- return JSON errors consistently;
- use `Cache-Control: no-store` for API responses containing private or dynamic data;
- use `X-Content-Type-Options: nosniff`.

Final browser evidence should confirm the frontend calls the intended production API and receives expected CORS headers.

## 8. Authentication tools

PyJWT is used for signed bearer tokens. Werkzeug password functions are used to hash and verify passwords.

Required configuration:

- `JWT_SECRET_KEY` supplied through environment variables;
- random production secret with sufficient length;
- no secret committed to Git;
- no token retained in screenshots, logs or Issues;
- protected endpoints validate tokens and user ownership;
- logout clears browser access to private views.

Authentication implementation still requires deployed negative tests and cross-user verification.

## 9. SQLAlchemy and databases

SQLAlchemy provides one data-access layer for SQLite and PostgreSQL.

### SQLite use

- bundled/local demonstration database;
- automated test databases;
- disposable catalogue-build and integrity verification;
- offline review of catalogue data.

SQLite must not be treated as persistent production storage on an ephemeral web-service filesystem.

### PostgreSQL use

- production persistent database;
- account, favorites, history, result snapshots and feedback storage;
- managed service connectivity through `DATABASE_URL`.

The deployed API must report PostgreSQL before the production database gate can pass.

### Database environment selection

`DATABASE_URL` is read from the environment. Without it, the application falls back to local SQLite.

Credentials must never be copied into source code or retained evidence.

## 10. Catalogue importer

`import_real_catalog.py` is used to build the public recommendation catalogue and retain provenance information.

The importer:

- downloads or reads defined public datasets;
- transforms source fields into the project schema;
- normalizes historical prices using documented fixed rules;
- keeps missing values as `Not specified`;
- inserts deterministic imported IDs;
- writes a human-readable catalogue CSV;
- validates expected counts and categories;
- clears private rows from the generated catalogue artifact.

Operational rule: run only against a disposable build copy. Do not run directly against production user data.

## 11. Automated testing

Canonical V3 command:

```bash
python -m pytest -q test_server.py
```

The current suite covers:

- database setup and health;
- filter parsing;
- recommendation pagination;
- account registration and login;
- private history and deletion;
- feedback;
- comparison;
- favorites.

The historical `test_mock.py` file targets removed V2 interfaces and is retained as a non-release compatibility audit.

### Test controls

- use isolated temporary databases;
- do not modify tracked repository files;
- record collection count and result;
- record Python and pytest versions;
- link results to the tested commit;
- rerun for the frozen release candidate.

## 12. GitHub Actions

The `V3 Test Evidence` workflow contains:

- a required V3 release-suite job;
- a visible non-blocking historical mock-audit job;
- Python 3.11 setup;
- dependency installation;
- environment and commit recording;
- collection and test execution;
- tracked-file integrity verification.

Recorded successful execution:

- workflow run `31096706920`;
- 12 collected, 12 passed in 1.23 seconds;
- tracked-file integrity passed;
- overall conclusion: success.

This evidence applies to the recorded PR ref. The final candidate requires a fresh run.

## 13. Frontend development

The frontend uses plain HTML, CSS and JavaScript to minimize build complexity and support GitHub Pages.

Implemented interface areas include:

- authentication;
- structured recommendation filters;
- loading, error and empty states;
- Top 5 and pagination;
- comparison;
- favorites and account centre;
- history restoration and deletion;
- feedback;
- sharing;
- responsive layout and accessibility attributes.

Browser developer tools are used for Network, console, responsive and accessibility evidence.

## 14. GitHub Pages

GitHub Pages hosts the static frontend.

Release evidence must record:

- public frontend URL;
- deployed source branch and commit where available;
- date/time;
- successful load without blocking console errors;
- observed API destination;
- desktop and mobile behaviour.

A live link without a commit or environment record is not sufficient release evidence.

## 15. Render

Render hosts the Flask/Gunicorn API and managed PostgreSQL environment.

Expected web-service configuration:

```text
Build command: pip install -r requirements.txt
Start command: gunicorn server:app
```

Required environment keys:

```text
DATABASE_URL
JWT_SECRET_KEY
```

Evidence should confirm only the presence and purpose of the keys, never their values.

Release verification should retain:

- deployed commit;
- successful service state;
- API health response;
- database dialect;
- restart/redeploy persistence;
- relevant redacted logs.

## 16. Design and modelling tools

Version-controlled Mermaid diagrams support review of:

- system context;
- logical architecture;
- deployment architecture;
- sequence flows;
- database relationships.

Externally editable UML, ERD and interface-prototype links may be retained when they are accessible, current and confirmed by the relevant owner. Placeholder or inaccessible links must not be presented as completed artifacts.

## 17. Secret and evidence handling

Never commit or retain:

- database passwords or full connection strings;
- JWT secret values;
- bearer tokens;
- real user passwords;
- personal email addresses used for private testing;
- provider credentials.

Before release:

- inspect tracked files and Git history for obvious secrets;
- redact screenshots and logs;
- use demonstration accounts with non-sensitive data;
- record only key names and safe metadata.

## 18. Dependency-change governance

A dependency addition or upgrade should include:

1. problem and rationale;
2. responsible technical owner;
3. selected version range;
4. compatibility and security considerations;
5. local installation result;
6. automated test result;
7. production impact;
8. rollback approach;
9. reviewed update to dependency documentation.

Dependencies must not be added solely because they are popular or convenient. The project should prefer the smallest supported toolset that meets current requirements.

## 19. Reproducible verification sequence

```bash
python -m venv .venv
# activate environment
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
python --version
python -m pip freeze
python -m pytest --collect-only -q test_server.py
python -m pytest -q test_server.py
git diff --exit-code
```

Database, browser and deployment checks are then executed using the dedicated acceptance and release records.

## 20. Review responsibilities

### Zaikun

- Flask, authentication and recommendation dependencies;
- canonical test scope;
- GitHub Actions workflow;
- Gunicorn and Render API wording.

### Yuyang

- SQLAlchemy and psycopg;
- SQLite/PostgreSQL roles;
- importer and provenance tooling;
- database verification and recovery controls.

### Guanyu

- frontend toolchain;
- GitHub Pages;
- browser developer tools;
- responsive and accessibility verification;
- interface-prototype tooling.

### Junjie

- Git/GitHub process;
- evidence integrity;
- release sequencing;
- cross-document consistency;
- approval and merge tracking.

## 21. Submission checklist

- [x] Runtime dependencies documented.
- [x] Development and deployment tools documented.
- [x] Canonical test command documented.
- [x] Database and importer safety boundaries documented.
- [x] Secret-handling rules documented.
- [x] Dependency-governance procedure documented.
- [ ] Formal component reviews recorded.
- [ ] Final clean-environment execution recorded.
- [ ] Final deployed environment verified.

This document is ready for formal component review. It should be updated only when the toolchain, dependency policy or retained execution evidence changes.
