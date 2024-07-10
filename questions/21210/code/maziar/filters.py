# Put you code here
from django import template


register = template.Library()


  
@register.filter(name='persian_int')
def persian_int(english_int):
    persian_nums = {'0':'۰', '1':'۱', '2':'۲', '3':'۳', '4':'۴', '5':'۵', '6':'۶', '7':'۷', '8':'۸', '9':'۹'}
    number = str(english_int)  #well it is going throw the whole string, i think it could be better at performance , 
    # and maybe there is no need to convert it to str!
    persian_dict = number.maketrans(persian_nums)
    result = number.translate(persian_dict)
    return result
