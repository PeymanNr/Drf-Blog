from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Author


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _("categories")


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _("posts")


class PostMedia(models.Model):
    IMAGE = 1
    VIDEO = 2
    TYPE_CHOICES = (
        (IMAGE, _('image')),
        (VIDEO, _('video')),
    )
    media_type = models.PositiveSmallIntegerField(_('media_type'), choices=TYPE_CHOICES, default=IMAGE)
    image = models.ImageField(upload_to='posts/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='medias')
    media_file = models.FileField(_("media_file"), upload_to='media/')

    class Meta:
        verbose_name = _('PostMedia')
        verbose_name_plural = _("PostsMedia")


class Comment(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('name'))
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _("comments")


class Relation(models.Model):
    from_user = models.ForeignKey(Author, related_name='followings', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Relation')
        verbose_name_plural = _("Relations")

    def __str__(self):
        return "{}>>{}".format(self.from_user.author.username, self.to_user.username)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _("likes")

    def __str__(self):
        return "{}>>{}".format(self.user.username, self.post.id)