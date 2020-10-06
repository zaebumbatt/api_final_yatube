from rest_framework import serializers

from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        extra_kwargs = {'post': {'required': False}}


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
        extra_kwargs = {'description': {'required': False}}


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    following = serializers.CharField()

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, data):
        user = self.context['request'].user
        following = User.objects.get(username=data.get('following'))
        try:
            Follow.objects.get(user=user, following=following)
        except Follow.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('Already followed')
        return data
