# V3 External User Acceptance Test Record

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative baseline:** `feature/product-database`  
**Meeting and participant record maintained by:** @Chu-Junjie  
**Required participants:** Two people who are not members of the project team  
**Document status:** Preparation template — both participant records remain `Not Run`

## 1. Record basis

The external-acceptance scope and defect-routing responsibilities are documented in the team meeting notes maintained by @Chu-Junjie. This template does not claim participant completion, opinions or satisfaction.

## 2. Named responsibilities

- @Chu-Junjie recruits participants, explains the session rules, observes without leading, records non-sensitive results, creates defect Issues and coordinates retesting.
- @Guanyu-Lu receives frontend, interface, responsive, accessibility or browser defects.
- @ZhengZaikun receives backend, API, authentication, recommendation, comparison, favorites, history, feedback or privacy defects.
- @tiantian09091 receives database, catalogue, source, PostgreSQL, persistence or recovery defects.

@Chu-Junjie does not change implementation maintained by @Guanyu-Lu, @ZhengZaikun or @tiantian09091.

## 3. Session rules

- Use a frozen, named candidate SHA and deployed URLs.
- Use non-sensitive demonstration credentials.
- Do not record passwords, tokens, private email addresses or unnecessary participant information.
- Allow the participant to attempt each task independently before providing a prompt.
- Record actual completion, prompts, confusion and failure.
- Do not convert team-member testing into external acceptance.
- Do not mark a task Passed because the API or automated tests passed.

## 4. Participant 1

```text
Participant ID: UAT-01
Status: Not Run
Date/timezone:
Candidate SHA:
Frontend URL:
API URL:
Device:
Browser/version:
Prior familiarity:
Consent recorded: Yes / No
Observer: @Chu-Junjie
```

### Tasks

| Task | Independent completion | Prompt required | Observation | Status | Defect assignment |
|---|---|---|---|---|---|
| Understand the landing page and begin | Not Run |  |  | Not Run | @Guanyu-Lu if applicable |
| Register and log in | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Find a product within a chosen budget | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Move to another result page | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Compare two products | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Save a favorite | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Reopen search history | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Submit feedback | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Share and reopen recommendation state | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Log out and confirm private views close | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |

### Participant 1 summary

```text
Tasks completed independently:
Tasks completed with prompts:
Tasks not completed:
Most confusing point:
Most useful function:
Trust or source concern:
Accessibility observation:
Would use again and why:
Defects created:
Overall result: Not Run / Passed / Failed / Blocked / Accepted Limitation
```

## 5. Participant 2

```text
Participant ID: UAT-02
Status: Not Run
Date/timezone:
Candidate SHA:
Frontend URL:
API URL:
Device:
Browser/version:
Prior familiarity:
Consent recorded: Yes / No
Observer: @Chu-Junjie
```

### Tasks

| Task | Independent completion | Prompt required | Observation | Status | Defect assignment |
|---|---|---|---|---|---|
| Understand the landing page and begin | Not Run |  |  | Not Run | @Guanyu-Lu if applicable |
| Register and log in | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Find a product within a chosen budget | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Move to another result page | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Compare two products | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Save a favorite | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Reopen search history | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Submit feedback | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun / @tiantian09091 |
| Share and reopen recommendation state | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |
| Log out and confirm private views close | Not Run |  |  | Not Run | @Guanyu-Lu / @ZhengZaikun |

### Participant 2 summary

```text
Tasks completed independently:
Tasks completed with prompts:
Tasks not completed:
Most confusing point:
Most useful function:
Trust or source concern:
Accessibility observation:
Would use again and why:
Defects created:
Overall result: Not Run / Passed / Failed / Blocked / Accepted Limitation
```

## 6. Consolidated findings

```text
Candidate SHA:
Participants completed: 0 / 2
Critical blockers:
High-priority usability findings:
Frontend Issues assigned to @Guanyu-Lu:
Backend/API/privacy Issues assigned to @ZhengZaikun:
Database/PostgreSQL/persistence Issues assigned to @tiantian09091:
Accepted limitations recorded by @Chu-Junjie:
Retest required: Yes / No
Release impact: Pending
```

## 7. Retest record

For each fixed defect:

```text
Issue:
Assigned to:
Fix PR and SHA:
Formal reviewer:
Retest participant or observer:
Retest environment:
Observed result:
Status:
```

## 8. Completion criteria

- [ ] @Chu-Junjie records two non-team participants and consent without unnecessary personal data.
- [ ] Both participants attempt the same critical scope on a named candidate.
- [ ] Independent completion and prompts are recorded honestly.
- [ ] Frontend findings are assigned to @Guanyu-Lu.
- [ ] Backend/API/privacy findings are assigned to @ZhengZaikun.
- [ ] Database/PostgreSQL/persistence findings are assigned to @tiantian09091.
- [ ] Blocking defects are fixed through separate reviewed Pull Requests and retested.
- [ ] @Chu-Junjie records the release impact in the team meeting notes and final checklist.

A prepared participant record is not an executed acceptance result.