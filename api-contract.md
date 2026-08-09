# API Contract — Database, Accounts and Pagination Revision

All responses are JSON. Successful reads return HTTP 200; account and feedback creation return 201. Invalid input returns 400, missing/invalid authentication returns 401, conflicts return 409 and unhandled failures return a generic 500 response.

## Health

`GET /api/health` reports `database`, table row counts and `joined_recommendation_candidates`. It also states that the catalogue is educational and prices are not live.

## Accounts

- `POST /api/auth/register`: `{ "username", "email", "password" }`; password requires 8+ characters.
- `POST /api/auth/login`: `{ "identifier", "password" }`, where identifier is a username or email.
- `GET /api/auth/me`: requires `Authorization: Bearer <token>`.

Register/login returns `{ "status", "token", "user" }`. Password hashes—not plaintext passwords—are stored.

## Recommendations

`POST /api/recommend` accepts:

```json
{
  "query": "portable laptop under $1500, no Apple",
  "category": "Laptops",
  "brand": null,
  "max_price": 1500,
  "excluded_brands": ["Apple"],
  "page": 1,
  "per_page": 20,
  "save_history": true
}
```

`per_page` defaults to 20 and is capped at 100. The response contains `data`, `count`, `total_candidates`, `page`, `per_page`, `total_pages`, the best five in `top_recommendations`, parsed `filters`, and an optional `history_id`. A valid bearer token causes page-one searches to be saved automatically.

Every result includes product ID/name/category/brand/price, match score/reason, specification fields, purchase URL and `data_source`.

`GET /api/products` supports the same filter and pagination fields.

## Search history

- `GET /api/history`: private paginated list for the authenticated user.
- `GET /api/history/<history_id>`: saved query, filters and result snapshot.
- `DELETE /api/history/<history_id>`: deletes the authenticated user's record.

Another user cannot read or delete a history record.

## Comparison

`GET|POST /api/compare` accepts exactly 2 or 3 unique joined product IDs (`ids=1,2` or `{ "product_ids": [1, 2] }`).

## Favorites

- `GET /api/favorites`: returns the authenticated user's saved products.
- `POST /api/favorites`: saves `{ "product_id": 123 }`; repeated saves are idempotent.
- `DELETE /api/favorites/<product_id>`: removes one saved product.
- `POST /api/favorites/compare`: accepts 2 or 3 IDs that must all belong to the authenticated user's favorites and share one product category.

Favorites are stored by `user_id` and are never exposed to another account.

## Feedback

- `POST /api/feedback`: `{ "vote": "up"|"down", "query", "history_id", "top_product_id" }`; the last two are optional.
- `GET /api/feedback`: aggregate up/down/total counts for demonstration and administration.

## Persistence

`DATABASE_URL` selects PostgreSQL in production. With no value the API uses `digital_products.db` for local development. `JWT_SECRET_KEY` must be configured to a random 32+ character value in production.
