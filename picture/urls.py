from django.urls import path

from . import views
urlpatterns = [
    path('', views.PictureList, name='home'),
    # path('add/', views.PictureAdd, name='picture_add'),
    path('detail/<int:pk>/', views.PictureDetail, name='picture_detail'),
    # path('videos/', views.VideoList, name='videos'),
    # path('video/detail/<int:pk>/', views.VideoDetail, name='video_detail'),
]

