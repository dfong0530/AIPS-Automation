import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, recipient, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "aips.dot@gmail.com"
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login("aips.dot@gmail.com", password)
       smtp_server.sendmail("aips.dot@gmail.com", recipient, msg.as_string())
    print("Message sent!")
