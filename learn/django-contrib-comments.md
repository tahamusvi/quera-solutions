# django-contrib-comments

## Overview
django-contrib-comments is a Django application that provides a way to add comments to any model in your Django project. It allows users to comment on posts, articles, or any other content you have in your web application.

## Installation
1. Install the package using pip:
```
pip install django-contrib-comments
```
2. Add `django.contrib.comments` to your `INSTALLED_APPS` in your Django project's `settings.py` file.
3. Run the initial database migrations:
```
python manage.py migrate
```

## Usage

1. In your Django model that you want to allow comments on, import the `Comment` model from `django.contrib.comments.models` and add a `ForeignKey` field to it:
```python
from django.db import models
from django.contrib.comments.models import Comment

class YourModel(models.Model):
    # your model fields
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='your_model_comments', null=True, blank=True)
```


2. In your Django view, use the `get_comment_list()` function from `django.contrib.comments.models` to retrieve the comments for a specific object:
```python
def menu_view(request):
    foods = Food.objects.all()
    comments_count = Comment.objects.all().count()
    try:
        c = int(request.GET.get('c'))
    except (ValueError, TypeError):
        c = -1

    if c == comments_count:
        messages.success(request, 'your comment successfully submitted.')
        return redirect('menu')
    return render(request, 'order_food/menu.html', {
        'foods': foods,
    })
```
3. In your Django template, you can display the comments using a loop:
```html
{% for food in foods %}
        <li>
            {{ food.name }}
            <ul>
                <li>{{ food.price }}</li>
                <li>{{ food.description }}</li>
            </ul>
            {% render_comment_list for food %}
            
            
            {% if user.is_authenticated %}
                {% get_comment_form for food as form %}
                    <form action="{% comment_form_target %}" method="POST">
                        {% csrf_token %}
                        {{ form.comment }}
                        {{ form.content_type }}
                        {{ form.object_pk }}
                        {{ form.timestamp }}
                        {{ form.security_hash }}
                        <input type="hidden" name="next" value="{% url 'menu'  %}" />
                        <input type="submit" value="Add comment" id="id_submit" />
                    </form>
            {% else %}
                <p>Please log in to leave a comment.</p>
            {% endif %}
        </li>
    {% endfor %}
```

## Configuration
You can customize the behavior of django-contrib-comments by setting various options in your Django project's `settings.py` file. For example, you can set the maximum number of comments to display, enable/disable comment moderation, and more.

Please refer to the [django-contrib-comments documentation](https://django-contrib-comments.readthedocs.io/en/latest/) for more information on configuration and advanced usage.