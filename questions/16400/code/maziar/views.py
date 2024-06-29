from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.db.models import Count
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponseForbidden
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test 
from django.contrib.auth.mixins import UserPassesTestMixin
from app.models import Movie, Seat,Ticket
from django.core.exceptions import PermissionDenied




def list_movies(request):
    return render(request, 'app/movies.html', {
        'movies': Movie.objects.all()
    })


def list_seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reserved_seat_ids = Ticket.objects.values('seat_id').filter(movie=movie_id)
    unreserved_seats = Seat.objects.exclude(id__in=reserved_seat_ids)
    return render(request, 'app/seats.html', {
        'seats': unreserved_seats,
        'movie':movie
    })



def reserve_seat(request, movie_id, seat_id):
    if not request.user.is_authenticated:
        return redirect(f'/login?next=/movie/{movie_id}/seats')

    movie = Movie.objects.get(id=movie_id)
    seat = Seat.objects.get(id=seat_id)
    seat=seat
    user=request.user
    movie = movie
    Ticket.objects.create(
            seat=seat,
            user=user,
            movie=movie,

        )

    return redirect('list_seats',movie_id)


def stats(request):
    if request.user.is_superuser:
        reservations = Ticket.objects.values('seat__number').annotate(total=Count('seat')).order_by('seat__number')
        data = {'stats': list(reservations)}
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseForbidden()



    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('list_movies')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



