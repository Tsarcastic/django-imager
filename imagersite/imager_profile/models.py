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


class ImagerProfile(models.Model):
    """."""
    
    user = models.ForeignKey(User, unique=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    fee = models.FloatField(blank=True)
    camera = models.CharField(max_length=255, choices=CAMERA_CHOICE)
    services = models.CharField(max_length=255, choices=SERVICES)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=255)
    photo_styles = models.CharField(max_length=255, choices=STYLEZ)
    # user
    # is_active
