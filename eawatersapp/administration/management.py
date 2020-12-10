from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from delegates.models import EAWATERS2020Delegate
from .zoom import register
from .mail import send_main_email



class ManageView(View):
	def get(self,request):
		if request.user.is_authenticated:
			delegates=EAWATERS2020Delegate.objects.all()
			return render(request,"manage/index.html",{'delegates':delegates})
		else:
			return redirect("/admin/login/?next=/en/manage")

	def post(self,request):
		title=request.POST["title"]
		first_name=request.POST["first_name"]
		last_name=request.POST["last_name"]
		email=request.POST["email"]
		phone=request.POST["phone"]
		country=request.POST["country"]
		organization=request.POST["organization"]
		job_title=request.POST["job_title"]
		association=request.POST["association"]
		mpesa_code=request.POST["mpesa_code"]



		delegate=EAWATERS2020Delegate()
		delegate.title=title
		delegate.first_name=first_name
		delegate.last_name=last_name
		delegate.email=email
		delegate.phone=phone
		delegate.country=country
		delegate.organization=organization
		delegate.job_title=job_title
		delegate.association=association
		delegate.mpesa_code=mpesa_code
		zoom_link=register("91233382906",email,first_name,last_name,country,country,phone,organization,job_title)
		delegate.zoom_link=zoom_link
		delegate.save()

		send_main_email(delegate)

		return redirect("/manage")


class SendEmailToOne(View):
	def post(self,request):
		delegate_id=request.POST["delegate_id"]
		delegate=EAWATERS2020Delegate.objects.get(pk=delegate_id)
		send_main_email(delegate)
		return redirect("/manage?action=yes")

class SendToAll(View):
	def post(self,request):
		delegates=EAWATERS2020Delegate.objects.all()
		for delegate in delegates:
			send_main_email(delegate)

		return redirect("/manage?action=yes")