from django.core.management.base import BaseCommand, CommandError
from career.models import Company

class Command(BaseCommand):
    
    def handle(self,*args,**options):
        companies = Company.objects.all()

        with open('company.csv','w') as file:
            # file.write('Name,Email,Phone\n')
            for c in companies:
                file.write(f"{c.name},{c.email},{c.phone}\n")
