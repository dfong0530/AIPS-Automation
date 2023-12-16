from dotenv import load_dotenv
import os
import csv
from email_module import send_email
from helper import generate_draft, updateRow

"""
See if Did_Email is labeled No

Generate Email Draft based on current versions

Send Email usng smtplib

Update New CSV file --> Did_Email (Yes), Email_Version (version.{email_number})
"""

load_dotenv('../.env')

username = os.getenv('Username')
password = os.getenv('Password')

#Modify
version = "1"
read_path = "../data/test.csv"
write_path = f"../data/write_v{version}.csv"

#Modify Possible Drafts in ./generate_email.py


write = []

with open(read_path, newline='') as f:
    reader = csv.reader(f)

    first_line = next(reader)
    write.append(list(first_line))

    for line in reader:

        write_line = list(line)

        if line[4] == "No":
            r, subject, draft = generate_draft(line[1], line[0], line[6])
            send_email(subject, draft, line[2], username, password)
            updateRow(write_line, version, r)

        write.append(write_line)


with open(write_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(write)






