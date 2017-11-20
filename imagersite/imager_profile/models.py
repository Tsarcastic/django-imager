from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    website = models.CharField(('Website'), blank=True)
    location = models.CharField(('Location'), blank=True)
    fee = models
    # website - str | url
    # location - str
    # fee - float
    # camera - str | choices
    # services - str | multiple choices
    # bio - str | large text
    # phone - str
    # photo_styles - str | multiple choices
    # user
    # is_active