from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='home-register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post', views.post, name='post')
]
