import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/smart')
sys.path.append('/home/peter/projects/smart/smart')


os.environ["DJANGO_SETTINGS_MODULE"] = "smart.settings"

application = get_wsgi_application()
