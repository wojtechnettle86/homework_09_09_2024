from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from .forms import MovieForm

def movies(request):
  mymovies = Movie.objects.all().values()
  template = loader.get_template('all_movies.html')
  context = {
    'mymovies': mymovies,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymovie = Movie.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymovie': mymovie,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def add_movie(request):
  if request.method == 'POST':
    form = MovieForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("movies")

  return render(request, 'add_movie.html', {'form': MovieForm()})
