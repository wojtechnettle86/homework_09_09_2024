from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('movie_db/', views.movies, name='movies'),
    path('movie_db/details/<int:id>', views.details, name='details'),
]