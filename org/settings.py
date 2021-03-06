import os
import sys
from os import path


FOUNDRY = {
    'sms_gateway_api_key': '',
    'sms_gateway_password': '',
    'layers': ('basic',)
}

# Paths

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def abspath(*args):
    """convert relative paths to absolute paths relative to PROJECT_ROOT"""
    return os.path.join(PROJECT_ROOT, *args)

SCRIPT_PATH =  path.abspath(path.dirname(__file__))
GEOIP_PATH = abspath('..')

PROJECT_MODULE = 'org'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# For Postgres (not location aware) do from command line
# echo "CREATE USER org WITH PASSWORD 'org'" | sudo -u postgres psql
# echo "CREATE DATABASE org WITH OWNER org ENCODING 'UTF8'" | sudo -u postgres psql

# For Postgres (location aware) do from command line
# echo "CREATE USER org WITH PASSWORD 'org'" | sudo -u postgres psql
# echo "CREATE DATABASE org WITH OWNER org ENCODING 'UTF8' TEMPLATE template_postgis" | sudo -u postgres psql

# For MySQL remember to first do from a MySQL shell:
# CREATE database org;
# GRANT ALL ON org.* TO 'org'@'localhost' IDENTIFIED BY 'org';
# GRANT ALL ON test_org.* TO 'org'@'localhost' IDENTIFIED BY 'org';
# FLUSH PRIVILEGES;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'org', # Or path to database file if using sqlite3.
        'USER': 'org', # Not used with sqlite3.
        'PASSWORD': 'org', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = abspath('../media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = abspath('../static/basic')

STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c0a6658d8eb7d883a8637daba5d2ad11e581de24c750f13998b42ce9'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'likes.middleware.SecretBallotUserIpUseragentMiddleware',
    'foundry.middleware.PaginationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

# A tuple of callables that are used to populate the context in RequestContext.
# These callables take a request object as their argument and return a
# dictionary of items to be merged into the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'preferences.context_processors.preferences_cp',
    'foundry.context_processors.foundry',
)

# AppDirectoriesTypeLoader must be after filesystem loader
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'foundry.loaders.AppDirectoriesTypeLoader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'org.urls'

INSTALLED_APPS = (
    # The order is important else template resolution may not work
    'org',
    'foundry',
    'downloads',
    'friends',
    'section',
    'gallery',
    'googlesearch',
    'export',
    'snippetscream',
    'generate',
#    'jmbo_calendar',
    'jmbo',
    'photologue',
    'captcha',
    'secretballot',
    'publisher',
    'category',
    'post',
    'likes',
    'gizmo',
    'object_tools',
    'registration',
    'preferences',
    'banner',
    'competition',
    'ckeditor',
    'contact',
    'poll',
    'simple_autocomplete',
    'pagination',
    'south',
    'compressor',
    'jmbo_analytics',
    'analytics',
    'gunicorn',
    'sites_groups',
    #'atlas',
    'tastypie',
    'social_auth',
    'dfp',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'raven.contrib.django',
    'raven.contrib.django.celery',
    'djcelery',
)

# Your ReCaptcha provided public key.
RECAPTCHA_PUBLIC_KEY = '6LccPr4SAAAAAJRDO8gKDYw2QodyRiRLdqBhrs0n'

# Your ReCaptcha provided private key.
RECAPTCHA_PRIVATE_KEY = '6LccPr4SAAAAAH5q006QCoql-RRrRs1TFCpoaOcw'

# Module containing gizmo configuration
ROOT_GIZMOCONF = '%s.gizmos' % PROJECT_MODULE

# URL prefix for ckeditor JS and CSS media (not uploaded media). Make sure to use a trailing slash.
CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'

# Specify absolute path to your ckeditor media upload directory.
# Make sure you have write permissions for the path, i.e/home/media/media.lawrence.com/uploads/
CKEDITOR_UPLOAD_PATH = abspath('../media/uploads/')

CKEDITOR_CONFIGS = {
    'default': {'toolbar_Full': [
        ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
        ['Link', 'Image', 'Flash', 'PageBreak'],
        ['TextColor', 'BGColor'],
        ['Smiley', 'SpecialChar'], ['Source'],
    ]},
}

# Restrict uploaded file access to user who uploaded file
CKEDITOR_RESTRICT_BY_USER = True

# LASTFM_API_KEY = '' # not used yet

LOGIN_URL = '/login'

LOGIN_REDIRECT_URL = '/'

# todo: add setting to foundry paster
AUTHENTICATION_BACKENDS = (
    'foundry.backends.MultiBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.twitter.TwitterBackend',
)

COMMENTS_APP = 'foundry'

SIMPLE_AUTOCOMPLETE = {
    'auth.user': {'threshold': 20},
    'category.category': {'threshold':20},
    'jmbo.modelbase': {
        'threshold': 50,
        'duplicate_format_function': lambda item, model, content_type: item.as_leaf_class().content_type.name
    }
}

STATICFILES_FINDERS = (
    'foundry.finders.FileSystemLayerAwareFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ADMIN_APPS_EXCLUDE = (
    'Cal',
    'Event',
    'Photologue',
    'Publisher',
    'Registration',
    'Auth',
)

ADMIN_MODELS_EXCLUDE = (
    'Groups',
    'Video files',
)

JMBO_ANALYTICS = {
    'google_analytics_id': 'UA-58792160-1',
}

PHOTOLOGUE_MAXBLOCK = 2 ** 20

DJANGO_ATLAS = {
    'google_maps_api_key': 'AIzaSyBvdwGsAn2h6tNI75M5cAcryln7rrTYqkk',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
         'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
         }
     },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'WARN',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'raven': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': True,
        },
        'sentry.errors': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'WARN',
            'propagate': False,
        },
    },
}

# See django-socialauth project for all settings
SOCIAL_AUTH_USER_MODEL = 'foundry.Member'
#FACEBOOK_APP_ID = ''
#FACEBOOK_API_SECRET = ''
#TWITTER_CONSUMER_KEY = ''
#TWITTER_CONSUMER_SECRET = ''

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
COMPRESS_CSS_HASHING_METHOD = 'content'

# Set else async logging to Sentry does not work
CELERY_QUEUES = {
    'default': {
        'exchange': 'celery',
        'binding_key': 'celery'
    },
    'sentry': {
        'exchange': 'celery',
        'binding_key': 'sentry'
    },
}

ADMIN_APPS_EXCLUDE = (
    'Cal',
    'Event',
    'Photologue',
    'Publisher',
    'Registration',
    'Auth',
    'Competition',
    'Djcelery',
    'Sites',
    'Social_Auth',
    'Analytics',
    'Show',
    'Music',
    'Atlas',
    'Jmbo',
    'Jmbo_Calendar',
    'Gallery',
    'Poll',
    'Foundry',
    'Category',
)

ADMIN_MODELS_EXCLUDE = (
    'Banner proxies',
    'Code banners',
    'Dfp banners',
    'Competition preferences',
    'Contact preferences',
    'Gallery preferencess',
    'Login Preferences',
    'Naughty Word Preferences',
    'Password Reset Preferences',
    'Registration Preferences',
    'Text overlay temporary downloads',
)


# Debug toolbar. Uncomment if required.
#INSTALLED_APPS += ('debug_toolbar',)
#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#INTERNAL_IPS = ('127.0.0.1',)

import djcelery
djcelery.setup_loader()
