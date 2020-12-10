from django.shortcuts import render
from django.views import View
from .models import Contact
from django.core.mail import send_mail
from django.template.loader import render_to_string

class ContactView(View):
    def get(self,request):
        return render(request,"contact.html",{"CONTACTED":False},None,None,None)
    def post(self,request):
        fullname=request.POST.get("fullname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")

        contact=Contact()
        contact.full_name=fullname
        contact.email=email
        contact.phone=phone
        contact.message=message
        contact.save()

        # send_mail('Interested In EACOSH','Hello, my name is '+fullname+'. I am contacting EACOSH concerning '+message+' Contact Me via '+ email +' and '+phone,'info@eacosh.com',['info@eacosh.com'],fail_silently=False)
        # send_mail('EACOSH','Thank You for expressing interest in EACOSH. We will contact you in a moment','info@eacosh.com',[email],fail_silently=False)

        return render(request,"contact.html",{"CONTACTED":True},None,None,None)