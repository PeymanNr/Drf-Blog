from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from blog.models import Post, PostMedia, Comment, Like


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('media_type', 'media_file')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title',)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title', 'post', 'reply')

    def validate(self, attrs):
        if len(attrs['title']) > 30:
            raise ValidationError(_('Title cannot be more than 30 characters'))
        return attrs

    def validate_reply(self, attrs):
        if attrs.reply is not None:
            raise ValidationError(_('you can not reply to a reply recursively'))
        return attrs


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title',)


class CommentRepliesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'title', 'user')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'title', 'user', 'replies')

    def get_replies(self, obj):
        serializer = CommentRepliesSerializer(obj.replies.all(), many=True)
        return serializer.data


class PostDetailSerializer(serializers.ModelSerializer):
    medias = PostMediaSerializer(many=True)
    comments = serializers.SerializerMethodField()
    author = serializers.CharField(source='author.author.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'medias', 'author', 'comments')

    def get_comments(self, obj):
        serializer = CommentListSerializer(obj.comments.filter(reply__isnull=True), many=True)
        return serializer.data


class LikeListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Like
        fields = ('user',)

