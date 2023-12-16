import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, recipient, username, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(username, password)
       smtp_server.sendmail(username, recipient, msg.as_string())
    print("Message sent!")
