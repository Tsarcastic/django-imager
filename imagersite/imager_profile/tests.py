"""Test for first day on imager site."""

from django.test import TestCase
from imager_profile.models import ImagerProfile, User   
import pytest
import factory_boy
import factory
# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """."""
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'Dan{n}')
    email = 'dan@theman.com'


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

    def ProfileTests(TestCase):
        """."""

        def setUp():
            """."""
            for i in range(50):
                profile = ImagerProfile()
                user = UserFactory.create()
                user.set_password('blah')
                user.save()
                profile.user = user
                profile.save()


    def test_user_has_website(self):
        """."""
        """Test that a user has a website."""
        test_user = User.objects.get(username='nemo')

    def test_profile_is_deleted_when_user_is(self):
        the_user = user.objects.get(id=10)
        the_user.profile.location = 'test_value'
        user.objects.filter(id=10).delete()
        assertIsNone(ImagerProfile.active().filter(location='test_value'))
        