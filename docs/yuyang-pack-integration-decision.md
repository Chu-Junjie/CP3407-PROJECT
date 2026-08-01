# Yuyang Database / US-05 Pack Integration Decision

## Decision

The team will use `yuyang_database_us05_update_v2.zip` as the database and US-05 comparison baseline.

## Supplied files

```text
server.py
product_specs.csv
test_database_us05.py
requirements.txt
docs/database_us05_update.md
```

## Accepted design changes

1. Add `product_specs` as a relational table linked to `products` by `ProductID`.
2. Preserve all 9,000 original behavioural records in `products`.
3. Import 33 specification records into `product_specs`.
4. Use an `INNER JOIN` for recommendation/demo flows requiring complete specifications.
5. Add `GET|POST /api/compare`, accepting exactly 2 or 3 unique valid IDs.
6. Store `PurchaseURL` in `product_specs`; do not create `brand_links`.
7. Add category inference and use-case keyword matching as rule-based logic.
8. Preserve the honesty limitations in `database_us05_update.md`.

## Additional work still required

The Yuyang pack is not the complete final system. The team must still:

- add the `feedback` table and safe persistence function;
- add `POST /api/feedback`;
- implement US-09 budget alternative;
- merge explicit `excluded_brands` request data with text exclusions;
- change invalid `max_price` handling from silent fallback to HTTP 400;
- reconcile old `test_server.py` and `test_mock.py` with the new two-table setup;
- integrate the final HTML frontend with real recommend/compare/feedback APIs;
- implement US-10 sharing;
- run all tests and CI;
- update README and technical evidence.

## Ownership transition

Yuyang owns the initial integration PR because the package changes the database import, schema and US-05 data. The package also contains `server.py`; Zaikun must review it before merge. After the Yuyang baseline PR is merged, Zaikun becomes the primary editor of `server.py` for the remaining backend tasks.

## Evidence status

The pack contents are supplied code and documentation, not proof that all tests passed. A feature becomes verified only after the team records the real command, result, PR, review and integration evidence.
