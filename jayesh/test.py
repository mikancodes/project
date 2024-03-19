import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

# Initialize Faker instance
fake = Faker()

# Generate synthetic data
data = []
for _ in range(10001):
    customer_id = fake.random_int(min=1, max=1000)
    transaction_id = fake.random_int(min=1000, max=9999)
    transaction_date = fake.date_between(start_date='-1y', end_date='today')
    amount = round(random.uniform(10, 500), 2)
    product_category = random.choice(['Electronics', 'Clothing', 'Home & Garden'])
    age = fake.random_int(min=18, max=80)
    gender = random.choice(['Male', 'Female'])
    income = fake.random_int(min=20000, max=150000)
    location = fake.random_element(elements=['New York', 'Los Angeles', 'Chicago', 'Houston'])
    page_visits = fake.random_int(min=1, max=30)
    time_spent_on_site = fake.random_int(min=5, max=120)
    purchase_count = fake.random_int(min=1, max=10)
    
    data.append([customer_id, transaction_id, transaction_date, amount, product_category, 
                 age, gender, income, location, page_visits, time_spent_on_site, purchase_count])

# Create DataFrame
df = pd.DataFrame(data, columns=['CustomerID', 'TransactionID', 'TransactionDate', 'Amount', 'ProductCategory',
                                 'Age', 'Gender', 'Income', 'Location', 'PageVisits', 'TimeSpentOnSite', 'PurchaseCount'])

# Save DataFrame to CSV
df.to_csv('combined_data_2000.csv', index=False)
