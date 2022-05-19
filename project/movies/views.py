from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Movie
from .serializers import MovieListSerializer
# Create your views here.

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

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # print(Movie.objects.filter(movie_id = movie_pk).count())
    if Movie.objects.filter(movie_id = movie_pk).count() == 1:
        pass
    else:
        # 해당 데이터가 없을 경우, movie_id와 pk가 동일한 데이터 생성
        movie_data = Movie(pk = movie_pk, movie_id = movie_pk)
        movie_data.save()
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == "GET":
        serializer = MovieListSerializer(movie)
        # print(serializer)
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