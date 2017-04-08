from django.conf.urls import include, url
from rest_framework import routers
from dmv import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'households', views.HouseholdViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'vehicles', views.VehicleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^households/(?P<pk>\d+)/relationships/(?P<related_field>[^/.]+)$',
        views.HouseholdRelationshipView.as_view(), name='household-relationships'),
    url(r'^persons/(?P<pk>\d+)/relationships/(?P<related_field>[^/.]+)$',
        views.PersonRelationshipView.as_view(), name='person-relationships'),
    url(r'^vehicles/(?P<pk>\d+)/relationships/(?P<related_field>[^/.]+)$',
        views.VehicleRelationshipView.as_view(), name='vehicle-relationship'),
]
