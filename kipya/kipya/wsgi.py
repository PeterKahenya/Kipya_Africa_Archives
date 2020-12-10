"""
WSGI config for kipya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/peter/projects/kipya')
sys.path.append('/home/peter/projects/kipya/kipya')

os.environ['DJANGO_SETTINGS_MODULE']='kipya.settings'

application = get_wsgi_application()
