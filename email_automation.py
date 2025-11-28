import smtplib

import ssl

from email.message import EmailMessage

EMAIL = "adityaraj29121887@gmail.com"
APP_PASSWORD = " "  #enter your own app password(previous password key is used and it is working)
RECEIVER  = "adityaraj01823@gmail.com"

msg = EmailMessage()

msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject "] = "testing kr rha hun bhai"

msg.set_content("BHAI email to autiomatically bhej gy ah python se")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as server:
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)