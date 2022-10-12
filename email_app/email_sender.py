import ssl
import smtplib
from email.message import EmailMessage
from app2 import password

# creating variables, emails have been changed for github push, and password on
# app2.py has been changed. but it worked!

email_sender = 'test@gmail.com'
email_password = password

email_receiver = 'test@hotmail.com'

subject = "Don't forget to subscribe."

body = """
When you watch a video, please hit like and subscribe.
"""

# creating an instance of the email library

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# sends the email message
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
