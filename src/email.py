from textwrap import dedent
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import sys

class SiteEmail():
    def __init__(self, debug:bool = False):
        # load_env() should have been run already from the dotenv module
        self.sender_email = os.environ.get('SMTP_SENDER')
        self.receiver_email = os.environ.get('SMTP_RECEIVER')
        self.smtp_server = os.environ.get('SMTP_SERVER')
        self.smtp_port = os.environ.get('SMTP_PORT')
        self.smtp_username = os.environ.get('SMTP_USER')
        self.smtp_password = os.environ.get('SMTP_PASSWORD')
        self.debug = debug

    def _dump(self, supplied_name: str, supplied_email: str, supplied_message: str):
        if self.debug:
            print('DEBUG: sending email')
            print(f'   SERVER          : {self.smtp_server}')
            print(f'   PORT            : {self.smtp_port}')
            print(f'   USERNAME        : {self.smtp_username}')
            print(f'   SUBMITTER_NAME  : {supplied_name}')
            print(f'   SUBMITTER_EMAIL : {supplied_email}')
            print(f'   MESSAGE         : {supplied_message}')



    def send(self, name:str, submitter_email:str, submitted_message:str):
        # create the envelop (the outgoing message)
        self._dump(name, submitter_email, submitted_message)
        envelope = MIMEMultipart()
        envelope["From"] = self.sender_email
        envelope["To"] = self.receiver_email
        envelope["Reply-To"] = submitter_email
        envelope["Subject"] = "CONTACT from shawngrover.ca"
        body = f"""
A contact request has been submitted at shawngrover.ca:

Name: {name}
Email: {submitter_email}
Message: {submitted_message}
        """
        envelope.attach(MIMEText(dedent(body), "plain"))


        try:
            # Send the envelope
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as mailserver:
                mailserver.starttls()
                mailserver.login(self.smtp_username, self.smtp_password)
                mailserver.sendmail(self.sender_email, self.receiver_email, envelope.as_string())
                mailserver.quit()
            # context = smtplib.SMTP(self.smtp_server, self.smtp_port)

            return True
        except smtplib.SMTPException as e:
            print(e)
            sys.exit()
            return False
