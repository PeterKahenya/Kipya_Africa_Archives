from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url
from utilities.views import ME2iCFPs

admin.autodiscover()

urlpatterns = i18n_patterns(
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(

    path('admin/', admin.site.urls),
    path('me2icfps',ME2iCFPs.as_view()),
    re_path(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

