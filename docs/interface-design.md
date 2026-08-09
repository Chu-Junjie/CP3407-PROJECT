# Interface Design Documentation

## Role

Guanyu Lu — UI/UX and Frontend Lead

## Project

Smart Digital Product Recommendation Platform

## Authoritative Baseline

- Branch: `feature/product-database`
- Frontend file: `index.html`
- Backend API: Flask / SQLAlchemy API
- Deployment model: GitHub Pages frontend calling Render API
- Database model: SQLite local demonstration; PostgreSQL through `DATABASE_URL` for production

## Purpose

This document explains the final as-built frontend interface design, user flow, design decisions, responsive behaviour, accessibility considerations and known limitations.

The document reflects the final implemented interface rather than early mock-only prototypes.

## Design Goal

The interface is designed to help users find suitable digital products through a simple recommendation workflow:

1. The user enters natural-language product requirements.
2. The system returns ranked recommendations.
3. The user reviews the Top 5 and browses additional matches.
4. The user compares 2 or 3 products.
5. The user can save products, view history, submit feedback and share results.

## Primary Users

The target users are general consumers who may not have deep hardware knowledge. The interface therefore prioritises:

- Simple input language
- Clear recommendation cards
- Visible scores and reasons
- Side-by-side comparison
- Safe product/source links
- Clear feedback and share actions
- Responsive desktop and mobile experience

## Main User Flow

```text
Open frontend
→ Enter product requirement
→ Submit recommendation request
→ View loading state
→ View Top 5 and full results
→ Inspect product cards and reasons
→ Select 2 or 3 products
→ Compare products
→ Save favorites or review history if logged in
→ Submit feedback
→ Share result link
# Page Structure
```

The final interface is organised into these major areas:

| Area | Purpose |
|------|---------|
| Header / brand area | Identifies the application and provides entry to account-related controls |
| Query input area | Allows users to describe their product needs in natural language |
| Status area | Shows loading, success, empty or error states |
| Top 5 area | Highlights the strongest recommendation results |
| Full results area | Allows browsing additional recommendation results where available |
| Product card area | Shows product identity, price, score, reason and available specification fields |
| Comparison area | Displays selected products side‑by‑side |
| Account center | Supports login, favorites and search history where available |
| Feedback area | Allows Helpful / Not Helpful response |
| Share area | Provides a safe shareable result state |

## Recommendation Input Design

The input is designed to accept natural language, such as:

> I need a lightweight laptop under $1500, no Apple

The user does not need to fill a long technical form. The interface depends on the backend to parse supported fields such as category, budget, brand and exclusions.

**Design reason:**
- Reduces friction for non‑technical users
- Matches the project requirement for natural‑language input
- Keeps the UI simple and approachable

## Loading, Success, Empty and Error States

| State | Design Behaviour |
|-------|------------------|
| Loading | The interface shows that the request is in progress and avoids duplicate/confusing actions |
| Success | Recommendation cards and Top 5 results are displayed |
| Empty | The interface clearly states that no matching products were found |
| Error | The interface shows a readable message and allows the user to recover |

These states are important because the frontend depends on a remote API. Users should understand whether the system is working, empty, or temporarily unavailable.

## Product Card Design

Each product card is designed to show:
- Product name
- Brand
- Category
- Price
- Match score or score
- Recommendation reason
- Available specification fields
- Product/source link where available
- Selection control for comparison
- Save/favorite action where applicable

**Design reason:**
- Users can quickly scan recommended products.
- Scores help prioritise options.
- Reasons increase transparency and trust.
- Specification fields support decision‑making.
- Missing fields are not invented.

## Top 5 Design

The Top 5 section gives users a quick shortlist of the strongest recommendations.

**Design reason:**
- Reduces choice overload
- Supports quick decision‑making
- Keeps the main recommendation result easy to understand
- Allows the user to continue browsing more results through pagination where supported

## Full Results and Pagination

The V3 interface supports browsing beyond the Top 5 where the backend provides paginated results.

**Design reason:**
- Top 5 gives a quick shortlist.
- Pagination allows broader exploration.
- Users can inspect more suitable products without loading an overwhelming single page.

## Product Comparison Flow

The comparison flow is designed around the rule:
> The user selects exactly 2 or 3 products.

The frontend sends selected product IDs to `/api/compare` and renders the returned comparison fields.

Comparison table fields may include:
- Product name
- Brand
- Category
- Price
- CPU
- GPU
- RAM
- Storage
- Screen
- Battery
- Weight
- Source / data field where available

**Design reason:**
- Side‑by‑side comparison is easier than reading separate product cards.
- Restricting to 2 or 3 products keeps the table readable.
- Backend‑provided values are used directly.
- Missing values are shown as N/A or Not specified.

## Favorites Design

When account features are available, the user can save products to favorites.

**Design reason:**
- Users can keep interesting products for later.
- Favorites support repeat comparison.
- Favorites are account‑owned and should not be visible to other users.

## Search History Design

Authenticated users can reopen previous recommendation searches and result snapshots.

**Design reason:**
- Users often compare products over multiple sessions.
- History supports continuity.
- Private history makes the system more useful than a one‑time recommendation page.

## Feedback Design

The interface supports Helpful / Not Helpful feedback.

**Design reason:**
- Provides a simple user feedback loop.
- Avoids long survey friction.
- Supports future recommendation improvement.
- Gives the user a sense of control.

The feedback UI should display success or error states clearly and avoid duplicate submissions while the request is pending.

## Share Design

The share function allows the user to share a recommendation state with another person.

**Design principles:**
- Share URL should not expose password, JWT, private history or account data.
- Shared state should restore the public recommendation context.
- Special characters and spaces should be safely encoded.
- The shared result should work in a second browser/private session.

## Product / Source Link Design

The product/source link is shown as a safe action such as:

> View Product / Source

or

> View Product / Manufacturer Page

**Design reason:**
- The system should not falsely claim every link is a direct checkout page.
- Links may point to product pages, manufacturer pages or source pages.
- Missing or invalid links should be hidden or shown as unavailable.

## Responsive Design

The interface was designed to remain usable across desktop and mobile viewports.

**Responsive considerations:**
- Cards stack on smaller screens.
- Main controls remain reachable.
- Comparison content remains readable or scrollable.
- Text and buttons avoid destructive overlap.
- The layout supports both quick desktop review and mobile browsing.

> Acceptance result: Pass

## Accessibility Considerations

The final interface considers basic accessibility:
- Important inputs and buttons use understandable labels.
- Status messages are written in text, not only color.
- Keyboard navigation reaches primary controls.
- Focus indicators are visible.
- Error messages are readable.
- Content remains usable under browser zoom.
- The layout does not depend on hover‑only interaction for core tasks.

> Accessibility result: Pass

## Visual Design Rationale

The interface uses a clean product‑dashboard style:
- Card‑based layout for recommendations
- Clear separation between Top 5 and full results
- Badges or score display for match strength
- Tables for comparison
- Simple buttons for feedback, sharing and links
- Neutral spacing and readable hierarchy

This style supports the project goal of reducing decision overload.

## Data Honesty and Limitation Wording

The interface must avoid misleading product claims.

**Required limitation wording:**
- Product data is educational prototype data.
- Prices are historical or dataset‑derived values, not live retail prices.
- Product/source links may not be checkout links.
- Missing specifications are shown honestly.
- The system does not guarantee current availability.

## Final Interface Review

| Area | Result |
|------|--------|
| Main user flow | Pass |
| Recommendation UI | Pass |
| Top 5 display | Pass |
| Product card readability | Pass |
| Comparison flow | Pass |
| Feedback flow | Pass |
| Share flow | Pass |
| Account center | Pass |
| Favorites | Pass |
| History | Pass |
| Desktop responsive design | Pass |
| Mobile responsive design | Pass |
| Keyboard accessibility | Pass |
| Error/empty/loading states | Pass |
| Data honesty wording | Pass |

## Conclusion

The final frontend interface supports the project’s main recommendation, comparison, feedback, account, favorites, history and share flows.

> Interface design result: Pass

The interface is ready for final release candidate review from the UI/UX and frontend perspective.
