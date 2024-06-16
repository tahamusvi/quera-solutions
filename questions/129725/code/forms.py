from django import forms
from .models import CustomUser
import re

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
        
