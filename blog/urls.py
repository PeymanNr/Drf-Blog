from django.urls import path
from blog.views import PostListAPI

urlpatterns = [

    path('category/', PostListAPI.as_view(), name='cat-list')

]
