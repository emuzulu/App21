from django.shortcuts import render
from datetime import date
from django.contrib.auth.models import User
from .models import Application


# Create your views here.


# TODO implement login and logout system

def login(request):
    pass


def logout(request):
    pass


def create_user(request):
    pass


# TODO implement filtering logic and then deleting logic

def delete(request):
    pass


def index(request):
    return render(request, "intern21/index.html")


def test(request):
    return render(request, "intern21/index.html")
