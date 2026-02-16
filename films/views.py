from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from films.models import Film, Category
from films.forms import CreateFilmForm, SearchForm
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
@login_required(login_url="/login/")
def film_list(request):
    limit = 3
    if request.method == 'GET':
        films = Film.objects.all()
        forms = SearchForm()
        if request.GET.get('search'):
            search = request.GET.get("search")
            films = Film.objects.filter(Q(title__icontains = search) | Q(description__icontains = search)) 
        category_id = request.GET.get('category_id')
        if category_id:
            films = Film.objects.filter(category_id=category_id)
        episode_choice = request.GET.get("episode_choice")
        if episode_choice:
            if episode_choice == "1":
                films = Film.objects.filter(episodes__gt=100)
            elif episode_choice == "2":
                films = Film.objects.filter(episodes__lt=100)
        genre = request.GET.getlist("genre")
        if genre:
            films = Film.objects.filter(genre__in=genre)
        page = int(request.GET.get('page')) if request.GET.get('page') else 1
        total = films.count()
        max_page = (total + limit - 1) // limit
        start = (page - 1) * limit
        stop = page * limit
        list_pages = range(1, max_page + 1)
        films = films[start: stop]
        return render(request, "films/film_list.html", context={"films": films, 'forms': forms, 'list_pages': list_pages})
@login_required(login_url="/login/")
def film_create(request):
    if request.method == 'GET':
        forms = CreateFilmForm()
        return render(request, 'films/film_create.html', context={'forms':forms})
    elif request.method == 'POST':
        forms = CreateFilmForm(request.POST, request.FILES)
        if forms.is_valid():
            Film.objects.create(
                profile = request.user.profile,
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

@login_required(login_url="/login/")
def film_detail(request, film_id):
    if request.method == 'GET':
        film = Film.objects.get(id=film_id)
        return render(request, "films/film_detail.html", context={'film': film})

def delete_film(request, film_id):
    film = Film.objects.get(id=film_id)
    if request.user.profile != film.profile:
        return HttpResponse('Permission denied')
    film.delete()
    return redirect('/films/')

