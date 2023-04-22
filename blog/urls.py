from django.urls import path
from blog.views import PostListAPI, PostDetailAPI

urlpatterns = [

    path('category/', PostListAPI.as_view(), name='cat-list'),
    path('post/<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),

]
