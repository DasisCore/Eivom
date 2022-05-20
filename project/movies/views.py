from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Movie, Comment
from .serializers import MovieListSerializer, CommentListSerializer, MovieSerializer
# Create your views here.


# 가지고 있는 영화 전체 serializer
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 영화 디테일 serializer
@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    if Movie.objects.filter(movie_id = movie_pk).count() == 1:
        pass
    else:
        # 해당 데이터가 없을 경우, movie_id와 pk가 동일한 데이터 생성
        movie_data = Movie(pk = movie_pk, movie_id = movie_pk)
        movie_data.save()
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == "GET":
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

    elif request.method == "DELETE":
        movie.delete()
        data = {
            'delete': f'데이터 {movie_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = MovieListSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 특정 영화 좋아요
@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_user.filter(pk=user.pk).exists():
        movie.like_user.remove(user.pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_user.add(user.pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 영화 상세 페이지 속 댓글 좋아요
@api_view(['POST'])
def comment_movie_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    if comment.movie_comment_like.filter(pk=user.pk).exists():
        comment.movie_comment_like.remove(user.pk)
        serializer = MovieSerializer(comment)
        return Response(serializer.data)
    else:
        comment.movie_comment_like.add(user.pk)
        serializer = MovieSerializer(comment)
        return Response(serializer.data)

# 전체 댓글 serializers
@api_view(['GET', 'POST'])
def comment_list(request, movie_pk): 
    comments = get_list_or_404(Comment, movie_id=movie_pk)
    # comment = get_list_or_404(Comment)
    if request.method == "GET":
        serialiezers = CommentListSerializer(comments, many=True)
        return Response(serialiezers.data)




# 이전 코드
# @api_view(['GET', 'DELETE', 'PUT'])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
    
#     if request.method == "GET":
#         serializer = MovieListSerializer(movie)
#         print(serializer)
#         return Response(serializer.data)

#     elif request.method == "DELETE":
#         movie.delete()
#         data = {
#             'delete': f'데이터 {movie_pk}번이 삭제되었습니다.'
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == "PUT":
#         serializer = MovieListSerializer(movie, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)