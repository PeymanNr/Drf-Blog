from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.user.username


class Author(models.Model):
    author = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='authors')



