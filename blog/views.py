from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Category, Post
from blog.serializers import PostDetailSerializer


# Create your views here.


class PostListAPI(APIView):
    def get(self, request, *args, **Kwargs):
        category = Category.objects.all()
        data = list()
        for cat in category:
            data.append({
                'id': cat.id,
                'name': cat.name,
            })

        return Response(data)


class PostDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(instance)
        return Response(serializer.data)