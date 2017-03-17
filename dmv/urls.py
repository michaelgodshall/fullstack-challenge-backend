from django.conf.urls import url
from dmv import views


urlpatterns = [
    url(r'^households$', views.HouseholdListCreateAPIView.as_view(), name='households'),
    url(r'^households/(?P<pk>\d+)$', views.HouseholdRetrieveUpdateDestroyAPIView.as_view(), name='household'),
    url(r'^persons$', views.PersonListCreateAPIView.as_view(), name='persons'),
    url(r'^persons/(?P<pk>\d+)$', views.PersonRetrieveUpdateDestroyAPIView.as_view(), name='person'),
    url(r'^vehicles$', views.VehicleListCreateAPIView.as_view(), name='vehicles'),
    url(r'^vehicles/(?P<pk>\d+)$', views.VehicleRetrieveUpdateDestroyAPIView.as_view(), name='vehicle'),
]
