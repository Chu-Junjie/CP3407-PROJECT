# Task 2 Database Evidence Tracker

## Document control

| Item | Current record |
|---|---|
| Coordinator | Chu Junjie |
| Task | Task 2 — Database integration and evidence |
| Working branch | `feature/share-ci-evidence` |
| Source branch | `main` |
| Tracking Issue | `#17` — Open |
| Project Board status | `In Progress` |
| Database implementation status | `In Progress` |
| Database test status | `Not executed or not yet evidenced` |
| Non-author review | `Not confirmed` |
| Database Pull Request | `Not confirmed` |
| Merge to main | `Not completed` |

## Acceptance evidence

| Requirement | Required evidence | Current status | Evidence reference |
|---|---|---|---|
| `products` contains 9,000 records | Actual database query or automated test output | Not evidenced | Pending |
| `product_specs` contains 33 records | Actual database query or automated test output | Not evidenced | Pending |
| Specification ProductIDs exist in `products` | Integrity query or passing automated test | Not evidenced | Pending |
| Valid feedback is stored | Insert test and database query result | Not evidenced | Pending |
| Invalid feedback vote is rejected | Passing validation test | Not evidenced | Pending |
| `/api/compare` remains available | Route test or reviewed implementation evidence | Not evidenced | Pending |
| Database tests execute successfully | Real command or CI output | Not executed | Pending |
| Non-author review completed | GitHub review record | Not started | Pending |
| Pull Request merged | GitHub merge record and commit | Not completed | Pending |

## User Story traceability scope

### US-02

Acceptance Criteria and database setup evidence must identify:

- the database initialization behaviour;
- the `products` and `product_specs` tables;
- record-count evidence;
- safe repeated initialization;
- actual test evidence.

### US-05

Acceptance Criteria and comparison evidence must identify:

- exactly 2 or 3 unique valid ProductIDs;
- complete specification fields;
- missing or invalid ID behaviour;
- the relationship between comparison results and database records;
- actual test evidence.

### US-07

Acceptance Criteria and link evidence must identify:

- links sourced from `product_specs.PurchaseURL`;
- safe behaviour when a URL is missing;
- no unsupported claim that every URL is a direct checkout page;
- actual database or API evidence.

### US-08

Acceptance Criteria and recommendation evidence must identify:

- recommendation data sourced from joined database records;
- the distinction between 9,000 behavioural records and 33 complete specification records;
- empty-result and alternative behaviour;
- actual test evidence.

## Evidence classification

Use only these statuses:

- `Not started`
- `In Progress`
- `Candidate`
- `Not executed`
- `Blocked`
- `Passed`
- `Failed`
- `Reviewed`
- `Merged`
- `Verified`

`Passed` requires an actual successful test run.

`Reviewed` requires a non-author GitHub review.

`Merged` requires a completed Pull Request merge.

`Verified` requires implementation, test and acceptance evidence—not merely supplied code.