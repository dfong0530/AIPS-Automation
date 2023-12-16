from dotenv import load_dotenv
import os
from email_module import send_email
from helper import generate_draft, writeToCSV

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
email_version = "1"
read_path = "../data/test.csv"
write_path = f"../data/write_v{email_version}.csv"

#Modify Possible Drafts in ./generate_email.py


with open(read_path) as r:
    with open(write_path) as w:

        for line in r:
            pass







