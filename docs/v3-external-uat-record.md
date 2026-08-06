# V3 External User Acceptance Test Record

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative baseline:** `feature/product-database`  
**Coordinator:** Junjie Chu  
**Tracking Issue:** #36  
**Required participants:** Two people who are not members of the project team  
**Document status:** Preparation template — no tester result is claimed

## 1. Purpose

This document records task-based acceptance testing by two independent non-team participants. The goal is to evaluate whether a new user can understand and complete the main V3 flows, not merely whether the API returns a successful status.

Both tester records begin as `Not Run`. Do not pre-fill positive answers, infer tester opinions or convert team-member testing into external UAT evidence.

## 2. Coordinator and ownership boundary

Junjie may recruit participants, explain the session rules, observe without leading, record consent, retain evidence, summarize findings and create Issues.

This UAT record does not authorize Junjie to modify teammate-owned frontend, backend, tests, datasets, database, importer or deployment configuration. A discovered defect must be assigned to the responsible owner.

## 3. Participant eligibility and privacy

Each participant must:

- not be a member of the project team;
- be able to give informed consent to participate;
- use only demonstration information;
- not enter a real password used elsewhere, personal payment information or sensitive personal data;
- understand that the product catalogue and prices are educational/historical rather than live retail information.

Record only the minimum participant information required for evidence. Use a participant code rather than a full legal name where appropriate.

## 4. Session status definitions

| Status | Meaning |
|---|---|
| `Not Run` | The task/session has not been executed. |
| `Completed independently` | The participant completed the task without intervention. |
| `Completed with prompt` | The participant completed the task after a neutral prompt; record the prompt. |
| `Not completed` | The participant could not complete the task. |
| `Blocked` | A technical/environment dependency prevented the task. |
| `Not applicable` | The task was deliberately excluded with a recorded reason. |

## 5. Facilitation rules

- Use the same task wording for both participants unless an accessibility accommodation is required.
- Do not tell the participant exactly where to click.
- A neutral prompt may restate the goal but must not reveal the solution.
- Record first-attempt behavior before helping.
- Record observed confusion even if the participant eventually succeeds.
- Do not ask leading questions such as “Was that easy?” before the rating questions.
- Retain screenshots or recordings only with participant consent.
- Redact usernames, emails, tokens and other identifiers from committed evidence.

## 6. Shared test environment

Complete before the first session.

| Field | Value |
|---|---|
| UAT batch ID | `UAT-YYYYMMDD-01` |
| Tested branch | `feature/product-database` |
| Tested commit SHA | `Not Run` |
| Frontend environment and URL | `Not Run` |
| API environment and URL | `Not Run` |
| Database mode | `Not Run` |
| Session location/mode | `In person / Remote: Not Run` |
| Coordinator | Junjie Chu |
| Evidence storage location | `Not Run` |
| Known blockers disclosed to testers | `Not Run` |

## 7. Standard participant task script

Read the introduction, then present one task at a time.

### Introduction

> This is an educational digital-product recommendation prototype. Please use demonstration details only. Product prices and catalogue information may come from historical public datasets and are not guaranteed to be current retail information. I am testing the product, not you. Please think aloud. I will usually observe without telling you where to click.

### Tasks

| ID | Participant instruction | Success condition |
|---|---|---|
| UAT-01 | “Start from the home page and find a laptop recommendation within a budget that you choose.” | The participant submits a meaningful query and reaches a visible results state. |
| UAT-02 | “Explain what you think the Top 5 section means, then view more results.” | The participant identifies the Top 5 and uses pagination or the available results navigation. |
| UAT-03 | “Choose two products and compare them.” | Exactly two distinct products are selected and a comparison result is reached. |
| UAT-04 | “Create a demonstration account or sign in using the supplied demonstration account.” | The participant reaches an authenticated state and can identify that they are signed in. |
| UAT-05 | “Save two products that interest you and find them again.” | Two favorites are added and the participant opens the favorites list. |
| UAT-06 | “Use your saved products to compare two products from the same category.” | A same-category favorites comparison is completed, or the participant clearly understands why a mixed-category selection is rejected. |
| UAT-07 | “Find a previous recommendation search and reopen it.” | The participant opens private history and restores a saved search/result snapshot. |
| UAT-08 | “Delete one saved history item.” | The selected history item is removed and stays removed after refresh where practical. |
| UAT-09 | “Give feedback on the recommendation.” | A positive or negative feedback action is submitted and acknowledged. |
| UAT-10 | “Share this recommendation and open it in a second browser/private window.” | A share URL is produced and the intended shareable state restores in the second session without exposing private account information. |
| UAT-11 | “Tell me where the product information comes from and whether you believe the displayed price is live.” | The participant can find or infer the source wording and does not incorrectly conclude that all prices are live. |
| UAT-12 | “Sign out, then check whether private favorites or history are still visible.” | Private data is no longer available while unauthenticated. |

## 8. Observation codes

Use these codes consistently in both records.

| Code | Observation |
|---|---|
| `NAV` | Navigation or page-location confusion |
| `WORD` | Label, instruction or terminology confusion |
| `STATE` | Loading, empty, success or error state was unclear |
| `AUTH` | Registration, login, logout or identity confusion |
| `TOP5` | Top 5 and full-result relationship was unclear |
| `PAGE` | Pagination was missed or misunderstood |
| `COMP` | Product selection or comparison confusion |
| `FAV` | Favorite workflow confusion |
| `HIST` | History/snapshot workflow confusion |
| `SHARE` | Share URL behavior or privacy confusion |
| `SOURCE` | Data-source or price-freshness misunderstanding |
| `MOBILE` | Responsive/mobile usability problem |
| `A11Y` | Keyboard, focus, label, contrast or other accessibility observation |
| `PERF` | Noticeable waiting, delay or perceived performance problem |
| `DEFECT` | A reproducible technical failure |

---

# Participant A Record

## A1. Participant and session metadata

| Field | Value |
|---|---|
| Participant code | `UAT-A` |
| Non-team status confirmed | Not Run |
| General role/background | Not Run |
| Relevant product-shopping experience | Not Run |
| Device | Not Run |
| Browser/version | Not Run |
| Viewport/screen | Not Run |
| Date/timezone | Not Run |
| Session duration | Not Run |
| Recording/screenshot consent | Not Run |
| Demonstration account used | Not Run |
| Facilitator | Junjie Chu |

## A2. Task results

| Task | Status | Time | Prompts given | Observation codes | Participant behavior/quote | Evidence | Linked Issue |
|---|---|---:|---|---|---|---|---|
| UAT-01 | Not Run | | | | | | |
| UAT-02 | Not Run | | | | | | |
| UAT-03 | Not Run | | | | | | |
| UAT-04 | Not Run | | | | | | |
| UAT-05 | Not Run | | | | | | |
| UAT-06 | Not Run | | | | | | |
| UAT-07 | Not Run | | | | | | |
| UAT-08 | Not Run | | | | | | |
| UAT-09 | Not Run | | | | | | |
| UAT-10 | Not Run | | | | | | |
| UAT-11 | Not Run | | | | | | |
| UAT-12 | Not Run | | | | | | |

## A3. Post-session questions

Ask after all tasks.

| Question | Participant response | Rating |
|---|---|---|
| What did you think this application was for? | Not Run | N/A |
| Which part was easiest? Why? | Not Run | N/A |
| Which part was most confusing? Why? | Not Run | N/A |
| Did you understand the difference between Top 5 and the other results? | Not Run | Yes/Partly/No |
| Did you understand that prices may be historical and not live? | Not Run | Yes/Partly/No |
| Did you feel confident that favorites/history were private to your account? | Not Run | 1–5 |
| How easy was it to find a recommendation? | Not Run | 1–5 |
| How easy was comparison? | Not Run | 1–5 |
| How easy were favorites and history? | Not Run | 1–5 |
| How easy was sharing? | Not Run | 1–5 |
| Overall satisfaction | Not Run | 1–5 |
| What is the one change you would make first? | Not Run | N/A |

## A4. Participant A summary

| Metric | Result |
|---|---|
| Tasks completed independently | Not Run |
| Tasks completed with prompt | Not Run |
| Tasks not completed | Not Run |
| Blocked tasks | Not Run |
| Critical defects | Not Run |
| Overall satisfaction | Not Run |
| Participant A acceptance decision | Not Run |

Coordinator summary: `Not Run`

---

# Participant B Record

## B1. Participant and session metadata

| Field | Value |
|---|---|
| Participant code | `UAT-B` |
| Non-team status confirmed | Not Run |
| General role/background | Not Run |
| Relevant product-shopping experience | Not Run |
| Device | Not Run |
| Browser/version | Not Run |
| Viewport/screen | Not Run |
| Date/timezone | Not Run |
| Session duration | Not Run |
| Recording/screenshot consent | Not Run |
| Demonstration account used | Not Run |
| Facilitator | Junjie Chu |

## B2. Task results

| Task | Status | Time | Prompts given | Observation codes | Participant behavior/quote | Evidence | Linked Issue |
|---|---|---:|---|---|---|---|---|
| UAT-01 | Not Run | | | | | | |
| UAT-02 | Not Run | | | | | | |
| UAT-03 | Not Run | | | | | | |
| UAT-04 | Not Run | | | | | | |
| UAT-05 | Not Run | | | | | | |
| UAT-06 | Not Run | | | | | | |
| UAT-07 | Not Run | | | | | | |
| UAT-08 | Not Run | | | | | | |
| UAT-09 | Not Run | | | | | | |
| UAT-10 | Not Run | | | | | | |
| UAT-11 | Not Run | | | | | | |
| UAT-12 | Not Run | | | | | | |

## B3. Post-session questions

| Question | Participant response | Rating |
|---|---|---|
| What did you think this application was for? | Not Run | N/A |
| Which part was easiest? Why? | Not Run | N/A |
| Which part was most confusing? Why? | Not Run | N/A |
| Did you understand the difference between Top 5 and the other results? | Not Run | Yes/Partly/No |
| Did you understand that prices may be historical and not live? | Not Run | Yes/Partly/No |
| Did you feel confident that favorites/history were private to your account? | Not Run | 1–5 |
| How easy was it to find a recommendation? | Not Run | 1–5 |
| How easy was comparison? | Not Run | 1–5 |
| How easy were favorites and history? | Not Run | 1–5 |
| How easy was sharing? | Not Run | 1–5 |
| Overall satisfaction | Not Run | 1–5 |
| What is the one change you would make first? | Not Run | N/A |

## B4. Participant B summary

| Metric | Result |
|---|---|
| Tasks completed independently | Not Run |
| Tasks completed with prompt | Not Run |
| Tasks not completed | Not Run |
| Blocked tasks | Not Run |
| Critical defects | Not Run |
| Overall satisfaction | Not Run |
| Participant B acceptance decision | Not Run |

Coordinator summary: `Not Run`

## 9. Combined results

Complete only after both sessions.

| Measure | Participant A | Participant B | Combined interpretation |
|---|---|---|---|
| Independent task completion | Not Run | Not Run | Not Run |
| Prompted completion | Not Run | Not Run | Not Run |
| Non-completion | Not Run | Not Run | Not Run |
| Overall satisfaction | Not Run | Not Run | Not Run |
| Understood Top 5 | Not Run | Not Run | Not Run |
| Understood historical-price limitation | Not Run | Not Run | Not Run |
| Privacy confidence | Not Run | Not Run | Not Run |

## 10. Findings and action register

Do not silently convert observations into implementation changes. Link each actionable finding to an owner.

| Finding ID | Evidence/tester | Observation | Severity | Responsible owner | GitHub Issue | Decision/status |
|---|---|---|---|---|---|---|
| `UAT-F01` | Not Run | Not Run | Not Run | Not Run | Not Run | Not Run |

Suggested severity interpretation:

- `Critical`: security/privacy loss, data corruption or core flow impossible for both testers;
- `High`: a required user story cannot be completed without help;
- `Medium`: completion is possible but confusing, misleading or error-prone;
- `Low`: cosmetic, wording or minor efficiency issue.

## 11. UAT release gate

The external UAT gate is satisfied only when:

- [ ] two eligible non-team participants completed the recorded sessions;
- [ ] tested commit and environment metadata are complete;
- [ ] no result was fabricated or inferred;
- [ ] every non-completed or blocked required task is explained;
- [ ] every Critical/High defect has an owner and resolution/retest decision;
- [ ] price/source limitations were understood or wording changes were assigned;
- [ ] private account data was not exposed between sessions;
- [ ] evidence was redacted and stored safely;
- [ ] the team recorded an explicit accept/reject decision for the tested release candidate.

## 12. Final acceptance decision

| Role | Name/code | Decision | Date/timezone | Notes |
|---|---|---|---|---|
| Participant A | UAT-A | Not Run | Not Run | |
| Participant B | UAT-B | Not Run | Not Run | |
| Coordinator | Junjie Chu | Not Run | Not Run | |
| Non-author reviewer | Not Run | Not Run | Not Run | |

Final UAT decision: `Not Run`

This decision applies only to the named commit and environment. It does not replace CI, security, database-provenance, deployment-persistence or final release evidence.
