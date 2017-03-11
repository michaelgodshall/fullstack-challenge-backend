from django.conf.urls import url
from dmv import views


urlpatterns = [
    url(r'^households', views.HouseholdListCreateAPIView.as_view(), name='households'),
    url(r'^persons', views.PersonListCreateAPIView.as_view(), name='persons'),
    url(r'^vehicles', views.VehicleListCreateAPIView.as_view(), name='vehicles')
]
