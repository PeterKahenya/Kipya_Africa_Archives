from django.views import View
from django.shortcuts import redirect,render
from  subscribers.models import Subscriber

class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,"home.html",{"subscribers":Subscriber.objects.all()})
        else:
            return redirect("/accounts/login")
    def post(self,request):
        if request.user.is_authenticated:
            return redirect("/dashboard")
        else:
            return redirect("/accounts/login")
