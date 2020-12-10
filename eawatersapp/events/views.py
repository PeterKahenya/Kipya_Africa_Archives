from django.shortcuts import render,redirect
from django.views import View
from attendees.models import Attendee
from .models import Registration
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
from sponsors.models import Sponsor


class Experience(View):
    def get(self, request):
        if request.user.is_authenticated:
            attendee=Attendee.objects.filter(user=request.user).first()
            registrations = Registration.objects.filter(attendee=attendee)
            sponsors=Sponsor.objects.all()
            return render(request,"experience.html",{"attendee":attendee,"registrations":registrations,"sponsors":sponsors})
        else:
            return redirect("/login")


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
	def get(self, request):
		return render(request,"login.html")
	def post(self,request):
		if request.user.is_authenticated:
			return redirect("/experience")
		else:
			data=json.loads(request.body.decode('utf-8'))
			email=data.get("email")
			print(email)
			user = authenticate(username=email, password=email)
			print(email)
			if user:
				login(request, user)
				return JsonResponse({"success":True})
			else:
				return JsonResponse({"success":False})

class ExpoView(View):
    def get(self, request,sponsor_id=None):
        if request.user.is_authenticated:
            attendee=Attendee.objects.filter(user=request.user).first()
            sponsor=Sponsor.objects.filter(id=sponsor_id,attendee=attendee).first()
            return render(request,"expo.html",{"attendee":attendee,"sponsor":sponsor,"sponsor_id":sponsor_id})
        else:
            return render(request,"expo.html",{"sponsor_id":sponsor_id})
