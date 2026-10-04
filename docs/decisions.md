## D-001: Olist data is non-commercial only
- Date: 2026-10-02
- Decision: Use Olist only for the portfolio. Paid work uses synthetic data.
- Reason: Olist license is CC BY-NC-SA 4.0 (NonCommercial).
- Consequence: Olist data and Olist-derived data are never committed to the repo.

## D-002 (superseded by D-005): Generator folder is named `generator/`
- Date: 2026-10-02
- Decision: Use `generator/` (not `data_generator/`).
- Reason: Matches repo-structure.md; one name used everywhere.

## D-003: Added processing to allowed order statuses (BR-ORD-06).
- Date: 2026-10-03
- Decision Olist is the answer key, so the rule was wrong, not the data
- Reason: Profiling the real Olist orders table showed 301 orders with this status. 


## D-004: Handling the 14 BR-ORD-05 exceptions in clean Olist
- Clean Olist has 8 non-delivered and 6 canceled orders(see olist_profile.md). 
- Decision: list them as expected failures.
- Reason: the clean copy is the answer key and is never edited.

## D-005: Generator folder stays `data_generator/`
- Date: 2026-10-04
- Decision: Keep `data_generator/` (supersedes D-002).
- Reason: Already created and used in the code; renaming adds work with no benefit.