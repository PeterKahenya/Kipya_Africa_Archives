from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.i18n import i18n_patterns
from administration.views import RecordTokens,AccessTokens
from delegates.views import DelegatesView,GetPackage
from sponsors.views import SponsorsView
from events.views import Experience,Login,ExpoView
from django.contrib.auth import logout
from django.shortcuts import redirect
from administration.views import ContactsView
from administration.management import ManageView,SendEmailToOne,SendToAll
from .home import *
import uuid

def logout_view(request):
    logout(request)
    return redirect("/")


admin.autodiscover()

urlpatterns = i18n_patterns(
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    re_path('^serviceworker.js$', service_worker),
    re_path('^firebase-messaging-sw.js$', firebase_messaging_sw),
    re_path('^manifest.json$', manifest),
    re_path('^sitemap.xml$', sitemap),
    path('newlead', ContactsView.as_view()),
    re_path(r'^', include('cms.urls')),
    path('tokens', RecordTokens.as_view()),
	path('delegates', DelegatesView.as_view()),
    path('manage', ManageView.as_view()),
    path('manage/send_to_one', SendEmailToOne.as_view()),
    path('manage/send_to_all', SendToAll.as_view()),
	path('sponsorships', SponsorsView.as_view()),
	path('package', GetPackage.as_view()),
	path('experience', Experience.as_view()),
	path('experience/<uuid:sponsor_id>', ExpoView.as_view()),
	path('login', Login.as_view()),
    path('logout', logout_view),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
