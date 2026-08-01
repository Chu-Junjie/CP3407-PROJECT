# Requirements Traceability — Yuyang Unified Baseline

This is a live matrix. `Candidate` means code was supplied but is not verified until merged and tested.

## Task 1 foundation evidence

| Evidence item | Record |
|---|---|
| Coordinator | Chu Junjie |
| Documentation branch | `docs/project-foundation-yuyang-unified` |
| Source branch | `main` |
| Source commit | `c1ac237` |
| Adoption decision | `docs/yuyang-pack-integration-decision.md` |
| Frozen contracts | `docs/frozen-decisions.md` |
| Definition of Done | `docs/definition-of-done.md` |
| Team ownership | `docs/team-task-allocation.md` |
| Current project status | `docs/project-status.md` |
| Tracking Issue | `#16` — Open |
| Project Board status | `In Progress` |
| Candidate test result | `Not executed` |
| Pull Request | `Not opened` |
| Non-author review | `Not started` |
| Current Task 1 status | `In Progress` |

| US | Requirement | Implementation / target | Tests / evidence | Owner | Current status |
|---|---|---|---|---|---|
| US-01 | Natural-language requirement extraction | Yuyang server candidate: category, brand, budget, exclusions, use cases | parser, validation and invalid input tests | Zaikun | Candidate / needs validation fixes |
| US-02 | Database setup/import | products + product_specs import, indexes, health counts | import, 9000/33 counts, join integrity, schema output | Yuyang | Candidate |
| US-03 | Top-5 leaderboard | joined spec-complete recommendation API + real HTML | recommend API tests and frontend Network evidence | Zaikun + Guanyu | Backend candidate / frontend pending |
| US-04 | Recommendation explanations | score reasons and use-case matches | score/reason tests and UI evidence | Zaikun + Guanyu | Candidate |
| US-05 | Compare 2–3 products | product_specs + `/api/compare` + comparison UI | exact count, invalid/missing IDs, field completeness | Yuyang + Zaikun + Guanyu | DB/backend candidate / UI pending |
| US-06 | Exclusions | merge text and explicit excluded_brands | exclusion API and regression tests | Zaikun | Partial |
| US-07 | Product link | `PurchaseURL` from product_specs and safe UI | URL validation and button/manual test | Yuyang + Guanyu | Data candidate / UI pending |
| US-08 | Feedback | feedback table, persistence, API and UI | valid up/down, invalid vote, DB insert | Yuyang + Zaikun + Guanyu | Planned |
| US-09 | Budget alternative | same category, cheaper, different ID, spec-complete | same category, cheaper, different, null case | Zaikun + Guanyu | Planned |
| US-10 | Share leaderboard | URL encode/restore and rerun recommend | special chars, exclusions, second-browser test | Junjie + Guanyu | Planned |

## Required evidence columns before final release

For every Story add:

- priority and justification;
- estimate and dependency;
- Acceptance Criteria;
- Issue;
- branch/commit;
- PR and reviewer;
- automated test command/result;
- manual acceptance result;
- deployment/demo link;
- final status.
