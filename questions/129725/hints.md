
# Question 129725

**Question Title**: Jalali calender and Mr.Jalal

**Question Link**: [Jalali calender and Mr.Jalal](https://quera.org/problemset/129725) 

**Difficulty Level**: 🟠
## Question Description
The main focus of the project is on useing Shamsi or jalali(potato potato ...) in Django, but there are some more challenges defining the models and writing functions to query and calculate some data. the last challenge is to build a nice interface for admin panel . 

## Approach
- its neccesary to use jalali library to be able to use Shamsi calender inb django.
In the end a fresh mind is needed to complete the forms and models.
I didnt really know how to write the code for data validation in forms classes!
Converting the fullname into firstname and lastname only in the admin panel was new lesson.
I liked my approach to make a difference between what user sees and what is beingsaved to database

## Key Points
- using jalali library, learing to write function within forms or admin or in models and being aware of how they really work
- Attention to detail and probability of each situation

## Sample Code
- convert georgian to shamsi
```python
    today = jdatetime.date.fromgregorian(date=timezone.now().date())
```
- using in model

```python
    from django_jalali.db.models import jDateField, jDateTimeField

    birthday_date = jDateField() 
    ceremony_datetime = jDateTimeField()  
```


## Status

- **Completed**

## Learning

- [django_jalali](./../../learn/django_jalali.md) 