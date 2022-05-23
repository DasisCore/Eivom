from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )

class ArticleLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )

class ArticleListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    article_like = ArticleLikeListSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'post_hit', 'user', 'article_like')




class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content',)



class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Comment
        fields = ('content',)



