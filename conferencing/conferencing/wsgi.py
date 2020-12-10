import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/conferencing')
sys.path.append('/home/peter/projects/conferencing/conferencing')


os.environ["DJANGO_SETTINGS_MODULE"] = "conferencing.settings"

application = get_wsgi_application() 