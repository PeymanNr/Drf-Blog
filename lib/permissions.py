from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission

from blog.models import Relation
User = get_user_model()


class RelationExists(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(id=view.kwargs['author_id']).first()
        if user:
            return Relation.objects.filter(from_user=request.user, to_user=user).exists()
        return False
