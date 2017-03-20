from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
from localflavor.us.models import USStateField, USZipCodeField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Household(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = USStateField()
    zip = USZipCodeField()
    number_of_bedrooms = models.PositiveSmallIntegerField()
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}, {1}, {2} {3}'.format(self.address, self.city, self.state, self.zip)

    def __init__(self, *args, **kwargs):
        super(Household, self).__init__(*args, **kwargs)
        # Store the original state of the is_completed field
        self.__original_is_completed = self.is_completed

    def save(self, *args, **kwargs):
        # Add a timestamp the first time is_completed is changed to True
        if self.is_completed and (self.is_completed != self.__original_is_completed):
            self.completed_at = now()
        super(Household, self).save(*args, **kwargs)
        self.__original_is_completed = self.is_completed


class Person(models.Model):
    GENDER_CHOICES = (
        ('f', 'Female'),
        ('m', 'Male')
    )

    household = models.ForeignKey(Household, related_name='people')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Vehicle(models.Model):
    household = models.ForeignKey(Household, related_name='vehicles')
    person = models.ForeignKey(Person, related_name='vehicles')
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2018)])
    license_plate = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.year, self.make, self.model)


# Create an API Token whenever a new user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
