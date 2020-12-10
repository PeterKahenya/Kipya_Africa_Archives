from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import requests
from attendees.models import Attendee
from delegates.models import Delegate
from payments.models import Payment
from events.models import Event,Registration
from django.contrib.auth.models import User
from django.http import JsonResponse
from decimal import Decimal
from django.contrib.auth import authenticate, login
from .zoom import register
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .mail import send_email
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from payments.models import Package


@method_decorator(csrf_exempt, name='dispatch')
class GetPackage(View):
    def get(self,request):
        # data = json.loads(request.body.decode('utf-8'))
        package_name=request.GET.get("name")
        print(package_name)
        package = Package.objects.filter(name=package_name).first()
        if package:
            return JsonResponse(data={"package":{"name":package.name,"amount":package.amount}})
        else:
            return JsonResponse(data={"message":"Invalid Package Type"})






@method_decorator(csrf_exempt, name='dispatch')
class DelegatesView(View):

    def success_email(self, to,payment,attendee):
        print("SENDING EMAILS IN VIEWS !!!")

        html_message = render_to_string('emails/register_success.html', {'attendee': attendee,"payment":payment })
        send_email(
            from_email="info@eawaters.com",
            to_emails=[to],
            subject="Confirmation of Registration for The 5th East Africa Water Summit and Expo",
            content=html_message,
            ccs=[],
            bccs=["peter@eawaters.com","info@eawaters.com"],
            attachments=[]
            )
        return True



    def register_delegate_to_event(self,email,first_name,last_name,attendee):
        for event in Event.objects.all():
            join_url=register(meeting_id=event.meeting_id,email=email,first_name=first_name,last_name=last_name,city=attendee.country,country=attendee.country,phone=attendee.phone,organization=attendee.organization,job_title=attendee.job_title)
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
        mpesa_code=data.get("mpesa_code")
        delegate_type=data.get("delegate_type")

        if delegate_type=="eac-delegate" or delegate_type=="intl-delegate":
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
            attendee.association=association
            attendee.save()

            return JsonResponse(data={"message":"Registration Success"})


        print(mpesa_code)
        if Payment.objects.filter(code=mpesa_code).first():
            return JsonResponse(data={"message":"That payment isn't correct"})


        payment_url = "https://tengenetsar.kipya-africa.com/api/shop/payment/payment-method-one/check"
        payment_response=requests.post(url=payment_url,data={"code":mpesa_code})
        print(payment_response.text)
        if payment_response.status_code==200 and not payment_response.json().get("NF"):
            print("Email Already exists")
            if User.objects.filter(username=email).first():
                print("Email Already exists")
                return JsonResponse(data={"message":"Email Already exists"})
            else:

                user=User.objects.create_user(email,email,email)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                print(user)

                attendee = Attendee()
                attendee.user=user
                attendee.title=title
                attendee.country=country
                attendee.phone=phone
                attendee.organization=organization
                attendee.job_title=job_title
                attendee.association=association
                attendee.save()

                print(attendee)

                payment=Payment()
                payment.method=payment_response.json().get("method")
                payment.amount=Decimal(payment_response.json().get("amount"))
                payment.account=payment_response.json().get("payment_by")
                payment.code=payment_response.json().get("code")
                payment.save()

                print(payment)

                delegate=Delegate()
                delegate.payment=payment
                delegate.attendee=attendee
                delegate.save()

                print(delegate)

                # self.register_delegate_to_event(email=email,first_name=first_name,last_name=last_name,attendee=attendee)
                self.success_email(to=email,payment=payment,attendee=attendee)

                login(request, user)

                return JsonResponse(data={"message":"success"})
        else:
            print("That payment isn't correct")
            print(payment_response.text)
            return JsonResponse(data={"message":"That payment isn't correct"})
