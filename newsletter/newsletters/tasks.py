from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from subscribers.models import Subscriber
import uuid
from .models import Newsletter, Post
from .mail import send_email

def send_newsletter(pk,scheme,host):
    print("sending actual newsletter")
    newsletter=Newsletter.objects.get(id=pk)
    posts=Post.objects.filter(newsletter=newsletter).order_by('created')

    html_message = render_to_string('newsletter_detail.html', {"newsletter":newsletter,"posts":posts,"scheme":scheme,"host":host})
    plain_message = strip_tags(html_message)
    
    subscribers=Subscriber.objects.filter(is_subscribed=True)

    from_email = 'Kipya Africa Limited <info@kipya-africa.com>'
    to = "info@kipya-africa.com"
    bccs = [subscriber.email for subscriber in subscribers]

    print(bccs)
    # bccs=["peter@africa-drilling-solutions.com"]
    subject=newsletter.newsletter_name

    status = send_email(from_email=from_email,to_emails=[to],subject=subject,content=html_message,ccs=[],bccs=bccs,attachments=[])
    newsletter.is_sent=True
    newsletter.save()
    return status

def test_newsletter(pk,test_email,scheme,host):
    newsletter=Newsletter.objects.get(id=pk)
    posts=Post.objects.filter(newsletter=newsletter).order_by('created')
    html_message = render_to_string('newsletter_detail.html', {"newsletter":newsletter,"posts":posts,"scheme":scheme,"host":host})
    plain_message = strip_tags(html_message)

    from_email = 'Kipya Africa Limited <info@kipya-africa.com>'
    to = test_email
    subject = newsletter.newsletter_name


    return send_email(from_email=from_email,to_emails=[to],subject=subject,content=html_message,ccs=[],bccs=["no-reply@kipya-africa.com"],attachments=[])

