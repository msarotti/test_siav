import json
from django.core.management.base import BaseCommand
from library.utils import import_books_from_json


class Command(BaseCommand):
    help = 'Import books from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_file',
            type=str,
            help='Path to the JSON file'
        )

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)

        import_books_from_json(data)
        self.stdout.write(self.style.SUCCESS('Books imported successfully'))
