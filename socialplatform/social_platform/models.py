from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    posts_count = models.IntegerField()
    posts = models.CharField(max_length=30)


class Post(models.Model):
    content = models.CharField(max_length=250)
    date_posted = models.DateField()
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=150)
    date_commented = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    owner = models.ForeignKey(User)
    post = models.ForeignKey(Post)
