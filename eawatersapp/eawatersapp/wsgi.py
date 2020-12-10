import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/eawatersapp')
sys.path.append('/home/peter/projects/eawatersapp/tengenetsar')


os.environ["DJANGO_SETTINGS_MODULE"] = "eawatersapp.settings"


application = get_wsgi_application()