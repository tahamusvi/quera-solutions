from django.core.management.base import BaseCommand,CommandError
from django.core.management import CommandParser
from career.models import Company
import argparse
from django.core.validators import validate_email


class Command(BaseCommand):
    help = 'Edit company information'
    def add_arguments(self, parser):
      #  parser = CommandParser(parser)

                # Positional argument: company name
        parser.add_argument('company_name', type=str)

                # Optional arguments
        parser.add_argument('--description', type=str)
        parser.add_argument('--phone', type=str)
        parser.add_argument('--email', type=str)
        parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
            company_name = options['company_name']
            description = options['description']
            phone = options['phone']
            email = options['email']
            name = options['name']

            try:
                company = Company.objects.get(name=company_name)
            except Company.DoesNotExist:
                raise CommandError("Company matching query does not exist.")
                
        
            if name:
                if len(name)>50:
                    raise CommandError(f'Error: Ensure this value has at most 50 characters (it has{len(name)}).')
                if Company.objects.filter(name=name).exists():
                    raise CommandError(f'Error: That name is already taken.')
                company.name = name
            else:
                raise CommandError("Name cannot be blank.")          




            if email:
                try:
                    validate_email(email)
                    company.email = email
                except Exception as e:
                    raise CommandError('Error: Enter a valid email address.')
            else:
                raise CommandError("Email cannot be blank.")               

         
            
            if phone:
                if len(phone) ==11:
                    if phone[:2] != '09':
                        raise CommandError("Error: Phone number format is not valid.")
                
                elif len(phone)==13:
                    if phone[:3] != '+98':
                        raise CommandError("Error: Phone number format is not valid.")
                
                elif len(phone)==14:
                    if phone[:4] != '0098':
                        raise CommandError("Error: Phone number format is not valid.")
                

                else:
                    raise CommandError("Error: Phone number format is not valid.")
            else:
                raise CommandError("Phone cannot be blank.")               


            
            if description:
                if len(description) > 200:
                    raise CommandError('Description should not exceed 200 characters.')
                else:
                    company.description = description    
                

            Company.objects.create(name=name, email=email, phone=phone, description=description if description else '')
           

            print(f'Company {company.name} has been updated.')
