# Task 3 Backend CI and Test Evidence

## 1. Document control

| Item | Current record |
|---|---|
| Coordinator | Chu Junjie |
| Task | Task 3 — Backend API, US-09, feedback and legacy test compatibility |
| Working branch | `feature/share-ci-evidence` |
| Current backend branch available remotely | `feature/product-database` |
| Planned final backend branch | `feature/final-backend` |
| Planned final backend branch status | Not present on the remote repository at the time of audit |
| Backend Pull Request | Not yet confirmed |
| Tracking Issue | Not yet recorded |
| Baseline commit | Not yet recorded |
| Overall Task 3 status | In Progress |

## 2. Coordinator scope

The coordinator evidence work for Task 3 covers:

- dependency and `requirements.txt` auditing;
- CI dependency preparation;
- Python compilation evidence;
- pytest discovery and execution evidence;
- test mapping for US-01–09;
- legacy and new test compatibility;
- regression and TDD evidence review;
- backend Pull Request completeness;
- Requirements Traceability, Definition of Done and Project Board updates.

Backend business logic changes to `server.py` remain the responsibility of the backend implementation owner. The coordinator records failures and evidence gaps rather than changing backend behaviour to force a passing result.

## 3. Status vocabulary

| Status | Meaning |
|---|---|
| Not executed | The command has not yet been run |
| Passed | The command completed successfully with supporting output |
| Failed | The command ran and reported one or more failures |
| Blocked | The command could not complete because of a documented blocker |
| Candidate | Code or configuration exists but has not been fully verified |
| Merged | The implementation Pull Request has entered `main` |
| Verified | The required evidence has been reviewed and confirmed |

## 4. Repository baseline

| Check | Actual result | Status |
|---|---|---|
| Current coordinator branch | `feature/share-ci-evidence` | Confirmed |
| `server.py` tracked in current `HEAD` | Present | Confirmed |
| `server.py` tracked in `origin/main` | Present | Confirmed |
| Local working-tree state observed during audit | `D server.py` | Blocked — local deletion must be restored before testing |
| Remote `feature/final-backend` branch | Not found | Not available |
| Remote `feature/product-database` branch | Present | Confirmed |
| Python source files observed | `CP3407_recommender_ui.py`, `server.py`, `test_mock.py`, `test_server.py` | Confirmed |

### Required local correction

Before running the Task 3 baseline, restore the tracked backend file:

```powershell
git restore --source=HEAD -- server.py
git status --short
Test-Path .\server.py
git diff -- server.py
```

Expected result:

- `D server.py` no longer appears in `git status --short`;
- `Test-Path .\server.py` returns `True`;
- `git diff -- server.py` produces no output.

## 5. Dependency baseline

| Check | Actual result | Status |
|---|---|---|
| `requirements.txt` in repository root | Missing | Blocked |
| Other dependency manifests | No `pyproject.toml`, `Pipfile`, `setup.py`, `setup.cfg` or `environment.yml` found | Confirmed |
| `python -m pip check` | `No broken requirements found.` | Passed for currently installed packages only |
| Flask import | `ModuleNotFoundError: No module named 'flask'` | Blocked |
| `requests` usage | Imported by `CP3407_recommender_ui.py` | Confirmed |
| `pytest` usage | Imported by `test_server.py` | Confirmed |
| Flask dependency | Required by the backend and Flask test client | Confirmed |
| Dependency installation from project manifest | Not executed | Blocked — manifest missing |
| Dependency consistency after installation | Not executed | Pending |

### Interpretation note

The successful `pip check` result only confirms that currently installed packages do not report broken dependencies. It does not confirm that all project dependencies are installed.

## 6. Proposed minimal dependency manifest

The initial dependency manifest should contain only direct dependencies confirmed by the current project:

```text
Flask
pytest
requests
```

Before committing, audit all Python imports and add another package only when the project directly imports or invokes it.

Recommended creation command:

```powershell
@(
    "Flask"
    "pytest"
    "requests"
) | Set-Content -Encoding utf8 .\requirements.txt
```

Do not generate the file using `pip freeze`, because that would include unrelated packages from the local machine.

## 7. Dependency installation evidence

| Check | Command | Actual result | Status |
|---|---|---|---|
| Install dependencies | `python -m pip install -r requirements.txt` | Not executed | Pending |
| Check installed dependencies | `python -m pip check` | Not executed after installation | Pending |
| Confirm Flask version | `python -c "from importlib.metadata import version; print(version('Flask'))"` | Not executed | Pending |
| Confirm pytest version | `python -c "from importlib.metadata import version; print(version('pytest'))"` | Not executed | Pending |
| Confirm requests version | `python -c "from importlib.metadata import version; print(version('requests'))"` | Not executed | Pending |

## 8. CI baseline

| Check | Command or evidence | Actual result | Status |
|---|---|---|---|
| GitHub Actions workflow | Repository workflow audit | No matching workflow evidence found during the initial search | Not confirmed |
| Python compilation | `python -m compileall -q .` | Not executed | Pending |
| Pytest collection | `python -m pytest --collect-only -q` | Not executed | Pending |
| Full pytest baseline | `python -m pytest -q` | Not executed | Pending |
| Coverage | Coverage tool/configuration not yet confirmed | Not executed |
| CI result | No completed CI run recorded | Not executed |

## 9. Evidence file locations

The following files should be generated from real command output:

| Evidence | File |
|---|---|
| Python compilation | `docs/evidence/task3-compile.txt` |
| Pytest collection | `docs/evidence/task3-pytest-collection.txt` |
| Full pytest baseline | `docs/evidence/task3-pytest-baseline.txt` |
| Coverage result, when configured | `docs/evidence/task3-coverage.txt` |

Recommended commands:

```powershell
New-Item -ItemType Directory -Force .\docs\evidence

python -m compileall -q . 2>&1 |
    Tee-Object -FilePath .\docs\evidence\task3-compile.txt

python -m pytest --collect-only -q 2>&1 |
    Tee-Object -FilePath .\docs\evidence\task3-pytest-collection.txt

python -m pytest -q 2>&1 |
    Tee-Object -FilePath .\docs\evidence\task3-pytest-baseline.txt
```

The exit code must be recorded immediately after each command.

## 10. Test baseline

| Check | Command | Actual result | Status |
|---|---|---|---|
| Python compilation | `python -m compileall -q .` | Not executed | Not executed |
| Test collection | `python -m pytest --collect-only -q` | Not executed | Not executed |
| Full test suite | `python -m pytest -q` | Not executed | Not executed |
| Legacy `test_server.py` | `python -m pytest test_server.py -v` | Not executed | Not executed |
| Legacy `test_mock.py` | `python -m pytest test_mock.py -v` | Not executed | Not executed |

## 11. Test-to-requirement mapping

Only real collected test names should replace the pending entries below.

| User Story | Required backend behaviour | Test evidence | Current status | Evidence gap |
|---|---|---|---|---|
| US-01 | Request and query input handling | Pending test discovery | Not confirmed | Test mapping required |
| US-02 | Database setup and product access | Pending test discovery | Not confirmed | Test mapping required |
| US-03 | Recommendation response behaviour | Pending test discovery | Not confirmed | Test mapping required |
| US-04 | Filters and response contract | Pending test discovery | Not confirmed | Test mapping required |
| US-05 | Compare exactly 2–3 unique valid ProductIDs | Pending test discovery | Not confirmed | Success and invalid-input tests required |
| US-06 | Empty-result and server-error handling | Pending test discovery | Not confirmed | Response-status tests required |
| US-07 | Product and purchase URL fields | Pending test discovery | Not confirmed | Field and null-handling tests required |
| US-08 | Count, message and budget alternative | Pending test discovery | Not confirmed | Contract tests required |
| US-09 | Category, brand, budget, exclusions and use-case rules | Pending test discovery | Not confirmed | Rule and regression tests required |

## 12. Task 3 completion gates

| Completion gate | Current status | Required evidence |
|---|---|---|
| `/api/recommend` returns the complete contract | Not verified | API response tests and actual output |
| `/api/compare` accepts only 2 or 3 unique valid ProductIDs | Not verified | Success, count, duplicate and invalid-ID tests |
| Invalid `max_price` returns HTTP 400 | Not verified | Regression test |
| Explicit and text-based exclusions are combined | Not verified | US-09 filter tests |
| `/api/feedback` returns HTTP 201 and persists the record | Not verified | API test and database query |
| US-09 rules are fully tested | Not verified | Test mapping and actual results |
| Legacy and new tests can be collected | Not verified | Successful pytest collection output |
| Backend Pull Request is reviewed and merged | Not completed | GitHub review and merge evidence |

Task 3 remains **In Progress** until every completion gate has supporting evidence.

## 13. Backend Pull Request audit

| Audit item | Current status |
|---|---|
| Backend implementation owner | Not recorded in this evidence file |
| Source branch | Not yet confirmed |
| Target branch | Expected `main`, not yet confirmed |
| Related Issue | Not confirmed |
| Pull Request | Not opened or not yet confirmed |
| Test commands included in PR | Not confirmed |
| Actual test output included | Not confirmed |
| Regression evidence | Not confirmed |
| Legacy test compatibility | Not confirmed |
| Non-author review | Not requested or not confirmed |
| Merge conflicts | Not confirmed |
| Merge status | Not completed |

## 14. Pull Request quality checklist

- [ ] The backend PR is linked to a Task 3 Issue.
- [ ] The source and target branches are correct.
- [ ] The PR does not remove required database joins to make legacy tests pass.
- [ ] `/api/recommend` response keys match the agreed contract.
- [ ] `/api/compare` preserves 2–3 unique valid ID validation.
- [ ] Invalid `max_price` has a regression test and returns HTTP 400.
- [ ] Explicit and text exclusions are tested together.
- [ ] `/api/feedback` returns HTTP 201 and writes to the database.
- [ ] US-09 rules have mapped tests.
- [ ] Old and new tests are collected successfully.
- [ ] Test output is provided, not only statements that testing was completed.
- [ ] A non-author reviewer has completed a GitHub review.
- [ ] All review conversations are resolved before merge.

## 15. Current blockers

| Blocker | Impact | Required action | Owner |
|---|---|---|---|
| `server.py` is locally deleted in the coordinator working tree | Compilation and test evidence would not represent the repository baseline | Restore from `HEAD` before testing | Chu Junjie |
| No dependency manifest exists | Clean installation and CI setup cannot be reproduced | Add a minimal audited `requirements.txt` | Chu Junjie |
| Flask is not installed in the current Python environment | Backend import and test collection may fail | Install from the new dependency manifest | Chu Junjie |
| Final backend branch is not present remotely | Final backend PR cannot yet be audited | Confirm the actual backend branch and PR with the implementation owner | Backend owner |
| Test discovery has not been executed | US-01–09 mapping cannot be completed | Run pytest collection and record output | Chu Junjie |
| GitHub Actions workflow is not confirmed | Automated CI status is unavailable | Audit or create the agreed workflow after dependencies are confirmed | Chu Junjie |

## 16. Next evidence actions

1. Restore `server.py` and confirm a clean source-code working tree.
2. Create the audited minimal `requirements.txt`.
3. Install dependencies from the manifest.
4. Record Python and dependency versions.
5. Run compilation and pytest collection.
6. Run the full baseline test suite.
7. Map real collected tests to US-01–09.
8. Create Issues for dependency, collection or regression failures.
9. Audit the backend PR when the implementation branch is available.
10. Update Requirements Traceability, Definition of Done and Project Board using actual results only.

## 17. Current conclusion

The Task 3 evidence baseline is not yet verified.

Confirmed facts at this stage:

- `server.py` exists in the repository baseline and in `origin/main`;
- the coordinator working tree showed a local deletion of `server.py`;
- no project dependency manifest was found;
- `pip check` found no conflicts among currently installed packages;
- Flask is missing from the current Python environment;
- `requests` and `pytest` are directly used by current project files;
- the planned final backend branch is not currently available remotely;
- compilation, test collection, full tests and coverage have not yet been evidenced.

Therefore, the accurate Task 3 status is:

```text
Dependency baseline: Blocked / In Progress
CI baseline: Not executed
Test discovery: Not executed
Backend PR: Not confirmed
Task 3: In Progress
```
