from django.shortcuts import render, redirect
from films.models import Film, Category
from films.forms import CreateFilmForm
from django.http import HttpResponse

# Create your views here.

def film_list(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        films = Film.objects.all()
        if category_id:
            films = Film.objects.filter(category_id=category_id)
        return render(request, "films/film_list.html", context={"films": films})

def film_create(request):
    if request.method == 'GET':
        forms = CreateFilmForm()
        return render(request, 'films/film_create.html', context={'forms':forms})
    elif request.method == 'POST':
        forms = CreateFilmForm(request.POST, request.FILES)
        if forms.is_valid():
            Film.objects.create(
                title=forms.cleaned_data.get('name'),
                episodes=forms.cleaned_data.get('episodes'),
                image=forms.cleaned_data.get('image')
            )
            return redirect('/films/')
        return HttpResponse('Error')

def base(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'base.html', context={'categories': categories})


def film_detail(request, film_id):
    if request.method == 'GET':
        film = Film.objects.get(id=film_id)
        return render(request, "films/film_detail.html", context={'film': film})

