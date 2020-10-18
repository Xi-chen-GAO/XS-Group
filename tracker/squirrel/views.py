# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from squirrel.models import Squirrel
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from squirrel.squirrel_operation import SquirrelOperation

squirrel_operation = SquirrelOperation()


def index(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'squirrel/index.html', context)


def map(request):
    # limit return
    sightings = Squirrel.objects.all()[:100]
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
        try:
            squirrel_operation.update(x, y, unique_squirrel_id, shift, date, age)
            res = {
                'status': 'success',
            }
        except Exception as e:
            print('Error:', e)
            res = {
                'status': 'failed',
            }
        return JsonResponse(res)


def stats(request):
    squirrels = squirrel_operation.get_all_squirrel()
    color_info_list, all_date = squirrel_operation.get_squirrel_color_by_day(squirrels)

    squirrel_operation.get_squirrel_age_by_location(squirrels)
    age_info_list, all_location = squirrel_operation.get_squirrel_age_by_location(squirrels)
    state_info = {
        'color_info_list': color_info_list,
        'all_date': all_date,
        'age_info_list': age_info_list,
        'all_location': all_location,
    }
    return render(request, 'squirrel/statistics.html', state_info)


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

    try:
        squirrel_operation.create(x, y, unique_squirrel_id, shift, date, age, primary_fur_color, location,
                                  specific_location, running, chasing, climbing, eating, foraging, other_activities,
                                  kuks,
                                  moans, tail_flags, tail_twitches, approaches, indifferent, runs_from)
        res = {
            'status': 'success',
        }
    except Exception as e:
        print('Error:', e)
        res = {
            'status': 'failed',
        }
    return JsonResponse(res)
