from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')


class Author(models.Model):
    author = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='authors')
