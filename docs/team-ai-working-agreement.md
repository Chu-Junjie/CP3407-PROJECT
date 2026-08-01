# Team–AI Working Agreement

## Purpose

This agreement prevents four members and multiple AI assistants from producing incompatible implementations or unsupported evidence.

## Shared truth sources

Priority order when information conflicts:

1. Current merged source code on `main`
2. Frozen API contract and database design
3. Executed test results and CI logs
4. GitHub Issues, Pull Requests and Project board
5. Updated traceability documentation
6. README claims
7. AI suggestions

An AI suggestion never overrides current code or a frozen contract automatically.

## Mandatory behaviour for every member

- Start from the latest `main` commit.
- Work only on the assigned branch.
- State the branch name and commit hash in the AI conversation.
- Give the AI the actual error output instead of paraphrasing it.
- Review every proposed file change before applying it.
- Run tests locally or in CI.
- Record the exact command and result.
- Update technical documentation in the same PR as the feature.
- Ask a non-author member to review the PR.
- Record known limitations honestly.

## Change-control rule

The following require explicit team approval before implementation:

- renaming frozen API fields;
- changing endpoint paths or status-code rules;
- adding/removing final database tables;
- replacing SQLite or the dataset;
- changing the final frontend framework;
- adding login, payment, ordering or an LLM;
- changing the meaning of a User Story.

Use `04_TEMPLATES/change-request-template.md` for any proposed contract change.

## AI output is provisional until verified

Mark every AI-produced item as one of:

- `PROPOSED`
- `IMPLEMENTED LOCALLY`
- `TESTED LOCALLY`
- `REVIEWED`
- `MERGED`
- `DEPLOYED`
- `ACCEPTANCE PASSED`

Only the final state supports marking a deployable User Story Done where deployment applies.

## Evidence integrity

Do not create or backdate:

- historical client feedback;
- fake failed tests to imitate TDD;
- invented Pull Requests or reviews;
- invented licence information;
- screenshots from a different code version;
- claims of coverage without a coverage command and output.
