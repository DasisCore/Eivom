from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Movie (models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)