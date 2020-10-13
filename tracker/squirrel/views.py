# Create your views here.
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from squirrel.models import Squirrel
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from squirrel.squirrel_operation import SquirrelOperation

squirrel_operation = SquirrelOperation()


def map(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'squirrel/map.html', context)


class IndexView(ListView):
    model = Squirrel
    template_name = 'squirrel/sightings.html'
    context_object_name = 'sightings'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_page = context['page_obj'].number
        context['start'] = (current_page - 1) * 10
        # print('context:',context)
        return context


@csrf_exempt
def squirrel(request, unique_squirrel_id):
    method = request.method

    if method == 'GET':
        squirrel_info = squirrel_operation.get_info(unique_squirrel_id)
        return JsonResponse(squirrel_info)
    else:
        x = request.POST.get('x')
        y = request.POST.get('y')
        unique_squirrel_id = request.POST.get('unique_squirrel_id')
        shift = request.POST.get('shift')
        date = request.POST.get('date')
        age = request.POST.get('age')

        squirrel_operation.update(x, y, unique_squirrel_id, shift, date, age)
        res = {
            'status': 'success',
        }
        return JsonResponse(res)


def stats(request):
    """
    统计数据
    1.按天数统计红松鼠和灰松鼠
    :param request:
    :return:
    """
    squirrels = squirrel_operation.get_all_squirrel()
    squirrel_color_by_day = squirrel_operation.get_squirrel_color_by_day(squirrels)
    return JsonResponse(squirrel_color_by_day)


@csrf_exempt
def squirrel_add(request):
    x = request.POST.get('x')
    y = request.POST.get('y')
    unique_squirrel_id = request.POST.get('unique_squirrel_id')
    shift = request.POST.get('shift')
    date = request.POST.get('date')
    age = request.POST.get('age')
    primary_fur_color = request.POST.get('primary_fur_color')
    location = request.POST.get('location')
    specific_location = request.POST.get('specific_location')
    running = request.POST.get('running')
    chasing = request.POST.get('chasing')
    climbing = request.POST.get('climbing')
    eating = request.POST.get('eating')
    foraging = request.POST.get('foraging')
    other_activities = request.POST.get('other_activities')
    kuks = request.POST.get('kuks')
    moans = request.POST.get('moans')
    tail_flags = request.POST.get('tail_flags')
    tail_twitches = request.POST.get('tail_twitches')
    approaches = request.POST.get('approaches')
    indifferent = request.POST.get('indifferent')
    runs_from = request.POST.get('runs_from')

    squirrel_operation.create(x, y, unique_squirrel_id, shift, date, age, primary_fur_color, location,
                              specific_location, running, chasing, climbing, eating, foraging, other_activities, kuks,
                              moans, tail_flags, tail_twitches, approaches, indifferent, runs_from)
    res = {
        'status': 'success',
    }
    return JsonResponse(res)


def input_data(request):
    base_path = os.getcwd()
    path = os.path.join(base_path, 'data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
    with open(path, 'r') as f:
        lines = f.readlines()
        for index, elements in enumerate(lines):
            if 1 <= index <= 50:
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
