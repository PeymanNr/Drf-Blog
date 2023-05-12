from django.urls import path, include
from blog.views import PostListAPI, PostDetailAPI, CommentListAPI, CommentRetrieveAPI, CommentCreateAPI, \
    AuthorPostViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('post', AuthorPostViewSet, 'author-post')
# author_post_detail = AuthorPostReadOnlyViewSet.as_view({'get': 'retrieve'})
# author_post_list = AuthorPostReadOnlyViewSet.as_view({'get': 'list'})

urlpatterns = [

    path('post/list/', PostListAPI.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
    path('comment/list/', CommentListAPI.as_view(), name='comment-list'),
    path('comment/create/', CommentCreateAPI.as_view(), name='comment-create'),
    path('comment/retrieve/<int:pk>/', CommentRetrieveAPI.as_view(), name='comment-retrieve'),
    # path('author/<str:username>/posts/', author_post_list, name='author-posts-list'),
    # path('author/<str:username>/posts/<int:post_id>', author_post_detail, name='author-posts-detail'),
    path('author/<str:username>/', include(router.urls)),

]
