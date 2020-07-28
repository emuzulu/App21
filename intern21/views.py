from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from .models import Application
from django.contrib.auth import logout, login, authenticate


# Create your views here.


# TODO implement login and logout system

def logout_view(request):
    logout(request)
    return render(request, "intern21/login.html", {
        "message": "User has been logged out"
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "intern21/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "intern21/login.html")


def create_user(request):
    pass


# TODO implement filtering logic and then deleting logic

def delete_view(request, app_id):
    if request.method == "POST":
        user = request.user
        app = user.applications.get(pk=app_id)
        Application.delete(app)
    return render(request, 'intern21/app.html', {
        "apps": user.applications.all()
    })


def add_view(request):
    if request.method == "POST":
        company = request.POST["company"]
        role = request.POST["role"]
        user = request.user
        date = datetime.now().date()
        app = Application(company=company, role=role, user=user, date=date)
        app.save()
    return render(request, 'intern21/app.html', {
        "apps": user.applications.all()
    })


def applications(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        user = request.user
        print(user.applications)
        return render(request, 'intern21/app.html', {
            "apps": user.applications.all()
        })


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "intern21/index.html")
