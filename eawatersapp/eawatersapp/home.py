import os
from django.http import HttpResponse
from . import settings

def service_worker(request):
    response = HttpResponse(open(os.path.join(settings.BASE_DIR,"static/pwa/sw.js")).read(), content_type='application/javascript')
    return response

def firebase_messaging_sw(request):
    response = HttpResponse(open(os.path.join(settings.BASE_DIR,"static/pwa/firebase-messaging-sw.js")).read(), content_type='application/javascript')
    return response

def manifest(request):
    response = HttpResponse(open(os.path.join(settings.BASE_DIR,"static/pwa/manifest.json")).read(), content_type='application/json')
    return response

def sitemap(request):
    response = HttpResponse(open(os.path.join(settings.BASE_DIR,"static/pwa/sitemap.xml")).read(), content_type='application/xml')
    return response
