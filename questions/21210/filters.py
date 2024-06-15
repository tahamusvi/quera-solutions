from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

numbers = {
    '1' : '۱',
    '2' : '۲',
    '3' : '۳',
    '4' : '۴',
    '5' : '۵',
    '6' : '۶',
    '7' : '۷',
    '8' : '۸',
    '9' : '۹',
    '0' : '۰',
}

@register.filter(name="num_per")
def replace_per(value):
    for key in numbers:
        value = value.replace(key,numbers[key])
    return value