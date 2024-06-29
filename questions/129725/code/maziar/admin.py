from Users.models import CustomUser
from django.contrib import admin

#from django_jalali.admin.filters import JDateFieldListFilter
#import django_jalali.admin as jadmin


class CustomUser_admin(admin.ModelAdmin):
   list_display = ['username','first_name','last_name','gender','national_code','birthday_date' ]
   list_filter=['username','full_name']
   search_fields = ['username', 'full_name']
   ordering = ('ceremony_datetime',)

   
   def first_name(self, obj):
        return obj.full_name.split()[0]

   def last_name(self, obj):
        return obj.full_name.split()[-1]


admin.site.register(CustomUser,CustomUser_admin)

