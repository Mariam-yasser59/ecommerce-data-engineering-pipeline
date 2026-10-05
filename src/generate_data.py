import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------
# Customers
# -------------------------

customers = []

for i in range(1, 101):
    customers.append({
        "customer_id": i,
        "first_name": f"Customer{i}",
        "last_name": f"Test{i}",
        "gender": random.choice(["Male", "Female"]),
        "city": random.choice([
            "Cairo",
            "Giza",
            "Alexandria",
            "Mansoura"
        ]),
        "country": "Egypt"
    })

customers_df = pd.DataFrame(customers)


# -------------------------
# Products
# -------------------------

products = []

categories = [
    "Electronics",
    "Clothing",
    "Home",
    "Beauty"
]

for i in range(1, 31):
    products.append({
        "product_id": i,
        "product_name": f"Product {i}",
        "category": random.choice(categories),
        "brand": f"Brand {random.randint(1, 5)}",
        "price": round(random.uniform(50, 5000), 2)
    })

products_df = pd.DataFrame(products)


# -------------------------
# Orders
# -------------------------

orders = []

start_date = datetime(2025, 1, 1)

for i in range(1, 501):
    order_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 100),
        "order_date": order_date.date(),
        "status": random.choice([
            "Completed",
            "Completed",
            "Completed",
            "Cancelled",
            "Pending"
        ])
    })

orders_df = pd.DataFrame(orders)


# -------------------------
# Order Items
# -------------------------

order_items = []

item_id = 1

for order_id in range(1, 501):

    number_of_products = random.randint(1, 4)

    selected_products = random.sample(
        range(1, 31),
        number_of_products
    )

    for product_id in selected_products:

        product_price = products_df.loc[
            products_df["product_id"] == product_id,
            "price"
        ].iloc[0]

        order_items.append({
            "order_item_id": item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": random.randint(1, 5),
            "unit_price": product_price
        })

        item_id += 1


order_items_df = pd.DataFrame(order_items)


# -------------------------
# Save CSV files
# -------------------------

customers_df.to_csv(
    "data/customers.csv",
    index=False
)

products_df.to_csv(
    "data/products.csv",
    index=False
)

orders_df.to_csv(
    "data/orders.csv",
    index=False
)

order_items_df.to_csv(
    "data/order_items.csv",
    index=False
)

print("CSV files generated successfully!")