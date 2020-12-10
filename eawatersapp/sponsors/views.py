from django.shortcuts import render
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import filters
import requests
from attendees.models import Attendee
from delegates.models import Delegate
from payments.models import Payment
from events.models import Event,Registration
from django.contrib.auth.models import User
from django.http import JsonResponse
from decimal import Decimal
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .mail import send_email
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from payments.models import Package
from .models import Sponsor

@method_decorator(csrf_exempt, name='dispatch')
class SponsorsView(View):

    def success_email(self, to,payment,attendee,sponsor):
        print("SENDING EMAILS IN VIEWS !!!")

        html_message = render_to_string('emails/sponsor_register_success.html', {'attendee': attendee,"payment":payment,"sponsor":sponsor })
        send_email(
            from_email="info@eawaters.com",
            to_emails=[to],
            subject="Confirmation of Registration for The 5th East Africa Water Summit and Expo",
            content=html_message,
            ccs=[],
            bccs=["peter@eawters.com","info@eawaters.com"],
            attachments=[]
            )
        return True



    def register_delegate_to_event(self,email,first_name,last_name,attendee):
        for event in Event.objects.all():
            join_url=register(meeting_id=event.meeting_id,email=email,first_name=first_name,last_name=last_name)
            registration=Registration()
            registration.event=event
            registration.attendee=attendee
            registration.link=join_url
            registration.save()












    def post(self, request):
        data=json.loads(request.body.decode('utf-8'))
        print(data)
        title=data.get("title")
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        country=data.get("country")
        phone=data.get("phone")
        email=data.get("email")
        organization=data.get("organization")
        job_title=data.get("job_title")
        association=data.get("association")
        sponsortship=data.get("sponsortship")

        mpesa_code=data.get("mpesa_code")

        if Payment.objects.filter(code=mpesa_code).first():
            return JsonResponse(data={"message":"That payment isn't correct"})


        payment_url = "https://tengenetsar.kipya-africa.com/api/shop/payment/payment-method-one/check"
        payment_response=requests.post(url=payment_url,data={"code":mpesa_code})
        if payment_response.status_code==200 and not payment_response.json().get("NF"):
            if User.objects.filter(username=email).first():
                return JsonResponse(data={"message":"Email Already exists"})
            else:

                user=User.objects.create_user(email,email,email)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                attendee = Attendee()
                attendee.user=user
                attendee.title=title
                attendee.country=country
                attendee.phone=phone
                attendee.organization=organization
                attendee.job_title=job_title
                attendee.association="N/A"
                attendee.save()

                payment=Payment()
                payment.method=payment_response.json().get("method")
                payment.amount=Decimal(payment_response.json().get("amount"))
                payment.account=payment_response.json().get("payment_by")
                payment.code=payment_response.json().get("code")
                payment.save()

                sponsor=Sponsor()
                sponsor.payment=payment
                sponsor.attendee=attendee
                sponsor.tier=sponsorship
                sponsor.save()

                """
                self.register_delegate_to_event(email=email,first_name=first_name,last_name=last_name,attendee=attendee)
                """
                self.success_email(to=email,payment=payment,attendee=attendee,sponsor=sponsor)

                login(request, user)

                return JsonResponse(data={"message":"success","sponsor_id":sponsor.id})
        else:
            print("That payment isn't correct")
            print(payment_response.text)
            return JsonResponse(data={"message":"That payment isn't correct"})
