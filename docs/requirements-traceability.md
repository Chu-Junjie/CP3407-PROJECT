# Requirements Traceability — Yuyang Unified Baseline

This is a live matrix. `Candidate` means code was supplied but is not verified until merged and tested.

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
