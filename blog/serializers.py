from rest_framework import serializers
from blog.models import Post, PostMedia


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('media_type', 'media_file')


class PostDetailSerializer(serializers.ModelSerializer):
    medias = PostMediaSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'medias')


