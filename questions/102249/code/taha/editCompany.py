from django.core.management.base import BaseCommand,CommandError
from django.core.management import CommandParser
from career.models import Company
import argparse
from django.core.validators import validate_email


class Command(BaseCommand):
    help = 'Edit company information'

    def add_arguments(self, parser):

        parser.add_argument('company_name', type=str)

        parser.add_argument('--description', type=str)
        parser.add_argument('--phone', type=str)
        parser.add_argument('--email', type=str)
        parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
            company_name = options['company_name']
            description = options['description']
            
            if 'name' in options:
                name = options['name'] 
            else:
                name = None 

            if 'phone' in options:
                phone = options['phone'] 
            else:
                phone = None 

            if 'email' in options:
                email = options['email']
            else:
                email = None 

            try:
                company = Company.objects.get(name=company_name)
            except Company.DoesNotExist:
                raise CommandError("Company matching query does not exist.")
            
            if name == '':
                raise CommandError("Name cannot be blank.")         

            if email == '':
                raise CommandError("Email cannot be blank.")  
            
            if phone == '':
                raise CommandError("Phone cannot be blank.")  

            if name:
                if len(name)>50:
                    raise CommandError(f'Error: Ensure this value has at most 50 characters (it has {len(name)}).')
                if Company.objects.filter(name=name).exists():
                    raise CommandError(f'Error: That name is already taken.')
                company.name = name
                     
            if email:
                try:
                    validate_email(email)
                    company.email = email
                except Exception as e:
                    raise CommandError('Error: Enter a valid email address.')

            if phone:
                if len(phone) == 11 and phone[:2] == '09':
                    company.phone = phone
                
                elif len(phone)==13 and phone[:3] == '+98':
                    company.phone = phone

                elif len(phone)==14 and phone[:4] == '0098':
                    company.phone = phone

                else:
                    raise CommandError("Error: Phone number format is not valid.")

            if description:
                if len(description) > 200:
                    raise CommandError('Description should not exceed 200 characters.')
                if description == '':
                   pass
                else:
                    company.description = description    
                


            company.save()