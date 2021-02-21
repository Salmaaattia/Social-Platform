from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, 'main_app/home.html', {'posts': Post.objects.all()})


def register(request):
    return render(request, 'main_app/register.html')


def login(request):
    return HttpResponse("please login")


def logout(request):
    return HttpResponse("logout")


def post(request):
    return HttpResponse("post")
