# Definition of Done

**Project:** Smart Digital Product Recommendation Platform  
**Applies to:** All User Stories, bugs, documentation tasks, and Iteration 3 release work

## 1. Purpose

This Definition of Done prevents a task from being marked complete merely because code was written. It aligns implementation with testing, integration, documentation, version control, deployment, and acceptance evidence.

## 2. User Story Definition of Done

A User Story may be moved to **Done** only when every applicable item below is complete.

### Requirements

- [ ] The User Story is written clearly and has a justified priority and estimate.
- [ ] Acceptance criteria are written before final implementation.
- [ ] Scope matches the actual dataset and technology.
- [ ] Unsupported claims have been removed or explicitly recorded as limitations.

### Design

- [ ] Relevant API, database, architecture, or UI design is documented.
- [ ] Field and component names match the frozen project contracts.
- [ ] The design explains why the selected approach is appropriate.
- [ ] Any required diagram has been updated to match the implemented system.

### Implementation

- [ ] The feature works with real project data, not final-interface mock data.
- [ ] The implementation satisfies every acceptance criterion.
- [ ] Existing completed behaviour has not been broken.
- [ ] Error, empty, and boundary cases are handled.
- [ ] No secrets, passwords, or private credentials are committed.

### Automated testing

- [ ] Tests cover normal behaviour.
- [ ] Tests cover at least one invalid or boundary case.
- [ ] A regression test exists for any fixed bug.
- [ ] All relevant automated tests have actually been executed.
- [ ] Test evidence records the command, date, number passed, and number failed.
- [ ] The team does not claim TDD unless the failing test was genuinely written and observed before the implementation fix.

### Integration and acceptance

- [ ] Frontend, backend, and database behaviour agree with the API contract.
- [ ] The feature passes a manual end-to-end acceptance test.
- [ ] The feature works in the integrated application.
- [ ] The feature works in the deployed application when deployment applies.
- [ ] Any user feedback or tester feedback is recorded honestly with date and tester role.

### Version control

- [ ] Work was completed on a feature/fix/documentation branch.
- [ ] Commits use descriptive messages.
- [ ] A Pull Request links the relevant Issue.
- [ ] The PR includes a summary, acceptance criteria, test evidence, and screenshots or API examples where relevant.
- [ ] At least one non-author teammate reviews the PR.
- [ ] Review comments are resolved before merge.
- [ ] The PR is merged into `main` and the related Issue is closed.

### Documentation

- [ ] README and `docs/` pages match the final implementation.
- [ ] Installation and run instructions are accurate.
- [ ] Known limitations are stated.
- [ ] The Requirements Traceability Matrix is updated.
- [ ] The responsible member has written the technical explanation for their own component.

## 3. Bug Definition of Done

A bug is Done only when:

1. The issue contains clear reproduction steps.
2. A test reproduces the failure when practical.
3. The root cause is documented.
4. The smallest correct fix is implemented.
5. The regression test passes.
6. The full relevant test suite passes.
7. A teammate reviews the change.
8. The fix is verified in the integrated application.
9. The issue is closed with evidence.

## 4. Documentation-task Definition of Done

A documentation task is Done only when:

- the document is based on real repository evidence;
- planned work and completed work are clearly distinguished;
- diagrams match actual components and data;
- terminology is consistent with code and API fields;
- broken, outdated, or contradictory claims are corrected;
- links and screenshots work;
- a teammate reviews technical accuracy.

## 5. Release Definition of Done

The final release may be tagged only when:

- [ ] All required User Stories have an honest final status.
- [ ] All blocking defects are closed or clearly documented.
- [ ] The final static interface no longer uses fixed mock recommendations.
- [ ] The real frontend-to-Flask-to-SQLite path works.
- [ ] Automated tests run successfully in a clean environment or CI.
- [ ] Required dependencies are documented in `requirements.txt` or equivalent.
- [ ] GitHub Actions shows a successful test workflow.
- [ ] The deployed application has been smoke-tested.
- [ ] At least two non-team acceptance tests have been recorded if available before submission.
- [ ] Architecture, database, interface, testing, tools, agile, deployment, and user-guide documentation are linked from README.
- [ ] A changelog and release tag are created.
- [ ] A final ZIP backup is created and opened to verify its contents.

## 6. Status definitions

| Status | Meaning |
|---|---|
| `Todo` | Not started or no evidence of active work. |
| `In Progress` | Actively being designed, implemented, tested, or reviewed. |
| `Blocked` | Cannot proceed because a named dependency is unresolved. |
| `Implemented` | Code exists, but integration, tests, deployment, or evidence remain incomplete. |
| `Done` | Every applicable Definition of Done item is satisfied. |
| `Deferred` | Removed from the final scope with an explicit reason and impact statement. |

`Implemented` and `Done` are intentionally different. A feature that exists only in mock data, only locally, or without tests must not be marked Done.

## 7. Evidence record template

```markdown
## Completion Evidence

- User Story / Issue:
- Owner:
- Branch:
- Pull Request:
- Acceptance criteria:
- Automated test command:
- Automated test result:
- Manual acceptance result:
- Deployment evidence:
- Documentation updated:
- Reviewer:
- Known limitations:
```

## 8. Integrity rule

The team must not fabricate past client feedback, test results, commits, TDD history, deployment results, dataset licences, or iteration evidence. Retrospective evidence must be labelled as retrospective, and current acceptance testing must use its actual date.


## Yuyang Unified Additional Checks

For US-05/07 database work, Done also requires:

- product_specs import and 33-row integrity evidence;
- ProductID join integrity;
- /api/compare validation for exactly 2 or 3 IDs;
- PurchaseURL limitations documented;
- old tests reconciled with the new two-table setup.
