import os
import requests
import base64
import uuid
import json
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.conf import settings


def send_main_email(attendee):
    from_email="East Africa Water Summit <info@eawaters.com>"
    subject="Zoom Link to Attend The 5th East Africa Water Summit"
    html_message = render_to_string('emails/delegate_feedback.html', {'delegate': attendee })
    plain_message = strip_tags(html_message)
    message = EmailMessage(subject,html_message,from_email,[attendee.email],["peter@eawaters.com"],reply_to=['info@eawaters.com'],headers={'Message-ID': str(uuid.uuid4()) },attachments=[])
    message.content_subtype = "html"
    message.send()

    return True

"""
def send_email(from_email="info@eawaters.com",to_emails=[],subject="",content="",ccs=[],bccs=[],attachments=[]):
    print("SENDING EMAILS !!!")
    send_email_url="https://api.sendgrid.com/v3/mail/send"
    headers={
        "Authorization":"Bearer "+"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",
        "Content-Type":"application/json"
    }
    tos=[{"email":email} for email in to_emails]
    bccs=[{"email":email} for email in bccs]
    ccs=[{"email":email} for email in ccs]
    attachments=[{"content":content,"type":mime,"disposition":"inline","filename":filename,"content_id":str(uuid.uuid4())} for content,mime,filename in attachments]


    data = {
        "personalizations": [
            {
            "to": tos,
            "subject": subject,
            "bcc":bccs,
            }
        ],
        "from": {
            "email": from_email
        },
        "content": [
            {
            "type": "text/html",
            "value": content
            }
        ]
    }   

    print(data)
    response=requests.post(url=send_email_url,data=json.dumps(data),headers=headers)
    print(response.text)
    return True


# send_email(from_email="info@eawaters.com",to_emails=["peter@kipya-africa.com"],subject="Testing EAWATERS",content="<strong>Testing 123</strong>",ccs=["peter@eawaters.com"],bccs=["peter@eacosh.com"],attachments=[(str(base64.b64encode(open("tokens.json","rb").read()),"utf-8"),"application/json","tokens.json")])

"""