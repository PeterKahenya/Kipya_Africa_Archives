from django.contrib import admin
from django.urls import path,include
from .home import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('courses/',include('courses.urls')),
    path('accounts/',include('accounts.urls')),
    path('payments/',include('payments.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
