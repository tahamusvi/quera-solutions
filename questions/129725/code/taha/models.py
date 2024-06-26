from django.db import models
from django_jalali.db.models import jDateField, jDateTimeField
from django.utils import timezone
import jdatetime

class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', ('Male')),
        ('F', ('Female')),
    )

    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    national_code = models.CharField(max_length=10)
    birthday_date = jDateField()  # Using JalaliDateField
    ceremony_datetime = jDateTimeField()  # Using JalaliDateTimeField
    country = models.CharField(max_length=100,default='Iran')


    def get_first_and_last_name(self):
        names = {}
        names['first_name'] , names['last_name'] = self.full_name.split(" ")
        return names

    def __str__(self) -> str:
        # return self.get_age()
        return self.username

    def get_age(self):
        today = jdatetime.date.fromgregorian(date=timezone.now().date())
        birth_date = self.birthday_date
        age = today.year - birth_date.year

        if today.month < birth_date.month:
            
            age -= 1
        elif today.month == birth_date.month:
            if today.day <= birth_date.day:
                age -= 1
        if self.is_birthday():
            age += 1 
        return age

    def is_birthday(self):
        today = jdatetime.date.fromgregorian(date=timezone.now().date())
        birth_date = self.birthday_date
        return (today.month, today.day) == (birth_date.month, birth_date.day)



    

