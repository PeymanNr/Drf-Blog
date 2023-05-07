from django.urls import path
from blog.views import PostListAPI, PostDetailAPI, CommentListAPI, CommentRetrieveAPI, CommentCreateAPI, \
    UserPostsListAPIView

urlpatterns = [

    path('post/list/', PostListAPI.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
    path('comment/list/', CommentListAPI.as_view(), name='comment-list'),
    path('comment/create/', CommentCreateAPI.as_view(), name='comment-create'),
    path('comment/retrieve/<int:pk>/', CommentRetrieveAPI.as_view(), name='comment-retrieve'),
    path('user/post/<int:author_id>/', UserPostsListAPIView.as_view(), name='user-posts-list'),

]
