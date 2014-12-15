from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from org.models import PetitionEntry


admin.site.register(PetitionEntry, admin.ModelAdmin)
