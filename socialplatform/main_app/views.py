from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request,
                  'main_app/home.html', {'posts':[]})


def post(request):
    return render(request,
                  'main_app/post.html', {'posts': Post.objects.all()})
