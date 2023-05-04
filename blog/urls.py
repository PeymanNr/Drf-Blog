from django.urls import path
from blog.views import PostListAPI, PostDetailAPI, CommentListAPI, CommentRetrieveAPI, CommentCreateAPI

urlpatterns = [

    path('post/list/', PostListAPI.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
    path('comment/list/', CommentListAPI.as_view(), name='comment-list'),
    path('comment/create/', CommentCreateAPI.as_view(), name='comment-create'),
    path('comment/retrieve/<int:pk>/', CommentRetrieveAPI.as_view(), name='comment-retrieve'),

]
