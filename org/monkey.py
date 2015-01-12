import re

from django.contrib.gis.geos import libgeos


version_regex = re.compile(r'^(?P<version>(?P<major>\d+)\.(?P<minor>\d+)\.(?P<subminor>\d+))((rc(?P<release_candidate>\d+))|dev)?-CAPI-(?P<capi_version>\d+\.\d+\.\d+)')
