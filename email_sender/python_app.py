from email.message import EmailMessage
import ssl
import smtplib
import app2

email_sender = 'yourmail@gmail.com'
email_password = app2.password

#temp mail
email_receiver = 'facaw68298@backva.com'
subject = 'don\'t forget to subscribe'
body = """
Hi I am learning python!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())