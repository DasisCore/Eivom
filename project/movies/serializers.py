from rest_framework import serializers
from .models import Movie, Comment
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        model = Movie
        fields = '__all__'


class CommnetListSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        model = Comment
        fields = '__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        model = Comment
        fields = '__all__'