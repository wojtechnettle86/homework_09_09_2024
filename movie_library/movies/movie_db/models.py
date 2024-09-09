from django.db import models

class Movie(models.Model):
  movie_name = models.CharField(max_length=255)
  director = models.CharField(max_length=255)
  year = models.CharField(max_length=255, null=True)
  genre = models.CharField(max_length=255, null=True)

  def __str__(self):
    return f"{self.movie_name}"
