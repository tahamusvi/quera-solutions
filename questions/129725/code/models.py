from django.db import models
from datetime import datetime, date
from django_jalali.db import models as jmodels
from jdatetime import datetime as jdatetime


class CustomUser(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) # a solution to differentiate what the user sees and what actaually is saved to database
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField()
    ceremony_datetime = jmodels.jDateTimeField()
    country = models.CharField(max_length=10,default='Iran')


    class Meta:
        ordering= ['-ceremony_datetime']

    def get_first_and_last_name(self):
        words = self.full_name.split()  # Split the full name into a list of words
        first_name = words[0]  # The first word is the first name
        last_name = words[-1]  # The last word is the last name
        result = {"first_name": first_name, "last_name": last_name}
        return result
    
    def get_age(self):
        current_date = jdatetime.now()  # dont forgert the imports and b the way its a nice syntax!
        age = current_date.year - self.birthday_date.year - ((current_date.month, current_date.day) < (self.birthday_date.month, self.birthday_date.day))

        return age
    

    
    def is_birthday(self):
        current_date = jdatetime.now()
        birth_date = self.birthday_date
        if birth_date and (current_date.day == birth_date.day) and (current_date.month == birth_date.month):
            return True
        return False


