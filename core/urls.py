"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from films.views import film_list, base, film_detail, film_create, delete_film, FilmListView, FilmCreateView, BaseView, DetailView, FilmDeleteView
from django.conf.urls import static
from django.conf import settings
from users.views import register, login_user, logout_user, update_user, delete_user, profile, update_profile
class_urls = [
    path("class/films/", FilmListView.as_view()),
    path('class/film_create', FilmCreateView.as_view()),
    path('class/base', BaseView.as_view()),
    path("class/films/<int:film_id>/", DetailView.as_view()),
    path("class/film_delete/<int:film_id>/", FilmDeleteView.as_view())

    ]

users = [
    path('register/', register),
    path('login/', login_user),
    path('logout/', logout_user),
    path('settings/', update_user),
    path('delete/', delete_user),
    path('profile/', profile),
    path('update_profile/', update_profile)
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', film_list),
    path('films/<int:film_id>/', film_detail),
    path('', base),
    path('film_create/', film_create ),
    path('delete_film/<int:film_id>/', delete_film),
    *users, *class_urls 
]+static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
