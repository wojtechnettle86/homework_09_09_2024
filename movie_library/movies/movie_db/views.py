from django.http import HttpResponse
from django.template import loader
from .models import Movie

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
