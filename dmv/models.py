from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from localflavor.us.models import USStateField, USZipCodeField


class Household(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = USStateField()
    zip = USZipCodeField()
    number_of_bedrooms = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}, {1}, {2} {3}'.format(self.address, self.city, self.state, self.zip)


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
