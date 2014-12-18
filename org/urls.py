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

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns.insert(0,
    url(
        r'^$',
        'org.views.home',
        {},
        name='home'
    ),
)
