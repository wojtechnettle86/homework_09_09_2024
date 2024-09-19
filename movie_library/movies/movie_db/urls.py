from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie_db/', views.movies, name='movies'),
    path('movie_db/details/<int:id>', views.details, name='details'),
    path('profile/', profile_page, name='profile'),
    path('register/', register_page, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]