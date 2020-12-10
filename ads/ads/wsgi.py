"""
WSGI config for ads project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/peter/projects/ads')
sys.path.append('/home/peter/projects/ads/ads')

os.environ['DJANGO_SETTINGS_MODULE']='ads.settings'

application = get_wsgi_application()
