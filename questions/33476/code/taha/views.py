from django.shortcuts import render
from order_food.models import *
from django_comments.models import Comment
from django.shortcuts import render,redirect
from django.contrib import messages

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