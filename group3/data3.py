import csv
import random
 
# Define the data
client_ip = "223.167.116.240"
timestamp = "[19/Mar/2024:06:22:25 +0000]"
request = "GET / HTTP/1.1"
response_status_codes = ["200 (OK)", "404", "500"]
 
# Generate 20 random URLs
referers = [
"http://www.randomsite123.com",
"http://www.exampleurl456.net",
"http://www.testwebsite789.org",
"http://www.randomlink101.com",
"http://www.samplepage2022.net",
"http://www.urlgenerator303.org",
"http://www.demo1234site.com",
"http://www.randomurl567.net",
"http://www.testpage789.org",
"http://www.examplelink101.com",
"http://www.urlsample2022.net",
"http://www.demo456page.org",
"http://www.testurl789.com",
"http://www.randomsite101.net",
"http://www.sampleurl2022.org",
"http://www.demopage456.com",
"http://www.randomlink789.net",
"http://www.testsite101.org",
"http://www.examplepage2022.com",
"http://www.urlgenerator303.net"
]
 
user_agent = "Mozilla/5.0 (Linusu Android 10 K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Nobile Safari/537.36"
 
# Write data to CSV file
with open('traffic_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for status_code in response_status_codes:
        for ref in random.sample(referers, 20):  # Select 20 random referers
            writer.writerow([client_ip, timestamp, request, status_code, ref, user_agent])
 
print("Data has been written to 'traffic_data.csv' file.")