from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the socialplatform index.")


def register(request):
    return render(request, 'main_app/register.html')


def login(request):
    return HttpResponse("please login")


def logout(request):
    return HttpResponse("logout")


def post(request):
    return HttpResponse("post")
