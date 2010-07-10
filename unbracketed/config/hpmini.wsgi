import os
import sys

from os.path import abspath, dirname, join

import site
site.addsitedir('/home/brian/proj/unbracketed/trunk/ve/lib/python2.6/site-packages')
sys.path.insert(0, abspath(join(dirname(__file__), '..', '..')))
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'unbracketed.config.hpmini'
application = WSGIHandler()
