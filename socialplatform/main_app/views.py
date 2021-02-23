from django.shortcuts import render, redirect

from django.utils import timezone
from .models import Post
from .forms import PostForm


def home(request):
    return render(request,
                  'main_app/home.html', {'posts': Post.objects.all()})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            post = Post()
            post.content = form.cleaned_data['text']
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,
                  'main_app/post.html', {'form': form})
