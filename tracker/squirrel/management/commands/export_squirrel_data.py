import csv
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
            lat_long = "POINT ({} {})".format(sq.x, sq.y)
            line = [sq.x, sq.y, sq.unique_squirrel_id, sq.hectare, sq.shift, sq.date, sq.hectare_squirrel_number,
                    sq.age, sq.primary_fur_color, sq.highlight_fur_color, sq.combination_of_primary_and_highlight_color,
                    sq.color_notes, sq.location, sq.above_ground_sighter_measurement, sq.specific_location, sq.running,
                    sq.chasing, sq.climbing, sq.eating, sq.foraging, sq.other_activities, sq.kuks, sq.quaas, sq.moans,
                    sq.tail_flags, sq.tail_twitches, sq.approaches, sq.indifferent, sq.runs_from, sq.other_interactions,
                    lat_long]
            line_list.append(line)
        return line_list
