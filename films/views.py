from django.shortcuts import render
from films.models import Film
# Create your views here.

def film_list(request):
    films = Film.objects.all()
    return render(request, "film_list.html", context={"films": films})
