from rest_framework import viewsets, exceptions
from rest_framework_json_api.views import RelationshipView
from rest_framework_json_api.utils import format_drf_errors
from dmv.models import Household, Person, Vehicle
from dmv.serializers import HouseholdSerializer, PersonSerializer, VehicleSerializer

HTTP_422_UNPROCESSABLE_ENTITY = 422


class JsonApiViewSet(viewsets.ModelViewSet):
    """
    This is an example on how to configure DRF-jsonapi from
    within a class. It allows using DRF-jsonapi alongside
    vanilla DRF API views.
    
    See https://github.com/django-json-api/django-rest-framework-json-api/blob/develop/example/views.py
    """
    # parser_classes = [
    #     rest_framework_json_api.parsers.JSONParser,
    #     rest_framework.parsers.FormParser,
    #     rest_framework.parsers.MultiPartParser,
    # ]
    # renderer_classes = [
    #     rest_framework_json_api.renderers.JSONRenderer,
    #     rest_framework.renderers.BrowsableAPIRenderer,
    # ]
    # metadata_class = rest_framework_json_api.metadata.JSONAPIMetadata

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.ValidationError):
            # some require that validation errors return 422 status
            # for example ember-data (isInvalid method on adapter)
            exc.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        # exception handler can't be set on class so you have to
        # override the error response in this method
        return super(JsonApiViewSet, self).handle_exception(exc)


class HouseholdViewSet(JsonApiViewSet):
    serializer_class = HouseholdSerializer
    queryset = Household.objects.all()


class PersonViewSet(JsonApiViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_fields = ('household',)


class VehicleViewSet(JsonApiViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_fields = ('household',)


class HouseholdRelationshipView(RelationshipView):
    queryset = Household.objects


class PersonRelationshipView(RelationshipView):
    queryset = Person.objects


class VehicleRelationshipView(RelationshipView):
    queryset = Vehicle.objects
