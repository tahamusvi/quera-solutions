
# Question 21210

**Question Title**: Filters and Translation

**Question Link**: [Filters and Translation](https://quera.org/problemset/21210) 

**Difficulty Level**: 🟢

## Question Description
In this question, we are going to give the possibility of Persianizing the figures for a postcard production site.


## Key Points
1. Using filters in templates:
   - You can use filters in Django templates to modify or format data before displaying it.

2. If you use `app-name/templatetags/filters.py` in a template, you must add `{% load filters %}`:
   - If you define custom filters in a file located at `app-name/templatetags/filters.py`, you need to load those filters in the template using the `{% load filters %}` tag.
   
## Filter Function Code
```python
@register.filter(name="num_per")
def replace_per(value):
    for key in numbers:
        value = value.replace(key,numbers[key])
    return value
```

## Status

- **Completed**
