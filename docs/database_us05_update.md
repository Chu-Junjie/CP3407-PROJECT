# Database Update for US-05 Product Spec Comparison

## Problem Found

The original product dataset supported recommendation filtering, but it did not fully support US-05 Product Spec Comparison.

Original fields:

- ProductID
- ProductCategory
- ProductBrand
- ProductPrice
- CustomerAge
- CustomerGender
- PurchaseFrequency
- CustomerSatisfaction
- PurchaseIntent

These fields are enough for category, brand, price, satisfaction, and purchase-intent recommendation scoring. However, they do not include the hardware specifications needed for side-by-side comparison.

## Database Improvement

To support US-05, a new `product_specs.csv` dataset was added and imported into a new SQLite table called `product_specs`.

New specification fields:

- ProductName
- CPU
- GPU
- RAM
- Storage
- ScreenSize
- BatteryLife
- Weight
- UseCase
- PurchaseURL

The `product_specs` table is joined with the existing `products` table through `ProductID`.

For the current US-05 demonstration, recommendations use an `INNER JOIN`. This means
the Top 5 is selected only from products that have complete specification records,
instead of returning products whose specifications would display as `Not available`.

Unique indexes are created for `ProductID` in both tables to protect the one-to-one
join and improve lookup performance.

## Data Provenance and Limitations

- The 9,000 recommendation records come from the project-provided
  `US-02 Database Setup & Import.csv` file. Its original external source, licence,
  collection date, and currency still need to be confirmed by the team.
- The 33 rows in `product_specs.csv` are a small educational prototype dataset
  prepared for the US-05 demonstration. They are not a complete market catalogue.
- Product prices are inherited from the original 9,000-row dataset. They must not
  be described as current, verified, or real-time market prices.
- Specification values and URLs should be checked against official manufacturer
  pages before production use.
- Some `PurchaseURL` values lead to a manufacturer homepage rather than a specific
  checkout page. They demonstrate URL storage but do not, by themselves, complete
  the US-07 Buy Now user story.

## Data Dictionary

| Field | Type | Purpose |
|---|---|---|
| `ProductID` | Integer | Unique link to the original `products` record |
| `ProductName` | Text | Human-readable model name |
| `CPU` | Text | Processor model |
| `GPU` | Text | Graphics processor/model |
| `RAM` | Text | Installed memory description |
| `Storage` | Text | Storage capacity and type |
| `ScreenSize` | Text | Display size |
| `BatteryLife` | Text | Claimed battery duration |
| `Weight` | Text | Product weight |
| `UseCase` | Text | Searchable use-case labels |
| `PurchaseURL` | URL text | Manufacturer or product information link |

## Backend Improvement

`server.py` was updated with:

- Automatic import for both `products` and `product_specs`
- Extended recommendation payloads containing real specification fields
- A new `/api/compare` endpoint for US-05
- Use-case keyword matching for queries such as gaming, study, office, portable, battery, creative, 3D, camera, and budget
- Natural-language category inference for laptops, smartphones, tablets, headphones, and smart watches
- Strict validation requiring exactly two or three valid IDs for `/api/compare`
- Configurable CORS origins and production-safe debug configuration

## Automated Database Tests

Run:

```text
pytest -q test_database_us05.py
```

The tests verify:

- Both tables are imported with the expected record counts
- Every specification `ProductID` exists in `products`
- No duplicate specification IDs or empty required fields exist
- Natural-language categories are recognised
- Recommended comparison products always contain specifications
- `/api/compare` accepts exactly two or three valid IDs
- Purchase URLs contain a valid HTTP/HTTPS scheme and hostname

## New API Evidence

Health check:

```text
GET /api/health
```

Expected evidence:

```text
records: 9000
spec_records: 33
```

Comparison endpoint:

```text
GET /api/compare?ids=5885,5937,5960
```

Expected evidence:

- Returns exactly the requested products when specification records exist
- Includes CPU, GPU, RAM, Storage, ScreenSize, BatteryLife, Weight, UseCase, and PurchaseURL
- Data comes from the SQLite database, not mock frontend data

## Practical 6 / Iteration 2 Database Note

The previous database design was sufficient for US-02 and US-03, but it was not enough for US-05. In Iteration 2, the database was improved by adding product specification records and a comparison API. This connects the user story requirement, database design, backend implementation, and testable API evidence.
