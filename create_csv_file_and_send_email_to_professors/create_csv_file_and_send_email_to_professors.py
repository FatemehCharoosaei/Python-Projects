import csv
import random
import datetime

# List of sample professors with their details
professors = [
    {"name": "Dr. John Doe", "university": "Harvard University", "ranking": 2, "research_field": "AI in Healthcare", "email": "johndoe@harvard.edu"},
    {"name": "Dr. Jane Smith", "university": "MIT", "ranking": 1, "research_field": "Medical Data Science", "email": "janesmith@mit.edu"},
    {"name": "Dr. Alan Turing", "university": "Stanford University", "ranking": 3, "research_field": "Machine Learning in Healthcare", "email": "alanturing@stanford.edu"},
    {"name": "Dr. Ada Lovelace", "university": "UC Berkeley", "ranking": 4, "research_field": "Data Analytics for Medicine", "email": "adalovelace@berkeley.edu"},
    {"name": "Dr. Tim Berners-Lee", "university": "Princeton University", "ranking": 5, "research_field": "AI and Patient Monitoring", "email": "timbernerslee@princeton.edu"}
]

# File name where the professor data will be saved as a CSV file
filename = "professors_info.csv"

# Create and write the professor data into the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "university", "ranking", "research_field", "email"])
    writer.writeheader()  # Write the header of the CSV
    for professor in professors:
        writer.writerow(professor)  # Write each professor's details into the CSV file

# Starting date for sending emails
start_date = datetime.date(2025, 1, 25)

# List to store the email schedule
email_schedule = []

# Generate email schedule by assigning each professor an email date every 2-3 days
for i in range(len(professors)):
    next_email_date = start_date + datetime.timedelta(days=random.randint(2, 3) * (i+1))  # Generate a random date within 2-3 days for each professor
    email_schedule.append({
        "professor": professors[i]["name"],
        "email": professors[i]["email"],
        "send_date": next_email_date
    })

# Print out the email schedule with the date to send emails
for email in email_schedule:
    print(f"Email to {email['professor']} ({email['email']}) should be sent on {email['send_date']}.")

# Confirmation message for CSV file creation
print("\nCSV file generated with professor data.")