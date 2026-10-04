# Olist Data Profile

Source: Olist Brazilian E-Commerce dataset (Kaggle), untouched.
Profiled with: data_generator/profiler.py

## olist_orders_dataset.csv
- Rows: 99,441. One row = one customer order.
- Columns: 8 (3 text, 5 datetime)
- Primary key candidate: order_id
- Purchase dates: 2016-09-04 to 2018-10-17
- Estimated delivery dates: up to 2018-11-12

### Columns and nulls
| Column | Type | Nulls | % |
|---|---|---|---|
| order_id | text | 0 | 0.00 |
| customer_id | text | 0 | 0.00 |
| order_status | text | 0 | 0.00 |
| order_purchase_timestamp | datetime | 0 | 0.00 |
| order_approved_at | datetime | 160 | 0.16 |
| order_delivered_carrier_date | datetime | 1,783 | 1.79 |
| order_delivered_customer_date | datetime | 2,965 | 2.98 |
| order_estimated_delivery_date | datetime | 0 | 0.00 |

Nulls rise down the order lifecycle: orders that stop early never get later dates.

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

### Findings
1. 8 orders are "delivered" but have no delivery date (IDs below).
   - 2d1e2d5bf4dc7227b3bfebb81328c15f
   - f5dd62b788049ad9fc0526e3ad11a097
   - 2ebdfc4f15f23b91474edf87475f108e
   - e69f75a717d64fc5ecdfae42b2e8e086
   - 0d3268bad9b086af767785e3f0fc0133
   - 2d858f451373b04fb5c984a1cc2defaf
   - ab7c89dc1bf4a1ead9d6ec1ec8968a84
   - 20edc82cf5400ce95e1afacc25798b31
2. 6 orders are "canceled" but have a delivery date (IDs below).
   - 1950d777989f6a877539f53795b4c3c3
   - dabf2b0e35b423f94618bf965fcb7514
   - 770d331c84e5b214bd9dc70a10b829d0
   - 8beb59392e21af5eb9547ae1a9938d06
   - 65d1e226dfaeb8cdc42f665422522d14
   - 2c45c33d2f9cb8ff8b1c86cc28c11c30
3. Total: 14 exceptions to BR-ORD-05 in the clean data.
4. "processing" (301 orders) was missing from BR-ORD-06; added (D-003).