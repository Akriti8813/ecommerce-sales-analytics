import pandas as pd

# Load datasets
orders = pd.read_csv("data/olist_orders_dataset.csv")
order_items = pd.read_csv("data/olist_order_items_dataset.csv")

# Merge datasets
df = pd.merge(orders, order_items, on="order_id")

# Convert date column
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

# Create month column
df["month"] = df["order_purchase_timestamp"].dt.to_period("M")

# Calculate revenue
revenue_by_month = df.groupby("month")["price"].sum()

print(revenue_by_month.head())
