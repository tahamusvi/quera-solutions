from django.core.management.base import BaseCommand
import csv
from pathlib import Path
from career.models import Company  # Assuming the model is in the same app


class Command(BaseCommand):
   help = 'Export company data to a CSV file'
   def handle(self,*args,**options):
      file_path=Path('company.csv')
      with open(file_path,'w',newline='') as csv_file:
         writer=csv.writer(csv_file)
         field_names = ['name', 'email', 'phone']
         writer.writerow(field_names)

         companies = Company.objects.all()
         for company in companies:
            row = [company.name,company.email,company.phone]
            writer.writerow(row)
      #print(f'{len(companies)} companies exported to {file_path}')
      
      
