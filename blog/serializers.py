from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blog.models import Post, PostMedia, Category, Comment


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('media_type', 'media_file')


class PostDetailSerializer(serializers.ModelSerializer):
    medias = PostMediaSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'medias')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title',)


class CommentListSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    member = serializers.CharField(source='member.user.username')

    class Meta:
        model = Comment
        fields = ('id', 'title', 'member', 'post')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title', 'post')

    def validate(self, attrs):
        if len(attrs['title']) > 10:
            raise ValidationError('Title cannot be more than 30 characters')


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title',)


