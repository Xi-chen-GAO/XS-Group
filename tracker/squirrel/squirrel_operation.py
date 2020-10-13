from squirrel.models import Squirrel
from django.forms.models import model_to_dict


class SquirrelOperation:
    def __int__(self):
        pass

    def _get_squirrel_by_unique_id(self, unique_id):
        squirrel = Squirrel.objects.filter(unique_squirrel_id=unique_id).first()
        return squirrel

    def _is_date_legal(self, date):
        if date and len(date) == 8:
            return True
        else:
            return False

    def _is_color_legal(self, color):
        if color and color != "":
            return True
        else:
            return False

    def get_all_squirrel(self):
        sqs = Squirrel.objects.all()
        return sqs

    def get_squirrel_color_by_day(self, squirrels):
        stats_info = {}
        for s in squirrels:
            date = s.date
            primary_fur_color = s.primary_fur_color
            if self._is_date_legal(date) and self._is_color_legal(primary_fur_color):
                stats_info.setdefault(date, {})
                stats_info[date].setdefault(primary_fur_color, 0)
                stats_info[date][primary_fur_color] += 1
        return stats_info

    def get_info(self, unique_id):
        squirrel = self._get_squirrel_by_unique_id(unique_id)
        if not squirrel:
            return {}
        else:
            return model_to_dict(squirrel)

    def update(self, x, y, unique_squirrel_id, shift, date, age):
        squirrel = self._get_squirrel_by_unique_id(unique_squirrel_id)
        if squirrel:
            squirrel.x = x
            squirrel.y = y
            squirrel.unique_squirrel_id = unique_squirrel_id
            squirrel.shift = shift
            squirrel.date = date
            squirrel.age = age
            squirrel.save()

    def create(self, x, y, unique_squirrel_id, shift, date, age, primary_fur_color, location, specific_location,
               running, chasing, climbing, eating, foraging, other_activities, kuks, moans, tail_flags, tail_twitches,
               approaches, indifferent, runs_from):
        squirrel = Squirrel()
        squirrel.x = x
        squirrel.y = y
        squirrel.unique_squirrel_id = unique_squirrel_id
        squirrel.shift = shift
        squirrel.date = date
        squirrel.age = age
        squirrel.primary_fur_color = primary_fur_color
        squirrel.location = location
        squirrel.specific_location = specific_location
        squirrel.running = running
        squirrel.chasing = chasing
        squirrel.climbing = climbing
        squirrel.eating = eating
        squirrel.foraging = foraging
        squirrel.other_activities = other_activities
        squirrel.kuks = kuks
        squirrel.moans = moans
        squirrel.tail_flags = tail_flags
        squirrel.tail_twitches = tail_twitches
        squirrel.approaches = approaches
        squirrel.indifferent = indifferent
        squirrel.runs_from = runs_from
        squirrel.save()
