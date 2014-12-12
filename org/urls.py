from django.conf.urls.defaults import patterns, url, include

from foundry.urls import *


urlpatterns += patterns('',

    url(
        r'^share-site-tile/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'org/share_site_tile.html'},
        name='share-site-tile'
    ),

    url(
        r'^signup-tile/$',
        'org.views.signup',
        {},
        name='signup-tile'
    ),

    url(
        r'^sign-petition-tile/$',
        'org.views.sign_petition',
        {},
        name='sign-petition-tile'
    ),

)
