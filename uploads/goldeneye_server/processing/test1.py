import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'kentc8748@gmail.com'
smtp_password = 'iglxzvodaxwsthmb'

# Set up the message
subject = 'Norton mail Tech Support!!!'
message = 'Welcome to the Tech Support'

msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Set up your list of recipients
to_emails = ['kamalkapkoti121@gmail.com','alokratan277@gmail.com','shahrukhsrk0571@gmail.com']

# Send the email to each recipient
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    for email in to_emails:
        msg['To'] = email
        server.sendmail(smtp_username, email, msg.as_string())

print("Mail Sent")
