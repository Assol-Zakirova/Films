from django.shortcuts import render
from users.forms import RegisterForms
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'GET':
        forms = RegisterForms()
        return render(request, 'users/register.html', context={'forms':forms})
    elif request.method == 'POST':
        forms = RegisterForms(request.POST)
        if not forms.is_valid:
            return HttpResponse('Error')
        user = User.objects.create_user(
            username=forms.cleaned_data.get('username'),
            password = forms.cleaned_data.get('password')
        )

    return render(request, 'users/register.html' )
