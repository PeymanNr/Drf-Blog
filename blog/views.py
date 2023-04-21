from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Category
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
