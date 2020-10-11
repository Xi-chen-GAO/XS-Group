from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from squirrel.models import Squirrel


def map(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'squirrel/map.html', context)


def input_data(request):
    path = r'/Users/zhaoyuwen/waibao/XS-Group/tracker/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
    with open(path, 'r') as f:
        lines = f.readlines()
        for index, elements in enumerate(lines):
            if index == 1:
                sq_info = elements.split(",")
                create_dict = {
                    "x": sq_info[0],
                    "y": sq_info[1],
                    "unique_squirrel_id": sq_info[2],
                    "hectare": sq_info[3],
                    "shift": sq_info[4],
                    "date": sq_info[5],
                    "hectare_squirrel_number": sq_info[6],
                    "age": sq_info[7],
                    "primary_fur_color": sq_info[8],
                    "highlight_fur_color": sq_info[9],
                    "combination_of_primary_and_highlight_color": sq_info[10],
                    "color_notes": sq_info[11],
                    "location": sq_info[12],
                    "above_ground_sighter_measurement": sq_info[13],
                    "specific_location": sq_info[14],
                    "running": sq_info[15],
                    "chasing": sq_info[16],
                    "climbing": sq_info[17],
                    "eating": sq_info[18],
                    "foraging": sq_info[19],
                    "other_activities": sq_info[20],
                    "kuks": sq_info[21],
                    "quaas": sq_info[22],
                    "moans": sq_info[23],
                    "tail_flags": sq_info[24],
                    "tail_twitches": sq_info[25],
                    "approaches": sq_info[26],
                    "indifferent": sq_info[27],
                    "runs_from": sq_info[28],
                    "other_interactions": sq_info[29],
                    "lat_long": sq_info[30],
                }
                s = Squirrel(**create_dict)
                s.save()
    return HttpResponse("input success")
