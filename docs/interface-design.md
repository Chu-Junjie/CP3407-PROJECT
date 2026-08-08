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
