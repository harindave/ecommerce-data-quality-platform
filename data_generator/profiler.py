import pandas as pd

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
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print(df.info())
print(df.order_status.value_counts())
