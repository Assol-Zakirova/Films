from django.shortcuts import render
from films.models import Film
# Create your views here.

def film_list(request):
    films = Film.objects.all()
    return render(request, "films/film_list.html", context={"films": films})

def base(request):
    return render(request, 'base.html')

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, "films/film_detail.html", context={'film': film})

