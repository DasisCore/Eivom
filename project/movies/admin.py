from django.contrib import admin
from .models import Genre, Movie
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_id', 'genre_name', )

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'released_date', 'vote_average',)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('content', 'movie', 'user',)



admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
# admin.site.register(Comment, CommentAdmin)