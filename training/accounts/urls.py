from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path("login/",LoginView.as_view(), name='accounts_login'),
    path("logout/",LogoutView.as_view(), name='accounts_logout'),
    path("signup/",signup, name='accounts_signup')
    
]
