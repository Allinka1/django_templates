# Create your views here.
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from user.forms import AuthenticationForm


def login(request):
    if request.method == 'POST':
        ...
    login_form = AuthenticationForm(request.POST)
    return render(request, 'login.html', {'login_form':login_form})


def logout(request):
    return HttpResponseRedirect('/')
