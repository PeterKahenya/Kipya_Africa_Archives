from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import ADSSubscriber,KipyaPotentialLead
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
import json
import uuid

@method_decorator(csrf_exempt, name='dispatch')
class AddSubscriberView(View):
    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))
        fullname=data["fullname"]
        email=data["email"]

        subscriber=ADSSubscriber()
        subscriber.fullname=fullname
        subscriber.email=email
        subscriber.save()
        subject="Africa Drilling Subscription"
        html_message = render_to_string('subscribe_email.html', {'subscriber': subscriber})
        plain_message = strip_tags(html_message)
        from_email = 'Africa Drilling Solutions <info@africa-drilling-solutions.com>'

        to="info@africa-drilling-solutions.com"
        message = EmailMessage(
                    subject,
                    html_message,
                    from_email,
                    [to],
                    [],
                    reply_to=['info@africa-drilling-solutions.com'],
                    headers={'Message-ID': str(uuid.uuid4()) },
                )
        message.content_subtype = "html"
        message.send()
        return JsonResponse({"IS_SUBSCRIBED":True })

@method_decorator(csrf_exempt, name='dispatch')
class RFPView(View):

    def send_intro(self,lead):
        subject="Kipya Africa Drilling - Who We Are"
        html_message = render_to_string('intro_email.html', {'lead': lead})
        plain_message = strip_tags(html_message)
        from_email = 'Kipya Africa Drilling Solutions <info@africa-drilling-solutions.com>'
        to=lead.email
        message = EmailMessage(
                    subject,
                    html_message,
                    from_email,
                    [to],
                    [],
                    reply_to=['info@africa-drilling-solutions.com'],
                    headers={'Message-ID': str(uuid.uuid4()) },
                )
        message.content_subtype = "html"
        print(to+"\n")
        message.send()

    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))
        fullname=data["fullname"]
        organization=data["organization"]
        email=data["email"]
        rfp_request=data["request"]

        potential=KipyaPotentialLead()
        potential.fullname=fullname
        potential.organization=organization
        potential.email=email
        potential.rfp_request=rfp_request
        potential.save()

        subject="Kipya Africa Drilling Lead"
        html_message = render_to_string('potential_lead.html', {'potential': potential})
        plain_message = strip_tags(html_message)
        from_email = 'Kipya Africa Drilling Solutions <info@africa-drilling-solutions.com>'

        to="info@africa-drilling-solutions.com"
        message = EmailMessage(
                    subject,
                    html_message,
                    from_email,
                    [to],
                    [],
                    reply_to=['info@africa-drilling-solutions.com'],
                    headers={'Message-ID': str(uuid.uuid4()) },
                )
        message.content_subtype = "html"
        message.send()

        # self.send_intro(potential)
        return JsonResponse({"IS_DONE":True })
