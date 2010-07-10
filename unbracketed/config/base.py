import os

DEBUG = False
LOCAL_DEV = False

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
ADMINS = ( ( 'Brian Luft','---------' ), )

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join( PROJECT_PATH, 'unbracketed.db' )            # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = False

SITE_URL = 'http://unbracketed.com'
MEDIA_URL = '%s%s' % (SITE_URL,'/site_media/')
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

SITE_ID = 1

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH,'templates'),)

INTERNAL_IPS = ( '127.0.0.1', )

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_EMAIL='brian@unbracketed.com'
SERVER_FROM_EMAIL='brian@unbracketed.com' 

SERVER_EMAIL='brian@unbracketed.com'
EMAIL_SUBJECT_PREFIX = '[UNBRACKETED] '

USE_I18N = False


CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_KEY_PREFIX = ''


MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.syndication',
    'django.contrib.markup',
    'django.contrib.admin',
    
    'django_extensions',
    #'debug_toolbar',
    
    'tagging',
    
    #TODO still using?
    'template_utils',
    'unbracketed.apps.projects',
    
    'unbracketed.apps.utils',
    'unbracketed.apps.content',
    'unbracketed.apps.stream',
    
    'south',
    'markitup',
)

INTERNAL_IPS = ( '127.0.0.1', )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'unbracketed.urls'


USE_I18N = False


#MARKUP_FILTER = ('markdown', {})

MARKITUP_PREVIEW_FILTER=('markdown.markdown', {})
#TODO:
#JQUERY_URL = 'jquery.min.js'
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/markitup'

TWITTER_USER = 'unbracketed'
TWITTER_PASSWORD = '******'
DELICIOUS_USER = 'kingoflunnova'
DELICIOUS_PASSWORD = '*****'
