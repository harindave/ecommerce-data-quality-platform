# Olist Data Profile

Source: Olist Brazilian E-Commerce dataset (Kaggle), untouched.
Profiled with: generator/profiler.py (use your real path)

## olist_orders_dataset.csv
- Rows: 99,441
- Columns: 8
- Primary key candidate: order_id

### Columns and nulls
| Column | Type | Nulls |
|---|---|---|
| order_id | text | 0 |
| customer_id | text | 0 |
| order_status | text | 0 |
| order_purchase_timestamp | datetime | 0 |
| order_approved_at | datetime | 160 |
| order_delivered_carrier_date | datetime | 1,783 |
| order_delivered_customer_date | datetime | 2,965 |
| order_estimated_delivery_date | datetime | 0 |

### Order status counts
| Status | Count |
|---|---|
| delivered | 96,478 |
| shipped | 1,107 |
| canceled | 625 |
| unavailable | 609 |
| invoiced | 314 |
| processing | 301 |
| created | 5 |
| approved | 2 |

### Observations
- Nulls in the three later date columns are expected for orders that haven't been delivered.
- processing exists in the data but wasn't in my original rule BR-ORD-06.