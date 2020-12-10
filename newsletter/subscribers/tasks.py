from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import EmailMessage
import uuid


@shared_task
def send_email(email_address,email_body,email_subject):
    from_email = 'Kipya Africa Limited <info@kipya-africa.com>'
    message = EmailMessage(email_subject,email_body,from_email,[email_address],[],headers={'Message-ID': str(uuid.uuid4()) },attachments=[])
    message.content_subtype = "html"
    message.send()

    return None