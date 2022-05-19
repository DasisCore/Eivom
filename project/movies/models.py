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
    original_title = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    released_date = models.DateField()
    vote_average = models.FloatField(null=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments_movie", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user