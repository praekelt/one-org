from org.settings import *


FOUNDRY['layers'] = ('basic',)
SITE_ID = 2

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
