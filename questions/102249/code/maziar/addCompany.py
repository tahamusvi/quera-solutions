from django.core.management.base import BaseCommand,CommandError
from django.core.validators import validate_email
from career.models import Company
from django.core.exceptions import ValidationError



class Command(BaseCommand):
	help = 'Create a new company'

	# def add_arguments(self,parser):
	# 	parser.add_argument("phone",type=str)
	# 	parser.add_argument("email",type=str)
	# 	parser.add_argument("name",type=str)
	# 	parser.add_argument("description",type=str,nargs='?')
		

	def handle(self,*args,**options):
			# description = options.get('description') if options.get('description') else None
			# name = options.get('name')
			# phone = options.get('phone')
			# email=options.get('email')
			while(True):
				name=input("name: ")
				cnt1=0
				if not name:
					error_msg = "Error: This field cannot be blank."
					self.stderr.write(error_msg)
				else:
					cnt1+=1

				if len(name)>50:
						error_msg=f"Error: Ensure this value has at most 50 characters (it has {len(name)})."
						self.stderr.write(error_msg)


				else:
					cnt1+=1
					
				
						# Validate if the company name is unique
				if Company.objects.filter(name=name).exists():
								error_msg="Error: That name is already taken."
								self.stderr.write(error_msg)
				else:
					cnt1+=1

				if cnt1==3:
						break

			while(True):

				email=input("Email: ")
				if not email:
					error_msg = "Error: This field cannot be blank."
					self.stderr.write(error_msg)
				else:	
					try: 
						validate_email(email)
						break
					except ValidationError:
						error_msg=('Error: Enter a valid email address.')
						self.stderr.write(error_msg)	 

			while(True):
				phone=input("Phone: ")
				
				if not phone:
					error_msg = "Error: This field cannot be blank."
					self.stderr.write(error_msg)	  
				else:	
					if len(phone) ==11:
						if phone[:2] != '09':
							error_msg=('Error: Phone number format is not valid.')
							self.stderr.write(error_msg)
						else:
							break
					elif len(phone)==13:
						if phone[:4] != '+989':
							error_msg=('Error: Phone number format is not valid.')
							self.stderr.write(error_msg)
						else:
							break
					
					elif len(phone)==14:
						if phone[:5] != '00989':
							error_msg=('Error: Phone number format is not valid.')
							self.stderr.write(error_msg)
						else:
							break

					else:
							error_msg=('Error: Phone number format is not valid.')
							self.stderr.write(error_msg)
								
			description=input("Description: ")
				#at first i was like i can leave this field if the user doesnt give anything for it turns out i need to say description=None otherwise my answer will be wrong

			Company.objects.create(name=name, email=email, phone=phone, description=description if description else None)
			self.stdout.write("Company successfully created!")	
