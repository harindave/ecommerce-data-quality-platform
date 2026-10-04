import pandas as pd

# Load the orders table from the untouched Olist copy.
# parse_dates gives real datetime columns, so min/max are dates, not text.
df = pd.read_csv(
    "data/olist_clean/olist_orders_dataset.csv",
    parse_dates=[
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ],
)
# First look: size, sample rows, types, nulls, status values.
# Tells me what the table contains before I write any test.
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
df.info()
print(df.order_status.value_counts())  # the allowed statuses for BR-ORD-06

# The five date columns I want to profile.
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
# Profile each date column: the range and the nulls show what "normal"
# looks like. Injected defects will be compared against this baseline.
for col in date_columns:
    # errors="coerce" turns unparseable values into NaT instead of crashing
    df[col] = pd.to_datetime(df[col], errors="coerce")
    min_date = df[col].min()
    max_date = df[col].max()
    null_counts = df[col].isnull().sum()
    null_percentage = (null_counts / len(df)) * 100
    print(
        f"{col}: {min_date} | {max_date} | Null Count: {null_counts} | Null Percentage: {null_percentage:.2f}%"
    )
# Check BR-ORD-05: a "delivered" order must have a delivery date.
# Finds clean-data exceptions so my tests don't fail on the answer key.
odd_orders = df[
    (df.order_status == "delivered") & (df.order_delivered_customer_date.isnull())
]
print(odd_orders["order_id"].tolist())

# Reverse of the check above: a non-delivered order should NOT have a
# delivery date. Finds the second group of BR-ORD-05 exceptions in clean data.
reverse_odd_orders = df[
    (df.order_status != "delivered") & (df.order_delivered_customer_date.notnull())
]
print(
    reverse_odd_orders["order_id"].tolist(), reverse_odd_orders["order_status"].tolist()
)
