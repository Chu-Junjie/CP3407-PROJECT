# V3 End-to-End Acceptance Evidence

**Project:** Smart Digital Product Recommendation Platform  
**Authoritative baseline:** `feature/product-database`  
**Coordinator:** Junjie Chu  
**Tracking Issue:** #36  
**Document status:** Preparation template — no execution result is claimed

## 1. Purpose

This document defines the repeatable end-to-end acceptance procedure for the V3 application. It connects the browser interface, Flask API, SQLAlchemy persistence layer and the intended deployed environments without treating code presence, a screenshot or a local unit-test result as final acceptance.

All scenarios in this initial template are `Not Run`. A scenario may be changed to `Passed`, `Failed`, `Blocked` or `Accepted Limitation` only after the named evidence has been retained.

## 2. Ownership boundary

Junjie may:

- coordinate the test session;
- execute acceptance steps;
- retain screenshots and browser Network evidence;
- record results, defects and limitations;
- update governance and traceability after evidence exists.

Junjie must not modify teammate-owned implementation as part of this evidence task. Defects in `index.html`, `server.py`, test files, datasets, database files, import scripts or deployment configuration must be returned to the responsible component owner through an Issue or PR review.

## 3. Status definitions

| Status | Meaning |
|---|---|
| `Not Run` | The scenario is prepared but has not been executed. |
| `Passed` | Every required observation matched the expected result and evidence is retained. |
| `Failed` | At least one required result did not match. A linked Issue is required. |
| `Blocked` | The scenario could not be executed because a named dependency was unavailable. |
| `Accepted Limitation` | The team explicitly accepts a known gap with reason, impact and approval recorded. |

## 4. Evidence integrity rules

- Record the tested commit SHA, frontend URL, API URL, database mode, date/timezone, browser and device.
- Use non-sensitive demonstration credentials only.
- Do not store passwords, JWT values or private tokens in screenshots or committed documents.
- Redact Authorization headers before retaining browser Network screenshots.
- A visual screenshot does not replace Network/API evidence where a request/response is central to the scenario.
- A local result is not deployment evidence.
- A GitHub Actions result is not browser E2E evidence.
- PostgreSQL persistence is not verified until a controlled restart or redeploy check is completed with the deployment owner.
- Each failure must link to an Issue, or be explicitly accepted as a limitation.
- Evidence filenames should use `YYYYMMDD-scenario-id-description`.

## 5. Test-run metadata

Complete one metadata block for each distinct environment.

| Field | Value |
|---|---|
| Run ID | `E2E-YYYYMMDD-01` |
| Date and timezone | `Not Run` |
| Coordinator/tester | `Not Run` |
| Tested branch | `feature/product-database` |
| Tested commit SHA | `Not Run` |
| Frontend environment | `Local / GitHub Pages / Other: Not Run` |
| Frontend URL | `Not Run` |
| API environment | `Local / Render / Other: Not Run` |
| API URL | `Not Run` |
| Database mode | `SQLite / PostgreSQL / Unknown: Not Run` |
| Browser and version | `Not Run` |
| Device/viewport | `Not Run` |
| Network conditions | `Not Run` |
| Related CI run | `Not Run` |

## 6. Preconditions

| ID | Precondition | Status | Evidence/notes |
|---|---|---|---|
| PRE-01 | The exact frontend and API URLs are recorded. | Not Run | |
| PRE-02 | The tested commit SHA is recorded. | Not Run | |
| PRE-03 | `/api/health` responds from the intended API environment. | Not Run | |
| PRE-04 | The health response identifies the expected database backend and table/count information. | Not Run | |
| PRE-05 | Browser developer tools are available for Network evidence. | Not Run | |
| PRE-06 | Two unique non-sensitive test accounts can be created or supplied. | Not Run | |
| PRE-07 | A same-category pair and a mixed-category pair of products are available for comparison checks. | Not Run | |
| PRE-08 | The deployment owner is available if a controlled persistence restart/redeploy is attempted. | Not Run | |

## 7. Core E2E scenario matrix

### 7.1 Application loading and API connection

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-01 | Open the frontend in a clean browser session. | The page loads without a fatal console error; primary controls are visible. | Full-page screenshot; console screenshot if warnings exist. | Not Run | |
| E2E-02 | Observe the initial loading state and allow data/API initialization to complete. | Loading feedback is visible and then resolves; the interface does not remain indefinitely blocked. | Short screen recording or two timestamped screenshots. | Not Run | |
| E2E-03 | Inspect the browser Network panel during the first API call. | The frontend calls the intended API origin, receives the documented response type and does not use a fixed final-result array. | Redacted Network request/response screenshot. | Not Run | |
| E2E-04 | Temporarily use an unavailable API URL or offline mode only where safe and reversible. | The interface shows a clear error state and remains usable enough to retry or recover. | Screenshot; exact reversible test method. | Not Run | |

### 7.2 Registration, login and identity

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-05 | Register Test User A with a unique demonstration username/email and valid password. | Registration succeeds once and returns the authenticated application state. | UI screenshot; redacted Network status/body. | Not Run | |
| E2E-06 | Repeat registration with the same username or email. | Duplicate registration is rejected with a clear message; no duplicate account is created. | UI and redacted Network evidence. | Not Run | |
| E2E-07 | Log out or clear the session, then log in using the documented identifier. | Valid credentials authenticate successfully and the correct user identity is shown. | UI screenshot; `/api/auth/me` redacted evidence. | Not Run | |
| E2E-08 | Attempt login with an incorrect password. | Login is rejected without exposing internal details. | UI and Network status evidence. | Not Run | |
| E2E-09 | Access an authenticated route without a token. | The API returns an authorization failure and private data is not displayed. | Redacted Network evidence. | Not Run | |

### 7.3 Recommendation, Top 5 and pagination

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-10 | Submit a normal recommendation query with a recognizable category and budget. | Results are returned with product identity, category, brand, price, score/reason and available specification/source information. | Results screenshot; redacted response sample. | Not Run | |
| E2E-11 | Compare the displayed page count with the API `count`, `page`, `per_page`, `total_candidates` and `total_pages`. | UI and API pagination values are internally consistent. | UI screenshot and response metadata. | Not Run | |
| E2E-12 | Verify the separate Top 5 section against `top_recommendations`. | Exactly the available Top 5 are shown separately and correspond to the API response. | Side-by-side evidence. | Not Run | |
| E2E-13 | Navigate to page 2 and then back to page 1 where more than one page exists. | The correct page data loads, page controls update and the application does not duplicate or silently reuse page 1. | Two page screenshots; Network evidence. | Not Run | |
| E2E-14 | Submit an out-of-range page or equivalent boundary through the documented UI/API path. | A safe empty/boundary response is shown; the application does not crash. | UI/Network evidence. | Not Run | |
| E2E-15 | Submit an empty or invalid query. | Validation or a clear empty/error state is shown according to the contract. | UI/Network evidence. | Not Run | |
| E2E-16 | Submit a query expected to produce no candidates. | A clear empty state appears; no invented products are displayed. | Screenshot; response evidence. | Not Run | |

### 7.4 Product links and source honesty

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-17 | Inspect several product/source links. | Links are valid absolute HTTP(S) links or are safely omitted/disabled; unsafe schemes are not opened. | UI screenshot; sampled URLs with sensitive data removed. | Not Run | |
| E2E-18 | Inspect price/source wording. | Historical or dataset-derived prices are not described as live retail prices; source information is visible where supplied. | Screenshot. | Not Run | |
| E2E-19 | Inspect products with missing specifications. | Missing values are represented honestly, such as `Not specified`; values are not invented. | Screenshot. | Not Run | |

### 7.5 Standard comparison

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-20 | Select exactly two valid products and compare them. | Comparison succeeds and shows two distinct products with aligned fields. | UI and Network evidence. | Not Run | |
| E2E-21 | Select exactly three valid products and compare them. | Comparison succeeds and shows three distinct products. | UI and Network evidence. | Not Run | |
| E2E-22 | Attempt comparison with fewer than two products. | The action is prevented or the API returns a clear validation error. | UI/Network evidence. | Not Run | |
| E2E-23 | Attempt comparison with more than three or duplicate product IDs through a safe test path. | The request is rejected according to the contract. | Redacted request/response. | Not Run | |

### 7.6 Favorites and favorite comparison

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-24 | As User A, add at least two products to favorites. | Favorites are saved and listed for User A. | UI and Network evidence. | Not Run | |
| E2E-25 | Refresh or sign out/in, then reopen favorites. | Favorites persist in the tested environment. | Before/after evidence. | Not Run | |
| E2E-26 | Compare two favorite products from the same category. | Comparison succeeds and identifies the shared category. | UI and Network evidence. | Not Run | |
| E2E-27 | Attempt favorite comparison using mixed categories. | The comparison is rejected with a clear same-category message. | UI and Network evidence. | Not Run | |
| E2E-28 | Remove a favorite and refresh. | The removed product no longer appears and the remaining count is correct. | Before/after evidence. | Not Run | |

### 7.7 Search history and saved snapshots

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-29 | While authenticated as User A, perform a recommendation search. | A history entry is created and a `history_id` is returned where documented. | UI and redacted Network evidence. | Not Run | |
| E2E-30 | Open the history list and select the saved search. | Query metadata and saved result snapshot are restored consistently. | History list/detail screenshots; Network evidence. | Not Run | |
| E2E-31 | Delete the selected history item. | The item is removed and does not return after refresh. | Before/after evidence. | Not Run | |
| E2E-32 | Access history while unauthenticated. | Access is rejected and no private history is displayed. | Redacted Network evidence. | Not Run | |

### 7.8 Cross-user privacy

Use two non-sensitive demonstration accounts. Do not attempt access beyond the application's normal documented identifiers and routes.

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-33 | Create data for User A, then sign in as User B and open favorites/history. | User B sees only User B's data. | Side-by-side redacted screenshots. | Not Run | |
| E2E-34 | As User B, safely request a known User A history identifier through the documented endpoint. | Access is rejected or the resource is not disclosed. | Redacted request/response. | Not Run | |
| E2E-35 | As User B, attempt deletion of the known User A history identifier through the documented endpoint. | Deletion is rejected; User A's entry remains. | Redacted response and User A recheck. | Not Run | |

### 7.9 Feedback

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-36 | Submit one positive feedback vote. | The API returns the documented creation response and the UI confirms submission. | UI and Network evidence. | Not Run | |
| E2E-37 | Submit one negative feedback vote in a separate valid action. | The response is accepted and aggregate values update consistently where displayed. | UI and Network evidence. | Not Run | |
| E2E-38 | Submit an invalid feedback value through a safe request path. | The request is rejected with a clear validation response. | Redacted request/response. | Not Run | |

### 7.10 Share URL and second-browser restoration

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-39 | Generate/copy the share URL after a recommendation search. | The URL contains only the documented share state and does not expose JWT/password/private history data. | Redacted URL and UI screenshot. | Not Run | |
| E2E-40 | Open the share URL in a second browser or private session. | The intended public/shareable query/result state is restored consistently. | First- and second-browser screenshots. | Not Run | |
| E2E-41 | Modify or remove a share parameter. | Invalid or incomplete state is handled safely without a crash. | Screenshot/Network evidence. | Not Run | |

### 7.11 Responsive, keyboard and accessibility observations

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| E2E-42 | Test at a representative desktop viewport. | Main controls, results, Top 5, pagination and comparison remain readable and usable. | Full-page screenshot with viewport size. | Not Run | |
| E2E-43 | Test at a representative mobile viewport/device. | Content reflows without destructive overlap or inaccessible controls. | Mobile screenshots with device/viewport. | Not Run | |
| E2E-44 | Navigate primary controls using keyboard only. | Focus is visible; major actions can be reached and activated in a logical order. | Short recording or ordered screenshots. | Not Run | |
| E2E-45 | Inspect form labels, button names, status messages and image alternatives where applicable. | Controls have understandable accessible names and state/error feedback is not color-only. | Accessibility-tree or inspector screenshots. | Not Run | |
| E2E-46 | Zoom to 200% on desktop. | Core content remains usable without losing required information or controls. | Screenshot. | Not Run | |

## 8. Deployed integration and persistence

These scenarios must not be marked Passed using local SQLite evidence.

| ID | Procedure | Expected result | Required evidence | Status | Issue/notes |
|---|---|---|---|---|---|
| DEP-01 | From the deployed frontend, execute a recommendation and inspect Network origin. | GitHub Pages or the final frontend calls the intended Render API successfully. | Frontend URL plus redacted Network evidence. | Not Run | |
| DEP-02 | Inspect `/api/health` in the deployed environment. | The response identifies the intended production database backend and expected table/count structure. | Redacted response and timestamp. | Not Run | |
| DEP-03 | Create a test account, favorite and history entry in the deployed environment. | All three operations succeed against the production persistence layer. | UI/Network evidence. | Not Run | |
| DEP-04 | With the deployment owner, perform or wait for a controlled service restart/redeploy, then log in again. | The account, favorite and history entry remain available. | Deployment event reference and before/after evidence. | Not Run | |
| DEP-05 | Confirm that no committed/default JWT secret is relied on in production without exposing the secret value. | Deployment owner provides configuration confirmation; authentication continues after restart as designed. | Owner confirmation or redacted configuration evidence. | Not Run | |

## 9. Evidence register

Add one row per retained item. Do not commit secrets or unredacted tokens.

| Evidence ID | Scenario | Type | File/link | Captured by | Date/timezone | Redaction checked |
|---|---|---|---|---|---|---|
| `EV-001` | `Not Run` | Screenshot/Network/Video/Log | `Not Run` | `Not Run` | `Not Run` | `Not Run` |

## 10. Defect and limitation register

| Scenario | Result | Issue | Owner | Severity | Retest commit | Retest status |
|---|---|---|---|---|---|---|
| `Not Run` | `Not Run` | `Not Run` | `Not Run` | `Not Run` | `Not Run` | `Not Run` |

## 11. Run summary

Complete only after execution.

| Metric | Value |
|---|---|
| Total applicable scenarios | Not Run |
| Passed | Not Run |
| Failed | Not Run |
| Blocked | Not Run |
| Accepted limitations | Not Run |
| Open linked defects | Not Run |
| Environment accepted for release | Not Run |

## 12. Sign-off

| Role | Name | Decision | Date/timezone | Notes |
|---|---|---|---|---|
| Coordinator | Junjie Chu | Not Run | Not Run | |
| Frontend owner/reviewer | Not Run | Not Run | Not Run | |
| Backend owner/reviewer | Not Run | Not Run | Not Run | |
| Database/deployment owner/reviewer | Not Run | Not Run | Not Run | |

A sign-off confirms only the named run and commit. It does not automatically close unrelated CI, security, data-provenance or release blockers.
