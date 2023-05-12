from django.contrib import admin
from django.contrib.admin import register
from blog.models import Post, Category, PostMedia, Comment, Relation, Like


# Register your models here.
class PostImageInline(admin.TabularInline):
    model = PostMedia


@register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'category', 'title', 'create_time',)
    inlines = [PostImageInline, ]


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'reply')


@register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'from_user')


@register(Like)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('user',)

