# Definition of Done

**Project:** Smart Digital Product Recommendation Platform  
**Applies to:** User Stories, defects, data work, documentation, deployment and final release  
**Authoritative implementation baseline:** `feature/product-database`  
**Meeting and governance record maintained by:** @Chu-Junjie

## 1. Purpose

This Definition of Done prevents implementation presence, meeting agreement, screenshots or partial test output from being reported as complete. Every applicable requirement must pass formal review, verification, integration and release controls.

## 2. Named responsibilities

- @ZhengZaikun confirms backend, API, authentication, recommendation, automated tests, CI and backend defects.
- @tiantian09091 confirms schema, catalogue, importer, provenance, PostgreSQL, persistence, recovery and database defects.
- @Guanyu-Lu confirms frontend, GitHub Pages, responsive behaviour, accessibility, browser E2E and frontend defects.
- @Chu-Junjie maintains team meeting notes, status, traceability, acceptance coordination, evidence links, reconciliation and release decisions.

@Chu-Junjie does not modify implementation maintained by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu without explicit approval.

## 3. Status definitions

| Status | Meaning |
|---|---|
| `Todo` | Work has not started or no current evidence exists. |
| `Planned` | Scope, named responsibility and dependencies are recorded. |
| `In Progress` | Work is actively being implemented, reviewed or verified. |
| `Implemented` | Code, data or documentation exists, but applicable gates remain open. |
| `Verified` | A named check passed for a named commit and environment. |
| `Blocked` | A recorded dependency prevents completion. |
| `Deferred` | The item is outside the current release with a recorded reason and impact. |
| `Done` | Every applicable criterion in this document is satisfied. |

`Implemented`, `Verified` and `Done` are not interchangeable.

## 4. Requirement and scope criteria

A User Story or change is not Done until:

- [ ] final wording and acceptance criteria are recorded;
- [ ] priority, estimate, dependencies and the named responsible person are recorded;
- [ ] scope decisions are documented in team meeting notes maintained by @Chu-Junjie;
- [ ] historical or replaced requirements are clearly labelled;
- [ ] unsupported product, price, licence, security or deployment claims are removed;
- [ ] deferred items include reason, impact and backlog status.

## 5. Design and contract criteria

- [ ] API, database, architecture and interface records match the implementation.
- [ ] Field, route, table and status names are consistent.
- [ ] Error, empty, boundary, authentication and authorization behaviour is defined.
- [ ] Privacy, persistence and recovery behaviour is documented where applicable.
- [ ] @ZhengZaikun approves backend/API/authentication/recommendation descriptions.
- [ ] @tiantian09091 approves database/catalogue/importer/PostgreSQL descriptions.
- [ ] @Guanyu-Lu approves frontend/responsive/accessibility descriptions.
- [ ] @Chu-Junjie confirms meeting-note and traceability consistency.

## 6. Implementation criteria

- [ ] every acceptance criterion is represented in the intended implementation;
- [ ] existing required behaviour has not regressed;
- [ ] errors and boundary cases are handled safely;
- [ ] missing data is displayed honestly and is not invented;
- [ ] no password, JWT, cookie, database URL or production secret is committed;
- [ ] the changed files match the Issue and Pull Request scope;
- [ ] implementation maintained by another named person is not changed without approval.

## 7. Automated-test criteria

- [ ] normal behaviour is covered;
- [ ] invalid and boundary behaviour is covered;
- [ ] authentication and privacy cases are covered for private data;
- [ ] a regression test is added for a fixed defect where practical;
- [ ] intended test files are collected and executed;
- [ ] command, date, commit SHA, environment, versions, counts and exit result are retained;
- [ ] tests leave tracked data/database files unchanged;
- [ ] a clean-environment or CI run passes;
- [ ] @ZhengZaikun confirms the current canonical suite and any backend/test result;
- [ ] @Chu-Junjie links the evidence without changing test implementation.

Canonical release command:

```bash
python -m pytest -q test_server.py
```

The historical `test_mock.py` audit remains non-release evidence.

## 8. Version control and review criteria

- [ ] work uses an appropriate branch;
- [ ] commits use descriptive messages;
- [ ] the Pull Request states purpose, changed files, evidence boundaries and known limitations;
- [ ] the Pull Request links the applicable Issue or traceability entry;
- [ ] the exact named reviewer is requested;
- [ ] Approval applies to the current PR head;
- [ ] requested changes are completed by the named person responsible for the affected area;
- [ ] review threads are resolved or explicitly documented;
- [ ] the PR is merged into the agreed target branch;
- [ ] status, meeting notes and traceability are updated.

## 9. Database and catalogue criteria

The database/catalogue work is not Done until:

- [ ] @tiantian09091 records exact release counts;
- [ ] products = 11,000 and product specifications = 2,000 are observed for the candidate;
- [ ] joined recommendation-ready rows = 2,000;
- [ ] category distribution = 800/833/300/61/6;
- [ ] duplicate product/specification IDs = 0;
- [ ] orphan specifications = 0;
- [ ] source, licence and transformation notes are reviewed;
- [ ] historical prices are not described as live retail prices;
- [ ] the importer is run against a disposable copy only;
- [ ] repeated generation does not create duplicates;
- [ ] PostgreSQL initialization and deployed counts are verified;
- [ ] data persists after restart or redeployment;
- [ ] backup and recovery steps are retained;
- [ ] @ZhengZaikun confirms API/database integration;
- [ ] @Chu-Junjie links the evidence and status.

## 10. Authentication, privacy and security criteria

- [ ] passwords are stored as hashes;
- [ ] registration validates required and duplicate fields;
- [ ] login accepts the documented identifier and rejects invalid credentials;
- [ ] JWT authentication rejects missing, malformed and invalid tokens;
- [ ] production secrets use environment configuration;
- [ ] Account B cannot read or delete Account A private favorites/history;
- [ ] private favorites and history persist in PostgreSQL;
- [ ] logs and evidence do not expose credentials or tokens;
- [ ] CORS is limited to the intended frontend behaviour;
- [ ] @ZhengZaikun confirms authentication/authorization;
- [ ] @tiantian09091 confirms persistence;
- [ ] @Guanyu-Lu confirms deployed login/logout/private-view behaviour;
- [ ] @Chu-Junjie retains non-sensitive evidence only.

## 11. Recommendation, pagination and comparison criteria

- [ ] response fields match the current API contract;
- [ ] category, budget, use-case and brand rules are applied consistently;
- [ ] Top 5 and paginated results are internally consistent;
- [ ] page and page-size boundaries are validated;
- [ ] empty and out-of-range results are handled;
- [ ] comparison accepts supported unique IDs and rejects invalid requests;
- [ ] favorite comparison enforces account and same-category rules;
- [ ] @ZhengZaikun confirms API and ranking behaviour;
- [ ] @Guanyu-Lu confirms deployed presentation and navigation.

US-09 Budget Alternatives is Deferred and is not a current Done criterion. Current acceptance verifies maximum-budget filtering only.

## 12. Frontend and accessibility criteria

- [ ] @Guanyu-Lu confirms the deployed frontend calls the intended Render API;
- [ ] register, login, logout and private account states work;
- [ ] recommendation, Top 5 and pagination work on desktop and mobile;
- [ ] comparison, favorites, history, feedback and share restoration work;
- [ ] loading, success, empty, validation, timeout and backend-error states are visible;
- [ ] links use safe `http` or `https` values with a clear fallback;
- [ ] keyboard access, visible focus, labels, readable errors and zoom/reflow are observed;
- [ ] browser Network evidence is retained;
- [ ] @ZhengZaikun confirms API observations;
- [ ] @tiantian09091 confirms data/persistence observations;
- [ ] @Chu-Junjie records status and defect links.

## 13. Defect criteria

A defect is Done only when:

1. reproduction steps, environment and candidate SHA are recorded;
2. the defect is explicitly assigned:
   - backend/API/test → @ZhengZaikun;
   - database/catalogue/PostgreSQL → @tiantian09091;
   - frontend/browser/accessibility → @Guanyu-Lu;
   - meeting/status/evidence record → @Chu-Junjie;
3. the root cause is identified;
4. the smallest correct fix is implemented by the assigned person;
5. a regression test or repeatable manual check is added where practical;
6. affected and relevant broader checks pass;
7. tracked data remains unchanged unless an intentional change is reviewed;
8. a non-author formally reviews the current fix head;
9. the integrated or deployed behaviour is retested;
10. the Issue closes with evidence.

## 14. Documentation criteria

- [ ] records are based on repository or executed evidence;
- [ ] team decisions are described as team meeting notes maintained by @Chu-Junjie;
- [ ] responsibilities use explicit GitHub mentions rather than generic descriptions;
- [ ] historical, Implemented, Verified, Blocked, Deferred and Done are distinguished;
- [ ] technical statements are approved by @ZhengZaikun, @tiantian09091 or @Guanyu-Lu for their named areas;
- [ ] commands, paths and links are checked;
- [ ] missing evidence remains missing;
- [ ] English-only project wording is used.

## 15. Integration and release criteria

The final release is not Done until:

- [ ] required Pull Requests receive formal Approvals for their current heads;
- [ ] approved records are merged into `feature/product-database`;
- [ ] a release-candidate SHA is frozen;
- [ ] @ZhengZaikun confirms final canonical CI;
- [ ] @tiantian09091 confirms catalogue integrity, PostgreSQL and persistence;
- [ ] @Guanyu-Lu confirms deployed desktop/mobile E2E and accessibility observations;
- [ ] @Chu-Junjie coordinates and records two non-team external-acceptance participants;
- [ ] blocking defects close or are explicitly accepted as non-critical limitations;
- [ ] the reconciliation file inventory is approved by @ZhengZaikun, @tiantian09091 and @Guanyu-Lu;
- [ ] the final PR is merged into `main`;
- [ ] final `main` CI and smoke checks pass;
- [ ] README, status, traceability, meeting notes, known limitations and release notes are current;
- [ ] tag, archive, checksum and recovery reference are retained.

## 16. Completion evidence template

```text
Requirement or Issue:
Named responsibility:
Meeting record:
Branch:
Commit SHA:
Pull Request:
Formal reviewer:
Acceptance criteria:
Automated command:
Environment:
Automated result:
Manual/deployed result:
Database result:
Evidence location:
Known limitations:
Final status:
```

## 17. Integrity rule

The team must not fabricate review, client feedback, tests, deployment, licence, security, recovery or iteration evidence. A meeting decision is not a formal Approval. A prepared record is not an executed result. A missing check remains unchecked.