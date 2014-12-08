from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from org.models import Signup, PetitionEntry


admin.site.register(Signup, admin.ModelAdmin)
admin.site.register(PetitionEntry, admin.ModelAdmin)
