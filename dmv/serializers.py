from rest_framework_json_api import serializers, relations
from dmv.models import Household, Person, Vehicle


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class HouseholdSerializer(serializers.ModelSerializer):
    persons = relations.ResourceRelatedField(many=True, read_only=True)
    vehicles = relations.ResourceRelatedField(many=True, read_only=True)

    included_serializers = {
        'persons': PersonSerializer,
        'vehicles': VehicleSerializer
    }

    class Meta:
        model = Household
        fields = ('id', 'address', 'city', 'state', 'zip', 'number_of_bedrooms', 'created_at', 'persons', 'vehicles')

    # class JSONAPIMeta:
    #     included_resources = ['persons', 'vehicles']  # include by default
