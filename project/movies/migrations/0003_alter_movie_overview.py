# Generated by Django 4.0.4 on 2022-05-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(null=True),
        ),
    ]
