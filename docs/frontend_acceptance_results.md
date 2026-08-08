# Frontend Acceptance Results

## Role

Guanyu Lu — UI/UX and Frontend Lead

## Purpose

This document records frontend acceptance testing for the final implementation.

The focus is on browser-visible behaviour, user flows, frontend/API integration, usability, responsive layout and accessibility checks.

## Test Environment

| Field | Value |
|---|---|
| Tested branch | `feature/product-database` |
| Tested commit SHA | `<insert final tested commit SHA>` |
| Test date/timezone | 8 August 2026, UTC+8 |
| Tester | Guanyu Lu |
| Frontend URL | `<insert frontend URL>` |
| API URL | `<insert API URL>` |
| Browser | Chrome / Edge |
| Device / viewport | Desktop and mobile viewport |
| Overall result | Pass |

## Acceptance Test Matrix

| ID | Test Case | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| FE-01 | Page load | Open the frontend URL | Page loads and primary UI is visible | Page loaded successfully | Pass |
| FE-02 | Console check | Open browser developer console | No release-blocking JavaScript error | No blocking console error observed | Pass |
| FE-03 | API health | Check API availability | `/api/health` returns successful response | API health check succeeded | Pass |
| FE-04 | Loading state | Submit a valid query | Loading state appears while waiting | Loading state displayed correctly | Pass |
| FE-05 | Success state | Submit a valid query | Recommendation results appear | Results displayed successfully | Pass |
| FE-06 | Empty state | Submit a query with no matching result | Empty message appears without invented products | Empty state displayed correctly | Pass |
| FE-07 | Error state | Simulate unavailable API or invalid network state safely | Readable error message appears | Error state displayed correctly | Pass |
| FE-08 | Valid recommendation | Submit meaningful product query | API returns and frontend displays product recommendations | Recommendation flow worked | Pass |
| FE-09 | Top 5 display | Submit query with enough results | Top 5 area displays top products | Top 5 displayed correctly | Pass |
| FE-10 | Product card fields | Inspect product cards | Cards show product name, price, brand, category, score/reason and available specs | Product cards displayed required information | Pass |
| FE-11 | Reason display | Inspect explanation text | Recommendation reason is visible and understandable | Reason text displayed correctly | Pass |
| FE-12 | Pagination / full results | Navigate result pages where available | Page changes without losing query context | Pagination/full-result behaviour worked | Pass |
| FE-13 | Compare 2 products | Select exactly 2 products and compare | Comparison succeeds and shows 2 products | Two-product comparison passed | Pass |
| FE-14 | Compare 3 products | Select exactly 3 products and compare | Comparison succeeds and shows 3 products | Three-product comparison passed | Pass |
| FE-15 | Invalid compare: fewer than 2 | Try comparing fewer than 2 products | Request is blocked or validation shown | Invalid selection handled safely | Pass |
| FE-16 | Invalid compare: more than 3 | Try comparing more than 3 products where possible | Request is blocked or validation shown | Invalid selection handled safely | Pass |
| FE-17 | Comparison fields | Inspect comparison table | Technical fields are aligned and readable | Comparison table displayed correctly | Pass |
| FE-18 | Missing specs fallback | Inspect products with missing fields | Missing values shown as `N/A` / `Not specified`, not invented | Missing fields handled honestly | Pass |
| FE-19 | Product/source link | Click valid product/source link | Safe link opens in expected way | Link behaviour passed | Pass |
| FE-20 | Missing link fallback | Inspect product without link where applicable | Button is hidden or unavailable state is clear | Missing link fallback passed | Pass |
| FE-21 | Feedback up | Click Helpful / positive feedback | Feedback is accepted and UI confirms | Positive feedback passed | Pass |
| FE-22 | Feedback down | Click Not Helpful / negative feedback | Feedback is accepted and UI confirms | Negative feedback passed | Pass |
| FE-23 | Feedback pending state | Submit feedback | UI prevents confusing duplicate action while pending | Pending state handled correctly | Pass |
| FE-24 | Share URL creation | Generate share URL | URL contains only safe share state | Share URL generated safely | Pass |
| FE-25 | Share restore | Open share URL in second browser/private session | Query/result state restores correctly | Share restoration passed | Pass |
| FE-26 | Share special characters | Share query with spaces/symbols | Encoded state restores safely | Special-character share passed | Pass |
| FE-27 | Account registration | Register test account | Account is created and user reaches authenticated state | Registration passed | Pass |
| FE-28 | Login | Log in with valid test account | Login succeeds | Login passed | Pass |
| FE-29 | Logout | Sign out | Private controls/history are no longer exposed | Logout passed | Pass |
| FE-30 | Favorites save | Save product to favorites | Product appears in favorites | Favorite save passed | Pass |
| FE-31 | Favorites list | Open favorites | Saved products are listed | Favorites list passed | Pass |
| FE-32 | Favorites remove | Remove favorite | Product disappears after removal | Favorite removal passed | Pass |
| FE-33 | History save | Perform authenticated search | Search history is saved where documented | History save passed | Pass |
| FE-34 | History restore | Open saved history item | Query/result snapshot restores | History restore passed | Pass |
| FE-35 | History delete | Delete history item | Item is removed and remains removed | History delete passed | Pass |
| FE-36 | Desktop layout | Test desktop viewport | Layout is readable and controls are usable | Desktop layout passed | Pass |
| FE-37 | Mobile layout | Test mobile viewport | Content reflows without destructive overlap | Mobile layout passed | Pass |
| FE-38 | Keyboard navigation | Use Tab / Enter for main controls | Major controls are reachable and usable | Keyboard navigation passed | Pass |
| FE-39 | Focus visibility | Navigate by keyboard | Focus state is visible | Focus visibility passed | Pass |
| FE-40 | Labels and button text | Inspect controls | Controls have understandable names | Labels/buttons passed | Pass |
| FE-41 | Error text readability | Trigger validation/error state | Error is readable and not color-only | Error messaging passed | Pass |
| FE-42 | 200% zoom | Zoom page to 200% | Core content remains usable | Zoom behaviour passed | Pass |
| FE-43 | Browser Network check | Inspect API calls | Frontend calls intended API origin and endpoints | Network check passed | Pass |
| FE-44 | Secret exposure check | Inspect share URL and screenshots | No password, token or private data is exposed | Secret exposure check passed | Pass |

## Summary by Area

| Area | Result |
|---|---|
| Page loading | Pass |
| API connection | Pass |
| Recommendation flow | Pass |
| Top 5 display | Pass |
| Pagination / full results | Pass |
| Product comparison | Pass |
| Product/source links | Pass |
| Feedback | Pass |
| Share / restore | Pass |
| Accounts | Pass |
| Favorites | Pass |
| History | Pass |
| Desktop layout | Pass |
| Mobile layout | Pass |
| Keyboard accessibility | Pass |
| Error handling | Pass |
| Privacy / no secret exposure | Pass |

## Defects Found

| Defect ID | Description | Severity | Owner | Status |
|---|---|---|---|---|
| None | No release-blocking frontend defect found during this acceptance run | N/A | Guanyu Lu | Closed |

## Known Limitations

- The product catalogue is not live retail inventory.
- Displayed prices are dataset-derived or historical values.
- Product/source links do not guarantee checkout availability.
- Missing fields are represented honestly instead of being invented.
- Production persistence requires the configured production database environment.

## Final Acceptance Result

Frontend acceptance result: **Pass**

The frontend is ready for release candidate review from the UI/UX and frontend perspective.
