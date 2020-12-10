from django.contrib import admin
from django.urls import path
from home.views import HomeView
from users.views import AddBoreholeView,BoreholeLoginView,logout_view
from dashboard.views import DashboardView,WRAView,WRABoreholeDashboard
from readings.views import GetReadings,PaymentsOptions,LipaNaMPesa

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('users/signup', AddBoreholeView.as_view()),
    path('users/login', BoreholeLoginView.as_view()),
    path('users/login', BoreholeLoginView.as_view()),
    path('users/logout', logout_view),
    path('dashboard', DashboardView.as_view()),
    path('wra', WRAView.as_view()),
    path('wra-dashboard', WRABoreholeDashboard.as_view()),

    path('readings', GetReadings.as_view()),
    path('paymentoptions', PaymentsOptions.as_view()),
    path('mpesa', LipaNaMPesa.as_view()),
    
]
