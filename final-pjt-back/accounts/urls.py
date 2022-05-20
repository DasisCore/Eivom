
from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.user_profile),
    path('<username>/follow/', views.follow),
    path('<username>/upload_img/', views.upload_img),
]
