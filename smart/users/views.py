from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from boreholes.models import Borehole, Meter
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/")


class AddBoreholeView(View):

    def get(self, request):
        return render(request, "signup.html", None, None, None, None)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("email")
        password = request.POST.get("password")
        meter_id = request.POST.get("meter_id")
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")

        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        meter = Meter()
        meter.device_id = meter_id
        meter.save()
        borehole = Borehole()
        borehole.longitude = longitude
        borehole.latitude = latitude
        borehole.meter = meter
        borehole.user = user
        borehole.save()

        if user is not None:
            login(request, user)
            return redirect("/dashboard", permanent=True)
        else:
            return render(request, "signup.html", None, None, None, None)


class BoreholeLoginView(View):
    def get(self, request):
        return render(request, "login.html", None, None, None, None)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect("/wra")
            else:
                if Borehole.objects.filter(user=user).exists():
                    login(request, user)
                    return redirect("/dashboard")
                else:
                    return render(request, "login.html", {"ERRORS": "Invalid login credentials"}, None, None, None)
        else:
            return render(request, "login.html", {"ERRORS": "Invalid login credentials"}, None, None, None)
