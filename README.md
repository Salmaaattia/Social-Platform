# Social-Platform
A Social Platform using Django 

### Steps:
1. Create virtual environment with any python version higher that 3.6
2. pip install -r requirements.txt
3. cd into socialplatform, where you can find the manage.py file.
4. run python manage.py runserver.

### Supported Functionality:
1. admin, can view/edit users and posts.
2. user can register with email, username and password.
3. user can login and logout.
4. authenticated user can add post.
5. authenticated user can view profile.


## Implementation
this project consists of two apps:
1. main_app: this app is responsible for handling the home page and the post.
2. users: handles the users, register, login, logout. etc.

### Models:
1. User table which is imported from django.contrib.auth.models directly.
3. Post, included in main_app.models.
4. Like, implemented but not used.
5. Comment, implemented but not used.

### Views:
1. main_app/ --> home view
2. register/ --> registeration
3. login/ --> login
4. logout/ --> logout
5. profile/ --> profile
6. admin/ --> admin site
7. main_app/post/ ---> create new post
