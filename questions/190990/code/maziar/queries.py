from .models import Employee,Product,Company,Order,Customer
from django.db.models import Avg,Sum,Q
from django.db.models import Count
import datetime
from django.utils import timezone
from datetime import timedelta, date

def young_employees(job: str):
   y_employess= Employee.objects.filter(job=job,age__lt=30)
   return y_employess


def cheap_products():
    # The ['price__avg'] part in the code is used to access the result of the aggregate 
    # function. Let's break it down further:
    # Product.objects.aggregate(Avg('price')): This part calculates the average of the price field 
    # for all the objects in the Product model. The aggregate() function returns a dictionary with 
    # the results of the aggregate functions applied to the queryset.
    # ['price__avg']: The result of the aggregate function is stored in a dictionary where the key 
    # is formed by combining the field name (price) and the aggregate function used (__avg), 
    # separated by a double underscore (__). So, the key price__avg refers to the average of the price field.
    average_price = Product.objects.aggregate(Avg('price'))['price__avg']

    products_below_avg=Product.objects.filter(price__lt=average_price).values_list('name',flat=True).order_by('price')
    return products_below_avg

# what is the difference between values() and list_values?
# In Django, both values() and values_list() are methods used for retrieving specific fields
#    from a queryset, but they have some differences in their behavior and the format of the
# data they return.
# values():
# values() returns a list of dictionaries, where each dictionary represents an object from
# the queryset and contains the specified fields as key-value pairs.
# Example:
# Python
# Copy
# products = Product.objects.values('name', 'price')
# This will return a queryset containing dictionaries like this:
# Python
# Copy
# [
#     {'name': 'Product 1', 'price': 10},
#     {'name': 'Product 2', 'price': 20},
#     ...
# ]
# values_list():
# values_list() returns a list of tuples, where each tuple represents an object from the
# queryset and contains the specified fields' values.
# By default, values_list() returns a list of tuples with the same length as the number of 
# fields specified in the values_list() method. If you set the flat parameter to True, it will
# return a single flat list containing the values of the specified fields.
# Example:
# Python
# Copy
# products = Product.objects.values_list('name', 'price')
# This will return a queryset containing tuples like this:
# Python
# Copy
# [
#     ('Product 1', 10),
#     ('Product 2', 20),
#     ...
# ]
# If you use flat=True:
# Python
# Copy
# products = Product.objects.values_list('name', 'price', flat=True)
# This will return a flat list like this:
# Python
# Copy
# ['Product 1', 10, 'Product 2', 20, ...]
# In summary, values() returns dictionaries with key-value pairs for the specified fields,
#  while values_list() returns a list of tuples (or a flat list if flat=True) containing the 
#  values of the specified fields. The choice between the two depends on the desired data
#  structure for further processing or displaying in your Django templates.

def products_sold_by_companies():

    companies_with_sold_products = Company.objects.annotate(
        sold_products_count=Sum('product__sold')
        # i dont understant why cant we use product_set__sold
    ).values_list('name', 'sold_products_count')
    return companies_with_sold_products


def sum_of_income(start_date: str, end_date: str):
    s_income=Order.objects.filter(time__lt=end_date,time__gt=start_date).aggregate(Sum('price'))['price__sum']
    return s_income


# def sum_of_income(start_date: str, end_date: str) -> dict:
#     s_income = Order.objects.filter(time__range=[start_date, end_date]).aggregate(total_income=Sum('price'))
#     return {'total_income': s_income['total_income']}

def good_customers():
    # Calculate the date one month ago from now
    one_month_ago = timezone.now() - timedelta(days=30)
    # Queryset to get customers with more than 10 orders in the last month
    result = (
        Customer.objects
        .annotate(order_count=Count('order', filter=Q(order__time__gte=one_month_ago)))
        .filter(order_count__gt=10)
        .values_list('name', 'phone')
    )
    return list(result)
def nonprofitable_companies():
      # Filter products that have been sold less than 100 times
    low_sales_products = Product.objects.annotate(sold_count=Count('order')).filter(sold_count__lt=100)
    
    # Filter companies with at least 4 products that have low sales
    low_sales_company_names = (
        Company.objects.filter(product__in=low_sales_products)
        .annotate(low_sales_product_count=Count('product'))
        .filter(low_sales_product_count__gte=4)
        .values_list('name', flat=True)
    )

    return list(low_sales_company_names)