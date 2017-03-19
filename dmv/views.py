from rest_framework import generics
from dmv.models import Household, Person, Vehicle
from dmv.serializers import HouseholdSerializer, PersonSerializer, VehicleSerializer


class HouseholdListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HouseholdSerializer
    queryset = Household.objects.all()
    
    
class HouseholdRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseholdSerializer
    queryset = Household.objects.all()


class PersonListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_fields = ('household',)
    

class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    

class VehicleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_fields = ('household',)
    
    
class VehicleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
