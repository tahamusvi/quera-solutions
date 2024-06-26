from django.contrib import admin
from django.db.models import F
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date']
    search_fields = ['username', 'full_name',]
    ordering = ['ceremony_datetime']

    def first_name(self, obj):
        return obj.full_name.split()[0] if obj.full_name else ''
    first_name.short_description = 'First Name'

    def last_name(self, obj):
        parts = obj.full_name.split()
        return ' '.join(parts[1:]) if len(parts) > 1 else ''
    last_name.short_description = 'Last Name'

admin.site.register(CustomUser, CustomUserAdmin)
