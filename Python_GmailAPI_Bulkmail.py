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
            flow = InstalledAppFlow.from_client_secrets_file('E:\Py_Jupyter\client_secret_apps.json', SCOPES)
            credentials = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    return credentials


def prepare_and_send_email(recipient, subject, message_text, attachment):

    credentials = authentication()

    try:
        service = build(serviceName='gmail', version='v1', credentials=credentials)

        message = create_message('ben.smith41349@gmail.com', recipient, subject, message_text, attachment)
        send_message(service, 'me', message)
    except HttpError as error:
        print(f"An error occurred: {error}")


def create_message(sender, to, subject, message_text, attachment):

    mime_message = EmailMessage()

    mime_message['From'] = sender
    mime_message['To'] = to
    mime_message['Subject'] = subject

    mime_message.set_content(message_text)

    attachment_filename = attachment
    type_subtype, _ = mimetypes.guess_type(attachment_filename)
    maintype, subtype = type_subtype.split('/')

    with open(attachment_filename, 'rb') as fp:
        attachment_data = fp.read()
    mime_message.add_attachment(attachment_data, maintype, subtype, filename=attachment_filename)

    return {'raw': base64.urlsafe_b64encode(mime_message.as_bytes()).decode()}


def send_message(service, user_id, message):

    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f"Message Id: {message['id']}")
        return message
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    recipients = ['clark.kent8748@gmail.com', 'shekhshahrukh492@gmail.com','shahrukhsrk0571@gmail.com','shahrukh.md@consultit.co.in'] 
    pic=r"E:\Py_Jupyter\web.jpeg"
    
    for recipient in recipients:
        prepare_and_send_email(recipient, 'Greeting from Hamza Aziz', 'This is a test email', pic)
