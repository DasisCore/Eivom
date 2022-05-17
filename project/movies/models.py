from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Movie (models.Model):
    title = models.CharField(max_length=100)
    movie_id = models.IntegerField()
    overview = models.TextField(null=True, blank=True)
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    vote_average = models.FloatField()
    genre = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)