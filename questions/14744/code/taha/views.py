from django.shortcuts import render,get_object_or_404
from .models import Book,Borrowing
from django.http import JsonResponse
from django.contrib.auth.models import User

def get_book_users(request,pk):
    book = get_object_or_404(Book,pk=pk)
    history = Borrowing.objects.filter(book=book)

    data = [
    ]

    for record in history:
        temp = {}
        temp["username"] = record.user.username
        temp["date"] = record.date
        data.append(temp)

    return JsonResponse(data, safe=False)


def borrow_book(request,book_id,user_name):
    status_code = 0
    try:
        user = User.objects.get(username=user_name)
        
    except User.DoesNotExist:
        status_code = 3
    


    try:
        book = Book.objects.get(pk=book_id)
        if book.user_borrowed is not None:
            return JsonResponse({ "status": 1, })
    except Book.DoesNotExist:
        status_code = 3

    
    
    if status_code == 0:
        user_book = None
        try:
            user_book = Book.objects.get(user_borrowed=user)
        except Book.DoesNotExist:
            pass
            
        if user_book is not None:
            return JsonResponse({ "status": 2, })
        else:
            book.borrow_book(user)
            status_code = 0
            
    elif status_code == 3:
        pass
    else:
        status_code = 4

    

    
    return JsonResponse({ "status": status_code, })



def return_book(request,book_id):
    status_code = 0
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        status_code = 2
    

    if status_code == 0:
        if book.user_borrowed is None:
            status_code = 1
        else:
            book.return_book()
            status_code = 0
    elif status_code == 2:
        pass
    else:
        status_code = 3

    
    return JsonResponse(
        { "status": status_code, }
    , safe=False)