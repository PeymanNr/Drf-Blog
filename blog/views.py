from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Category, Post, Comment
from blog.serializers import PostDetailSerializer, PostListSerializer, CommentListSerializer, CommentCreateSerializer, \
    CommentUpdateSerializer, LikeListSerializer
from lib.pagnation import SmallPageNumberPagination, StandardPagination
from lib.permissions import RelationExists
from rest_framework import viewsets


# Create your views here.


class PostListAPI(APIView):
    def get(self, request, *args, **kwargs):

        posts = Post.objects.all()

        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(instance)
        return Response(serializer.data)


class CommentCreateAPI(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return CommentListSerializer
    #     return self.serializer_class
    #


class CommentListAPI(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticated,)
    # pagination_class = SmallPageNumberPagination
    pagination_class = StandardPagination


class CommentRetrieveAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return CommentUpdateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class AuthorPostsListAPIView(ListAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'author_id'
    serializer_class = PostDetailSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticated, RelationExists]
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author_id=self.kwargs[self.lookup_url_kwarg])


class AuthorPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'post_id'
    serializer_class = PostDetailSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author__author__username=self.kwargs['username'])

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'get_likes_list':
            return LikeListSerializer
        return self.serializer_class

    @action(detail=True)
    def get_likes_list(self, request, *args, **kwargs):
        post = self.get_object()
        queryset = post.likes.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
