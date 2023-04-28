from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Category, Post, Comment
from blog.serializers import PostDetailSerializer, PostListSerializer, CommentListSerializer


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


class CommentListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        comments = CommentListSerializer(data=request.data)
        if comments.is_valid():
            instance = comments.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)




