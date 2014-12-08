from django.db import models

from jmbo.models import ModelBase


class Signup(models.Model):
    email = models.CharField(max_length=64, unique=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("email",)

    def __unicode__(self):
        return email


class PetitionEntry(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=16, unique=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "Petition Entries"

    def __unicode__(self):
        return mobile_number

