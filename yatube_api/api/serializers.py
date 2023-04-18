import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from posts.models import Comment, Follow, Group, Post

from rest_framework import serializers

User = get_user_model()


class Base64ImageField(serializers.ImageField):
    """Serializer поля image."""

    def to_internal_value(self, data):
        if isinstance(data, str) or data.startwith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    """Serializer модели Post."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    image = Base64ImageField(
        required=False,
        allow_null=True,
    )

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post
        read_only_fields = ('id', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer модели Comment."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('id', 'created', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer модели Group."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group
        read_only_fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    """Serializer модели Follow."""
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError(
                'Автор не может подписаться на себя!'
            )
        return attrs
