from django import forms
from .models import CustomUser
import re
from django_jalali.forms import widgets



class CustomUserForm(forms.ModelForm):
   # username = forms.CharField(max_length=256)
   # full_name = forms.CharField(max_length=256)
   # gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES)
    national_code = forms.CharField(max_length=10,min_length=10)
   # birthday_date = widgets.jDateInput()
   # ceremony_datetime = widgets.jDateTimeInput()
  #  country = forms.CharField(max_length=100, initial='Iran')

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        parts = full_name.split()
        if len(parts) < 2:
            raise forms.ValidationError("Full name must contain at least first and last name.")
        
        first_name = parts[0].capitalize()
        last_name = ' '.join([part.capitalize() for part in parts[1:]])
        
        if full_name != f"{first_name} {last_name}":
            raise forms.ValidationError("Full name must be in title case format.")
        
        return f"{first_name} {last_name}"

    class Meta:
        model = CustomUser
        fields = '__all__'
        #['username', 'full_name', 'gender', 'national_code', 'birthday_date', 'ceremony_datetime', 'country']











"""
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    def clean_national_code(self):
            national_code = self.cleaned_data['national_code']
            if len(national_code) != 10:
                raise forms.ValidationError("National code invalid")
    
    def clean_full_name(self):
            full_name = self.cleaned_data['full_name']
            words = full_name.split()

            if len(words) != 2:
                raise forms.ValidationError("Full name must include first and last names.")

            for word in words:
                if not re.match("^[A-Z][a-z]+$", word):
                    raise forms.ValidationError("First and last names must be title-cased English words.")

            return full_name
        
"""
