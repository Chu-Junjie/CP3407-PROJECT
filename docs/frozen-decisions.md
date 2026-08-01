# Frozen Decisions for Final Integration — Yuyang Unified Baseline

**Freeze date:** 1 August 2026

## Architecture

```text
Browser HTML/CSS/JavaScript
→ Flask routes and validation
→ recommendation / comparison / feedback functions
→ SQLite
   ├── products (9,000 behavioural records)
   ├── product_specs (33 specification records)
   └── feedback (US-08)
```

## Final database scope

```text
products
product_specs
feedback
```

`brand_links` is not part of the final design. US-07 uses `product_specs.PurchaseURL`.

## Product data rules

- `products` remains the source of category, brand, price and behavioural scoring fields.
- `product_specs` provides ProductName, CPU, GPU, RAM, Storage, ScreenSize, BatteryLife, Weight, UseCase and PurchaseURL.
- `ProductID` links the two tables.
- The 33 specification rows are an educational prototype set, not a complete market catalogue.
- Prices are inherited from the original dataset and are not current verified retail prices.
- URLs may lead to manufacturer or information pages rather than checkout pages.

## Final API scope

```text
GET  /api/health
GET  /api/products
POST /api/recommend
GET|POST /api/compare
POST /api/feedback
```

### Recommend request

```text
query
category
brand
max_price
excluded_brands
```

### Recommend response

```text
status
message
filters
count
data
budget_alternative
```

Every result must expose real joined fields required by the UI, including specification fields and `purchase_url`.

### Compare

- Accept exactly 2 or 3 unique valid ProductIDs.
- Return HTTP 400 for invalid, duplicate, missing or specification-less IDs.

### Feedback

- `vote` is `up` or `down`.
- Persist feedback in SQLite and return `feedback_id`.

## User Story decisions

- US-05: real side-by-side specification comparison using `product_specs` and `/api/compare`.
- US-07: open stored manufacturer/product-information URL; do not claim exact Buy Now checkout.
- US-08: validated feedback persisted in `feedback`.
- US-09: one cheaper same-category product with specification data, or `null`.
- US-10: URL parameters; no share/session table.

## Scope exclusions

No login, payment, orders, LLM, framework migration, database migration, live price scraping or market-wide product catalogue.
