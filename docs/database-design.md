# Database Design Contract — Yuyang US-05 Unified Scheme

## 1. Final relational design

```text
products (9,000 rows)
    ProductID 1 ───── 0..1 product_specs.ProductID (33 rows)
    ProductID 1 ───── 0..* feedback.top_product_id
```

Final tables:

```text
products
product_specs
feedback
```

There is no `brand_links` table. US-07 uses `product_specs.PurchaseURL`.

## 2. `products`

Existing behavioural dataset fields:

| Field | Purpose |
|---|---|
| ProductID | Join identifier |
| ProductCategory | Category filter |
| ProductBrand | Brand preference/filter/exclusion |
| ProductPrice | Budget filter and cheaper alternative |
| CustomerAge | Behavioural source field |
| CustomerGender | Behavioural source field |
| PurchaseFrequency | Ranking/comparison support |
| CustomerSatisfaction | Ranking/comparison support |
| PurchaseIntent | Ranking/comparison support |

The import must preserve 9,000 rows. A unique ProductID index is required because the original pandas import may not create a declared primary key.

## 3. `product_specs`

Source: `product_specs.csv`, 33 educational prototype records.

| Field | Type | Purpose |
|---|---|---|
| ProductID | Integer | Unique link to products |
| ProductName | Text | Human-readable model name |
| CPU | Text | Processor or device processor description |
| GPU | Text | Graphics description or Not applicable |
| RAM | Text | Memory description |
| Storage | Text | Storage description |
| ScreenSize | Text | Display size or Not applicable |
| BatteryLife | Text | Claimed duration |
| Weight | Text | Product weight |
| UseCase | Text | Rule-based use-case labels |
| PurchaseURL | Text | Manufacturer/product-information URL |

Required evidence:

- 33 rows imported;
- no duplicate ProductID;
- every ProductID exists in products;
- required display fields are nonblank;
- URL has HTTP/HTTPS scheme and host;
- unique ProductID index exists.

## 4. `feedback`

Minimum schema:

```sql
CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vote TEXT NOT NULL CHECK (vote IN ('up', 'down')),
    query_text TEXT NOT NULL DEFAULT '',
    category TEXT,
    brand TEXT,
    max_price REAL CHECK (max_price IS NULL OR max_price > 0),
    excluded_brands TEXT NOT NULL DEFAULT '[]',
    top_product_id INTEGER,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (top_product_id) REFERENCES products(ProductID)
);
```

`excluded_brands` may be stored as JSON text. The backend must validate before insert.

## 5. Recommendation join policy

The accepted Yuyang design uses an `INNER JOIN` between products and product_specs for recommendation and comparison flows that must show complete specs.

Consequences:

- final displayed recommendations come from 33 spec-complete records;
- all Top-5 results can be compared without `Not available` for required fields;
- the system must disclose that the demonstration catalogue is limited;
- the 9,000 rows remain useful as the source pool and behavioural data, but only linked records are display candidates.

## 6. US-05 compare rule

`/api/compare` accepts exactly 2 or 3 unique ProductIDs.

A requested ID is valid only when it exists in the joined products/product_specs view. Missing or specification-less IDs return HTTP 400 with `missing_ids`.

## 7. US-07 URL rule

`PurchaseURL` is returned with each joined product. The UI label should be `View Product` or `View Manufacturer Page`, not a guaranteed checkout action.

## 8. Data provenance limitations

- The original source and licence of the 9,000-row file still require team confirmation.
- The 33-row specs file is an educational prototype dataset prepared for demonstration.
- Specs and URLs are not a complete market catalogue.
- Prices are not real-time or verified retail prices.
- No scraping or automatic price updates are included.

## 9. Database ownership

- Yuyang owns schema/import/data quality.
- Zaikun owns backend use after the baseline merge.
- Guanyu consumes returned fields only.
- Junjie checks evidence and traceability.
