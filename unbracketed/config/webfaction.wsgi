import os
import sys

from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "unbracketed", "ve", "src")))
sys.path.insert(0, abspath(join(dirname(__file__), "unbracketed","ve","lib","python2.5","site-packages")))
sys.path.insert(0, abspath(join(dirname(__file__), "unbracketed", "unbracketed")))

sys.path = ['/home/luftyluft/webapps/django_1_02_wsgi/unbracketed', '/home/luftyluft/webapps/django_1_02_wsgi/lib/python2.5'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'unbracketed.config.webfaction'
application = WSGIHandler()
