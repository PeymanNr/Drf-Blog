from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _("authors")



