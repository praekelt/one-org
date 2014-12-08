from django.conf.urls.defaults import patterns, url, include

from foundry.urls import *


urlpatterns += patterns('',

    url(
        r'^share-site-tile/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'org/share_site_tile.html'},
        name='share-site-tile'
    ),

)
