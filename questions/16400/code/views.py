from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from app.models import Movie, Seat,Ticket
from django.db.models import Count
from django.http import JsonResponse

def list_movies(request):
    return render(request, 'app/movies.html', {
        'movies': Movie.objects.all()
    })



def list_seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    reserved_seats = Ticket.objects.filter(movie=movie).values_list('seat_id', flat=True)
    available_seats = Seat.objects.exclude(id__in=reserved_seats)

    return render(request, 'app/seats.html', {
        'movie': movie,
        'seats': available_seats
    })



def reserve_seat(request, movie_id, seat_id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=movie_id)
        seat = get_object_or_404(Seat, id=seat_id)
        ticket = Ticket(movie=movie,user=request.user,seat=seat)
        ticket.save()
        return redirect('list_seats', movie_id=movie_id)
    else:
        return redirect(f'/login?next=/movie/{movie_id}/seats')





from django.http import JsonResponse, HttpResponseForbidden

def stats(request):
    if request.user.is_authenticated and request.user.is_superuser:
        seat_stats = Ticket.objects.values('seat__number').annotate(total=Count('seat__number')).order_by('seat__number')

        data = {
            'stats': list(seat_stats)
        }

        return JsonResponse(data)
    else:
        return HttpResponseForbidden('Forbidden')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list_movies')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

