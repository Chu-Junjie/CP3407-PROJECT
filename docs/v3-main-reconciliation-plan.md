# Release-to-`main` Reconciliation Plan

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative V3 baseline:** `feature/product-database`  
**Target branch:** `main`  
**Meeting record maintained by:** @Chu-Junjie  
**Status:** Prepared for formal review; no reconciliation branch has been created

## 1. Record basis

The integration direction, responsibility boundaries and review sequence are documented in the team meeting notes maintained by @Chu-Junjie. This plan does not authorise branch creation, conflict resolution, merging or release.

## 2. Recorded branch snapshot

- V3 head when planning began: `7c406515bd4b657372fe519869596825cdf91d56`
- `main` head when planning began: `d8f2d3a3f4d0ff6df1be4a1e813f0451c50073b0`
- recorded merge base: `1c5696fe36a0d6ee4ca875267fa02e0278a51831`
- recorded state: diverged

@Chu-Junjie must refresh these values immediately before reconciliation begins.

## 3. Named decisions

| Area | Decision required from |
|---|---|
| Backend, API, authentication, recommendation, automated tests and dependencies | @ZhengZaikun |
| Database, catalogue, specifications, importer, provenance, PostgreSQL and binary database handling | @tiantian09091 |
| Frontend, GitHub Pages and deployment-interface behaviour | @Guanyu-Lu |
| Meeting notes, changed-file inventory, status, traceability, README and release records | @Chu-Junjie |

@Chu-Junjie must not choose an implementation version on behalf of @ZhengZaikun, @tiantian09091 or @Guanyu-Lu.

## 4. Reconciliation principle

Start from the verified V3 release candidate. Preserve the V3 implementation unless the named person responsible for an area approves another version. Bring in useful `main`-only historical evidence selectively without restoring obsolete code or obsolete completion claims.

Do not:

- overwrite V3 with `main`;
- automatically choose a binary database;
- use an older backend, frontend or dataset merely because it exists on `main`;
- mark any release gate passed because a file was retained;
- merge to `main` before formal reviews and runtime evidence are complete.

## 5. File decisions

### Preserve from the release baseline unless explicitly changed

| Path or area | Confirmation |
|---|---|
| `server.py`, `test_server.py`, runtime dependencies and current API contract | @ZhengZaikun |
| `index.html` and deployed frontend behaviour | @Guanyu-Lu |
| `import_real_catalog.py`, catalogue/specification data, schema and PostgreSQL direction | @tiantian09091 |
| governance, meeting, acceptance and release records | @Chu-Junjie, with technical statements confirmed by the named person above |

### Review for selective preservation from `main`

| `main`-only material | Confirmation |
|---|---|
| Task 3 CI logs, command logs, failure evidence and test-side-effect records | @ZhengZaikun |
| database evidence and historical data notes | @tiantian09091 |
| frontend evidence and deployment notes | @Guanyu-Lu |
| project status and meeting records | @Chu-Junjie |

Historical evidence must be labelled historical and must not be used as final V3 runtime evidence.

## 6. Required process

1. @Chu-Junjie records the frozen V3 candidate SHA and refreshes the comparison with `main`.
2. @Chu-Junjie creates a file-by-file inventory and separates implementation, data, historical evidence and project records.
3. @ZhengZaikun records backend/test/dependency decisions.
4. @tiantian09091 records database/catalogue/importer decisions.
5. @Guanyu-Lu records frontend decisions.
6. @Chu-Junjie records the agreed decisions in the team meeting notes.
7. A reconciliation branch is created from the verified V3 candidate only after explicit approval.
8. Technical changes enter through commits approved by the named person responsible for the affected area.
9. @ZhengZaikun reruns the canonical suite.
10. @tiantian09091 reruns database integrity and PostgreSQL checks.
11. @Guanyu-Lu reruns deployed desktop/mobile browser checks.
12. @Chu-Junjie updates README, status, traceability, release notes and rollback information.
13. The final PR to `main` receives formal GitHub Approvals from @ZhengZaikun, @tiantian09091 and @Guanyu-Lu.
14. Merge occurs only after all required checks pass.

## 7. Final PR evidence

The final reconciliation PR must identify:

- source candidate SHA;
- target `main` SHA;
- retained and discarded files with reasons;
- decisions from @ZhengZaikun, @tiantian09091 and @Guanyu-Lu;
- CI result;
- database/PostgreSQL result;
- browser E2E result;
- external-acceptance result;
- known limitations;
- rollback procedure.

## 8. Completion criteria

- [ ] @Chu-Junjie records a fresh branch comparison and file inventory.
- [ ] @ZhengZaikun confirms backend/test/dependency decisions.
- [ ] @tiantian09091 confirms database/catalogue/importer decisions.
- [ ] @Guanyu-Lu confirms frontend decisions.
- [ ] The verified V3 implementation is preserved.
- [ ] Historical evidence retained from `main` is clearly labelled.
- [ ] Required CI, database, deployment, persistence, E2E and external-acceptance gates pass.
- [ ] @ZhengZaikun, @tiantian09091 and @Guanyu-Lu approve the final PR to `main`.
- [ ] The final PR is merged and the result is recorded by @Chu-Junjie.

No unchecked item may be inferred as complete from meeting agreement or document presence.