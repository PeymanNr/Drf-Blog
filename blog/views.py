from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Category, Post, Comment
from blog.serializers import PostDetailSerializer, PostListSerializer, CommentListSerializer, CommentCreateSerializer, \
    CommentUpdateSerializer


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


class CommentListCreateAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.filter(reply__isnull=True)
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return self.serializer_class


class CommentRetrieveAPI(RetrieveUpdateAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.filter(reply__isnull=True)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return CommentUpdateSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(user=self.request.user)





