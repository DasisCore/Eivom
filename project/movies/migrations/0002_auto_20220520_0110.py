# Generated by Django 3.2.12 on 2022-05-19 16:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie_comment_like',
            field=models.ManyToManyField(related_name='like_movie_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='like_user',
            field=models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
