import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/mail')
sys.path.append('/home/peter/projects/mail/mail')


os.environ["DJANGO_SETTINGS_MODULE"] = "mail.settings"


application = get_wsgi_application()