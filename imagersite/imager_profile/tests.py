"""Test for first day on imager site."""

from django.test import TestCase
from imager_profile.models import ImagerProfile, User   
import pytest
import factory_boy
# Create your tests here.


class ProfileTestCase(TestCase):
    """Test test."""

    def test_add_user(self):
        """Test adding a user."""
        user = User(username='nemo', email='nemo@none.net')
        user.set_password = "blahblahblah"
        user.save
        profile = ImagerProfile(website='www.nope.net',
                                location='nowhere',
                                fee=1000000.55,
                                bio='Herp de derp',
                                phone='555-5555',
                                user=user)
        profile.save()

    def test_user_has_website(self):
        """Test that a user has a website."""
        