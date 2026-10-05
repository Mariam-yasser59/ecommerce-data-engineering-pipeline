import pandas as pd


# =========================
# 1. Read CSV files
# =========================

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")


# =========================
# 2. Remove duplicates
# =========================

customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
order_items = order_items.drop_duplicates()


# =========================
# 3. Fix data types
# =========================

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

products["price"] = pd.to_numeric(
    products["price"],
    errors="coerce"
)

order_items["quantity"] = pd.to_numeric(
    order_items["quantity"],
    errors="coerce"
)

order_items["unit_price"] = pd.to_numeric(
    order_items["unit_price"],
    errors="coerce"
)


# =========================
# 4. Handle missing values
# =========================

products["price"] = products["price"].fillna(0)

order_items["quantity"] = order_items["quantity"].fillna(0)

order_items["unit_price"] = order_items["unit_price"].fillna(0)


# =========================
# 5. Create total amount
# =========================

order_items["total_amount"] = (
    order_items["quantity"]
    * order_items["unit_price"]
)


# =========================
# 6. Remove invalid records
# =========================

orders = orders.dropna(
    subset=["order_id", "customer_id", "order_date"]
)

order_items = order_items.dropna(
    subset=["order_id", "product_id"]
)


# =========================
# 7. Display results
# =========================

print("Customers:", len(customers))
print("Products:", len(products))
print("Orders:", len(orders))
print("Order Items:", len(order_items))

print("\nOrder Items Preview:")
print(order_items.head())

print("\nData Cleaning Completed Successfully!")