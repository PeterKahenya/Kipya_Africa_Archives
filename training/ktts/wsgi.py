import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/training')
sys.path.append('/home/peter/projects/training/ktts')


os.environ["DJANGO_SETTINGS_MODULE"] = "ktts.settings"

application = get_wsgi_application()
