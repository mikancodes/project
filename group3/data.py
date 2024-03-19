import csv
from faker import Faker
import random
import datetime
import geoip2.database
 
fake = Faker()
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
 
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
 
# Get country from IP using geoip2
def get_country_from_ip(ip):
    try:
        response = reader.country(ip)
        country = response.country.name
    except:
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
 
print("Dummy table created and saved as 'dummy_table.csv'.")