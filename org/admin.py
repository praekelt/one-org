from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from org.models import TrivialContent


admin.site.register(TrivialContent, ModelBaseAdmin)
