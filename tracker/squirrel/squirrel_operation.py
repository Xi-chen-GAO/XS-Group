from squirrel.models import Squirrel
from django.forms.models import model_to_dict


class SquirrelOperation:
    def __int__(self):
        pass

    def _get_squirrel_by_unique_id(self, unique_id):
        squirrel = Squirrel.objects.filter(unique_squirrel_id=unique_id).first()
        return squirrel

    def _is_date_legal(self, date):
        if date:
            return True
        else:
            return False

    def _is_color_legal(self, color):
        if color and color != "":
            return True
        else:
            return False

    def _is_age_legal(self, age):
        if age and age != "":
            return True
        else:
            return False

    def _is_location_legal(self, location):
        if location and location != "":
            return True
        else:
            return False

    def get_all_squirrel(self):
        sqs = Squirrel.objects.all()
        return sqs

    def get_squirrel_color_by_day(self, squirrels):
        stats_info = {}
        all_date = []
        all_color = []
        for s in squirrels:
            date = s.date
            primary_fur_color = s.primary_fur_color
            if self._is_date_legal(date) and self._is_color_legal(primary_fur_color):
                date_str = str(date)
                all_date.append(date)
                all_color.append(primary_fur_color)
                stats_info.setdefault(date_str, {})
                stats_info[date_str].setdefault(primary_fur_color, 0)
                stats_info[date_str][primary_fur_color] += 1
        # 去重+排序
        all_date = sorted(list(set(all_date)))
        all_date = [str(n) for n in all_date]
        all_color = set(all_color)

        color_info_list = []
        for color in all_color:
            color_datas = []
            for date in all_date:
                data = stats_info[date].get(color, 0)
                color_datas.append(data)
            color_info = {
                'name': color,
                'type': 'bar',
                'barGap': 0,
                'data': color_datas,
            }
            color_info_list.append(color_info)

        return color_info_list, all_date

    def get_squirrel_age_by_location(self, squirrels):
        stats_info = {}
        all_age = []
        all_location = []
        for s in squirrels:
            age = s.age
            location = s.location
            if self._is_age_legal(age) and self._is_location_legal(location):
                all_age.append(age)
                all_location.append(location)
                stats_info.setdefault(location, {})
                stats_info[location].setdefault(age, 0)
                stats_info[location][age] += 1

        all_age = set(all_age)
        all_location = list(set(all_location))
        age_info_list = []
        for age in all_age:
            age_info = {
                'name': age,
                'type': 'bar',
                'stack': '总量',
                'label': {
                    'show': 'true',
                    'position': 'insideRight'
                },
                'data': []
            }
            for location in all_location:
                data = stats_info[location].get(age, 0)
                age_info['data'].append(data)
            age_info_list.append(age_info)
        # all_location = list(set(location))
        # all_age = set(all_age)
        #
        # color_info_list = []
        # for location in all_location:
        #     color_datas = []
        #     for date in all_date:
        #         data = stats_info[date].get(color, 0)
        #         color_datas.append(data)
        #     color_info = {
        #         'name': color,
        #         'type': 'bar',
        #         'barGap': 0,
        #         'label': 'labelOption',
        #         'data': color_datas,
        #     }
        #     color_info_list.append(color_info)

        return age_info_list, all_location

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
