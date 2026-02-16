from django.shortcuts import render, redirect
from users.forms import RegisterForms, LoginForms, UpdateForm, UpdateProfileForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.method == 'GET':
        forms = RegisterForms()
        return render(request, 'users/register.html', context={'forms':forms})
    elif request.method == 'POST':
        forms = RegisterForms(request.POST)
        if not forms.is_valid():
            return HttpResponse('Error')
        User.objects.create_user(
            username=forms.cleaned_data.get('username'),
            password = forms.cleaned_data.get('password')
        )

    return redirect('/films/')

def login_user(request):
    if request.method == 'GET':
        forms = LoginForms()
        return render(request, 'users/login.html', context={'forms':forms})
    if request.method == 'POST':
        forms = LoginForms(request.POST)
        if not forms.is_valid():
            return HttpResponse('Error')
        user = authenticate(request, username=forms.cleaned_data.get('username'), password=forms.cleaned_data.get('password'))
        if user is None:
            return HttpResponse('There is not such user')
        login(request, user)
    return redirect('/films/') 

def logout_user(request):
    logout(request)
    return redirect('/')

def update_user(request):
    if request.method == 'GET':
        forms = UpdateForm()
        return render(request, 'users/update.html', context={'forms':forms})

    if request.method == 'POST':
        forms = UpdateForm(request.POST)

        if not forms.is_valid():
            return HttpResponse('Error')

        current_user_id = request.user.id
        user = User.objects.get(id=current_user_id)
        user.username = forms.cleaned_data.get('username')
        user.set_password(forms.cleaned_data.get('password'))
        user.save()
    return redirect('/films/')

def delete_user(request):
    if request.user.is_authenticated:
        current_user_id = request.user.id
        User.objects.filter(id=current_user_id).delete()
        logout(request)
        return redirect('/')
    else:
        return HttpResponse('Log in')

def profile(request):
    return(render(request, 'users/profile.html'))

def update_profile(request):
    if request.method == "GET":
        forms = UpdateProfileForm(request.POST or None)
        return render(request, "users/update_profile.html", context={"forms": forms})

    if request.method == "POST":
        forms = UpdateProfileForm(request.POST, request.FILES)
        if not forms.is_valid():
            return HttpResponse("Error")
        request.user.profile.age = forms.cleaned_data.get("age")
        request.user.profile.image = forms.cleaned_data.get("image")

        request.user.username = forms.cleaned_data.get("username")
        request.user.email = forms.cleaned_data.get("email")
        request.user.first_name = forms.cleaned_data.get("first_name")
        request.user.last_name = forms.cleaned_data.get("last_name")

        request.user.save()
        request.user.profile.save()

    return redirect("/films/")
 
