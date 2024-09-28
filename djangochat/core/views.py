from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, LogInForm

# Create your views here.
def  frontpage(request):
    return render(request, 'core/frontpage.html')


def user_logout(request)->HttpResponse:
    logout(request)
    return render(request, 'core/frontpage.html', {}) 


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("frontpage")
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("frontpage") #finds path that is NAMED frontpage
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {'form': form})