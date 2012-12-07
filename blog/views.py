# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from django.http import Http404
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from blog.models import Article
from blog.serializers import UserSerializer, ArticleSerializer

import logging

logger = logging.getLogger(__name__)

class UserList(APIView):
    """
    get list of users or post to create new one
    """
    def get(self, request, format=None):
        """
        get index view
        """
        users = User.objects.all()
        serializer = UserSerializer(users)
        return render_to_response('users.html.haml', {'users': serializer.object})
    def post(self, request, format=None):
        return

    def new(self, request, format=None):
        """
        GET /users/new
        """
        return

class UserItem(APIView):
    """
    deal with each user
    """
    def get_object(self, username):
        """
        get user by username
        """
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        if format == 'json':
            return Response(serializer.data)
        else:
            return render_to_response('user.html.haml', {'user': serializer.object, 'format': format})

    def put(self, request, username, format=None):
        return

    def delete(self, request, username, format=None):
        """
        DELETE /users/:username
        """
        return

    def new(self, request, username, format=None):
        return
    def edit(self, request, username, format=None):
        """
        GET /users/:username/edit
        """
        return

class ArticleList(APIView):
    """
    Article List
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles)
        return render_to_response('articles.html.haml', {'articles': serializers.object})

    def post(self, request, format=None):
        return

    def new(self, request, format=None):
        """
        GET /users/new
        """
        return
class ArticleItem(APIView):
    """
    for individual article
    """
    def get_article(self, slug):
        """
        get article by slug
        """
        try:
            return Article.objects.get(slug=slug)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        """
        individual article
        """
        article = self.get_article(slug)
        serializer = ArticleSerializer(article)
        return render_to_response('article.html.haml', {'article': serializer.object})

    def put(self, request, slug, format=None):
        return

    def delete(self, request, slug, format=None):
        return

    def edit(self, request, slug, format=None):
        return
