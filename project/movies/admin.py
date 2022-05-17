from django.contrib import admin
from .models import Genre, Movie, Comment
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'movie', 'user',)



admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)