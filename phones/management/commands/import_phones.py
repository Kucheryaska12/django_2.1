import csv
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        for phone in phones:
            try:
                Phone.objects.create(name=phone['name'],
                                 price=phone['price'],
                                 image=phone['image'],
                                 release_date=phone['release_date'],
                                 lte_exists=phone['lte_exists']
                                 )
            except IntegrityError:
                pass
