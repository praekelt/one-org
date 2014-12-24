from django.db import models
from django.core.validators import validate_email, RegexValidator

from jmbo.models import ModelBase

from org.constants import COUNTRIES


class validators():
    validate_phone = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be between 9 and 15 numerical values.")
    validate_name = RegexValidator(regex=r'^[a-zA-Z]*$', message="Name must only include alpha characters.")

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
    name = models.CharField(
        max_length=255,
        validators=[validators.validate_name]
    )
    country = models.CharField(
        max_length=255,
        choices=COUNTRIES
    )
    mobile_number = models.CharField(
        max_length=16,
        blank=True,
        validators=[validators.validate_phone]
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
        return self.mobile_number


