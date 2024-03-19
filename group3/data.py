# import csv
# from faker import Faker
 
# fake = Faker()
 
# # Generate fake data
# for i in range(1,10001):
#     client_ip = fake.ipv4()
#     timestamp = fake.date_time_this_year().strftime("[%d/%b/%Y:%H:%M:%S +0000]")
#     request = "GET / HTTP/1.1"
#     response_status_code = "200 (OK)"
#     referer = fake.uri()
#     user_agent = fake.user_agent()
    
# # Prepare data
# data = [
#     ["Client IP", "Timestamp", "Request", "Response Status Code", "Referer", "User Agent"],
#     [client_ip, timestamp, request, response_status_code, referer, user_agent]
# ]
 
# # Write dataset to CSV file
# with open('dummy_table.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)
 
# print("Dummy table created and saved as 'dummy_table.csv'.")


import csv
from faker import Faker
import random
import datetime
 
fake = Faker()
 
# Generate random data for the query
def generate_random_data():
    client_ip = fake.ipv4()
    timestamp = fake.date_time_this_year().strftime("[%d/%b/%Y:%H:%M:%S +0000]")
    request = random.choice(["GET", "POST", "PUT", "DELETE"]) + " " + fake.uri_path()
    response_status_code = random.choice(["200 (OK)", "404 (Not Found)", "500 (Internal Server Error)"])
    referer = fake.uri() if random.random() < 0.5 else None  # Half of the time, referer will be None
    user_agent = fake.user_agent()
    return client_ip, timestamp, request, response_status_code, referer, user_agent
 
# Generate dataset with 10,000 random entries
def generate_dataset(num_entries):
    dataset = [["Client IP", "Timestamp", "Request", "Response Status Code", "Referer", "User Agent"]]
    for _ in range(num_entries):
        data = generate_random_data()
        dataset.append(data)
    return dataset
 
# Generate dataset with 10,000 random entries
dataset = generate_dataset(10000)
 
# Write dataset to CSV file
with open('dummy_table_random_data_10000.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dataset)
 
print("Dummy table with 10,000 random data entries created and saved as 'dummy_table_random_data_10000.csv'.")