from email.mime.multipart import MIMEMultipart

# mime - multipurspose internet mail extensions. Defines the standard for email messages
# multipart subpackage exposes class called MIMEMultipart. We can send email message which
# include both html and plain content

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Tadas Savickas"
message["to"] = "testtesttest@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html")
message.attach(MIMEImage(Path("image.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testtesttest@gmail.com", "password123")
    smtp.send_message(message)
print("Sent...")
