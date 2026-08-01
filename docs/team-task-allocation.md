# Team Task Allocation — Yuyang Unified Version

## Junjie Chu — Project, Quality and Release Lead

Owns:

- contract freeze and change control;
- Requirements/Acceptance Criteria/traceability;
- requirements and GitHub Actions reconciliation;
- US-10 sharing/restoration;
- final acceptance testing;
- release, audit and handoff.

Must not replace Yuyang/Zaikun/Guanyu technical sections with invented summaries.

## Guanyu Lu — UI/UX and Frontend Lead

Owns:

- removal of final mock recommendations;
- real `/api/recommend` integration;
- US-05 selection and 2–3 product comparison via `/api/compare`;
- specification rendering;
- US-07 PurchaseURL button;
- US-08 feedback UI;
- US-09 alternative UI;
- US-10 share UI hooks;
- as-built interface design and accessibility evidence.

## Zaikun Zheng — Backend and Recommendation Lead

Owns after the Yuyang baseline merge:

- final `server.py` ownership;
- recommend validation and response contract;
- preservation and completion of `/api/compare`;
- explicit exclusions and rule-based parsing;
- US-09 budget alternative;
- `/api/feedback` route;
- Bug #15 regression;
- old/new backend test reconciliation;
- API, architecture and algorithm documentation.

## Yuyang Zhou — Data, Database and US-05 Data Lead

Owns:

- initial Yuyang pack integration PR;
- `products` and `product_specs` import/integrity;
- `product_specs.csv` and provenance limitations;
- database schema, indexes, ERD and data dictionary;
- `feedback` table and persistence function;
- data/DB tests and deployment initialization;
- database sections of US-05 and US-07.

## Primary branches

| Branch | Owner | Purpose | Reviewer |
|---|---|---|---|
| `feature/database-us05-specs` | Yuyang | Integrate product_specs, compare baseline, feedback schema | Zaikun |
| `feature/final-backend` | Zaikun | Final recommend/compare/feedback/US-09/test compatibility | Guanyu + Yuyang |
| `feature/final-frontend` | Guanyu | Real API, US-05 and US-07–10 UI | Zaikun |
| `feature/share-ci-evidence` | Junjie | US-10 utilities, CI, traceability, release evidence | Guanyu + Zaikun |

## Mandatory common responsibility

Every member must provide one technical delivery, tests, documentation, descriptive commits, one PR and at least one non-author review.
