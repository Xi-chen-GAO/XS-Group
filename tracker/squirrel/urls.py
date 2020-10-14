from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.map, name='map'),
    path('sightings', views.IndexView.as_view(), name='sightings'),
    path('sightings/add', views.squirrel_add, name='squirrel_add'),
    path('sightings/stats', views.stats, name='stats'),
    path('sightings/<unique_squirrel_id>', views.squirrel, name='squirrel'),
]