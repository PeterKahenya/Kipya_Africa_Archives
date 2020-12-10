from django.contrib import admin
from django.urls import path,include
from subscribers.views import AddSubscriberView,SubscriberList,Unsubscribe
from .home import HomeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view()),
    path('newsletters/',include('newsletters.urls')),
    path('subscribers/', login_required(SubscriberList.as_view())),
    path('subscribers/add', AddSubscriberView.as_view()),
    path('subscribers/unsubscribe', Unsubscribe.as_view()),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
]
