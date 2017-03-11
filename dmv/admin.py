from django.contrib import admin
from dmv.models import Household, Person, Vehicle


admin.site.register([Household, Person, Vehicle])
