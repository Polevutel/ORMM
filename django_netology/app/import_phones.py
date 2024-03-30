import csv
from django.core.management.base import BaseCommand
from your_app_name.models import Phone

class Command(BaseCommand):
    help = 'Import phone data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phone = Phone(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists']
                )
                phone.save()

        self.stdout.write(self.style.SUCCESS('Phone data imported successfully'))
