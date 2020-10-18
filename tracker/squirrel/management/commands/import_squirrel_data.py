import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
from squirrel.utils import CSV_Opertion

csv_operation = CSV_Opertion()


class Parser:
    def get_bool(self, data_str):
        bool_dict = {
            'true': True,
            'false': False,
        }
        return bool_dict.get(data_str, None)

    def get_date(self, date_str):
        try:
            date = datetime.strptime(date_str, "%m%d%Y")
        except Exception as e:
            return None
        return date


parser = Parser()


class Command(BaseCommand):
    help = 'import_squirrel_data'

    def add_arguments(self, parser):
        parser.add_argument('import_squirrel_data', type=str)

    def handle(self, *args, **options):
        path = options.get('import_squirrel_data')
        lines = csv_operation.read(path)
        for index, row in enumerate(lines):
            if index != 0:
                sq_info = row
                create_dict = {
                    "x": sq_info[0],
                    "y": sq_info[1],
                    "unique_squirrel_id": sq_info[2],
                    "hectare": sq_info[3],
                    "shift": sq_info[4],
                    "date": parser.get_date(sq_info[5]),
                    "hectare_squirrel_number": sq_info[6],
                    "age": sq_info[7],
                    "primary_fur_color": sq_info[8],
                    "highlight_fur_color": sq_info[9],
                    "combination_of_primary_and_highlight_color": sq_info[10],
                    "color_notes": sq_info[11],
                    "location": sq_info[12],
                    "above_ground_sighter_measurement": sq_info[13],
                    "specific_location": sq_info[14],
                    "running": parser.get_bool(sq_info[15]),
                    "chasing": parser.get_bool(sq_info[16]),
                    "climbing": parser.get_bool(sq_info[17]),
                    "eating": parser.get_bool(sq_info[18]),
                    "foraging": parser.get_bool(sq_info[19]),
                    "other_activities": sq_info[20],
                    "kuks": parser.get_bool(sq_info[21]),
                    "quaas": parser.get_bool(sq_info[22]),
                    "moans": parser.get_bool(sq_info[23]),
                    "tail_flags": parser.get_bool(sq_info[24]),
                    "tail_twitches": parser.get_bool(sq_info[25]),
                    "approaches": parser.get_bool(sq_info[26]),
                    "indifferent": parser.get_bool(sq_info[27]),
                    "runs_from": parser.get_bool(sq_info[28]),
                    "other_interactions": sq_info[29],
                    "lat_long": sq_info[30],
                }
                s = Squirrel(**create_dict)
                s.save()

        self.stdout.write(self.style.SUCCESS('Successfully input data'))
