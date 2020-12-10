# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

message = Mail(
    from_email='info@eawaters.com',
    to_emails='peter@kipya-africa.com',
    subject='Peter Kahenya is Testing Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)