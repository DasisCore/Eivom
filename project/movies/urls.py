from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/comments/', views.comment_list), # 한 영화에 대한 댓글들
    path('<int:movie_pk>/comments/<int:comment_pk>/like', views.comment_movie_like), # 영화 댓글에 대한 좋아요
]
