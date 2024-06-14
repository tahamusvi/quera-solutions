from django import forms
from django.forms import ModelForm
from .models import Product,Category
from django.core.exceptions import ValidationError



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price > 1000:
            raise ValidationError("Product is too expensive")
        return price

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) <= 20:
            raise ValidationError("Product must have a good description")
        return description


