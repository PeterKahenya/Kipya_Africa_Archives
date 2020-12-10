from django.shortcuts import render
from django.views import View

class PricingView(View):
    def get(self,request):
        return render(request,"pricing.html",None,None,None,None)
    