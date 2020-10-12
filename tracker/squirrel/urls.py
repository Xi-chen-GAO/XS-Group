from django.urls import path

from . import views

urlpatterns = [
    path('map', views.map, name='map'),
    # path('sightings', views.sightings, name='sightings'),
    path('sightings', views.IndexView.as_view(), name='sightings'),
    path('sightings/add', views.squirrel_add, name='squirrel_add'),
    path('sightings/<unique_squirrel_id>', views.squirrel, name='squirrel'),
    path('input_data', views.input_data, name='input_data'),
]