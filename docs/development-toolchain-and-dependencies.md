# Development Toolchain and Dependency Governance

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative implementation baseline:** `feature/product-database`  
**Team meeting and governance record maintained by:** @Chu-Junjie  
**Status:** Prepared for formal review

This record documents the development, test, data and deployment tools agreed in the team meeting notes. Commands are procedures and do not imply successful execution unless linked evidence identifies a named commit and environment.

## 1. Named responsibilities

- @ZhengZaikun confirms Python runtime, Flask, API dependencies, automated tests, CI and Render API configuration.
- @tiantian09091 confirms SQLAlchemy, SQLite, PostgreSQL, catalogue-import tools, backup and recovery procedures.
- @Guanyu-Lu confirms HTML/CSS/JavaScript, GitHub Pages, browser tools, responsive testing and design tools.
- @Chu-Junjie maintains meeting notes, Git/GitHub workflow, dependency-change records, evidence links and release controls.

## 2. Source control and review

The project uses Git and GitHub for:

- Issues with explicit assignments;
- branches separated by work area;
- focused commits;
- Pull Requests into `feature/product-database` before final reconciliation;
- formal GitHub Reviews for current PR heads;
- GitHub Actions evidence;
- final controlled integration into `main`.

Review routing:

- backend/API/test changes → @ZhengZaikun;
- database/catalogue/importer changes → @tiantian09091;
- frontend/GitHub Pages changes → @Guanyu-Lu;
- meeting/status/traceability/release-record changes → @Chu-Junjie, with technical statements confirmed by the named person above.

## 3. Python and runtime dependencies

Current runtime manifest roles:

| Dependency | Purpose | Confirmation |
|---|---|---|
| Flask | REST API and request handling | @ZhengZaikun |
| Flask-Cors | Browser/API origin handling | @ZhengZaikun and @Guanyu-Lu |
| Gunicorn | Render production process | @ZhengZaikun |
| PyJWT | Token creation and validation | @ZhengZaikun |
| SQLAlchemy | SQLite/PostgreSQL data access | @ZhengZaikun and @tiantian09091 |
| psycopg binary package | PostgreSQL driver | @tiantian09091 and @ZhengZaikun |
| pytest | Automated test execution | @ZhengZaikun |

The production runtime dependency file must remain consistent with the Render build command. Test dependency installation must be documented consistently for local and CI use.

## 4. Local environment procedure

Example Windows PowerShell procedure:

```powershell
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
python server.py
```

Serve the frontend separately:

```powershell
python -m http.server 8000
```

These commands are procedures. A successful clean-environment result must record the commit SHA, Python version, commands, exit codes and observed application response.

## 5. Automated tests and CI

Canonical release command:

```bash
python -m pytest -q test_server.py
```

Recorded workflow evidence:

- run `31096706920`;
- Ubuntu 24.04.4;
- Python 3.11.15;
- pytest 9.1.1;
- 12 collected and 12 passed;
- tracked-file integrity passed.

@ZhengZaikun formally reviews PR #35 and reruns the canonical suite for the frozen release candidate. `test_mock.py` remains a visible historical non-release audit.

## 6. Database and catalogue tools

| Tool | Purpose | Confirmation |
|---|---|---|
| SQLite | Bundled local catalogue and disposable verification | @tiantian09091 |
| PostgreSQL | Deployed persistence through `DATABASE_URL` | @tiantian09091, with API integration confirmed by @ZhengZaikun |
| SQLAlchemy | Shared schema/query layer | @tiantian09091 and @ZhengZaikun |
| `import_real_catalog.py` | Build or refresh a clean catalogue artifact | @tiantian09091 |
| SQL queries and health output | Counts, joins, duplicates, orphans and engine identity | @tiantian09091 |

The importer must run against a disposable copy and must not run directly against production user data.

## 7. Frontend and browser tools

| Tool | Purpose | Confirmation |
|---|---|---|
| HTML, CSS and JavaScript | Static responsive interface | @Guanyu-Lu |
| GitHub Pages | Frontend hosting | @Guanyu-Lu |
| Browser Developer Tools | Console, Network, responsive and accessibility observations | @Guanyu-Lu |
| Figma or retained design artifacts | Interface design reference where available | @Guanyu-Lu |

Browser evidence must record the visible frontend commit, API destination, device/viewport, browser version and observed result. Screenshots do not replace Network evidence for API, authentication, privacy or persistence claims.

## 8. Render deployment

Expected API service configuration:

```text
Build command: pip install -r requirements.txt
Start command: gunicorn server:app
Environment names: DATABASE_URL, JWT_SECRET_KEY
```

- @ZhengZaikun confirms the Render service commit, commands, startup and `/api/health` behaviour.
- @tiantian09091 confirms the PostgreSQL environment and persistence.
- @Guanyu-Lu confirms the browser calls the intended Render API.
- @Chu-Junjie records evidence without secret values.

## 9. Secret handling

Do not retain:

- passwords;
- JWT values;
- cookies or authorization headers;
- database connection strings;
- private participant data;
- local environment files containing credentials.

- @ZhengZaikun confirms application secrets use environment configuration.
- @tiantian09091 confirms database credentials and backups are handled outside repository content.
- @Guanyu-Lu ensures browser screenshots do not expose tokens or private values.
- @Chu-Junjie checks Issues, PRs, meeting notes and release evidence before final publication.

## 10. Dependency-change procedure

For any new or upgraded dependency:

1. the named person responsible for the affected area creates an Issue;
2. record the reason, version/range, compatibility risk and rollback plan;
3. update the dependency manifest on a separate branch;
4. install in a clean environment;
5. run the affected automated tests;
6. run database or browser checks where applicable;
7. open a Pull Request and request formal review from the affected named people;
8. merge only after evidence passes;
9. @Chu-Junjie updates the meeting and release records.

## 11. Failure routing

- Python/Flask/API/authentication/test/CI failure → @ZhengZaikun;
- SQLAlchemy/catalogue/importer/PostgreSQL/backup failure → @tiantian09091;
- HTML/CSS/JavaScript/GitHub Pages/browser/accessibility failure → @Guanyu-Lu;
- meeting/status/evidence/release-record inconsistency → @Chu-Junjie.

## 12. Verification status

| Area | Status |
|---|---|
| Dependency roles documented | Prepared |
| Canonical CI evidence for recorded PR ref | Passed |
| Final-candidate CI | Pending |
| Clean-environment installation | Pending final candidate |
| Disposable catalogue verification | Not Run |
| Deployed PostgreSQL verification | Unverified |
| GitHub Pages/Render E2E | Not Run |
| Final secret-safety record | Not Run |

## 13. Completion criteria

- [ ] @ZhengZaikun formally approves backend runtime, tests, CI and Render API sections.
- [ ] @tiantian09091 formally approves SQLAlchemy, PostgreSQL, importer and recovery sections.
- [ ] @Guanyu-Lu formally approves frontend, GitHub Pages, browser and design-tool sections.
- [ ] @Chu-Junjie confirms meeting-note, governance and evidence consistency.
- [ ] Clean-environment, final CI, deployed PostgreSQL and browser evidence are linked after execution.

Formal approval of this document does not replace execution evidence.