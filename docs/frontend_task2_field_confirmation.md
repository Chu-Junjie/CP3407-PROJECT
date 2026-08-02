# Task 2 Frontend Field Confirmation

## Role

Guanyu Lu — UI/UX and Frontend Lead

## Task 2 Scope

This document confirms the database/API fields required by the frontend after the
Yuyang database / US-05 baseline update.

The frontend does not modify the database schema. The purpose of this review is
to confirm that the recommendation, comparison and product-link data can support
the final UI.

## Confirmed Recommendation Fields

The frontend expects each `/api/recommend` product item to provide:

| Field | Frontend Usage | Required |
|---|---|---|
| product_id | Product selection and compare request | Yes |
| product_name / name | Product card title | Yes |
| brand | Product metadata | Yes |
| category | Product metadata | Yes |
| price | Product price display | Yes |
| match_score | Match badge | Yes |
| reason | Recommendation explanation | Yes |
| cpu | Specification summary and comparison table | Optional |
| gpu | Specification summary and comparison table | Optional |
| ram | Specification summary and comparison table | Optional |
| storage | Specification summary and comparison table | Optional |
| screen_size | Specification summary and comparison table | Optional |
| battery_life | Specification summary and comparison table | Optional |
| weight | Specification summary and comparison table | Optional |
| use_case | Additional explanation or filtering support | Optional |
| purchase_url | View Product / Manufacturer Page button | Optional |

## Confirmed Compare Flow

The frontend will allow the user to select exactly 2 or 3 products.

The selected `product_id` values will be sent to `/api/compare`.

Expected request shape:

```json
{
  "product_ids": [11126, 12926]
}
