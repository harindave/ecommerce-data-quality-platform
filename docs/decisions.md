## D-001: Olist data is non-commercial only
- Date: 2026-10-02
- Decision: Use Olist only for the portfolio. Paid work uses synthetic data.
- Reason: Olist license is CC BY-NC-SA 4.0 (NonCommercial).
- Consequence: Olist data and Olist-derived data are never committed to the repo.

## D-002: Generator folder is named `generator/`
- Date: 2026-10-02
- Decision: Use `generator/` (not `data_generator/`).
- Reason: Matches repo-structure.md; one name used everywhere.

## D-003 Added processing to allowed order statuses (BR-ORD-06).
Why: Profiling the real Olist orders table showed 301 orders with this status. 
Olist is the answer key, so the rule was wrong, not the data.
Date: 2026-10-03

