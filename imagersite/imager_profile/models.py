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
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Profile for users of the site.
    Connects with Django's built-in User model"""

    active = ProfileManager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    fee = models.FloatField(blank=True)
    camera = models.CharField(max_length=255, choices=CAMERA_CHOICE)
    services = models.CharField(max_length=255, choices=SERVICES)
    bio = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=255)
    photo_styles = models.CharField(max_length=255, choices=STYLEZ)

    @property
    def is_active(self):
        return self.user.is_active

    def __repr__(self):
        return """
        user: {}
        website: {}
        location: {}
        fee: {}
        camera: {}
        services: {}
        bio: {}
        phone: {}
        photo_styles: {}""".format(self.user,
                                   self.website,
                                   self.location,
                                   self.fee,
                                   self.camera,
                                   self.services,
                                   self.bio,
                                   self.phone,
                                   self.photo_styles)
