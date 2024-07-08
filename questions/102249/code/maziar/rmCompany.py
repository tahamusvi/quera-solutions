from django.core.management.base import BaseCommand, CommandError
from career.models import Company
import sys
from django.core.management import CommandParser


class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('names', nargs='*', type=str)
        parser.add_argument('--all', action='store_true', help='Remove all companies')



    def handle(self,*args,**options):
         names = options['names']
         remove_all = options['all']

         if remove_all:
            Company.objects.all().delete()

         for name in names:
             if Company.objects.filter(name=name).exists():
                 Company.objects.get(name=name).delete()
             else:
                 error_msg= f"{name} matching query does not exist."
                 self.stderr.write(error_msg)    
                 