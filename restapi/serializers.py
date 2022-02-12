from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Story


class UserSerializer(serializers.ModelSerializer):
    stories = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = User
        fields = ['author', 'url', 'username', 'email', 'stories']

    def get_stories(self, user):
        queryset = Story.objects.using('lite').filter(author=user).values()
        return queryset

class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('__all__')





