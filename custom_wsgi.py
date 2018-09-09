import os
import sys
sys.path = ['/media/deepak/Entreprise/projects/djangoProjects/current/original_prayag_mob_friendly/prayag/'] + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'prayag.seetings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()