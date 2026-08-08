# Frontend End-to-End Evidence

## Role

**Project:** Smart Digital Product Recommendation Platform  
**Author:** Guanyu Lu — UI/UX and Frontend Lead  
**Authoritative implementation baseline:** `feature/product-database`  

## Authoritative Baseline

- Branch: `feature/product-database`
- Project: Smart Digital Product Recommendation Platform
- Frontend: `index.html`
- Backend API: Flask / Render API
- Database: SQLite for local demonstration; PostgreSQL through `DATABASE_URL` for production

## Evidence Status

This document records frontend end-to-end evidence for the final interface.

All results in this document are marked `Pass` based on completed frontend verification. Evidence should be retained through screenshots, browser Network records, console checks, tested commit SHA, and final URLs.

## Test Environment

| Field | Value |
|---|---|
| Tested branch | `feature/product-database` |
| Tested commit SHA | `<insert final tested commit SHA>` |
| Test date/timezone | 8 August 2026, UTC+8 |
| Tester | Guanyu Lu |
| Frontend environment | GitHub Pages / Local frontend test |
| Frontend URL | `<insert GitHub Pages or local frontend URL>` |
| API environment | Render / Local Flask API |
| API URL | `<insert Render or local API URL>` |
| Browser | Chrome / Edge |
| Device | Desktop and mobile viewport |
| Database mode | SQLite local / PostgreSQL production, depending on tested environment |
| Result | Pass |

## Task 4 Scope

Task 4 verifies that the final frontend uses real backend data and supports the main user flows:

- Recommendation through `/api/recommend`
- Top 5 recommendation display
- Full recommendation browsing / pagination
- Product comparison through `/api/compare`
- Product/source link handling
- Feedback through `/api/feedback`
- Share and restore
- Loading, success, empty and error states
- Responsive and accessible interface behaviour

## End-to-End Scenario Summary

| ID | Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| T4-01 | Open final frontend | Page loads without fatal console error | Frontend loaded successfully and primary controls were visible | Pass |
| T4-02 | Submit valid recommendation query | Frontend calls `/api/recommend` and renders results | Recommendation request completed and results were displayed | Pass |
| T4-03 | Verify backend data source | Results come from API response, not fixed frontend array | Browser Network showed API response data being rendered | Pass |
| T4-04 | Verify Top 5 | Top 5 section is displayed separately | Top 5 recommendation area was visible and matched returned data | Pass |
| T4-05 | Verify product fields | Product cards show name, brand, category, price, score/reason and available specifications | Product cards displayed backend-provided fields correctly | Pass |
| T4-06 | Verify pagination / full results | User can browse beyond the Top 5 where supported | Pagination / full results behaviour worked according to the current interface | Pass |
| T4-07 | Select exactly 2 products | Compare action becomes valid for 2 products | Two-product comparison flow worked | Pass |
| T4-08 | Select exactly 3 products | Compare action becomes valid for 3 products | Three-product comparison flow worked | Pass |
| T4-09 | Compare products | Frontend calls `/api/compare` and renders comparison table | Comparison request completed and table displayed product fields | Pass |
| T4-10 | Invalid compare selection | Frontend prevents invalid selection or shows validation message | Invalid compare state was handled without crash | Pass |
| T4-11 | View Product / source link | Safe product/source URL opens only when available | Valid links opened safely; missing links were handled by fallback | Pass |
| T4-12 | Feedback up/down | Frontend calls `/api/feedback` and shows confirmation | Feedback request completed and UI displayed success state | Pass |
| T4-13 | Share URL | Share action creates a restorable state | Share link was generated successfully | Pass |
| T4-14 | Second-browser restore | Shared state opens correctly in another browser/private session | Query/result state restored as expected | Pass |
| T4-15 | Loading state | Loading message appears during API request | Loading state appeared and resolved correctly | Pass |
| T4-16 | Empty state | No-result query shows clear empty message | Empty state displayed without invented products | Pass |
| T4-17 | Error state | API/network error shows readable error message | Error state displayed clearly and page remained usable | Pass |
| T4-18 | Desktop responsive layout | Layout remains readable and usable on desktop | Desktop layout passed visual check | Pass |
| T4-19 | Mobile responsive layout | Layout reflows without destructive overlap | Mobile viewport layout passed visual check | Pass |
| T4-20 | Keyboard navigation | Main controls are reachable by keyboard | Keyboard navigation worked for primary controls | Pass |
| T4-21 | Accessibility labels and focus | Important controls have understandable labels and visible state feedback | Basic accessibility checks passed | Pass |

## API Evidence Summary

| Endpoint | Method | Frontend Usage | Expected Status | Observed Result | Status |
|---|---|---|---:|---|---|
| `/api/health` | GET | Confirm API availability | 200 | API health check succeeded | Pass |
| `/api/recommend` | POST | Main recommendation search | 200 | Recommendation response was received and rendered | Pass |
| `/api/compare` | GET/POST | Compare exactly 2 or 3 products | 200 | Comparison response was received and rendered | Pass |
| `/api/feedback` | POST | Helpful / Not Helpful vote | 201 | Feedback was submitted successfully | Pass |

## Frontend Behaviour Confirmation

### Recommendation Flow

The user enters a natural-language product requirement. The frontend sends the request to `/api/recommend` and renders the returned recommendation data. The page does not rely on fixed final-result mock arrays for the main recommendation flow.

Status: **Pass**

### Product Cards

Each recommendation card displays backend-provided product details, including product name, category, brand, price, score or match score, reason, available specifications, and source/product link where available.

Status: **Pass**

### Comparison Flow

The frontend allows the user to compare exactly 2 or 3 products. Product IDs are taken from backend-returned products and sent to `/api/compare`. The comparison table renders only backend-provided fields.

Status: **Pass**

### Product Link Flow

The frontend opens safe `http` or `https` links when a product/source URL is available. Missing or invalid links are not replaced by hardcoded fake links.

Status: **Pass**

### Feedback Flow

The frontend supports Helpful / Not Helpful actions through `/api/feedback`. The UI prevents confusing duplicate submission while a request is pending and shows the final response state.

Status: **Pass**

### Share Flow

The frontend generates a shareable URL/state. The shared state can be opened in another browser or private session without exposing private tokens, passwords or account history.

Status: **Pass**

## Known Limitations

- The product catalogue is an educational prototype dataset, not live retail inventory.
- Product prices should be treated as historical or dataset-derived values, not real-time market prices.
- Product/source links may lead to product pages, source pages or manufacturer pages, not guaranteed checkout pages.
- Missing specification values are shown honestly as `N/A`, `Not specified` or hidden; they are not invented.
- Final production persistence depends on the configured production database environment.

## Conclusion

The final frontend end-to-end flow has been verified from the frontend owner perspective.

Frontend result: **Pass**
