from org.settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'org_live',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'org_live',
    }
}

COMPRESS_ENABLED = True

#SENTRY_DSN = 'ENTER_YOUR_SENTRY_DSN_HERE'
SENTRY_CLIENT = 'raven.contrib.django.celery.CeleryClient'
