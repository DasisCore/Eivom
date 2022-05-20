from rest_framework import serializers
from .models import Movie, Comment

from django.contrib.auth import get_user_model
User = get_user_model()



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class MovieListSerializer(serializers.ModelSerializer):
    
    like_user = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'movie_id', 'like_user' )






class MovieSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Movie
        fields = '__all__'







class MovieCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class CommentListSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    movie_comment_like = MovieCommentLikeSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = '__all__'
        fields = ('id', 'content', 'created_at', 'updated_at', 'movie', 'user', 'movie_comment_like' )







class CommentSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Comment
        fields = '__all__'