import pandas as pd

from db_connection import engine


# =========================
# Read cleaned data
# =========================

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")


# =========================
# Load data into PostgreSQL
# =========================

customers.to_sql(
    "customers",
    engine,
    schema="staging",
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    engine,
    schema="staging",
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    engine,
    schema="staging",
    if_exists="replace",
    index=False
)

order_items.to_sql(
    "order_items",
    engine,
    schema="staging",
    if_exists="replace",
    index=False
)


print("Data loaded successfully into PostgreSQL!")