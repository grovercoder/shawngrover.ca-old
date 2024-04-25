from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated
from textwrap import dedent
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

print(f"USE_CORS: {os.environ.get('USE_CORS')}")
if os.environ.get('USE_CORS').lower() == 'true':
    print('using CORS')
    origins = [
        f"{os.environ.get('WEB_SERVER')}:{os.environ.get('WEB_PORT', 8000)}/",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

@app.post("/contact", response_class=HTMLResponse)
def handle_contact_request(name: Annotated[str, Form()], email: Annotated[str, Form()], message: Annotated[str, Form()]):
    try:
            send_email(name, email, message)
            return """
<div class="response thanks">
    <h2>Thank you.</h2>
    <p>Your message has been sent and I'll reply as soon as possible.</p>
</div>
"""
    except:
         return """
<div class="response error">
    <h2>Something went wrong</h2>
    <p>Your post was received but could not be sent along properly.</p>
    <p>Please try again in a while.</p>
</div>
"""
app.mount("/", StaticFiles(directory=".", html=True), name="static")


def send_email(name: str, sender: str, message: str):
    sender_email = os.environ.get('SMTP_SENDER')
    receiver_email = os.environ.get('SMTP_RECEIVER')
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT')
    smtp_username = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    envelope = MIMEMultipart()
    envelope["From"] = sender_email
    envelope["To"] = receiver_email
    envelope["reply-to"] = sender
    envelope["Subject"] = "CONTACT from shawngrover.ca"
    body = f"""
A contact request has been submitted at shawngrover.ca:

Name: {name}
Email: {sender}
Message: {message}
    """
    envelope.attach(MIMEText(dedent(body), "plain"))

    print(f'connecting to server: {smtp_server}  [{smtp_port}]')
    context = smtplib.SMTP(smtp_server, smtp_port)
    context.starttls()
    print('logging in')
    context.login(smtp_username, smtp_password)
    print('sending mail')
    context.sendmail(sender_email, receiver_email, envelope.as_string())
    context.quit()
    print('done')

