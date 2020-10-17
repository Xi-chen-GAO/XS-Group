import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel


class Command(BaseCommand):
    help = 'export_squirrel_data'

    def add_arguments(self, parser):
        parser.add_argument('export_squirrel_data', type=str)

    def handle(self, *args, **options):
        path = options.get('export_squirrel_data')

        data = self.get_lines()
        f = open(path, 'w')
        writer = csv.writer(f)
        for i in data:
            writer.writerow(i)
        f.close()

        self.stdout.write(self.style.SUCCESS('Successfully output data'))

    def get_lines(self):
        sqs = Squirrel.objects.all()
        title = ['X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date', 'Hectare Squirrel Number', 'Age',
                 'Primary Fur Color', 'Highlight Fur Color', 'Combination of Primary and Highlight Color',
                 'Color notes', 'Location', 'Above Ground Sighter Measurement', 'Specific Location', 'Running',
                 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans',
                 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from', 'Other Interactions',
                 'Lat/Long', ]
        line_list = [title]
        for sq in sqs:
            line = []
            line.append(sq.x)
            line.append(sq.y)
            line.append(sq.unique_squirrel_id)
            line.append(sq.hectare)
            line.append(sq.shift)
            line.append(sq.date)
            line.append(sq.hectare_squirrel_number)
            line.append(sq.age)
            line.append(sq.primary_fur_color)
            line.append(sq.highlight_fur_color)
            line.append(sq.combination_of_primary_and_highlight_color)
            line.append(sq.color_notes)
            line.append(sq.location)
            line.append(sq.above_ground_sighter_measurement)
            line.append(sq.specific_location)
            line.append(sq.running)
            line.append(sq.chasing)
            line.append(sq.climbing)
            line.append(sq.eating)
            line.append(sq.foraging)
            line.append(sq.other_activities)
            line.append(sq.kuks)
            line.append(sq.quaas)
            line.append(sq.moans)
            line.append(sq.tail_flags)
            line.append(sq.tail_twitches)
            line.append(sq.approaches)
            line.append(sq.indifferent)
            line.append(sq.runs_from)
            line.append(sq.other_interactions)
            lat_long = "POINT ({} {})".format(sq.x, sq.y)
            line.append(lat_long)
            line_list.append(line)
        return line_list
