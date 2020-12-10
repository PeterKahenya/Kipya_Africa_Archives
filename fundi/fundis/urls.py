from django.urls import path,include
from .views import FundiView
urlpatterns = [
    path('',FundiView.as_view())
]
