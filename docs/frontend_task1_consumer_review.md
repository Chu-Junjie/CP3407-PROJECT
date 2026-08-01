# Task 1 Frontend Consumer Review

## Role
Guanyu Lu — UI/UX and Frontend Lead

## Current Branch
feature/frontend-api-integration

## Current Frontend State
The current frontend uses fetch to call the Flask /api/recommend endpoint.
The main recommendation flow does not rely on fixed mockRecommendations.
The UI supports loading, success, empty and error states.

## Local Integration Evidence
Test query:
I need a gaming laptop under $1500, no Apple

Observed result:
- category = Laptops
- budget = 1500
- exclusions = ["apple"]
- Top 5 laptop recommendations returned
- No Apple products appeared
- Each product included a reason
- Specification fields were displayed when returned by the backend

## /api/recommend Field Map
| Field | Frontend Usage | Required |
|---|---|---|
| product_id | selection and compare request | Yes |
| product_name | product card title | Yes |
| brand | product card metadata | Yes |
| category | product card metadata | Yes |
| price | product card price | Yes |
| match_score | match badge | Yes |
| reason | recommendation explanation | Yes |
| specs | optional specification display | Optional |
| purchase_url | View Product button | Optional |
| budget_alternative | budget alternative card | Optional |

## /api/compare Flow
The user selects exactly 2 or 3 products. The frontend collects product_id
values and calls /api/compare. The comparison table only displays fields
returned by the backend. Missing specification values are shown as N/A.

## UI States
| State | Behaviour |
|---|---|
| Loading | Disable submit and show loading message |
| Success | Show Top 5 recommendations |
| Empty | Show no matching products message |
| Error | Show readable API/network error |

## Conflict Files and Ownership
| File | Owner / Rule |
|---|---|
| index.html | Guanyu |
| server.py | Zaikun final owner; Guanyu version is candidate for local integration |
| product_specs.csv | Yuyang |
| api-contract.md | Junjie/Zaikun maintain, Guanyu reviews |

## API Questions / Gaps
- Freeze /api/compare as GET or POST.
- Freeze feedback vote values.
- Confirm whether score is match_score or score.
- Confirm budget_alternative response shape.
- Confirm purchase_url field name.
