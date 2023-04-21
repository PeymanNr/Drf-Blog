from django.contrib import admin
from django.contrib.admin import register
from account.models import Author, Member
# Register your models here.


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author',)


@register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user',)
