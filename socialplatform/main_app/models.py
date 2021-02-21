from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class User(models.Model):
#     name = models.CharField(max_length=50)
#     birth_date = models.DateField()
#     posts_count = models.IntegerField()
#     posts = models.CharField(max_length=30)


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=150)
    date_commented = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner
