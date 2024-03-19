import csv
import random
import datetime
import requests
from faker import Faker
 
fake = Faker()
 
# Generate fake data for each column
def generate_fake_data():
    client_ip = fake.ipv4()
    country = get_country_from_ip(client_ip)
    timestamp = fake.date_time_this_year()
    request = random.choice(["GET", "POST", "PUT", "DELETE"]) + " " + fake.uri_path()
    response_code = random.choice([200, 404, 500])
    referer = fake.uri()
    user_agent = fake.user_agent()
    
    return client_ip, country, timestamp, request, response_code, referer, user_agent
 
# Get country from IP using ipstack API
def get_country_from_ip(ip):
    try:
        response = requests.get(f"http://api.ipstack.com/{ip}?access_key=YOUR_ACCESS_KEY")
        data = response.json()
        country = data['country_name']
    except Exception as e:
        print(f"Error getting country for IP {ip}: {e}")
        country = "Unknown"
    return country
 
# Generate dataset with fake data
def generate_dataset(num_entries):
    dataset = []
    for _ in range(num_entries):
        data = generate_fake_data()
        dataset.append(data)
    return dataset
 
# Generate dataset with 10,000 entries
dataset = generate_dataset(10000)
 
# Write dataset to CSV file
with open('dummy_table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Client IP", "Country", "Timestamp", "Request", "Response Code", "Referer", "User Agent"])
    writer.writerows(dataset)
 
print("Dummy table created and saved as 'dummy_table2.csv'.")