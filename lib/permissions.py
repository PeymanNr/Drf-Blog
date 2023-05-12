from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission

from account.models import Author
from blog.models import Relation
User = get_user_model()


class RelationExists(BasePermission):
    def has_permission(self, request, view):
        user = Author.objects.filter(username=view.kwargs['username']).first()
        if user:
            return Relation.objects.filter(from_user=request.user, to_user=user).exists()
        return False
