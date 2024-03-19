import csv
import random
import datetime
# Define product and category lists
products = [
   {"product_id": 1001, "product_name": "Laptop", "category": "Electronics", "unit_price": 800},
   {"product_id": 2002, "product_name": "Smartphone", "category": "Electronics", "unit_price": 500},
   {"product_id": 3003, "product_name": "Headphones", "category": "Electronics", "unit_price": 100},
   {"product_id": 4004, "product_name": "Sneakers", "category": "Fashion", "unit_price": 50},
   {"product_id": 5005, "product_name": "Sunglasses", "category": "Fashion", "unit_price": 30},
   {"product_id": 6006, "product_name": "T-shirt", "category": "Fashion", "unit_price": 20}
]
# Generate sample data
data = []
for i in range(1, 10001):
   product = random.choice(products)
   quantity = random.randint(1, 10)
   total_price = quantity * product["unit_price"]
   customer_id = random.randint(101, 200)
   timestamp = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
   region = random.choice(["North", "South", "East", "West"])
   data.append([i, product["product_id"], product["product_name"], product["category"], quantity, product["unit_price"], total_price, customer_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), region])
# Write sample data to CSV file
with open('sales_data.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["transaction_id", "product_id", "product_name", "category", "quantity", "unit_price", "total_price", "customer_id", "timestamp", "region"])
   writer.writerows(data)
print("CSV file 'sales_data.csv' has been created.")