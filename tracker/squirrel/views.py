from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def map(request):
    # return HttpResponse("Hello, world. map")
    context = {
        'sightings': [{
            'latitude': 40.782091,
            'longitude': -73.964285,
        }]
    }
    return render(request, 'squirrel/map.html', context)
