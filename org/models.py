from django.db import models
from django.core.validators import validate_email

from jmbo.models import ModelBase

from org import monkey
from org.constants import COUNTRIES


class Signup(models.Model):
    email = models.CharField(
        max_length=64,
        unique=True,
        validators=[validate_email]
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("email",)

    def __unicode__(self):
        return email


class PetitionEntry(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(
        max_length=255,
        choices=COUNTRIES
    )
    mobile_number = models.CharField(
        max_length=16,
        blank=True
    )
    email = models.CharField(
        max_length=64,
        validators=[validate_email],
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "Petition Entries"

    def __unicode__(self):
        return mobile_number

