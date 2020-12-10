from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
import json
import uuid
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.utils.crypto import get_random_string
from .tasks import send_email


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['fullname', 'email']

# class SubscriberList(APIView):
#     """
#         List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Subscriber.objects.all()
#         serializer = SubscriberSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SubscriberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SubscriberList(View):
    def get(self, request, format=None):
        subscribers = Subscriber.objects.all()
        return render(request,"subscribers_list.html",{"subscribers":subscribers})

@method_decorator(csrf_exempt, name='dispatch')
class AddSubscriberView(View):
    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))
        fullname=data["fullname"]
        email=data["email"]
        
        p_subscriber=Subscriber.objects.filter(email=email)
        subscriber=None
        if not p_subscriber:
            subscriber=Subscriber()
            subscriber.fullname=fullname
            subscriber.email=email
            subscriber.is_subscribed=True
            subscriber.save()
        else:
            subscriber=p_subscriber.first()
            subscriber.is_subscribed=True
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
        # message.send()

        return JsonResponse({"IS_SUBSCRIBED":True })

@method_decorator(csrf_exempt, name='dispatch')
class RFPView(View):
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

        subject="Africa Drilling Lead"
        html_message = render_to_string('potential_lead.html', {'potential': potential})
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
        return JsonResponse({"IS_DONE":True })

class Unsubscribe(View):
    def get(self,request,special_token=None,email=None):
        special_token,email=request.GET.get('unsb_token'),request.GET.get('email')
        if special_token and email:
            subscriber=Subscriber.objects.filter(special_token=special_token,email=email).first()
            if subscriber:
                subscriber.is_subscribed=False
                subscriber.save()
                return render(request,"unsubscribe.html",{"SUBSCRIBE_DONE":True})

        return render(request,"unsubscribe.html",{"SUBSCRIBE_DONE":False})


    def post(self,request):
        email_address=request.POST.get("email")
        subscriber=Subscriber.objects.filter(email=email_address).first()
        if subscriber:
            subscriber.special_token=str(get_random_string(length=64))
            subscriber.save()
            subject="Kipya Africa Weekly Newsletter Opt Out"

            scheme=request.scheme
            host=request.META["HTTP_HOST"]

            html_message = render_to_string('unsubscribe_email.html', {'special_token': subscriber.special_token,"email":email_address,"scheme":scheme,"host":host})
            send_email.delay(email_address,html_message,subject)
            return render(request,"unsubscribe.html",{"LINK_SENT":True})

        return render(request,"unsubscribe.html",{"LINK_SENT":False})
