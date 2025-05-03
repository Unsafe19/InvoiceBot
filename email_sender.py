import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
import unicodedata
import os

def normalize_filename(filename):
    return unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')

def send_email(receiver_email, subject, body, attachment_path, sender_email, sender_password):
    msg = MIMEMultipart()
    msg['From'] = str(Header(sender_email, 'utf-8'))
    msg['To'] = str(Header(receiver_email, 'utf-8'))
    msg['Subject'] = str(Header(subject, 'utf-8'))

    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    with open(attachment_path, "rb") as attachment:
        filename = os.path.basename(attachment_path)
        safe_filename = normalize_filename(filename)
        part = MIMEApplication(attachment.read(), _subtype="pdf")
        part.add_header('Content-Disposition', 'attachment', filename=str(Header(safe_filename, 'utf-8')))
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
