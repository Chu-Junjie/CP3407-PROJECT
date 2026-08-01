# API Contract — Yuyang Unified Scheme

## Common response rules

- Valid success: HTTP 200, except feedback creation uses HTTP 201.
- Invalid user input: HTTP 400 with a readable `message`.
- Valid search with no matches: HTTP 200 and `data: []`.
- Internal failure: HTTP 500 without exposing stack traces.

## GET `/api/health`

Expected fields include:

```json
{
  "status": "success",
  "database": "digital_products.db",
  "products_table": "products",
  "product_specs_table": "product_specs",
  "records": 9000,
  "spec_records": 33
}
```

## POST `/api/recommend`

### Request

```json
{
  "query": "gaming laptop under $2500, no Apple",
  "category": "Laptops",
  "brand": null,
  "max_price": 2500,
  "excluded_brands": ["Apple"]
}
```

Rules:

- category and brand may be inferred when not explicitly supplied;
- explicit category and brand must be validated;
- explicit `excluded_brands` and query-text exclusions are merged and deduplicated;
- invalid/non-positive max_price returns 400, not silent removal;
- use-case keywords may influence scoring;
- results come from the joined spec-complete dataset.

### Response

```json
{
  "status": "success",
  "message": "5 recommendations found",
  "filters": {
    "query": "gaming laptop under $2500, no Apple",
    "category": "Laptops",
    "brand": null,
    "max_price": 2500,
    "excluded_brands": ["Apple"],
    "use_cases": ["gaming"]
  },
  "count": 5,
  "data": [
    {
      "product_id": 5899,
      "product_name": "HP Omen 16",
      "category": "Laptops",
      "brand": "HP",
      "price": 1000.0,
      "match_score": 85,
      "reason": "matches category; within budget; fits gaming",
      "cpu": "Intel Core i7",
      "gpu": "NVIDIA RTX 4060",
      "ram": "16GB",
      "storage": "1TB SSD",
      "screen_size": "16.1 inch",
      "battery_life": "6 hours",
      "weight": "2.35 kg",
      "use_case": "gaming performance",
      "purchase_url": "https://www.hp.com/"
    }
  ],
  "budget_alternative": null
}
```

`price` in examples must be taken from actual API output; documentation must not invent current retail prices.

## GET or POST `/api/compare`

GET example:

```text
/api/compare?ids=5885,5937,5960
```

POST example:

```json
{"product_ids": [5885, 5937, 5960]}
```

Rules:

- exactly 2 or 3 unique integer IDs;
- all IDs must exist in joined products/product_specs;
- invalid, duplicate or missing IDs return 400;
- response returns the requested specification fields and behavioural comparison fields.

## POST `/api/feedback`

Request:

```json
{
  "vote": "up",
  "query": "gaming laptop under $2500",
  "category": "Laptops",
  "brand": null,
  "max_price": 2500,
  "excluded_brands": ["Apple"],
  "top_product_id": 5899
}
```

Success: HTTP 201

```json
{
  "status": "success",
  "message": "Feedback recorded",
  "feedback_id": 1
}
```

Vote must be `up` or `down`.

## US-09 budget alternative

- reference: first recommendation;
- same category;
- lower ProductPrice;
- different ProductID;
- must have a product_specs row;
- return strongest eligible item or `null`.

## US-10 sharing

Supported URL fields:

```text
query, category, brand, max_price, excluded_brands
```

Comparison selections may optionally be encoded only if implementation and tests remain simple; the minimum US-10 acceptance criterion is restoring recommendation filters and rerunning `/api/recommend`.
