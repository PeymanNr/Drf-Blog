from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authors')



