# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user.forms import UserLoginForm, UserRegistrationForm, UserChangePassword, UserInterviewForm
from django.urls import reverse_lazy


def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data.get('username'), 
                password=login_form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)

                redirect_url = reverse_lazy('profile')
                return HttpResponseRedirect(redirect_url)

            login_form.add_error(None, 'check username and password')
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')

@login_required
def profile(request):

    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                password=form.cleaned_data.get('password1')
            )

            redirect_url = reverse_lazy('login')
            return HttpResponseRedirect(redirect_url)

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        change_form = UserChangePassword(request.POST)
        if change_form.is_valid():
            old_password = change_form.cleaned_data.get('old_password')
            if request.user.check_password(old_password):
                new_password = change_form.cleaned_data.get('new_password')
                request.user.set_password(new_password)
                request.user.save()
                logout(request)

                redirect_url = reverse_lazy('login')
                return HttpResponseRedirect(redirect_url)

            else:
                change_form.add_error(None, 'enter your current password ')
    else:
        change_form = UserChangePassword()
    return render(request, 'change_password.html', {'change_form': change_form})


def interview(request):
    if request.method == 'POST':
        interview_form = UserInterviewForm(request.POST)
        if interview_form.is_valid():
            gender = int(interview_form.cleaned_data.get('gender'))
            age = interview_form.cleaned_data.get('age')
            english = int(interview_form.cleaned_data.get('english'))
            for_male = gender == 1 and age >= 20 and english >= 5
            for_female = gender == 2 and age > 22 and english > 4
            if for_male or for_female:

                redirect_url = reverse_lazy('suit')
            else:
                redirect_url = reverse_lazy('no_suit')
            return HttpResponseRedirect(redirect_url)
    else:
        interview_form = UserInterviewForm()

    return render(request, 'interview.html', {'interview_form': interview_form})


def suit(request):

    return render(request, 'Yes.html')


def no_suit(request):

    return render(request, 'No.html')
