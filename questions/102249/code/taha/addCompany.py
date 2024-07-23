from django.core.management.base import BaseCommand,CommandError
from django.core.validators import validate_email
from career.models import Company
from django.core.exceptions import ValidationError



class Command(BaseCommand):
	help = 'Create a new company'
		
	def handle(self,*args,**options):
		while(True):
			name = input("name: ")
			if not name:
				self.stderr.write("Error: This field cannot be blank.")
			else:
				if len(name)>50:
					self.stderr.write(f"Error: Ensure this value has at most 50 characters (it has {len(name)}).")
				else:
					if Company.objects.filter(name=name).exists():
						self.stderr.write("Error: That name is already taken.")
					else:
						break

		while(True):
			email = input("Email: ")
			if not email:
				self.stderr.write("Error: This field cannot be blank.")
			else:
				try:
					validate_email(email)
					break
				except Exception as x:
					self.stderr.write('Error: Enter a valid email address.')


		while(True):
			phone = input("Phone: ")
			if not phone:
				self.stderr.write("Error: This field cannot be blank.")
			else:
				
				if len(phone) == 11 and phone[0:2]== '09':
					break
				elif len(phone) == 13 and phone[0:3]== '+98':
					break
				elif len(phone) == 14 and phone[0:4]== '0098': 
 					break
				else:
					self.stderr.write("Error: Phone number format is not valid.")

					
							
		description = input("Description: ")

		Company.objects.create(name=name, email=email, phone=phone, description=description if description else None)

		self.stdout.write("Company successfully created!")	