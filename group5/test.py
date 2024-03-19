import csv
import random
from faker import Faker
from datetime import datetime, timedelta
 
fake = Faker()
 
# Function to generate random hire dates
def generate_hire_date():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 12, 31)
    return fake.date_time_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d')
 
# Generate data for 10,000 employees
data = []
for i in range(1, 10001):
    name = fake.name()
    department = random.choice(['Sales', 'Marketing', 'IT', 'HR', 'Operations'])
    job_title = fake.job()
    hire_date = generate_hire_date()
    salary = random.randint(40000, 100000)
    sales_target = random.randint(50000, 150000) if department == 'Sales' else None
    project_completion_rate = round(random.uniform(70, 95), 2)
    customer_satisfaction_score = round(random.uniform(3.5, 5.0), 1)
    hours_worked = random.randint(140, 180)
    attendance_record = f"{random.randint(90, 98)}%"
    late_arrivals = random.randint(0, 3)
    training_hours_completed = random.randint(20, 60)
    certifications_attained = random.randint(0, 3)
    peer_review_score = round(random.uniform(4.0, 5.0), 1)
    manager_review_score = round(random.uniform(4.0, 5.0), 1)
    overall_performance_score = round((peer_review_score + manager_review_score) / 2, 2)
    data.append([i, name, department, job_title, hire_date, "", salary, sales_target,
                 project_completion_rate, customer_satisfaction_score, hours_worked,
                 attendance_record, late_arrivals, training_hours_completed,
                 certifications_attained, peer_review_score, manager_review_score,
                 overall_performance_score])
 
# Write data to CSV file
headers = ["EmployeeID", "Name", "Department", "JobTitle", "HireDate", "TerminationDate",
           "Salary", "SalesTarget", "ProjectCompletionRate", "CustomerSatisfactionScore",
           "HoursWorked", "AttendanceRecord", "LateArrivals", "TrainingHoursCompleted",
           "CertificationsAttained", "PeerReviewScore", "ManagerReviewScore",
           "OverallPerformanceScore"]
 
with open('employee_performance_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)
 
print("CSV file generated successfully.")