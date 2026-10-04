   # Schema (Olist orders)

   ## olist_orders_dataset
   | Column | Type | Notes |
   |---|---|---|
   | order_id | text | primary key candidate (BR-ORD-01) |
   | customer_id | text | links to customers (BR-ORD-02) |
   | order_status | text | 8 allowed values (BR-ORD-06) |
   | order_purchase_timestamp | datetime | never null |
   | order_approved_at | datetime | nullable |
   | order_delivered_carrier_date | datetime | nullable |
   | order_delivered_customer_date | datetime | nullable |
   | order_estimated_delivery_date | datetime | never null |

   Other tables: to be added after profiling.

## orders
order_id (text) | customer_id (text) | order_status (text)
order_purchase_timestamp, order_approved_at, order_delivered_carrier_date,
order_delivered_customer_date, order_estimated_delivery_date (all datetime)
Key: order_id. Link: customer_id points to customers.