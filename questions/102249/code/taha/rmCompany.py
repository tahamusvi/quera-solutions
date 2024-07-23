from django.core.management.base import BaseCommand, CommandError
from career.models import Company


class Command(BaseCommand):
    help = 'delete company'

    def add_arguments(self, parser):

        parser.add_argument('company_names', type=str,nargs='*')

        parser.add_argument('--all', action='store_true', help='Delete all companies')

    def handle(self, *args, **options):

        if options['all']:
            for company in Company.objects.all():
                company.delete()
        
        else:
            for company_name in options['company_names']:
                try:
                    company = Company.objects.get(name=company_name)
                    company.delete()
                except Company.DoesNotExist:
                    self.stderr.write(f"{company_name} matching query does not exist.")
