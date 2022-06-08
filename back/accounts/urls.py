from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.user_profile),
    path('follow/<username>/', views.follow),
    path('upload_img/<username>/', views.upload_img),
]

    # path('profile/<username>/comments/', views.comment_create),
    # path('profile/<username>/comments/<int:comment_pk>', views.comment_update_or_delete),