from django.conf.urls.defaults import patterns, url, include

from foundry.urls import *

import settings


urlpatterns += patterns('',

    url(
        r'^share-site-tile/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'org/share_site_tile.html'},
        name='share-site-tile'
    ),

    url(
        r'^sign-petition-success/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'org/sign_petition_success.html'},
        name='sign-petition-success'
    ),

    url(
        r'^404/$',
        'django.views.generic.simple.direct_to_template',
        {'template':'404.html'},
        name='four-o-four'
    ),

)

# Pre-empt so we override root
urlpatterns.insert(0,
    url(
        r'^$',
        'org.views.home',
        {},
        name='home'
    ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )
