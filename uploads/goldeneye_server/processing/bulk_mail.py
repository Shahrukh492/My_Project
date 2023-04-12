import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

# Set up the message details
from_address = 'your_email@gmail.com'
to_address = ['recipient1@gmail.com', 'recipient2@gmail.com', 'recipient3@gmail.com']
subject = 'Your email subject'
message_body = 'Your email message'

# Create the message object and set the message details
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = ', '.join(to_address)
msg['Subject'] = subject
msg.attach(MIMEText(message_body, 'plain'))

# Connect to the SMTP server and send the message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    for recipient in to_address:
        msg['To'] = recipient
        server.sendmail(from_address, recipient, msg.as_string())
