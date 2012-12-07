from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Article

class UserSerializer(serializers.ModelSerializer):
    """
    Serializers for Users
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializers for Article
    """
    class Meta:
        model = Article
        fields = ('id', 'slug', 'title', 'content')
