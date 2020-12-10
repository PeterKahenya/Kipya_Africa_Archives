from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from .models import ME2iCFP


class ME2iCFPs(View):
    def get(self):
        return redirect("/")
    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))
        # print("post"+data)
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        email=data.get("email")
        industry=data.get("industry")
        idea=data.get("idea")

        me2icfp=ME2iCFP()
        me2icfp.first_name=first_name
        me2icfp.last_name=last_name
        me2icfp.email=email
        me2icfp.industry=industry
        me2icfp.idea=idea
        me2icfp.save()

        return JsonResponse({"success":True})
    
        