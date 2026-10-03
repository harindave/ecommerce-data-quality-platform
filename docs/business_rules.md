# Business Rules to Test
 
Each rule has an ID so it can be traced in test cases and a traceability matrix. 
## Orders
| ID | Rule |
|---|---|
| BR-ORD-01 | order_id is unique and not null |
| BR-ORD-02 | Every order references an existing customer_id |
| BR-ORD-03 | Date chain: purchase_timestamp <= approved_at <= delivered_carrier_date <= delivered_customer_date (where present) |
| BR-ORD-04 | estimated_delivery_date is after purchase_timestamp |
| BR-ORD-05 | order_status matches filled dates (e.g. "delivered" must have delivered_customer_date; "canceled" must not) |
| BR-ORD-06 | order_status is one of the allowed values (created, approved, invoiced, shipped, delivered, canceled, unavailable, processing) |
| BR-ORD-07 | Delivery delay (days) = delivered_customer_date - estimated_delivery_date, calculated correctly |
 
## Order items
| ID | Rule |
|---|---|
| BR-ITM-01 | (order_id, order_item_id) is unique |
| BR-ITM-02 | Every item references an existing order, product, and seller |
| BR-ITM-03 | price and freight_value are non-negative |
| BR-ITM-04 | Sum of item prices + freight per order should reconcile with payment totals for that order (within a small tolerance — a decision) |
 
## Payments
| ID | Rule |
|---|---|
| BR-PAY-01 | Every order has at least one payment record |
| BR-PAY-02 | payment_value is non-negative |
| BR-PAY-03 | payment_type is one of the allowed values |
| BR-PAY-04 | Sum of payment_value for an order should reconcile with the order's item + freight total |
 
## Customers
| ID | Rule |
|---|---|
| BR-CUS-01 | customer_id is unique and not null |
| BR-CUS-02 | zip_code_prefix is a valid format |
| BR-CUS-03 | No exact duplicate customer rows (same name + email + address) |
 
## Generated additions (returns, shipments, SCD history)
| ID | Rule |
|---|---|
| BR-RET-01 | Every return references an existing order |
| BR-RET-02 | return_date is after the order's delivered_customer_date |
| BR-SHP-01 | Shipment events for an order are in chronological order |
| BR-SCD-01 | A customer's address history has non-overlapping effective date ranges |