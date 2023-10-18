import base64
import mimetypes
import os
from email.message import EmailMessage
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def authentication():
    credentials = None

    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file(
            'token.json',
            SCOPES
        )

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('path/home/client_secret_apps.json', SCOPES)
            credentials = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    return credentials


def prepare_and_send_email(recipient, subject, message_text):

    credentials = authentication()

    try:
        service = build(serviceName='gmail', version='v1', credentials=credentials)

        message = create_message('sendyourmail@gmail.com', recipient, subject, message_text)
        send_message(service, 'me', message)
    except HttpError as error:
        print(f"An error occurred: {error}")


def create_message(sender, to, subject, message_text):

    mime_message = EmailMessage()

    mime_message['From'] = sender
    mime_message['To'] = to
    mime_message['Subject'] = subject

    mime_message.set_content(message_text)


    return {'raw': base64.urlsafe_b64encode(mime_message.as_bytes()).decode()}


def send_message(service, user_id, message):

    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f"Message Id: {message['id']}")
        return message
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":

    recipients = ['info@linquip.com','sojangeneraltradingllc@gmail.com','info@expeditiontravelandtourism.com','info@pristellar.com','sierracartel.ae@gmail.com','tanujchauhan76@gmail.com']
    sub="Proposal For Website Promotion!"
    msg="""
Hello, 

I found your email contact I would like to discuss a business. 

Top Ranking in Google: 

Website Promotion (SEO, SMO, PPC, Google, Yahoo and Bing). 
Email us back to get a full Proposal. So let me know if you would be  

Interested or like me to mail you more details or schedule a call?  

We would love to work with you! 

Please just send me your Skype ID. 

Thanks & Regards,
Your Name
"""
    
    for recipient in recipients:
        prepare_and_send_email(recipient, sub, msg)
        print(f'Email sent to {recipient}')

print("Mail sent successfull")
