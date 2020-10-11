from django.urls import path

from . import views

urlpatterns = [
    path('map', views.map, name='map'),
    path('sightings', views.sightings, name='sightings'),
    path('input_data', views.input_data, name='input_data'),
]