from django.contrib import admin
from django.urls import path
from api.views import SendEmailView
from django.http import HttpResponse

def home_ok(request):
	return HttpResponse("ok")


urlpatterns = [
	path('',home_ok),
    path('admin/', admin.site.urls),
    path('send/', SendEmailView.as_view()),

]
