from django.contrib import admin
from django.contrib.admin import register
from blog.models import Post, Category


# Register your models here.


@register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'category', 'title', 'create_time',)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
