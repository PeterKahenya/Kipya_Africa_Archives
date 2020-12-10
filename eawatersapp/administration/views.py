from django.shortcuts import render,redirect
from django.views import View
from .models import Contact
import json
from django.http import JsonResponse

class RecordTokens(View):
    def get(self,request):
        print(request)
        return render(request,"tokens.html",{"token":request.GET.get("code")})
    def post(self,request):
        print(request.POST)

class AccessTokens(View):
    def get(self,request):
        print(request)
        return render(request,"tokens.html",{"token":request.GET.get("code")})
    def post(self,request):
        print(request)
        print(request.POST)

class ContactsView(View):
    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))

        print("request.POST"+str(data))

        your_name=data.get("your_name")
        issue=data.get("issue")
        phone=data.get("phone")
        email=data.get("email")
        organization=data.get("organization")
        message=data.get("message")

        contact=Contact()
        contact.your_name=your_name
        contact.issue=issue
        contact.email=email
        contact.organization=organization
        contact.message=message
        contact.phone=phone
        contact.save()

        return JsonResponse({"success":True})