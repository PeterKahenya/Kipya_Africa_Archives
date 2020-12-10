import os
import sys


from django.core.wsgi import get_wsgi_application
sys.path.append('/home/peter/projects/newsletter')
sys.path.append('/home/peter/projects/newsletter/newsletter')

os.environ['DJANGO_SETTINGS_MODULE']= 'newsletter.settings'

application = get_wsgi_application()
