from org.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'org',
        'USER': 'org',
        'PASSWORD': 'org',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MEDIA_ROOT = '%s/../org-media-qa/' % BUILDOUT_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'org_qa',
    }
}

CKEDITOR_UPLOAD_PATH = '%s/../org-media-qa/uploads/' % BUILDOUT_PATH
