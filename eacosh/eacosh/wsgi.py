import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/eacosh')
sys.path.append('/home/peter/projects/eacosh/eacosh')


os.environ["DJANGO_SETTINGS_MODULE"] = "eacosh.settings"

application = get_wsgi_application()    
