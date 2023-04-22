from django.contrib import admin
from django.contrib.admin import register
from blog.models import Post, Category, PostMedia


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
