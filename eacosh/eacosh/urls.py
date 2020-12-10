from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from register.views import NewAttendeeView
from home.views import HomeView
from about.views import AboutView
from speakers.views import SpeakersView
from pricing.views import PricingView
from contact.views import ContactView

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('speakers/', SpeakersView.as_view()),
    path('pricing/', PricingView.as_view()),
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
