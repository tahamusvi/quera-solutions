## Introduction to `django_jalali`

The `django_jalali` library is a Django-specific package that provides support for Jalali (Persian) date and datetime fields. Jalali calendar is the official calendar system used in Iran and some other countries in the region.

By using `django_jalali`, you can easily work with Jalali dates and datetimes in your Django models, forms, and templates, without having to worry about the conversion between Gregorian and Jalali calendars.

## Installation and Configuration

1. **Install the library**:
   You can install the `django_jalali` library using pip:
   ```
   pip install django-jalali
   ```

2. **Add to Django settings**:
   In your Django project's `settings.py` file, add `django_jalali` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       # Other apps...
       'django_jalali',
   ]
   ```

3. **Configure the timezone**:
   Make sure that the `TIME_ZONE` setting in your Django project's `settings.py` file is set to the appropriate timezone. For example, for Iran, you would set it to:
   ```python
   TIME_ZONE = 'Asia/Tehran'
   ```

## Using Jalali Date and Datetime Fields

1. **Define Jalali fields in your models**:
   In your Django models, you can use the `jDateField` and `jDateTimeField` provided by the `django_jalali.db.models` module to define Jalali date and datetime fields, respectively:
   ```python
   from django.db import models
   from django_jalali.db.models import jDateField, jDateTimeField

   class MyModel(models.Model):
       jalali_date = jDateField()
       jalali_datetime = jDateTimeField()
   ```

2. **Work with Jalali data in your code**:
   When working with Jalali date and datetime fields, you can use the `jdatetime` module provided by the `django_jalali` library. This module provides a Jalali-aware version of the standard Python `datetime` module, allowing you to seamlessly work with Jalali dates and times.
   ```python
   import jdatetime

   # Create a Jalali date
   jalali_date = jdatetime.date(1401, 4, 5)

   # Create a Jalali datetime
   jalali_datetime = jdatetime.datetime(1401, 4, 5, 10, 30, 0)
   ```

3. **Display Jalali data in templates**:
   In your Django templates, you can use the `|jalali` filter provided by the `django_jalali` library to format Jalali date and datetime values:
   ```html
   {{ my_object.jalali_date|jalali }}
   {{ my_object.jalali_datetime|jalali }}
   ```

4. **Handle Jalali data in forms**:
   When working with Jalali date and datetime fields in Django forms, the `django_jalali` library automatically handles the conversion between Gregorian and Jalali calendars, making it seamless for the user.

By using the `django_jalali` library, you can easily integrate Jalali date and datetime functionality into your Django applications, providing a better user experience for users in Jalali calendar-based regions.