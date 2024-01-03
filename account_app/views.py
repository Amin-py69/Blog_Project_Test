from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, EditProfileUser

# user = User


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('account_app:login')
    else:
        form = LoginForm()
    return render(request, 'account_app/login.html', {'form': form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'account_app/register.html', {})


def logout_user(request):
    logout(request)
    return redirect('/')


def edit_user_profile(request):
    user = request.user
    form = EditProfileUser(instance=user)
    if request.method == 'POST':
        form = EditProfileUser(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'account_app/edit-profile.html', {'form': form})