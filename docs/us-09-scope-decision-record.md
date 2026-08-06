# US-09 Budget Alternatives — V3 Scope Decision Record

**Tracking Issue:** #40  
**Current status:** `Scope confirmation required`  
**Coordinator:** Chu Junjie  
**Decision date:** Not decided  
**Selected option:** Not decided

## 1. Purpose

This document is the version-controlled decision record for whether US-09 Budget Alternatives remains in the V3 release scope.

It does not select an option in advance and does not claim that the feature is implemented, verified or required for release.

## 2. Current evidence boundary

- The historical README labels US-09 as `In-Progress`.
- The current V3 governance baseline records that scope confirmation is required.
- No final V3 acceptance criteria, automated-test evidence or deployed-E2E evidence has been approved for US-09.
- Zaikun and Guanyu have been asked in Issue #40 to record component impact and recommend Option A, B or C.

Until the team completes this record, US-09 must not be described as `Done`, `Verified` or a confirmed V3 release requirement.

## 3. Decision options

### Option A — Retain the original feature

V3 must provide a cheaper qualifying alternative for recommendation results.

The final requirement must define:

- the percentage or absolute price difference that counts as cheaper;
- whether the alternative must be in the same product category;
- which use-case requirements and core specifications cannot be sacrificed;
- whether an alternative is evaluated for every Top-5 result or only where a valid candidate exists;
- API response fields;
- frontend presentation and comparison wording;
- empty-state behaviour;
- automated and deployed acceptance evidence;
- delivery estimate and release impact.

### Option B — Revise the feature

Replace the historical story with a V3-compatible optional-alternative requirement.

The final requirement must define:

- exact user value and final story wording;
- eligibility and ranking rules;
- API and UI behaviour;
- relationship to the separate Top 5 and paginated result list;
- acceptance criteria and tests;
- delivery estimate and release impact.

### Option C — Defer the feature

Remove US-09 from the current V3 release commitment while retaining it in the product backlog.

The final record must define:

- reason for deferral;
- user and assessment impact;
- V3 limitation wording;
- README/status correction required later;
- future milestone or `Unscheduled`;
- demonstration wording that avoids implying the feature is present.

## 4. Backend, recommendation and API owner input

**Owner:** Zaikun (`ZhengZaikun`)  
**Issue #40 response:** Pending

### Required response

- Recommended option: Pending
- Reason: Pending
- Price eligibility rule: Pending / Not applicable
- Category constraint: Pending / Not applicable
- Core specification safeguards: Pending / Not applicable
- Ranking behaviour: Pending / Not applicable
- API fields or contract change: Pending / Not applicable
- Backend implementation change: Pending / Not applicable
- Automated tests required: Pending / Not applicable
- Estimate: Pending
- Main risk: Pending
- Release impact: Pending

## 5. Frontend, interaction and browser-E2E owner input

**Owner:** Guanyu (`Guanyu-Lu`)  
**Issue #40 response:** Pending

### Required response

- Recommended option: Pending
- Reason: Pending
- Alternative-card presentation: Pending / Not applicable
- Price-difference wording: Pending / Not applicable
- Empty-state behaviour: Pending / Not applicable
- Top-5 relationship: Pending / Not applicable
- Pagination relationship: Pending / Not applicable
- Desktop/mobile interaction: Pending / Not applicable
- Accessibility impact: Pending / Not applicable
- Browser-E2E scenarios required: Pending / Not applicable
- Estimate: Pending
- Main risk: Pending
- Release impact: Pending

## 6. Coordinator scope and schedule assessment

**Owner:** Junjie (`Chu-Junjie`)  
**Assessment status:** Pending owner input

The coordinator assessment must record:

- whether the selected option is achievable without bypassing current CI, database, deployment and E2E blockers;
- whether new implementation would violate the current change-control period;
- whether the work changes the release-candidate date;
- whether separate backend and frontend Issues/branches/PRs are required;
- whether the feature should be included in the final demonstration or recorded as a known limitation.

The coordinator does not estimate or select technical implementation on behalf of the component owners.

## 7. Final team decision

Complete only after owner input exists.

| Field | Final value |
|---|---|
| Selected option | Pending |
| Final requirement wording | Pending |
| Reason | Pending |
| Backend/API impact | Pending |
| Frontend impact | Pending |
| Automated-test impact | Pending |
| Deployed-E2E impact | Pending |
| Release/schedule impact | Pending |
| Known limitation | Pending |
| Future backlog/milestone | Pending |
| Decision participants | Pending |
| Decision date and timezone | Pending |

## 8. Acceptance criteria if Option A or B is selected

Do not populate as approved criteria until the team selects Option A or B.

- [ ] Eligibility rule is deterministic and documented.
- [ ] Alternative belongs to the approved category relationship.
- [ ] Required use-case constraints and core specifications are preserved.
- [ ] API response contract is documented.
- [ ] Frontend presentation and empty state are documented.
- [ ] Top-5 and pagination interaction is unambiguous.
- [ ] Automated tests cover valid alternative, no valid alternative, boundary values and invalid data.
- [ ] Deployed E2E confirms the intended API request and UI response.
- [ ] Source and historical-price wording does not imply live retail data.
- [ ] Owner-controlled implementation PRs receive review and pass agreed release checks.

## 9. Completion criteria if Option C is selected

- [ ] Deferral reason is recorded.
- [ ] Current V3 scope explicitly excludes US-09.
- [ ] Historical README `In-Progress` wording is scheduled for correction.
- [ ] Demonstration and report limitations are approved.
- [ ] Backlog status or future milestone is recorded.
- [ ] No implementation is removed merely to support the decision without the technical owner's approval.

## 10. Documents requiring later correction

The following may require a separately approved update after the decision:

- `README.md`;
- `docs/project-status.md`;
- `docs/requirements-traceability.md`;
- `docs/v3-execution-plan.md`;
- `docs/final-acceptance-and-release-checklist.md`;
- V3 release evidence index;
- demonstration and final-report wording.

No status correction should be committed before the final decision is approved.

## 11. Implementation process if work is required

1. Record the final Issue #40 decision.
2. Create separate owner-controlled implementation Issues where required.
3. Zaikun owns backend, algorithm, API and automated-test work.
4. Guanyu owns frontend, interaction and browser-E2E implementation work.
5. Each owner uses an independent branch and Pull Request.
6. Preserve the current V3 baseline and do not merge directly to `main`.
7. Execute the agreed complete test suite.
8. Execute deployed E2E for the final acceptance criteria.
9. Update governance and README wording only after evidence exists.

## 12. Review checklist

### Zaikun

- [ ] My recommendation and impact assessment are recorded accurately.
- [ ] Algorithm, API and automated-test requirements are technically feasible and unambiguous.
- [ ] No backend result is claimed without evidence.

### Guanyu

- [ ] My recommendation and interaction assessment are recorded accurately.
- [ ] UI, empty-state, responsive and E2E requirements are unambiguous.
- [ ] No frontend/deployed result is claimed without evidence.

### Junjie

- [ ] The final selected option is explicitly approved by the team.
- [ ] Schedule and release impact are recorded without inventing owner estimates.
- [ ] Required later document corrections are identified.
- [ ] No teammate-owned implementation is modified through this decision record.

## 13. Non-authorization statement

This decision record does not authorize:

- choosing Option A, B or C without the required team decision;
- modifying backend, recommendation logic, API, tests or frontend;
- changing README or current status documents;
- marking US-09 as `Done` or `Verified`;
- merging a technical implementation;
- merging V3 to `main`.
