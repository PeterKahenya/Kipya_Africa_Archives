from django.shortcuts import render
from django.views import View

class SpeakersView(View):
    def get(self,request):
        return render(request,"speakers.html",None,None,None,None)