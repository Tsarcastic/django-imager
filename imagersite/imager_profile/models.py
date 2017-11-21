from django.db import models
from django.contrib.auth.models import User

CAMERA_CHOICE = (
    ('1', 'One'),
    ('Banana', 'Two'),
    ('Turtle', 'Pie'))

SERVICES = (
    ('Go home', 'One'),
    ('Or not', 'Two'))

STYLEZ = (
    ('Old Timey', 'One'),
    ('New Timey', 'Two'))


class ProfileManager(models.Manager):
    def get_queryset(self):
        return super(ProfileManager, self).get_queryset()
        .filter(user.is_active=True)


class ImagerProfile(models.Model):
    """Profile for users of the site.
    Connects with Django's built-in User model"""

    def is_active(self):
        return user.is_active

    active = models.ProfileManager()
    profiles = models.Manager()

    user = models.ForeignKey(User, unique=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    fee = models.FloatField(blank=True)
    camera = models.CharField(max_length=255, choices=CAMERA_CHOICE)
    services = models.CharField(max_length=255, choices=SERVICES)
    bio = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=255)
    photo_styles = models.CharField(max_length=255, choices=STYLEZ)
